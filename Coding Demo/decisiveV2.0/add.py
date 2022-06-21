file1 = open("file.txt" , "r+")

# T = ["Plotbuilding - character connections/ships \n", "Plotbuilding - subplots \n", "Plotbuilding - main plot structure \n", "Plotbuilding - worldbuilding \n", "Storyboard - Trailer \n", "Learn Music Making - Piano Basics (20 hrs of practice) \n", "Learn Music Making - Epic Music Cover of the Halloween Soundtrack \n", "Learn Music Making - Epic Music Cover of the Requiem for a Dream Soundtrack \n", "Learn Music Making - Song-Write for any of the trailers \n", "Website Art - MC Animations \n", "Website Art - Character Front/Back \n", "Website Art - Setting Hexagons \n", "Website Art - Setting Images \n", "Website Art - Setting INNER Images \n", "2D Asset Creation - Shops/Restaurants \n", "2D Asset Creation - Environments \n", "2D Asset Creation - Weapons \n", "2D Asset Creation - Creatures \n", "2D Asset Creation - Implants (External and Internal) \n", "2D Asset Creation - Crowds \n", "2D Asset Creation - Robots \n", "2D Asset Creation - Everyday Worldbuilding things (what would you see if you were walking on the streets in this world) \n", "Hacking - CTF/Practice \n", "Hacking - Find something to add to blog to boost experience \n", "Animate a cool Fight Scene or something \n", "Practice Art Fundimentals for 30 Mins to 1 hr - Draw a Box Lessons \n", "Practice Art Fundimentals for 30 Mins to 1 hr - Gesture/Anatomy Practice \n", "Practice Art Fundimentals for 30 Mins to 1 hr - Expressions \n", "Practice Art Fundimentals for 30 Mins to 1 hr - Dynamic Poses \n", "Make a Mini 10 Panel Comic for Fun"]

# file1.writelines(T)
file1.seek(0)
# print("\n".join(file1.readlines()))

for index, value in enumerate(file1,1):
	print(("{}.{}\n\n".format(index,value)))

while True:
	userInput = input("type something: \n")
	if userInput != "exit":
		file1.writelines("\n"+ userInput)		
		file1.seek(0)
		for index, value in enumerate(file1,1):
			print(("{}.{}\n\n".format(index,value)))
	
	# elif userInput != "exit" or userInput == str(2):


	else:
		file1.close()
		break


# file1.close()

#--------------------------------------------------
# yay it works!!! DIS RITE HERE!!

# for index, value in enumerate(file1,1):
# 	print(("{}.{}\n\n".format(index,value)))

#--------------------------------------------------

# this does what i want but does not show index:
#print("\n".join(file1.readlines()))

#---------------------------------------------------

# this doesnt quite do what i want it to do - just keeps repeating the first index on each iteration:
# for index, value in enumerate(file1,1):
# 	print(("{}.{}\n\n".format(index,value)).join(file1.readlines()))

#---------------------------------------------------

#orignal - no file version - from list within pythoh:
# for index, value in enumerate(tasks,1):
# 	print("{}.{}\n\n".format(index,value))

# ----------------------------------------------------

# Plotbuilding - character connections/ships
# Plotbuilding - subplots
# Plotbuilding - main plot structure
# Plotbuilding - worldbuilding
# Storyboard - Trailer
# Learn Music Making - Piano Basics (20 hrs of practice)
# Learn Music Making - Epic Music Cover of the Halloween Soundtrack
# Learn Music Making - Epic Music Cover of the Requiem for a Dream Soundtrack
# Learn Music Making - Song-Write for any of the trailers
# Website Art - MC Animations
# Website Art - Character Front/Back
# Website Art - Setting Hexagons
# Website Art - Setting Images
# Website Art - Setting INNER Images
# 2D Asset Creation - Shops/Restaurants
# 2D Asset Creation - Environments
# 2D Asset Creation - Weapons
# 2D Asset Creation - Creatures
# 2D Asset Creation - Implants (External and Internal)
# 2D Asset Creation - Crowds
# 2D Asset Creation - Robots
# 2D Asset Creation - Everyday Worldbuilding things (what would you see if you were walking on the streets in this world)
# Hacking - CTF/Practice
# Hacking - Find something to add to blog to boost experience
# Animate a cool Fight Scene or something
# Practice Art Fundimentals for 30 Mins to 1 hr - Draw a Box Lessons
# Practice Art Fundimentals for 30 Mins to 1 hr - Gesture/Anatomy Practice
# Practice Art Fundimentals for 30 Mins to 1 hr - Expressions
# Practice Art Fundimentals for 30 Mins to 1 hr - Dynamic Poses
# Make a Mini 10 Panel Comic for Fun


