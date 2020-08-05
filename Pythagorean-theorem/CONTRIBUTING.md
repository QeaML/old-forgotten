# General coding guidelines
* Avoid advanced coding practices.
	Make sure that the code demostrates that, what a developer would see most of the time developing with the language.
* Keep it tidy.
	Use indentation and other visual goodies to make your code as readable as it can get.
* Use comments when shakinh up the formula.
	While all of these samples are coded almost exactly the same (right now at least), there is no confusion on what does what do. But if you're shaking up the formula, make sure to make comments about what you did differently, to avoid possible confusion.
* Keep the lines short.
	Ensure all the lines of code are under 80 characters in length, for readability's sake. *This does not apply to documentation.*
	
# Update a language checklist
* Made only positively neccessary changes.
	We don't want the code to get big changes that make it cluttered, but only slightly faster. Only make changes if e.g. a rookie mistake was made, or an update happened and the code no longer runs/compiles properly.
* Properly describe your commits.
	Add not only the commit title but also the description to describe what you changed (and optionally, what) in a nice list.
* The general formula stays the same.
	Don't repurpose a variable. If the formula has been decided on by the original submitter, stick to it.
	
## Update a langage notices
You can make slight updates, like changing `1` to `1.0`, but these aren't guaranteed to be accepted unless you change the whole file to also use that `.0`.

# Add a language checklist
* There are 2 functions: `distance2d` and `distance3d` which both accept 2 sets of coordinates: `from` and `to`.
	This is done so the code is universal across languages to be easier to comapre between them, which is the main purpose of this repository.
* The code actually runs/compiles and prints the distance between `x=1.0,y=2.0,z=3.0` and `x=4.0,y=5.0,z=6.0`. (It should be around `5.196`)
	So that the code seen here can be trusted, and produces an expected result.
* It is coded like all the other examples, with `diff x`, `diff y` and `delta` variables for `distance2d` and `from 2d`, `to 2d`, `diff x`, `diff y` and `delta` variables for `distance3d`. Both functions should return the variable `delta`. (Format the variables according to the language you're using: `diff_x` and `diffX` will both be A-OK.)
	This is a repeat of the first point. This will ensure all languages will have the same general structure, but how you calculate these values can be in any way possible.
* You have properly updated the table of languages in the README.
	Make sure all the required information is included in the table, as well as the language count is incremented.
	
## Add a language notices
In case the language you're adding doesn't come pre-packed with the required functions, feel free to add them in yourself, as long as they produce the expected result.
