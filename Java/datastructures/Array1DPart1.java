package com.hackerrank.java.datastructures;

import java.util.Scanner;

public class Array1DPart1 {
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		int[] integers = new int[scanner.nextInt()];

		for (int i = 0; i < integers.length; i++) {
			integers[i] = scanner.nextInt();
		}

		scanner.close();

		for (int i = 0; i < integers.length; i++) {
			System.out.println(integers[i]);
		}
	}
}
