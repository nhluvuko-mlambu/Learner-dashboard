learners=[]

# Update name Function
def update_name(learner):
    new_name=input("New Name: ").strip()
    if new_name== "":
        print("Name can not be empty ")
        return
    learner["name"]=new_name
    print("Succesfully updated name.")


#Update email Function
def update_email(learner):
    new_email=input("New email: ").strip()
    if new_email== "":
        print("Email cannot be empty.")
        return
    learner["email"]=new_email
    print("Successfully updated email.")

#update grade Functions
def update_grade(learner):
    new_grade=input("New grade: ").strip()
    if new_grade== "":
        print("grade cannot be empty.")
        return
    learner["grade"]=new_grade
    print("Successfully updated grade.")

#Update email Function
def update_email(learner):
    new_email=input("New email: ").strip()
    if new_email== "":
        print("Email cannot be empty.")
        return
    learner["email"]=new_email
    print("Successfully updated email.")

#Update mark Function
def update_mark(learner):
    subject=input("Subject: ")

    if subject in learner["subjects"]:

        while True:
            try:
                new_mark=float(input("New mark: "))
                if new_mark<0 or new_mark>100:
                    print("Mark must be between 0 and 100.")
                    continue
                break
            except ValueError:
                print("Invalid entry")

        learner["subjects"][subject]=new_mark
    else:
        print("Subject not found")


#Update learner function
def update_learner():
    print("\n---UPDATE LEARNER---")
    #Condition checking if we have learners 
    if len(learners)==0:

        print("No Learners Found")
        return

    name=input("\nSearch Name: ")

    for learner in learners:
        if learner["name"]==name:
            while True:
                print("\n---UPDATE LEARNER---")
                print("\n1.Update Name.")
                print("2.Update Email.")
                print("3.Update Grade.")
                print("4.Update Mark.")
                print("5.Cancel.")

                
                choice=input("\nChoice: ")

                if choice =="1":
                    update_name(learner)

                elif choice=="2":
                    update_email(learner)
                elif choice=="3":
                    update_grade(learner)
                elif choice=="4":
                    update_mark(learner)
                elif choice=="5":
                    print("Done")
                    break
        else:
            print("\nLearner not found")


#Display Menu
def display_menu():
    print("*"*40)
    print("""           WELCOME TO LEARNER
                DASHBOARD""")
    print("*"*40)

    print("\n1.Add Learner.")
    print("2.View Learners.")
    print("3.Update learner.")
    print("4.Exit.")

#Add Learner Function
def add_learner():
    print("\n---ADD LEARNER---")
    first_name=input("\nFirst Name: ")
    last_name=input("Last Name: ")
    name=f"{first_name} {last_name}"

    email=input("Email: ")
    grade=input("Grade: ")

    subjects={}
    for i in range(2):
        subject=input(f"Subject {i+1}: ")

        while True:
            try:
                mark=float(input(f"{subject} Mark: "))
                if mark<0 or mark>100:
                    print("\nMarks should be between 0 and 100.")
                    continue
                break
            except ValueError:
                print("\nInvalid Mark.")

        subjects[subject]=mark

    learner={"name":name,
             "email":email,
             "grade":grade,
             "subjects":subjects}

    learners.append(learner)
    print("\nLearner Successfully added.")


# Fuctions that view learners
def view_learners():
    print("\n---LEARNERS---")
    #Condition checking if we have learners 
    if len(learners)==0:
        print("No Learners Found")
        return
    #Checking each and every learner in the list of learners and display them
    for number, learner in enumerate(learners,start=1):
 
        print(f"{number}.{learner}")

# Main Functions  
def main():

    while True:
        display_menu()

        choice=input("\nChoose: ")

        if choice=="1":
            add_learner()
        elif choice=="2":
            view_learners()
        elif choice=="3":
            update_learner()

        elif choice=="4":
            print("\nGoodbye.")
            break
        else:
            print("Invalid Entry.")
        
    
#Calling Main Function
main()
