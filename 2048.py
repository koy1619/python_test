#! /usr/bin/python

from sys import exit
import random


def comb():
	global line, plus
	
	if line[1] == line[0]:
		line[0] = 2 * line[0]
		line[1] = 0
		plus += line[0]
	elif line[2] == line[0] and line[1] == 0:
		line[0] = 2 * line[0]
		line[2] = 0
		plus += line[0]
	elif line[3] == line[0] and line[1] == 0 and line[2] == 0:
		line[0] = 2 * line[0]
		line[3] = 0
		plus += line[0]

		
	if line[2] == line[1]:
		line[1] = 2 * line[1]
		line[2] = 0
		plus += line[1]
	elif line[3] == line[1] and line[2] == 0:
		line[1] = 2 * line[1]
		line[3] = 0
		plus += line[1]

	if line[3] == line[2]:
		line[2] = 2 * line[2]
		line[3] = 0
		plus += line[2]

	
'''
	while i < 3:
		if line[i + 1] == line[i]:
			line[i] = 2 * line[i]
			line[i + 1] = 0
		i += 1
'''	
def push():
	global line
	i = 0

	while i < 3:
		if line[i] == 0:
			line[i] = line[i + 1]
			line[i + 1] = 0
		i += 1

def move():
	push()
	push()
	push()

def right():
	global a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3, line, plus
	global a0x, a1x, a2x, a3x, b0x, b1x, b2x, b3x, c0x, c1x, c2x, c3x, d0x, d1x, d2x, d3x	
	plus = 0
	
	line = [a3, a2, a1, a0]
	comb()
	move()
	a3x = line[0]
	a2x = line[1]
	a1x= line[2]
	a0x = line[3]

	line = [b3, b2, b1, b0]
	comb()
	move()
	b3x = line[0]
	b2x = line[1]
	b1x = line[2]
	b0x = line[3]
	
	line = [c3, c2, c1, c0]
	comb()
	move()
	c3x = line[0]
	c2x = line[1]
	c1x = line[2]
	c0x = line[3]

	line = [d3, d2, d1, d0]
	comb()
	move()
	d3x = line[0]
	d2x = line[1]
	d1x = line[2]
	d0x = line[3]
	
def left():
	global a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3, line, plus
	global a0x, a1x, a2x, a3x, b0x, b1x, b2x, b3x, c0x, c1x, c2x, c3x, d0x, d1x, d2x, d3x	
	plus = 0
	
	line = [a0, a1, a2, a3]
	comb()
	move()
	a0x = line[0]
	a1x = line[1]
	a2x = line[2]
	a3x = line[3]

	line = [b0, b1, b2, b3]
	comb()
	move()
	b0x = line[0]
	b1x = line[1]
	b2x = line[2]
	b3x = line[3]
	
	line = [c0, c1, c2, c3]
	comb()
	move()
	c0x = line[0]
	c1x = line[1]
	c2x = line[2]
	c3x = line[3]

	line = [d0, d1, d2, d3]
	comb()
	move()
	d0x = line[0]
	d1x = line[1]
	d2x = line[2]
	d3x = line[3]
	
def up():
	global a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3, line, plus
	global a0x, a1x, a2x, a3x, b0x, b1x, b2x, b3x, c0x, c1x, c2x, c3x, d0x, d1x, d2x, d3x	
	plus = 0
	
	line = [a0, b0, c0, d0]
	comb()
	move()
	a0x = line[0]
	b0x = line[1]
	c0x = line[2]
	d0x = line[3]

	line = [a1, b1, c1, d1]
	comb()
	move()
	a1x = line[0]
	b1x = line[1]
	c1x = line[2]
	d1x = line[3]
	
	line = [a2, b2, c2, d2]
	comb()
	move()
	a2x = line[0]
	b2x = line[1]
	c2x = line[2]
	d2x = line[3]

	line = [a3, b3, c3, d3]
	comb()
	move()
	a3x = line[0]
	b3x = line[1]
	c3x = line[2]
	d3x = line[3]
	
def down():
	global a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3, line, plus
	global a0x, a1x, a2x, a3x, b0x, b1x, b2x, b3x, c0x, c1x, c2x, c3x, d0x, d1x, d2x, d3x	
	plus = 0
	
	line = [d0, c0, b0, a0]
	comb()
	move()
	d0x = line[0]
	c0x = line[1]
	b0x = line[2]
	a0x = line[3]

	line = [d1, c1, b1, a1]
	comb()
	move()
	d1x = line[0]
	c1x = line[1]
	b1x = line[2]
	a1x = line[3]
	
	line = [d2, c2, b2, a2]
	comb()
	move()
	d2x = line[0]
	c2x = line[1]
	b2x = line[2]
	a2x = line[3]

	line = [d3, c3, b3, a3]
	comb()
	move()
	d3x = line[0]
	c3x = line[1]
	b3x = line[2]
	a3x = line[3]
	
	
def place():
	global a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3		
	global a0x, a1x, a2x, a3x, b0x, b1x, b2x, b3x, c0x, c1x, c2x, c3x, d0x, d1x, d2x, d3x	

	sum = 0
	table = [a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3]
	
	for point in table:
	
		if point == 0:
			sum += 1
		
	x = random.randint(1, sum) - 1
	z = 0
	
	while z < 16:
		if table[z] == 0:
			if z == x:
#				give_num()
				i = random.randrange(2,6,2)
				table[z] = i
				z = 233
			else: 
				z += 1
		else: 
			z += 1
			x += 1

			if z == 16:
				print "You lose."
				exit(0)
	

	a0 = table[0] 
	a1 = table[1]
	a2 = table[2]	
	a3 = table[3]
	b0 = table[4]
	b1 = table[5]
	b2 = table[6]
	b3 = table[7]
	c0 = table[8]
	c1 = table[9]
	c2 = table[10]
	c3 = table[11]
	d0 = table[12]
	d1 = table[13]
	d2 = table[14]
	d3 = table[15]

	a0x = table[0] 
	a1x = table[1]
	a2x = table[2]	
	a3x = table[3]
	b0x = table[4]
	b1x = table[5]
	b2x = table[6]
	b3x = table[7]
	c0x = table[8]
	c1x = table[9]
	c2x = table[10]
	c3x = table[11]
	d0x = table[12]
	d1x = table[13]
	d2x = table[14]
	d3x = table[15]

def show():
	print """
	%d			%d			%d			%d
	%d			%d			%d			%d
	%d			%d			%d			%d
	%d			%d			%d			%d			
	""" % (a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3)
	
	print "Score:" , score
	
	


#Game Start

print "\nWelcome to 2048!"
print "Join the numbers and get to the 2048 tile!"
print "Use 8246 or WSAD to slide."
print "Input back to undo."
	
a0 = a1 = a2 = a3 = b0 = b1 = b2 = b3 = c0 = c1 = c2 = c3 = d0 = d1 = d2 = d3 = 0	
a0x = a1x = a2x = a3x = b0x = b1x = b2x = b3x = c0x = c1x = c2x = c3x = d0x = d1x = d2x = d3x = 0	
check = 0
undo_allowed = False
score = score0 = score1 =0
plus = 0


line = ["nyan", "nayny", "nyanya", "nyanyan"]

place()
place()
show()

history1 = [a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3]


while True:
	bear = raw_input("\n\nSlide > ")
	
	if bear == "8" or bear == "W" or bear == "w":
		print "UP Slide"
		up()
		score = score + plus
	elif bear == "2" or bear == "S" or bear == "s":
		print "DOWN Slide"
		down()
		score = score + plus
	elif bear == "4" or bear == "A" or bear == "a":
		print "LEFT Slide"
		left()
		score = score + plus
	elif bear == "6" or bear == "D" or bear == "d":
		print "RIGHT Slide"
		right()
		score = score + plus
	elif bear == "back":
		print "Returning to last move..."

	else:
		print "Enter 8246 to slide!" 
		
	table1 = [a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3]
	table2 = [a0x, a1x, a2x, a3x, b0x, b1x, b2x, b3x, c0x, c1x, c2x, c3x, d0x, d1x, d2x, d3x]
	#print table1
	#print table2
	
	if table1 == table2:
		if bear == "back" and undo_allowed == True:
			a0 = history0[0] 
			a1 = history0[1]
			a2 = history0[2]	
			a3 = history0[3]
			b0 = history0[4]
			b1 = history0[5]
			b2 = history0[6]
			b3 = history0[7]
			c0 = history0[8]
			c1 = history0[9]
			c2 = history0[10]
			c3 = history0[11]
			d0 = history0[12]
			d1 = history0[13]
			d2 = history0[14]
			d3 = history0[15]
			history1 = history0
			score = score0
			score1 = score0
			undo_allowed = False
			#print "You can't undo in the next time!"
				
			show()
		elif bear == "back" and undo_allowed == False:
			print "Can't undo in the first move..."
		else:
			print "Can't move like this..."
		
	else:
		for check_win in table2:
			if check_win == 2048 and check == 0:
				print "You win!"
				check = 1
		if undo_allowed == False and bear == "back":
			print "You can only undo once..."
		else:
			undo_allowed = True
			#print "Undo Unlocked"
			
			a0 = a0x
			a1 = a1x
			a2 = a2x
			a3 = a3x
			b0 = b0x
			b1 = b1x
			b2 = b2x
			b3 = b3x
			c0 = c0x
			c1 = c1x
			c2 = c2x
			c3 = c3x
			d0 = d0x 
			d1 = d1x
			d2 = d2x
			d3 = d3x
		
			place()
			show()

			#status save
			history0 = history1
			history1 = [a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3]
			score0 = score1
			score1 = score
		
			#survival check
			up()
			table1 = [a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3]
			table2 = [a0x, a1x, a2x, a3x, b0x, b1x, b2x, b3x, c0x, c1x, c2x, c3x, d0x, d1x, d2x, d3x]
			if table1 != table2:
				print "Keep going!"
			else:
				down()
				table1 = [a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3]
				table2 = [a0x, a1x, a2x, a3x, b0x, b1x, b2x, b3x, c0x, c1x, c2x, c3x, d0x, d1x, d2x, d3x]
				if table1 != table2:
					print "Keep going!"
				else:
					left()
					table1 = [a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3]
					table2 = [a0x, a1x, a2x, a3x, b0x, b1x, b2x, b3x, c0x, c1x, c2x, c3x, d0x, d1x, d2x, d3x]
					if table1 != table2:
						print "Keep going!"
					else:
						right()
						table1 = [a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3]
						table2 = [a0x, a1x, a2x, a3x, b0x, b1x, b2x, b3x, c0x, c1x, c2x, c3x, d0x, d1x, d2x, d3x]
						if table1 != table2:
							print "Keep going!"
						else:
							if check == 0:
								print "You lose. QAQ"
							else:
								print "You can do better."
							
							again = raw_input("Try again? (Y/N)\n>")
							if again == "Y" or again == "y":
								a0 = a1 = a2 = a3 = b0 = b1 = b2 = b3 = c0 = c1 = c2 = c3 = d0 = d1 = d2 = d3 = 0	
								#a0x = a1x = a2x = a3x = b0x = b1x = b2x = b3x = c0x = c1x = c2x = c3x = d0x = d1x = d2x = d3x = 0	
								check = 0
								score = 0
								undo_allowed = False
								place()
								place()
								show()

							else:
								print "See you next time!"
								exit(0)

			a0x = a0
			a1x = a1
			a2x = a2
			a3x = a3
			b0x = b0
			b1x = b1
			b2x = b2
			b3x = b3
			c0x = c0
			c1x = c1
			c2x = c2
			c3x = c3
			d0x = d0 
			d1x = d1
			d2x = d2
			d3x = d3

		
'''		
		table1 = [a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3]
		zero = 0
		for check_lose in table1:
			if check_lose == 0:
				zero = 1
			
		table2 = [a0x, a1x, a2x, a3x, b0x, b1x, b2x, b3x, c0x, c1x, c2x, c3x, d0x, d1x, d2x, d3x]

		print table1
		print table2
		
		left()
		right()
		up()
		down()
		table2 = [a0x, a1x, a2x, a3x, b0x, b1x, b2x, b3x, c0x, c1x, c2x, c3x, d0x, d1x, d2x, d3x]

		print table1
		print table2
		
		if table1 == table2 and zero == 0:
			print "You lose QAQ"
			#exit(0)

'''
