# jqutils
`jqutils` is a set of constants and utility classes for Java.

# How to build
1. Open `cmd`.
2. `git clone` this repository.
3. Simply use `build`.

This process will generate a `jqutils.jar` in the root folder of the cloned repo. You can now use this instead of a JAR you'd download from the releases page. 

# How to use
1. Build the JAR from source or download a JAR from the releases page.
2. Put the JAR in your [`%CLASSPATH%`](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/classpath.html) folder.
3. Add this to your code: `import qeaml.jqutils.*;`

You can now use all the classes provided by jqutils in your code:

# Classes

## `JQ`
Contains a utility `print(String)` method, and utility constants (like alphabet, punctuation etc.)

## `ArrayGenerator`
Constructor:
```java
ArrayGenerator<T>(ArrayList<T>);
```
Example:
```java
package example;

import java.util.ArrayList;
import qeaml.jqutils.*;

public class ArrayGeneratorExample{
	public static void main(String[] argv){
		ArrayList fruits = new ArrayList<String>();
		fruits.add("apple");
		fruits.add("banana");
		fruits.add("grape");
		ArrayGenerator gen = new ArrayGenerator<String>(fruits);
		//generates ArrayList of randomly chosen elements from fruits ArrayList
		ArrayLits random = gen.generate(10);
		JQ.print(random.toString());
	}
}
```

## `ArrayRandomizer`
Constructor:
```java
ArrayRandomizer<T>(ArrayList<T>);
```
Example:
```java
package example;

import java.util.ArrayList;
import qeaml.jqutils.*;

public class ArrayRandomizerExample{
	public static void main(String[] argv){
		ArrayList fruits = new ArrayList<String>();
		fruits.add("apple");
		fruits.add("banana");
		fruits.add("grape");
		ArrayRandomizer rando = new ArrayRandomizer<String>(fruits);
		//generates ArrayList of elements from fruits in random order
		ArrayLits random = gen.randomize();
		JQ.print(random.toString());
	}
}
```