import re
import sys
import time
import webbrowser
def nameRaise(name):
    if re.search("[0-9]",name): 
        raise Exception("Name information cannot contain numbers")
    elif re.search("[.:,;!'^]",name):
        raise Exception("Name information cannot contain punctuation marks")
    elif re.search("^\s",name):
        raise Exception("name information cannot start with a space")


def numRaise(num):
    if re.search("[a-z]",num):
        raise Exception("The number information cannot contain lowercase letters")
    elif re.search("[A-Z]",num):
        raise Exception("The number information cannot contain uppercase letters")
    elif re.search("[.:,;!'^]",num):    
        raise Exception("Number information cannot contain punctuation marks")
    elif re.search("\s",num):    
        raise Exception("Number information cannot contain spaces")
    
def mailRaise(mail):
    if not re.search(".com$",mail):
        raise Exception("Valid mail information must end with '.com'")
    if re.search("\s",mail):
        raise Exception("Mail information cannot contain spaces")    

print("-".center(168,"-"))
print(" |Student registration| ".center(90,"~"))
class students_info:
    def __init__(self):
        self.student = ["Name and Surname","Number","Mail"]
        self.reg_student()
        
    def reg_student(self):
        while True:
            name_surname = input("name and surname: ")        
            try:
                nameRaise(name_surname)
            except Exception as ex:
                print(ex)
            else:   
                break
           
        while True:
            number = input("number: ")
            try:
                numRaise(number)
            except Exception as ex:
                print(ex)
            else: 
                break
        while True:           
            mail = input("mail: ")
            try:
                mailRaise(mail)
            except Exception as ex:
                print(ex)
            else:  
                break    
        self.student.insert(1,name_surname)
        self.student.insert(3,number)
        self.student.append(mail)
        return self.student
    
    
    def ConverttoDict(self):
        convertDict = {self.student[i]: self.student[i + 1] for i in range(0, len(self.student), 2)}
        return convertDict

info = students_info()    

def infoCheck():
    counter = 1
    while counter < 4:
        check_name = input("\nPlease enter name and surname for authentication: ")
        if check_name == info.ConverttoDict()["Name and Surname"] or check_name == info.ConverttoDict()["Name and Surname"].upper() or check_name == info.ConverttoDict()["Name and Surname"].lower() or check_name == info.ConverttoDict()["Name and Surname"].capitalize() or check_name == info.ConverttoDict()["Name and Surname"].title():
            print("\n")
            print(" Welcome ".center(25,"*"))
            break
        elif counter == 3:
            print('<< Please tyr again later >>')
            sys.exit()
        else:
            counter += 1
            print('Authentication failed')    
infoCheck()                  


                        
'''
lineer algebra
introduction to python
statistics
probability
algorithm
'''


import random as rn
lessons = []
counter = 1
print('\nYou must choose at least 3 courses for grade assessment')
while counter < 6:
    lesson1 = input('\nChoose course: ')
    lessons.append(lesson1)
    if counter == 5:
        break
    check_continue = input("\nPress any key other than 'n' to continue selecting a lesson. \nPress n to finish the course selection: ")
    if check_continue == 'n':
        break
    else:
        counter += 1

if len(lessons) < 3:
    print('\nYou failed in class')
    sys.exit()
else:
    if len(lessons) >= 3:
        print('\ncourse selection is succesful')      

# select a course for the exam      
while True:
    choose_course = input('\nSelect a course for the exam: ')
    if choose_course in lessons:
        print(f"\nYou can take the exam of the '{choose_course}' lesson") 
        points = {choose_course: 
        {'midtern exam': rn.randint(1,100),
         'second midtern exam': rn.randint(1,100),
         'final': rn.randint(1,100)
             }
         }
        exam_login = input("\nPlease press the 'y' key to enter the exam: ")
        if exam_login == "y":
            print("Loading exam page...")
            time.sleep(1)
            webbrowser.open("https://prnt.sc/war02t", new=0, autoraise=True)
        print("\nYour exam is being checked, please wait...")
        time.sleep(2)
        show = input("\nYou can use the 'show' command to see the results: ")
        if show == 'show':
            print("Achieving your results please wait...\n")
            time.sleep(2)
            for key,value in points.items():
                for inkey,invalue in value.items():
                    print(f"{inkey} : {invalue}")
        break
    else:
        print("You can only choose the courses you took before")
        beforeLessonShow = input("\nPress 'y' to view the lessons you have taken. \nPress 'enter' to continue without viewing")
        if beforeLessonShow == "y":
            print(lessons)
   
def calculate_average():
    # midtern exam: %30
    # second midtern exam: %20
    # final :%50
    return (points[choose_course]['midtern exam'] * 0.3) + (points[choose_course]['second midtern exam'] * 0.2) + (points[choose_course]['final'] * 0.5)

   
# your GPA in math class is ...
print(f"\nYour GPA in {choose_course} class is '{calculate_average()}'. Your success will be determined after the evaluations.")

def letter_grade():
    if calculate_average() >= 90:
        AA ='AA'
        return AA
    elif calculate_average() < 90 and calculate_average() >= 70:
        BB = 'BB'
        return BB    
    elif calculate_average() < 70 and calculate_average() >= 50:  
        CC ='CC'  
        return CC
    elif calculate_average() < 50 and calculate_average() >=30:
        DD = 'DD' 
        return DD 
    elif calculate_average() < 30:
        FF = 'FF'
        return FF
# press a key to see the letter grade    
if letter_grade() == 'FF':
    print(f"\nYour GPA in {choose_course} class is {calculate_average()}. Your letter grade is {letter_grade()}")
    sys.exit()
check_gradeShow = input("\nPress 'l'  key to see the letter grade: ")
if check_gradeShow == 'l':
    print(letter_grade())    

