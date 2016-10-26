package com.hackerrank.java.introduction;

import java.text.NumberFormat;
import java.util.Locale;
import java.util.Scanner;

public class CurrencyFormatter {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		double payment = scanner.nextDouble();
		scanner.close();

		NumberFormat formatter = NumberFormat.getCurrencyInstance(Locale.US);
		System.out.printf("US: %s%n", formatter.format(payment));
		formatter = NumberFormat.getCurrencyInstance(new Locale("en", "in"));
		System.out.printf("India: %s%n", formatter.format(payment));
		formatter = NumberFormat.getCurrencyInstance(Locale.CHINA);
		System.out.printf("China: %s%n", formatter.format(payment));
		formatter = NumberFormat.getCurrencyInstance(Locale.FRANCE);
		System.out.printf("France: %s%n", formatter.format(payment));
	}

}
