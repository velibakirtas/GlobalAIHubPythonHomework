
name = input("Name: ")
surname = input("\nSurname: ")
while True:
    try:
        age = int(input("\nAge: "))
        break
    except Exception:
        print("Age information should only consist of numbers") 
birthday = input("\nDate of birth (Please just write the year information): ")

    

person_info = []
def list_append(self):
    
    person_info.append(self)

list_append(name)  
list_append(surname)  
list_append(age)  
list_append(birthday)  


for i in person_info:
    print(i)

ageCal = person_info[2]
if ageCal < 18:
    print("\nYou can't go out because it's too dangerous") 
elif ageCal > 18:
    print("\nYou can go out to the street.")       