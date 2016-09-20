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
    # # John leaves Matt to be coached by Kylie
    john.removeCoach(matt)
    kylie.addTrainee(john)
    printer(users)
    # Works with kylie
    # kylie.fullInfection(1)
    # Works with chris
    # chris.fullInfection(1)
    john.fullInfection(1)
    sarah.fullInfection(2)
    printer(users)

def printer(users):
    for x in users:
        print(x)
    print("*"*50)

if __name__ == "__main__":
    main()