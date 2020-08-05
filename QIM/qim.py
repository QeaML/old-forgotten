"""QIM"""

from sys import argv
from PIL import Image

CONTEXT = []
MAP = {}
VERINFO = (0, 1, 6)

def do_command(src):
    """does all the commands, basically the entirety of this is coded in here"""
    def debug_log(msg):
        if '--debug' in argv:
            print(msg)
    statements = []
    last_statement = 0
    in_string = False
    string_start = 0
    if src.strip() != "":
        if not (src[-1] == ";" or src[-1] == "\n"):
            src += ";"
        for i in range(0, len(src)):
            if src[i] == "\"":
                in_string = not in_string
                if in_string:
                    string_start = i + 1
            if src[i] == ";" or src[i] == "\n" and not in_string:
                debug_log(f"statement {last_statement}:{i}")
                debug_log(f"          {src[last_statement:i]}")
                statements.append(src[last_statement:i])
                last_statement = i + 1
            if i == len(src)-1 and in_string:
                print("parser err: INFINITE_STRING\n    :: String missing closing quote\n    :: @ "+str(i))
        for i in range(0, len(statements)):
            if "#" in statements[i]:
                statements[i] = statements[i][:statements[i].find('#')].strip()
            else:
                statements[i] = statements[i].strip()
        for i in range(0, len(statements)):
            if not (statements[i] == '' or statements[i].startswith('#')):
                tokens = statements[i].split(' ')
                keyword = tokens[0]
                args = tokens[1:]
                after_macro = False
                def print_error(code, desc):
                    statement = statements[i]
                    line = 0
                    lines = src.split('\n')
                    for j in range(0, len(lines)):
                        if statement in lines[j]:
                            line = j
                            break
                    print(f"err: {code.upper()}\n    :: {desc}\n    :: @ {line+1}L\n    ::   {lines[line].strip()}")
                    return "err"
                def expect_str(inp, strict = True):
                    started = False
                    if str(inp)[0] == '"':
                        started = True
                    if started:
                        buffer = []
                        for j in str(inp)[1:]:
                            if j != '"':
                                buffer.append(j)
                            elif j == '"':
                                started = False
                                break
                        if not started:
                            return "".join(buffer)
                        else:
                            print_error("invalid_literal", "String missing end quote")
                            return None
                    else:
                        try:
                            MAP[inp]
                        except KeyError:
                            print_error("invalid_literal", "Variable '"+inp+"' does not exist")
                            return None
                        else:
                            if strict:
                                if not isinstance(MAP[inp], str):
                                    print_error("invalid_literal", "Variable '"+inp+"' does not contain text")
                                    return None
                                else:
                                    return MAP[inp]
                            else:
                                return MAP[inp]
                def expect_int(inp):
                    started = False
                    if str(inp)[0] == '"':
                        started = True
                    if started:
                        buffer = []
                        for j in str(inp)[1:]:
                            if j != '"':
                                buffer.append(j)
                            elif j == '"':
                                started = False
                                break
                        if not started:
                            strin = "".join(buffer)
                            if not strin.endswith("%"):
                                try:
                                    int(strin)
                                except ValueError:
                                    print_error("invalid_literal", "Could not convert '"+strin+"' to number.")
                                    return None
                                else:
                                    return int(strin)
                        else:
                            print_error("invalid_literal", "String missing end quote")
                            return None
                    else:
                        if inp.endswith("%"):
                            try:
                                int(inp[:-1])
                            except ValueError:
                                print_error("invalid_literal", "Could not convert '"+inp+"' to number.")
                                return None
                            else:
                                return int(inp[:-1])/100
                        else:
                            try:
                                int(inp)
                            except ValueError:
                                print_error("invalid_literal", "Could not convert '"+inp+"' to number.")
                                return None
                            else:
                                return int(inp)
                def do_debug():
                    global in_debug
                    in_debug = True
                    while in_debug:
                        x = input(f"DEBUGGER@{i}: ")
                        if x == "return":
                            in_debug = False
                        elif x == "vars":
                            print(MAP)
                        elif x == "context":
                            print(CONTEXT)
                        elif x == "eval":
                            do_command(x[5:])
                        elif x == "dump":
                            statement = statements[i]
                            line = 0
                            lines = src.split('\n')
                            for j in range(0, len(lines)):
                                if statement in lines[j]:
                                    line = j+1
                                    break
                            print(MAP, CONTEXT, statements, line, sep="\n")
                        else:
                            print()
                global CONTEXT
                if len(CONTEXT) > 0:
                    if keyword == "macro":
                        if args[1] == "begin":
                            args[0] = expect_str(args[0])
                            if args[0] is not None:
                                if not args[0] in CONTEXT:
                                    if args[0] is not None:
                                        CONTEXT.append(args[0])
                                        MAP[args[0]] = []
                                else:
                                    print_error("invalid_keyword", "Macro '"+args[0]+"' has been already started")
                        elif args[1] == "end":
                            if not after_macro:
                                args[0] = expect_str(args[0])
                                if args[0] is not None:
                                    if args[0] in CONTEXT:
                                        CONTEXT.remove(args[0])
                                        after_macro = True
                                    else:
                                        return print_error("invalid_keyword", "Not in macro '"+args[0]+"'")
                        elif args[1] == "run":
                            args[0] = expect_str(args[0])
                            if args[0] is not None:
                                try:
                                    MAP[args[0]]
                                except KeyError:
                                    return print_error("invalid_arguments", "Macro '"+args[0]+"' does not exist")
                                else:
                                    if isinstance(MAP[args[0]], list):
                                        for statement in MAP[args[0]]:
                                            do_command(statement)
                        else:
                            return print_error("invalid_arguments", "Invalid macro command '"+args[0]+"'")
                    elif keyword == "debug":
                        if debug:
                            do_debug()
                    else:
                        for c in CONTEXT:
                            MAP[c].append(statements[i])
                else:
                    if keyword == "load":
                        if len(args) < 2:
                            return print_error("invalid_arguments", "Not enough arguments")
                        else:
                            args[1] = expect_str(' '.join(args[1:]))
                            if args[1] is not None:
                                try:
                                    open(args[1])
                                except FileNotFoundError:
                                    return print_error("no_file", "Could not find file '"+args[1]+"'")
                                else:
                                    MAP[args[0]] = Image.open(args[1])
                                    print("Successfully loaded file '"+args[1]+"' into variable '"+args[0]+"'.")
                    elif keyword == "set":
                        if len(args) < 2:
                            return print_error("invalid_arguments", "Not enough arguments")
                        else:
                            args[1] = expect_str(' '.join(args[1:]), strict = False)
                            if args[1] is not None:
                                MAP[args[0]] = args[1]
                    elif keyword == "resize":
                        if len(args) < 3:
                            return print_error("invalid_arguments", "Not enough arguments")
                        elif len(args) > 3:
                            return print_error("invalid_arguments", "Too many arguments")
                        else:
                            try:
                                MAP[args[0]]
                            except KeyError:
                                return print_error("invalid_arguments", "Variable '"+args[0]+"' does not exist")
                            else:
                                args[1:2] = (expect_int(args[1]), expect_int(args[2]))
                                if not None in args[1:2]:
                                    box = (int(args[1]*MAP[args[0]].size[0]), int(args[2]*MAP[args[0]].size[1]))
                                    MAP[args[0]] = MAP[args[0]].resize(box)
                                    print("Image resized to "+str(tuple(args[1:])))
                    elif keyword == "scale":
                        if len(args) < 2:
                            return print_error("invalid_arguments", "Not enough arguments")
                        elif len(args) > 2:
                            return print_error("invalid_arguments", "Too many arguments")
                        else:
                            try:
                                MAP[args[0]]
                            except KeyError:
                                return print_error("invalid_arguments", "Variable '"+args[0]+"' does not exist")
                            else:
                                if args[1].endswith("%"):
                                    percentage = int(args[1][:-1])/100
                                    old_size = MAP[args[0]].size
                                    new_size = (int(old_size[0]*percentage), int(old_size[1]*percentage))
                                    MAP[args[0]] = MAP[args[0]].resize(new_size)
                                    print("Image resized to "+str(new_size))
                                else:
                                    return print_error("invalid_literal", "'resize' only accepts percentage factors")
                    elif keyword == "show":
                        if len(args) < 1:
                            return print_error("invalid_arguments", "Not enough arguments")
                        elif len(args) > 1:
                            return print_error("invalid_arguments", "Too many arguments")
                        else:
                            try:
                                MAP[args[0]]
                            except KeyError:
                                return print_error("invalid_arguments", "Variable '"+args[0]+"' does not exist")
                            else:
                                MAP[args[0]].show()
                    elif keyword == "crop":
                        if len(args) < 5:
                            return print_error("invalid_arguments", "Not enough arguments")
                        elif len(args) > 5:
                            return print_error("invalid_arguments", "Too many arguments")
                        else:
                            try:
                                MAP[args[0]]
                            except KeyError:
                                return print_error("invalid_arguments", "Variable '"+args[0]+"' does not exist")
                            else:
                                args[1:4] = expect_int(args[1]), expect_int(args[2]), expect_int(args[3]), expect_int(args[4])
                                if not None in args[1:4]:
                                    m = MAP[args[0]]
                                    if float in [type(a) for a in args[1:4]]:
                                        box = (m.size[0] * args[1], m.size[1] * args[2], m.size[0] * args[3], m.size[1] * args[4])
                                        box = (int(box[0]), int(box[1]), int(box[2]), int(box[3]))
                                    else:
                                        box = (args[1], args[2], args[3], args[4])
                                    MAP[args[0]] = MAP[args[0]].crop(box = box)
                                    print("Image cropped to "+str(box))
                    elif keyword == "autocrop":
                        if len(args) < 1:
                            return print_error("invalid_arguments", "Not enough arguments")
                        elif len(args) > 1:
                            return print_error("invalid_arguments", "Too many arguments")
                        else:
                            try:
                                MAP[args[0]]
                            except KeyError:
                                return print_error("invalid_arguments", "Variable '"+args[0]+"' does not exist")
                            else:
                                box = MAP[args[0]].getbbox()
                                MAP[args[0]] = MAP[args[0]].crop(box = box)
                                print("Image cropped to "+str(tuple(box)))
                    elif keyword == "save":
                        if len(args) < 2:
                            return print_error("invalid_arguments", "Not enough arguments")
                        else:
                            try:
                                MAP[args[0]]
                            except KeyError:
                                return print_error("invalid_arguments", "Variable '"+args[0]+"' does not exist")
                            else:
                                args[1] = expect_str(' '.join(args[1:]))
                                if args[1] is not None:
                                    try:
                                        MAP[args[0]].save(args[1])
                                    except ValueError:
                                        return print_error("invalid_arguments", "Could not determine image format from filename.")
                                    except IOError:
                                        return print_error("io_error", "There was a problem writing to the file: It might exist but won't be usable.")
                                    else:
                                        print("File succesfully saved to file '"+args[1]+"'")
                    elif keyword == "macro":
                        if len(args) < 2:
                            return print_error("invalid_arguments", "Not enough arguments")
                        elif len(args) > 2:
                            return print_error("invalid_arguments", "Too many arguments")
                        else:
                            if args[1] == "begin":
                                args[0] = expect_str(args[0])
                                if args[0] is not None:
                                    if not args[0] in CONTEXT:
                                        if args[0] is not None:
                                            CONTEXT.append(args[0])
                                            MAP[args[0]] = []
                                    else:
                                        print_error("invalid_keyword", "Macro '"+args[0]+"' has been already started")
                            elif args[1] == "end":
                                if not after_macro:
                                    args[0] = expect_str(args[0])
                                    if args[0] is not None:
                                        if args[0] in CONTEXT:
                                            CONTEXT.remove(args[0])
                                            after_macro = True
                                        else:
                                            return print_error("invalid_keyword", "Not in macro '"+args[0]+"'")
                            elif args[1] == "run":
                                args[0] = expect_str(args[0])
                                if args[0] is not None:
                                    try:
                                        MAP[args[0]]
                                    except KeyError:
                                        return print_error("invalid_arguments", "Macro '"+args[0]+"' does not exist")
                                    else:
                                        if isinstance(MAP[args[0]], list):
                                            for statement in MAP[args[0]]:
                                                do_command(statement)
                            else:
                                return print_error("invalid_arguments", "Invalid macro command '"+args[0]+"'")
                    elif keyword == "debug":
                        if debug:
                            do_debug()
                        else:
                            print_error("invalid_keyword", "'debug' was not expected at this time")
                    elif keyword == "listvars":
                        varlist = {}
                        for j in MAP:
                            if isinstance(MAP[j], list):
                                varlist[j] = "(macro)"
                            elif isinstance(MAP[j], Image.Image):
                                varlist[j] = "(image)"
                            else:
                               varlist[j] = MAP[j]
                        print('\n'.join([f"{k} = {varlist[k]}" for k in varlist]))
                    elif keyword == "help":
                        print(open('qimhelp', 'rt').read())
                    else:
                        return print_error("invalid_keyword", f"Invalid keyword: '{keyword}'")
    else:
        return
            
if __name__ == '__main__':
    inter = True
    file = False
    filename = ""
    preset = None
    debug = False
    for argument in argv:
        if argument.startswith('--file='):
            filename = argument[7:]
            file = True
            inter = False
        if argument.startswith('--preset='):
            preset = argument[9:]
        if argument == "--debug":
            debug = True
    if inter:
        print(f"QIM v{VERINFO[0]}.{VERINFO[1]}/{VERINFO[2]}\nWrite \"help;\" for help.")
        while True:
            x = input('> ')
            do_command(x)
    elif file:
        try:
            open(filename)
        except FileNotFoundError:
            print("err: NO_FILE\n    :: File not found\n    :: @ inter_file")
        else:
            if preset is not None:
                file = 'set preset "'+preset+'";'+open(filename, 'rt').read()
            else:
                file = open(filename, 'rt').read()
            if debug:
                print("WORKING ON FILE: "+"-"*20)
                print(file)
                print("-"*20)
            do_command(file)