#MA. LEAH JOHANNAH A. ERMAC BSCS-III
#2015-1030

import fileinput

fname = raw_input("\nEnter your file name: ")
file_name = open(fname, 'a+')
file_name.close()

print("\n--------------------------------------------------------------------------------")
print("This program will ADD, DELETE, UPDATE, SEARCH and PRINT a student's basic info.")
print("--------------------------------------------------------------------------------")

while True:

	option = raw_input("\n\tSelect one: ADD, DELETE, UPDATE, SEARCH or PRINT: ")

	if(option == "ADD"):
		opt_add = open(fname, 'a+')
		
		while True:
			
			id_num = raw_input("\nEnter your ID number: ") + " "
			name = raw_input("\nEnter your full name: ") + " "
			course = raw_input("\nEnter your course: ") + " "
			stud_info = id_num + name + course + '\n'
			
			file_name2 = open(fname, 'a+')
			file_name2.write(stud_info)
			file_name2.close()

			ch_add = raw_input("\nWant to ADD again? ")
			if ch_add == 'no':
				break
	
	elif(option == "DELETE"):

		while True:

			opt_del = open(fname)
			extra = []
			delete = raw_input("\nEnter the ID number you want to DELETE: ")
			
			for line in opt_del:
				string = line.split()
				if string[0] == delete:
					print("\n" + line + "\nSuccessfully deleted")

				elif not string[0] == delete:
					extra.append(line)
			
			opt_del.close()
			opt_del = open(fname, 'w')
			opt_del.writelines(extra)
			opt_del.close()

			ch_del = raw_input("\nWant to DELETE again? ")
			if ch_del == 'no':
				break

	elif(option == "UPDATE"):
			
			update = raw_input("\nSearch the ID number you want to UPDATE:")
			
			id_num = raw_input("\nEnter the new ID number: ") + " "
			name = raw_input("\nEnter the new full name: ") + " "
			course = raw_input("\nEnter the new course: ") + " "

			replace = id_num + name + course + '\n'

			for line in fileinput.FileInput(fname,inplace = 1):

				if update in line:
					line = line.replace(line, replace)

				print line,
			print("\nSuccessfully updated\n")

	elif(option == "SEARCH"):

			search = raw_input("\nThe ID number you want to search: ")
			fopen = open(fname, 'r')
			print("\n")

			for line in fopen:
				bana = line.split()
				if bana[0] == search:
					print(line)
			fopen.close()

	elif(option == "PRINT"):

			fopen = open(fname, 'r')
			print("\n")
			for line in fopen:
				print(line)
			
			fopen.close()

	choice = raw_input("\nWant to do it again? ")
	if choice == 'no':
		break
