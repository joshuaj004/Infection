# This is the main file that will use the Users class
from User import User


def main():
    print("Hello world!")
    matt = User()
    print(matt)
    print(matt.getCoaches())
    print(matt.getTrainees())
    print(matt.getVersion())

if __name__ == "__main__":
    main()