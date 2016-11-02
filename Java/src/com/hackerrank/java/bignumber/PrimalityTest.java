package com.hackerrank.java.bignumber;

import java.math.BigInteger;
import java.util.Scanner;

public class PrimalityTest {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		BigInteger bigInteger = scanner.nextBigInteger();
		scanner.close();
		
		System.out.println((bigInteger.isProbablePrime(0) ? "" : "not ") + "prime");
	}
}
