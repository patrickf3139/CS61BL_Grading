#! /usr/bin/python
# Author: Patrick Fong
# Updated: 05/19/2014

import os
import sys

ROSTER = """\
Edit this string to contain your students' logins and names, one student per line.
Format below:
cs61bl-x1 FIRST_MIDDLE_LAST1
cs61bl-x2 FIRST_MIDDLE_LAST2
...
"""

HELPTEXT = """\
Usage: get-work.py DEADLINE ASSIGNMENT 
       get-work.py -n ASSIGNMENT
       get-work.py -h

get-work will create a directory named ASSIGNMENT. Within it, each submission for ASSIGNMENT \
with timestamps <= DEADLINE will be retrieved into a directory named after its submitter. \
DEADLINE should be given in the form yyyymmddhhmm. Use the -n option to download all \
assignments, ignoring deadline.
"""

if __name__ == "__main__":
	if sys.argv[1][0] == "-":
		if sys.argv[1] == "-n":
			# use a deadline that is effectively irrelevant
			deadline = "209904200000"
			assignment = sys.argv[2]
		elif sys.argv[1] == "-h":
			print(HELPTEXT)
			sys.exit()
		else:
			print("Invalid arguments. Use n for no deadline, h for help.")
			sys.exit()
	else:
		deadline = sys.argv[1]
		assignment = sys.argv[2]
		if len(deadline) != 12 or not deadline.isdigit():
			sys.exit("invalid date given: must be yyyymmddhhmm")

	os.system("mkdir " + assignment)
	os.chdir(assignment)
	os.system("get-submissions " + assignment)

	# maps logins to the timestamp of the latest subm unpacked for that login
	time_stamps = dict() 

	# This loops processes each link, calling lookat on it if
	# it is on your roster, is not late, but is later than the subm 
	# already unpacked for that login. os.listdir does not output in
	# a sorted manner so timestamps have to be tracked
	for subm in os.listdir("."):
	 	login = subm[0:9]
	 	subm_date = subm[10:]
	 	if login not in ROSTER:
	 		pass
	 	elif subm_date > deadline:
	 		os.system("echo " + subm.replace(".", " : ", 1) + " >> late")
	 	# unpack subm if subm_date is later than that of the last subm for this login unpacked
	 	elif subm_date > time_stamps.get(login, 0):
	 		os.system("lookat -d " + login + " " + subm)
	 		time_stamps[login] = subm_date
	 	os.system("rm " + subm)

	# Add to file grades only logins from roster whose 
	# work you have called lookat on 
	for line in ROSTER.split("\n"):
		if line[0:9] in time_stamps:
			os.system("echo " + line + ">> grades")