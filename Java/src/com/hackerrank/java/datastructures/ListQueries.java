package com.hackerrank.java.datastructures;

import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class ListQueries {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		List<Integer> ints = new ArrayList<Integer>();

		int capacity = scanner.nextInt();
		
		for (int i = 0; i < capacity; i++) {
			ints.add(scanner.nextInt());
		}
		
		for (int i = scanner.nextInt(); i >= 0; i--) {
			switch(scanner.next()) {
				case "Insert":
					ints.add(scanner.nextInt(), scanner.nextInt());
					break;
				case "Delete":
					ints.remove(scanner.nextInt());
					break;
			}
		}
		
		scanner.close();
		
		System.out.println(ints.toString().replaceAll("[|]|,", ""));
	}
}
