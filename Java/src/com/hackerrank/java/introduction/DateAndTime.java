package com.hackerrank.java.introduction;

import java.util.Scanner;
import java.util.Calendar;

public class DateAndTime {

	public static void main(String[] args) {
		Calendar calendar = Calendar.getInstance();

		Scanner scanner = new Scanner(System.in);

		calendar.set(Calendar.MONTH, 9 - 1);
		calendar.set(Calendar.DAY_OF_MONTH, 5);
		calendar.set(Calendar.YEAR, 2015);

		scanner.close();

		System.out.println(
				java.time.DayOfWeek.of(Math.floorMod(calendar.get(Calendar.DAY_OF_WEEK) - 2, 7) + 1).toString());
	}

}
