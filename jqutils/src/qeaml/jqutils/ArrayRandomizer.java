package qeaml.jqutils;

import java.util.ArrayList;
import java.util.Random;

public class ArrayRandomizer<T>{
	private ArrayList<T> array;
	private Random random;
	
	public ArrayRandomizer(ArrayList<T> srcArray){
		array = srcArray;
		random = new Random();
	}
	
	public ArrayList<T> randomize(){
		ArrayList<T> tmp = new ArrayList<T>();
		ArrayList<T> tmp2 = array;
		
		for(int i = 0; i < array.size(); i++){
			T value = array.get(random.nextInt(array.size()));
			tmp.add(value);
			tmp2.removeIf(entry -> entry == value);
		}
		
		return tmp;
	}
}