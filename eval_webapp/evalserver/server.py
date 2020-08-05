import json
from socket import create_server
from subprocess import run, PIPE, STDOUT
from threading import Thread

CONFIG = {}

with open('lang-config.cfg', 'rt') as f:
    major = "GLOBAL"
    for line in f.read().splitlines():
        if line.startswith(';') or len(line.strip()) == 0:
            continue

        line = line.strip()
        if line.startswith('@'):
            major = line[1:]
            CONFIG[major] = {}

        else:
            key = line.split(':')[0].strip()
            value = ':'.join(line.split(':')[1:]).strip()
            CONFIG[major][key] = value

class ConnectionThr(Thread):
    def __init__(self, conn):
        super(ConnectionThr, self).__init__()
        self.conn = conn
        self.alive = True
        self.start()

    def run(self):
        while self.alive:
            data = self.conn.recv(8192)
            packet = json.loads(data)
            lang = packet["lang"]
            src = packet["src"]

            file_ext = CONFIG["file-ext"][lang]
            exec = CONFIG["exec"][lang]
            compiled = CONFIG["compiled"][lang] == "y"

            file = f"__src.{file_ext}"
            try:
                open(file)
            except FileNotFoundError:
                mode = "xt"
            else:
                mode = "wt"

            with open(file, mode) as f:
                f.write(src)

            out = ""
            if compiled:
                out += "COMPILATION --------------------------------------------------------------------\n"
                comp = run([exec, file, "-o", "__res"], stdout=PIPE, stderr=STDOUT, text=True)
                out += comp.stdout
                if comp.returncode != 0:
                    out += f"Compiler exited with non-zero exit code: {comp.returncode}"

                else:
                    out += "Compilation successful.\n\nEXECUTION ----------------------------------------------------------------------\n"
                    proc = run(["__res"], stdout=PIPE, stderr=STDOUT, text=True)
                    out += proc.stdout
                    out += f"Return code: {proc.returncode}"

            else:
                proc = run([exec, file], stdout=PIPE, stderr=STDOUT, text=True)
                out = proc.stdout
            if out == "":
                out = "(empty)"
                
            self.conn.send(bytes(out, 'utf-8'))

sock = create_server(('localhost', 33780))     
while True:
    c, _ = sock.accept()
    ConnectionThr(c)