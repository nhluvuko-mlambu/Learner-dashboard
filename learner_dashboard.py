learners=[]

def display_menu():
    print("*"*40)
    print("""           WELCOME TO LEARNER
                DASHBOARD""")
    print("*"*40)

    print("\n1.Add Learner.")
    print("2.View Learners.")
    print("3.Update learner.")
    print("4.Exit.")

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
 
        print(f"{number}.{learner["name"]}")

 
def main():

    while True:
        display_menu()

        choice=input("Choose: ")

        if choice=="1":
            add_learner()
        elif choice=="2":
            view_learners()

        elif choice=="4":
            print("\nGoodbye.")
            break
        else:
            print("Invalid Entry.")
        
    

main()
