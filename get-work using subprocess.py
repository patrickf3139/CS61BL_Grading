# Author:Patrick Fong
#Though os.system is deprecated and subprocess.call
#is much more flexible, subprocess is much slower 
#and needlessly complicated for the purposes of
#this script. This is version of the script is
#here for reference only and no longer updated.

import subprocess
import os
import sys

ROSTER = """\
cs61bl-ad SUHYOUN_HAN 
cs61bl-ae KEVIN_SHAN-BO_CHIAN 
cs61bl-af NITISH_PADMANABAN 
cs61bl-ag YISHENG_CHAN 
cs61bl-ah SEOK_HWAN_JEE 
cs61bl-ai GARRETT_TAYLOR_GORDON 
cs61bl-aj COLIN_PETER_RODWELL 
cs61bl-ak JUNG_YOUN_KWAK 
cs61bl-al JINGCHEN_WU 
cs61bl-am KEVIN_CHARLES_MARC_DEVROEDE 
cs61bl-an CHARLES_CIRCLAEYS 
cs61bl-aq ANTHONY_CARLOS_MENDOZA 
cs61bl-ar NEERAV_DIXIT 
cs61bl-at MAX_PASHALL_KRALL 
cs61bl-au ZI_YANG_KAN 
cs61bl-av JUNJIE_NG 
cs61bl-aw STANLEY_SZU_LIN_FANG 
cs61bl-ax KIWOOK_LEE 
cs61bl-ay SHYAM_BHAKTA
cs61bl-az ROBERT_MICHAEL_DOOLEY 
cs61bl-ba MIQUEL_LLOBET_SANCHEZ 
cs61bl-bc HEE_HWANG 
cs61bl-bd ZACKERY_RUSSELL_FIELD 
cs61bl-bf TED_AVTAR 
cs61bl-bh CHERYL_HE 
cs61bl-bi CHENNING_ZHANG 
cs61bl-bj SHERRY_LI_XU 
"""

HELPTEXT = """\
Usage: python get-work.py ASSIGNMENT DEADLINE
       python get-work.py -n ASSIGNMENT
       python get-work.py -h

get-work will create a directory named ASSIGNMENT. Within it, each submission for ASSIGNMENT \
with timestamps <= DEADLINE will be retrieved into a directory named its submitter. DEADLINE \
should be given in the form yyyymmddhhmm. Use the -n option to set no deadline.
"""

if __name__ == "__main__":
	if sys.argv[1][0] == "-":
		if sys.argv[1] == "-n":
			#deadline effectively irrelevant
			deadline = "209901010000"
			assignment = sys.argv[2]
		elif sys.argv[1] == "-h":
			print(HELPTEXT)
			sys.exit()
		else:
			print("Invalid options. Use n for no deadline, h for help.")
			sys.exit()
	else:
		assignment = sys.argv[1]
		deadline = sys.argv[2]
		if len(deadline) != 12:
			sys.exit("invalid date given: must be yyyymmddhhmm")

	subprocess.check_call(["mkdir", assignment])
	os.chdir(assignment)
	subprocess.call(["get-submissions", assignment])
	submissions = os.listdir(".")
	#stores logins whose work has already been retrieved to prevent overwriting
	processed = set() 

	subprocess.call(["touch", "late"])
	late_submissions = open("late", "a")
	#This loops processes each link, calling lookat on it if
	#it is on your roster, is not late, and has not already
	#been processed. Since lookat retrieves the latest
	#submission, it is guaranteed to be the latest one
	#that is not late.

	for subm in submissions:
	 	login = subm[0:9]
	 	subm_date = subm[10:]
	 	if login not in ROSTER:
	 		pass
	 	elif subm_date > deadline:
	 		#append late submissions to file late
	 		subprocess.call(["echo", subm], stdout=late_submissions)
	 	elif login not in processed:
	 		subprocess.call(["lookat", "-d", login, subm])
	 		processed.add(login)
	 	subprocess.call(["rm", subm])

	subprocess.call(["touch", "grades"])
	grades_file = open("grades", "a")
	#Add only usernames from roster whose work you have
	#called lookat on to file grades
	for line in ROSTER.split("\n"):
		if line[0:9] in processed:
			subprocess.call(["echo", line], stdout=grades_file)