import random

def all_commands():
    pass

def areas_to_cover():
    pass

def rules():
    print("Rules:")
    print("1. You can see the helpful commands that you can use ")
    print("by writing 'help commands' .")
    print("2. You can check your inventory, get items, use items, ")
    print("and go different rooms.")
    print("3. You can quit the game whenever you want when you ")
    print("discover the back exit once. ")
    print("4. There will be 4 obstacles you will have to work on. ")

def main():

    print("-------------------------------------")
    print("### Welcome to the Adventure Game! ###")
    print("-------------------------------------")
    print("Here are the required information and rules:")
    print("-------------------------------------")
    print("You are the detective who is trying to uncover")
    print("the hidden truth about a murder. The truth lies")
    print("in this mansion and your goal is the find it by")
    print("exploring different places, obtaining tools, and")
    print("working hard. Good luck to you adventurer!!")
    print("-------------------------------------")
    rules()
    print()
    print("(You can see the rules whenever you type rules(). )")
    print("-------------------------------------")

    is_running = True
    while is_running:
        print("You are at the entrance of the mansion.")
        print("You are observing the mansion from outside and")
        print("it has a front door to the east. What will you do?")
        print("You know that you have no option but to enter.")
        print("You are in the foyer now (the small hallway of entrance).")
        print("You see that there is one more door in front of you (to the east).")
        print("When you go through that door as well, you see that it leads")
        print("to a library. Now, there are 2 bookshelves on the north and south")
        print("and 3 new doors in north, east and south. ")
        print("What would you like to do(enter number)? 1.go north, 2. go east,")
        action = input("3. go south, 4. go to north bookshelf, 5. go to south bookshelf.")

if __name__ == '__main__':
    main()