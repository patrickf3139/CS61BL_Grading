#!/bin/python

# Author:Patrick Fong

import sys
import os

if __name__ == "__main__":
	folder = sys.argv[1]

	os.chdir(folder)
	os.system("rm -f output")
	os.system("cp ../first10primes.txt .")
	os.system("javac PrimeGenerator.java")

	for i in range(1, 11):
		os.system("java PrimeGenerator " + str(i) + " | cut -d' ' -f5 >> output")
	os.system("diff output first10primes.txt")
	os.system("time -p java PrimeGenerator 10000")
	os.system("rm first10primes.txt")
	