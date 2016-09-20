# This is the main file that will use the Users class
from User import User


def main():
    tester()


def tester():
    matt = User("matt")
    sarah = User("sarah")
    james = User("james")
    john = User("john")
    kylie = User("kylie")
    chris = User("chris")
    users = [matt, sarah, james, john, kylie, chris]
    # Matt coaches Sarah, James, and John
    matt.addTrainee(sarah)
    matt.addTrainee(james)
    matt.addTrainee(john)
    # Kylie coaches Chris
    kylie.addTrainee(chris)
    printer(users)
    print("*"*50)
    # # John leaves Matt to be coached by Kylie
    john.removeCoach(matt)
    kylie.addTrainee(john)
    printer(users)

def printer(users):
    for x in users:
        print(x)

if __name__ == "__main__":
    main()