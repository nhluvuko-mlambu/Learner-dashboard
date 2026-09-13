learners=[]

def display_menu():
    print("*"*40)
    print("""           WELCOME TO LEARNER
                DASHBOARD""")
    print("*"*40)

    print("\n1.Add Learner")
    print("2.Exit ")

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


def main():

    while True:
        display_menu()

        choice=int(input("Choose: "))

        if choice==1:
            add_learner()
        elif choice==2:
            print("\nGoodbye.")
            break
        else:
            print("Invalid Entry.")
        
    



main()
