package qeaml.jqutils;

import java.util.Random;

public class JQ{
	public static String VERSION = "1.1.0";
	public static int VERSIONNUM = 0x010100;
	
	public static String alphabet = "abcdefghijklmnopqrstuwvxyz";
	public static String numbers = "1234567890";
	public static String consonants = "bcdfghjklmnpqrstwvxyz";
	public static String vowels = "aeiou";
	public static String punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
	public static String chars = alphabet+numbers+punctuation;
	public static String whitespace = " \t\n\r";
	public static Random random = new Random();
	

	public static void print(Object o){
		System.out.println(o.toString());
	}
}