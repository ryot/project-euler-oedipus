# ---------------------------------------------------
# Project Euler Problem Solver by Ryo Tulman 7/10/13
# ---------------------------------------------------
# A dual-purpose exercise in refreshing my math skills and learning Python
# Thank you Tuhin Srivasta @Gumroad for introducing me to Project Euler

import sys

def oedipus(p):
	myAnswer = 0

	if (p == 1):
		for x in range(0, 1000):
			if x%3 or x%5 is 0:
				myAnswer += x

	elif (p == 2):
		prev = 1
		curr = 2
		while curr < 4000000:
			if curr%2 is 0:
				myAnswer += curr
			new = curr + prev
			prev = curr
			curr = new

	# elif (p == 3):
	# 	#find largest prime factor of num
	# 	num = 600851475143
	# 	myAnswer = 2
	# 	while num%myAnswer != 0:
	# 		myAnswer += 1
	
	else:
		myAnswer = "I'm stumped. Goodbye world."

	print myAnswer
	print "THE END"


print "Meet Ryo's Oedipus, slayer of the Project Euler Sphinx."
problemNumber = int(input('Which problem troubles you? '))
oedipus(problemNumber)
sys.exit()
