import sys
import os

if __name__ == "__main__":
	folder = sys.argv[1]

	os.system("cp TestMeasurement.java " + folder)
	os.chdir(folder)
	os.system("javac TestMeasurement.java")
	os.system("java TestMeasurement")
	# print("***************************************")
	# os.system("cat MeasurementTest.java")
	# print()