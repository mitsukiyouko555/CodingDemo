# use this for testing the remove functions with file objects
lines = []
file2 = open("file.txt" , "r+")
file2.seek(0)

while True:
		userInput = input("Pick 1 to remove last line; 2 to remove a specific line. (Type exit to exit)\n\n")

		if userInput != "exit" and userInput == str(1):
				lines = file2.readlines()
				file2.seek(0)
				file2.truncate()
				file2.writelines(lines[:-1])
				for index, value in enumerate(lines,1):
					print(("{}.{}\n\n".format(index,value)))
				continue

		elif userInput == str(2):
			taskToRemove = input("input the number of the task you want to remove: \n\n")
			with open("file.txt", "r+") as file2:
				lines = file2.readlines()
				file2.seek(0)				
				file2.truncate()
				file2.writelines(lines[int(taskToRemove)-1])
				for index, value in enumerate(file2,1):
					print(("{}.{}\n\n".format(index,value)))
				break

		elif userInput == str("exit"):
			file2.close()
			break
