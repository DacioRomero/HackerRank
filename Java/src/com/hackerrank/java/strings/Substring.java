package com.hackerrank.java.strings;

import java.util.Scanner;

public class Substring {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		String string = scanner.next();
		int start = scanner.nextInt();
		int end = scanner.nextInt();

		scanner.close();

		System.out.println(string.substring(start, end));
	}
}
