# eval_webapp
A simple webapp for evaluating code snippets. This is nothing but a simple proof of concept. 

## EvalServer
The EvalServer is a simple, customizable server running on port 33780 that allows us to run any bit of code and return the stdout after execution.

Currently there are only 4 languages supported out of the box, but more can be added:
* Python
* JavaScript (via Node.js)
* Ruby
* C++ (via `g++`)

You can launch by `cd`'ing into `evalserver` and running `python server.py`. Once you've started it, you can start the webapp.

You can add more languages by modifying the [lang-config.cfg](evalserver/lang-config.cfg) file.

By default, it looks like this:
```cfg
; file extension
@file-ext
    py: py
    js: js
    rb: rb
    cpp: cpp

; interpreter/compiler
@exec
    py: python
    js: node
    rb: ruby
    cpp: g++

; "y" if the language is compiled, "n" otherwise
@compiled
    py: n
    js: n
    rb: n
    cpp: y
```

For an example, let's add C. First we add the file extension. The first `c` is the name of the language we get sent, and the second `c` is the file extension that will be used.

under `@file-ext`:
```
    c: c
```

Then we add the compiler (`gcc`). The `c` is the name of the language we get sent, and the `gcc` is the name of the executable that will be ran with the source code.

under `@exec`:
```
    c: gcc
```

Next, we flag it as "compiled". The `c` is the name of the language we get sent, and the `y` flags it as a compiled language. Replacing the `y` with an `n` flags it as an interpreted language. 

under `@compiled`:
```
    c: y
```

Lastly, we need to allow the language to be selected in the UI. Go to `inputform.py`, and where the `SelectField` is instatiated, you will have to add your language under `choices`. Add another element to the array formatted like this: `("<name of language in server>", "<display name>")`.

Example:
```py
        choices=[
            ('py', 'Python'), 
            ('js', 'JavaScript'),
            ('rb', 'Ruby'),
            ('cpp', 'C++'),
            ('c', 'C')          # this is the one we added.
        ]
```

## The webapp
Start it with `flask run`, and navigate to `localhost:5000/input`.