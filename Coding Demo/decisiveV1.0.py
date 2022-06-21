# this program will have a list of things i want to do but cant decide which one to work on.
# it will randomly pick one for me to work on
# eventually it will be able to add or remove tasks to the list via user input
# prompt will either give an option to roll the dice or add or remove a task

# Tasks:

# "1. Plotbuilding - character connections/ships" 
# , "2. Plotbuilding - subplots" 
# , "3. Plotbuilding - main plot structure" 
# , "4. Plotbuilding - worldbuilding" 

# , "5. Storyboard - Trailer" 

# , "6. Learn Music Making - Piano Basics (20 hrs of practice)" 
# , "7. Learn Music Making - Epic Music Cover of the Halloween Soundtrack" 
# , "8. Learn Music Making - Epic Music Cover of the Requiem for a Dream Soundtrack" 
# , "9. Learn Music Making - Song-Write for any of the trailers" 

# , "10. Website Art - MC Animations" 
# , "11. Website Art - Character Front/Back" 
# , "12. Website Art - Setting Hexagons" 
# , "13. Website Art - Setting Images" 
# , "14. Website Art - Setting INNER Images" 

# , "15. 2D Asset Creation - Shops/Restaurants" 
# , "16. 2D Asset Creation - Environments" 
# , "17. 2D Asset Creation - Weapons" 
# , "18. 2D Asset Creation - Creatures" 
# , "19. 2D Asset Creation - Implants (External and Internal)" 
# , "20. 2D Asset Creation - Crowds" 
# , "21. 2D Asset Creation - Robots" 
# , "22. 2D Asset Creation - Everyday Worldbuilding things (what would you see if you were walking on the streets in this world)" 

# , "23. Hacking - CTF/Practice" 
# , "24. Hacking - Find something to add to blog to boost experience" 

# , "25. Animate a cool Fight Scene or something" 

# , "26. Practice Art Fundimentals for 30 Mins to 1 hr - Draw a Box Lessons" 
# , "27. Practice Art Fundimentals for 30 Mins to 1 hr - Gesture/Anatomy Practice" 
# , "28. Practice Art Fundimentals for 30 Mins to 1 hr - Expressions" 
# , "29. Practice Art Fundimentals for 30 Mins to 1 hr - Dynamic Poses" 

# ", 30. Make a Mini 10 Panel Comic for Fun"

import random

#-------------------------------------------------------------------------------------
#This is a list of tasks. Need to use something that keeps data like pickle but here is what i have for now so far:
#-------------------------------------------------------------------------------------

tasks = ["Plotbuilding - character connections/ships", "Plotbuilding - subplots", "Plotbuilding - main plot structure", "Plotbuilding - worldbuilding" , "Storyboard - Trailer", "Learn Music Making - Piano Basics (20 hrs of practice)" , "Learn Music Making - Epic Music Cover of the Halloween Soundtrack" , "Learn Music Making - Epic Music Cover of the Requiem for a Dream Soundtrack" , "Learn Music Making - Song-Write for any of the trailers" , "Website Art - MC Animations" , "Website Art - Character Front/Back" , "Website Art - Setting Hexagons", "Website Art - Setting Images" , "Website Art - Setting INNER Images" , "2D Asset Creation - Shops/Restaurants" , "2D Asset Creation - Environments" , "2D Asset Creation - Weapons", "2D Asset Creation - Creatures" , "2D Asset Creation - Implants (External and Internal)", "2D Asset Creation - Crowds" , "2D Asset Creation - Robots", "2D Asset Creation - Everyday Worldbuilding things (what would you see if you were walking on the streets in this world)" , "Hacking - CTF/Practice", "Hacking - Find something to add to blog to boost experience", "Animate a cool Fight Scene or something" , "Practice Art Fundimentals for 30 Mins to 1 hr - Draw a Box Lessons" , "Practice Art Fundimentals for 30 Mins to 1 hr - Gesture/Anatomy Practice" , "Practice Art Fundimentals for 30 Mins to 1 hr - Expressions" , "Practice Art Fundimentals for 30 Mins to 1 hr - Dynamic Poses", "Make a Mini 10 Panel Comic for Fun"]


banner = ("-")*50 + "\n" + "\n" + """    DECISIVE - By みつき \n
    |\  |---  /- || (-- || \    / |---
    | | |--- |   ||  \  ||  \  /  |---
    |/  |---  \- || __) ||   \/   |---
""" + "\n" + "\n"+ ("-")*50


urTaskBanner = """
 \ -\  /-/ /------\  |--  --| |------\\
  \-\ /-/  | |--| |  | |  | | | [  ] |
   | | |   | |__| |  | \__/ | | |\ --/
   |___|   \ _____/  \______| |_| \__\
\n
   -------  /----\  /-----\  |-| /--/ 
   |_   _| | [  ] | \_____   |  /  /   []
     | |   | |--| | ----- \  |  \  \    
     |_|   |_|  |_| \_____/  |_| \__\  []
       

"""


print("\n" + banner+ "\n")

#-------------------------------------------------------------------------------------
#print the list in the format of index, value with each list item separated by 2 lines:
#-------------------------------------------------------------------------------------

for index, value in enumerate(tasks,1):
	print("{}.{}\n\n".format(index,value))

#while true (input != exit or 4) ask these questions: Pick an option: 1. Random Task; 2. Add a Task to the list; 3. Remove a task from list; 4. Exit

while True:

	try:
		userInput = input("\n \n" + (("-")*50) +"\n"+ "\n" "Pick An Option: \n \n 1. Random Task \n \n 2. Add a task/tasks to the list \n \n 3. Remove a task/tasks from list \n \n 4. Exit" + "\n" + "\n" + (("-")*50)+ "\n" + "YOUR CHOICE: ")
#-------------------------------------------------------------------------------------
#if Random Task (1) is picked, display a random item from the list:
#-------------------------------------------------------------------------------------

		if userInput == str(1):
			print((("-")*50)+ "\n" + urTaskBanner + random.choice(tasks) + "\n")
			continue
			# this works

#-------------------------------------------------------------------------------------
#if Add Task/tasks is selected (2), ask if they want to add task, show task list, or go back:
#-------------------------------------------------------------------------------------

		elif userInput == str(2):
		# add a task/tasks to the list - allow user to add one or more tasks to the list - appends it to the bottom (include a show task list button) (1.Add Task, 2.Show Task List , 3. back)
			addTask = input("\n \n" + (("-")*50) +"\n"+ "\n" "Pick An Option: \n \n 1. Add Task \n \n 2. Show Task List \n \n 3. Back" + "\n" + "\n" + (("-")*50)+ "\n" + "YOUR CHOICE: "+ "\n")
			while addTask != str(3):

#-------------------------------------------------------------------------------------
#if Add task is selected, add the item to the bottom of the list and display list in the format of index, value with each list item separated by 2 lines:
#-------------------------------------------------------------------------------------

				if addTask == str(1):
					appendInput = input("Task to Add to List: (Press Crtl+C to go back.)\n\n")
					tasks.append(appendInput)
					print("\n\n")
					for index, value in enumerate(tasks,1):
						print("{}.{}\n\n".format(index,value))
					continue
			# this works

#-------------------------------------------------------------------------------------
#if show task list (2) was selected, display the UPDATED list in the format of index, value with each list item separated by 2 lines
#-------------------------------------------------------------------------------------

				elif addTask == str(2):
					print("\nShow Task List:\n")
					for index, value in enumerate(tasks,1):
						print("{}.{}\n\n".format(index,value))
					break
			# this works

#-------------------------------------------------------------------------------------
#if break (3) go back to main prompt
#-------------------------------------------------------------------------------------

				elif addTask == str(3):
					break
#-------------------------------------------------------------------------------------
#if user enters something othe than the valid options, note "please select 1,2, or 3"
#-------------------------------------------------------------------------------------

			# this works
				elif addTask != str(1) or addTask != str(2) or addTask != str(3):
					print("Please Select 1, 2, or 3")
					break

#-------------------------------------------------------------------------------------
#if Remove a task/tasks from list from the original prompt was selected, ask if user wants to remove task, show task list, or go back
#-------------------------------------------------------------------------------------

		elif userInput == str(3):
			removeTask = input("\n \n" + (("-")*50) +"\n"+ "\n" "Pick An Option: \n \n 1. Remove Task \n \n 2. Show Task List \n \n 3. Back" + "\n" + "\n" + (("-")*50)+ "\n" + "YOUR CHOICE: "+ "\n")
			while removeTask != str(3):

#-------------------------------------------------------------------------------------
# From the removeTask list, if 1, remove task is selected, ask user if they want to remove task based on number, remove bottom-most task, or go back.
#-------------------------------------------------------------------------------------

				if removeTask == str(1):
					removeTaskPrompt = input("\n \n" + (("-")*50) +"\n"+ "\n" "Pick An Option: \n \n 1. Remove a Task Based on Number \n \n 2. Remove Last/Bottom-Most Task \n \n 3. Back" + "\n" + "\n" + (("-")*50)+ "\n" + "YOUR CHOICE: "+ "\n")

#-------------------------------------------------------------------------------------
#if remove task based on number is selected, take user input and -1 (as first item in the list starts from 0. if you didnt do this if the user enters 5 it would remove 6 istead of 5. this makes it so that if u pick 5 it actually removes 5)
# then it displays the UPDATED list in the format of index, value with each list item separated by 2 lines
#-------------------------------------------------------------------------------------

					if removeTaskPrompt == str(1):
						numberToRemove = input("Enter the Number of the Item you want to remove from the list: \n\n")
						removeDTaskList = tasks.pop(int(numberToRemove) - 1)
						
						# ^ YAY it works! remove a task based on number or remove last/bottom-most task (pop user input -1)
						
						print("\nShow Task List:\n")
						for index, value in enumerate(tasks,1):
							print("{}.{}\n\n".format(index,value))
						continue				

#-------------------------------------------------------------------------------------
#if remove last/bottom-most task (2) is selected, it removes the last item on the list and displays the UPDATED list in the format of index, value with each list item separated by 2 lines
#-------------------------------------------------------------------------------------

					elif removeTaskPrompt == str(2):
						tasks.pop(-1)
						print("\nShow Task List:\n")
						for index, value in enumerate(tasks,1):
							print("{}.{}\n\n".format(index,value))
							continue
	
#-------------------------------------------------------------------------------------
#if back (3) is selected break out of inner loop
#-------------------------------------------------------------------------------------

					elif removeTaskPrompt == str(3):
							break
#-------------------------------------------------------------------------------------
#if user enters something othe than the valid options, note "please select 1,2, or 3"
#-------------------------------------------------------------------------------------

					elif removeTaskPrompt != str(1) or removeTaskPrompt != str(2) or removeTaskPrompt != str(3):
						print("Please Select 1, 2, or 3")
						continue

#-------------------------------------------------------------------------------------
#if show task list (2) was selected, display the UPDATED list in the format of index, value with each list item separated by 2 lines
#-------------------------------------------------------------------------------------

			#removetask 2 - show task list
				elif removeTask == str(2):
							print("\nShow Task List:\n")
							for index, value in enumerate(tasks,1):
								print("{}.{}\n\n".format(index,value))
							break
			# this works

#-------------------------------------------------------------------------------------
#if back (3) is selected break out of inner loop
#-------------------------------------------------------------------------------------	

			#removetask 3 - back
				elif removeTask == str(3):
					break

#-------------------------------------------------------------------------------------
#if user enters something othe than the valid options, note "please select 1,2, or 3"
#-------------------------------------------------------------------------------------

				elif removeTask != str(1) or removeTask != str(2) or removeTask != str(3):
					print("Please Select 1, 2, or 3")
					break

			# this works

#-------------------------------------------------------------------------------------
#if Exit (4) is selected, it quits the program
#-------------------------------------------------------------------------------------

		elif userInput == str(4):
			break
			# this works

#-------------------------------------------------------------------------------------
#on the initial prompt, if user enters something othe than the valid options, note "please select 1,2, 3 or 4"
#-------------------------------------------------------------------------------------

		elif userInput != str(1) or userInput != str(2) or userInput != str(3) or userInput != str(4):
			print("Please Select 1, 2, 3, or 4")
			continue
			# this works
#-------------------------------------------------------------------------------------
#forgot what this does, but except has to be there or it will throw an error and putting anything except pass messes up the rest of the code functions.
#-------------------------------------------------------------------------------------
	except:
		pass


#-----------------------------------
#Testing

# 1 - WORKS
# 2 - WORKS
# 2-1 - WORKS
# 2-2 - WORKS
# 2-3- WORKS
# 3 - WORKS
# 3-1-1 - WORKS
# 3-1-2 - WORKS
# 3-1-3 - WORKS
# 3-2 - WORKS
# 3-3 - WORKS
# 4 - WORKS
# Overall Invalid Entry - Works
# NESTED Invalid Entry - Works but throws user back into initial prompt loop instead of keeping them in the nested loop.. would like it to not do that but it technically works...

# This Program, with NO Persistence only took me 6 hours to make!
# now all i need to do is get it to write to something that can be kept and updated.

