package qeaml.jqutils;

import java.util.ArrayList;
import java.util.Random;

public class ArrayGenerator<T>{
	private ArrayList<T> array;
	private Random random;
	
	public ArrayGenerator(ArrayList<T> srcArray){
		array = srcArray;
		random = new Random();
	}
	
	public ArrayList<T> generate(int length){
		ArrayList<T> tmp = new ArrayList<T>();
		
		for(int i = 0; i < length; i++){
			T value = array.get(random.nextInt(array.size()));
			tmp.add(value);
		}
		
		return tmp;
	}
}