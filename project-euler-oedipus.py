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

	elif (p == 6):
		numbers = range(1, 101)
		sumA = sumB = 0
		for n in numbers:
			sumA += n*n
		for n in numbers:
			sumB += n
		sumB = sumB*sumB
		myAnswer = sumB - sumA

	elif (p == 8):
		num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
		stringNum = str(num)
		

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
