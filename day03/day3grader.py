import sys
import os
import time 

if __name__ == "__main__":
	folder = sys.argv[1]

	os.system("cp TestAccount.java" + " " + folder)
	os.chdir(folder)
	os.system("javac TestAccount.java ")
	os.system("java TestAccount | diff ../outAccountTest - ")
	print("***************************************")
	os.system("cat AccountTester.java")
	os.system("javac AccountTester.java ")
	os.system("java AccountTester")
	print("***************************************")
	os.system("cat bug.info")
	print()