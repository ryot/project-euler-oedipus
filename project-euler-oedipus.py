# ---------------------------------------------------
# Project Euler Problem Solver by Ryo Tulman 7/10/13
# ---------------------------------------------------
# A dual-purpose exercise in refreshing my math skills and learning Python
# Thank you Tuhin Srivasta @Gumroad for introducing me to Project Euler

import sys
import math
from datetime import datetime

def oedipus(p):
	start = datetime.now()
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

	elif (p == 3):
		num = 600851475143
		currDivisor = 2
		while num > 1:
			if num%currDivisor == 0:
				num /= currDivisor
				currDivisor = 2
			else:
				currDivisor += 1
				myAnswer = currDivisor
	
	elif (p == 4):
		for a in range(100, 1000):
			for b in range(100, 1000):
				p = a * b
				prod = str(p)
				prodReversed = prod[::-1]
				if prodReversed == prod:
					if int(prod) > myAnswer:
						myAnswer = int(prod)

	elif (p == 5):
		myAnswer = math.factorial(20)
		divisors = range(1, 21)
		answerFound = False
		while answerFound is False:
			startAnswer = myAnswer
			for n in divisors:
				testQuotient = myAnswer/n
				works = True
				for p in divisors:
					if testQuotient%p != 0:
						works = False
						break
				if works is True:
					myAnswer = testQuotient
			if myAnswer == startAnswer:
				answerFound = True

	else:
		myAnswer = "I'm stumped. Goodbye world."

	end = datetime.now()
	print myAnswer
	print end - start
	print "THE END"


print "Meet Ryo's Oedipus, slayer of the Project Euler Sphinx."
problemNumber = int(input('Which problem troubles you? '))
oedipus(problemNumber)
sys.exit()
