import sqlite3

print("Should be in <.db>")
data_name = raw_input("\nEnter your database name: ") + '.db'

dots = sqlite3.connect(data_name)
curs = dots.cursor()

class Student (object):

    def __init__(self, firstName, middleInit, lastName, idNum, Course):
        self.fname = firstName
        self.min = middleInit
        self.lname = lastName
        self.idnum = idNum
        self.course = Course



def create_table():
    curs.execute('CREATE TABLE IF NOT EXISTS studentRecord(FirstName TEXT, MiddleInitial TEXT, LastName TEXT, ID TEXT, Course TEXT)')

def add_entry(student):
    curs.execute("INSERT INTO studentRecord (FirstName, MiddleInitial, LastName, ID, Course) VALUES (?,?,?,?,?)",
        (student.fname, student.min, student.lname, student.idnum, student.course))
    dots.commit()

def delete_entry():
    idno = raw_input("\nEnter the ID Number: ")
    curs.execute("DELETE FROM studentRecord WHERE ID = ?", (idno,))
    dots.commit()

def search_entry():
    select = raw_input("\nEnter the ID Number: ")
    curs.execute("SELECT * FROM studentRecord where ID = ?", (select,))
    for row in curs.fetchall():
        print (row)

def update_entry():
    select = raw_input("\nEnter the ID Number: ")
    choice = raw_input("\nWhat do you want to update? \n>>>FName\n>>>LName\n>>>MInitial\n>>>Course\n\n>>>")
    if choice == "FName":
        change = raw_input("\nEnter new first name: ")
        dots.execute("UPDATE studentRecord set FirstName = ? where ID = ?", (change,select,))
        dots.commit()
    elif choice == "LName":
        change = raw_input("\nEnter new last name: ")
        dots.execute("UPDATE studentRecord set LastName = ? where ID = ?", (change,select,))
        dots.commit()
    elif choice == "MInitial":
        change = raw_input("\nEnter new middle initial: ")
        dots.execute("UPDATE studentRecord set MiddleInitial = ? where ID = ?", (change,select,))
        dots.commit()
    elif choice == "Course":
        change = raw_input("\nEnter new course: ")
        dots.execute("UPDATE studentRecord set Course = ? where ID = ?", (change,select,))
        dots.commit()

def sort_entry():
    choice = raw_input("\nSort how?: LName, ID, Course: \n>>>")
    print("\n")
    if choice == "LName":
        curs.execute("SELECT*FROM studentRecord ORDER BY LastName ASC")
        for row in curs.fetchall():
            print(row)
        dots.commit()
    if choice == "ID":
        curs.execute("SELECT*FROM studentRecord ORDER BY ID ASC")
        for row in curs.fetchall():
            print(row)
        dots.commit()
    if choice == "Course":
        curs.execute("SELECT*FROM studentRecord ORDER BY Course ASC")
        for row in curs.fetchall():
            print(row)
        dots.commit()
def prints():
    curs.execute("SELECT*FROM studentRecord")
    print("\n")
    for row in curs.fetchall():
        print (row)




def main():
    create_table()
    prints()
    while(True):

        choice1 = raw_input("\nChoose: ADD, DELETE, UPDATE, SORT, SEARCH, PRINT: ")
        if choice1 == "ADD":
            fn = raw_input("\nFirst Name: ")
            mi = raw_input("\nMiddle Initial: ")
            ln = raw_input("\nLast Name: ")
            i = raw_input("\nID Number: ")
            co = raw_input("\nCourse: ")
            student = Student(fn, mi, ln, i, co)
            add_entry(student)
        if choice1 == "DELETE":
            delete_entry()
        if choice1 == "SEARCH":
            search_entry()
        if choice1 == "UPDATE":
            update_entry()
        if choice1 == "SORT":
            sort_entry()
        if choice1 == "PRINT":
            prints()

        choice2 = raw_input("\nDo you want to exit? Y/N: ")
        if choice2 == "Y":
            break


    prints()
    curs.close()
    dots.close()


if __name__ == '__main__':
    main()