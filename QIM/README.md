# QIM (QeaML's Image Manipulator)
QIM is a "scripting" language for image manipulation. Really, it's just a fancy wrapper for PIL. It's also coded entirely in one function so not the most efficient way of coding it either.

## About
### Running QIM
1. Install pillow: `pip install pillow`
2. Use `py qim.py` for interactive shell, or `py qim.py --file=<filename>` to run a script from a `*.qim` file.

#### Other arguments:
* `--debug`: enables debug mode (reveals inner workings)

* `--preset=<text>`: pre-set a variable for a script

### SYNTAX
QIM has very basic syntax:

`(keyword) (argument) (argument) (...);`

The semicolon and newline both act as statement sepatators, meaning you can
use either to split your statement. For comments use the # character
like this:
```
<code>
# comment
<more code>
```
Arguments can be: numbers, strings or variables (see: data types). Each
keyword has a minimum amount of arguments that need to be specified for it
to work, but not all of them have maximum arguments.

### KEYWORDS
Some basic keywords:

`load <variable> <filename: string>;`

Loads a file from disk into the specified variable. Min args: 2.

`show <variable>;`

If variable is image, it will be saved on disk in a temporary
directory and shown to you. Min/max args: 1.

`setvar <variable> <value: string>;`

Assign a value to a variable. Min args: 2.

`macro <name: string> <action>;`

Manage macros (define and run). Min/max args: 2.

### DATA TYPES
Some keyword accept arguments which can be literals. These literals can be:

* Variables: "containers" for data which do not need a declaration, can
be modified at any time and can contain any of the literals (but not
another variable).

* Strings: strings of text, must start and end with `"`. If there's 2
strings in the space of one arguments, only the first one is passed
through.

* Numbers: can be normal integetrs, like `1`, `22`, or `666`, or
percentages like `1%`, `20%` or `69%`. These can also be embedded in
strings.

### MACROS
Want to run the same actions multiple times? Macros got your back! (macros
aren't functions: they do not accept arguments nor do they have a return
value) To start making macros all you need is the `macro` keywords (see:
keywords). About the keyword in detail:
#### SYNTAX
   `macro <name: string> <action>`

#### ARGUMENTS
* name - The name of the macro you wish to manage.

* action - The action you wish to perform on the selected macro.

#### ACTIONS
* begin - Begins the definition of a macro.

* end - Ends the definition of a macro.

* run - Executes the macro.
