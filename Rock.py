
import random

personPlay = ""
computerPlay = ""
clist = ["r", "p", "s"]

personPlay = input("Enter R, P, or S: ")
computerPlay = random.choice(clist)
personPlay = personPlay.lower()

print("Computer chose: " + computerPlay)

if personPlay=="r":
	if computerPlay=="r":
		print("tie")
	elif computerPlay=="p":
		print("lose")
	else:
		print("win!")
elif personPlay=="p":
	if computerPlay=="r":
		print("win!")
	elif computerPlay=="p":
		print("tie")
	else:
		print("lose")
elif personPlay=="s":
	if computerPlay=="r":
		print("lose")
	elif computerPlay=="p":
		print("win!")
	else:
		print("tie")
else:
	print("what")


# get player's play 

# make player's play uppercase for comparison

# generate computer's play (0,1,2)

# set computer's play depending on the computerInt variable


# see who won (use nested if statements):



