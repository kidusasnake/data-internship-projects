#create a menu function that contain options
def menu():
    print("student grade tracker system")
    print("1.Add student")
    print("2.View student")
    print("3.view top student")
    print("4.view lowest scorer")
    print("5.view leaderboard")
    print("6.Search for student")
    print("7.Delete student record")
    print("8.Update student record")
    print("9.exit")

students=[]
top_scorer=("",0)
lowest_scorer=("",100)
try:
    with open("students.txt","r")as file:
        for line in file:
            name,average=line.strip().split(",")
            students.append((name,float(average)))
except FileNotFoundError:
    pass

#create add student function

def add_student():
    name=input("enter name:")
    scores=[]
    for i in range(3):
        score=int(input("enter their scores:"))
        scores.append(score)
    average=sum(scores)/len(scores)
    return (name,average)
#cerate search function to search students
def search_student(students):
    name=input("Enter name to search: ")
    found=False #is a flag variable to track if something happen so in this case it tracks if the student was found
    for s in students:
        if s[0].lower()==name.lower():
            print(f"Found: {s[0]} | Average={round(s[1],2)}")
            found=True
            break
    if not found:
        print("Student not found!")
#create a delete function
  def delete_student(students):
    name=input("Enter name to delete:")
    found=False
    for s in students:
        if s[0].lower()==name.lower():
            students.remove(s)
            print("Student removed.")
            break
    
    print("Student not found!")
#cerate an  update function
def update_student(students):
    name=input("Enter a name to update:")
    for i,s in enumerate(students):
        if s[0].strip().lower()==name.strip().lower():
            print(f"Current Average={round(s[1],2)}")
            scores=[]
            for j in range(3):
                while True:
                    try:
                        score=(int(input(f"enter the new scores{j+1}: ")))
                        if 0<=score<=100:
                            break
                        else:
                            print("score must be between 0 and 100")
                    except ValueError:
                        print("Invalid input.please enter a number.")
                scores.append(score)

            new_avg=sum(scores)/len(scores)
            students[i]=(name,new_avg)
            print("Record updated")
            return
    print("student not found!")

        
while True:
    menu()
    choice=(input("Enter  your choice: "))
  #add student name and scores
    if choice=="1":
        student=add_student()
        students.append(student)
        with open("students.txt","a") as file:
            file.write(f"{student[0]},{student[1]}\n")
        print("student added successfully!")
#view student entry
    elif choice=="2":
        if students:
            for s in students:
                print(f"{s[0]}-average={round(s[1],2)}")
        else:
            print("no student available")
#display top scorer
    elif choice=="3":
        if students:
            top_scorer=max(students,key=lambda x:x[1])
            print(f"Top scorer is:{top_scorer[0]}")
            print(f"average = {round(top_scorer[1],2)}")
        else:
            print("No student available")
  #display lowest scorer
    elif choice=="4":
        if students:
            lowest_scorer=min(students,key=lambda x:x[1])
            print(f"lowest score is:{lowest_scorer[0]}")
            print(f"average = {round(lowest_scorer[1],2)}")
  #display leaderboard
    elif choice=="5":
        if students:
            students_sorted=sorted(students,key=lambda x:x[1],reverse=True)
            print(f"{'rank':<5} {'name':<12} {'average':<8}")
            for rank,student in enumerate(students_sorted,start=1):
                print(f"{rank:<5} {student[0]:<12} {round(student[1],2)}")
        else:
            print("No student record")
  #search for students
    elif choice=="6":
        if students:
            search_student(students)
        else:
            print("no student record")
  #delete student entry
    elif choice=="7":
        if students:
            delete_student(students)
        else:
            print("no student record")
  #update student record
    elif choice=="8":
        if students:
            update_student(students)
        else:
            print("no student record")
  #exit
    elif choice=="9":
        print("Goodbye")
        break
    
    else:
        print("invalid input")
