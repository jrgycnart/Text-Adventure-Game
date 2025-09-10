import sys

def start():
    print("Welcome to the Forest of Choices!")
    print("You find yourself at the edge of a mysterious forest. The sun is setting.")
    print("Do you:")
    print("1. Enter the forest")
    print("2. Walk along the edge")
    choice = input("> ")
    if choice == "1":
        forest_path()
    elif choice == "2":
        edge_path()
    else:
        print("Invalid choice. Try again.")
        start()

def forest_path():
    print("\nYou step into the forest. The trees are thick, and it's getting dark.")
    print("You hear a rustling in the bushes.")
    print("Do you:")
    print("1. Investigate the sound")
    print("2. Ignore it and continue forward")
    choice = input("> ")
    if choice == "1":
        investigate_bush()
    elif choice == "2":
        deep_forest()
    else:
        print("Invalid choice. Try again.")
        forest_path()

def edge_path():
    print("\nYou walk along the edge, keeping the forest to your left.")
    print("You spot a small cottage with smoke rising from the chimney.")
    print("Do you:")
    print("1. Knock on the cottage door")
    print("2. Avoid the cottage and keep walking")
    choice = input("> ")
    if choice == "1":
        cottage()
    elif choice == "2":
        open_field()
    else:
        print("Invalid choice. Try again.")
        edge_path()

def investigate_bush():
    print("\nYou approach the bush carefully.")
    print("A friendly fox jumps out and offers you a shiny key!")
    print("Do you:")
    print("1. Accept the key")
    print("2. Politely decline")
    choice = input("> ")
    if choice == "1":
        print("\nYou take the key. Suddenly, a hidden door appears in a tree nearby.")
        print("You unlock the door and discover a treasure chest filled with gold!")
        print("Congratulations! You found the treasure and won the game!")
        sys.exit()
    elif choice == "2":
        print("\nYou decline the key. The fox shrugs and disappears into the forest.")
        deep_forest()
    else:
        print("Invalid choice. Try again.")
        investigate_bush()

def deep_forest():
    print("\nYou venture deeper into the forest. The path splits in two.")
    print("Do you:")
    print("1. Take the left path")
    print("2. Take the right path")
    choice = input("> ")
    if choice == "1":
        print("\nThe left path leads to a clearing where you find a magical pond.")
        print("You drink from it and feel rejuvenated, but decide to head home, safe and sound.")
        print("You survived your adventure!")
        sys.exit()
    elif choice == "2":
        print("\nThe right path becomes narrower until you find yourself lost.")
        print("Night falls, and you spend a cold night in the forest. Game over.")
        sys.exit()
    else:
        print("Invalid choice. Try again.")
        deep_forest()

def cottage():
    print("\nYou knock on the door. An old woman answers and invites you in.")
    print("She offers you soup and a bed for the night.")
    print("Do you:")
    print("1. Accept her hospitality")
    print("2. Politely decline and leave")
    choice = input("> ")
    if choice == "1":
        print("\nYou enjoy a warm meal and a restful sleep. In the morning, she gives you a map to hidden treasure.")
        print("You follow the map and become rich! You win!")
        sys.exit()
    elif choice == "2":
        print("\nYou thank her and continue your journey. Eventually, you find your way home, safe but unchanged.")
        print("You survived your adventure!")
        sys.exit()
    else:
        print("Invalid choice. Try again.")
        cottage()

def open_field():
    print("\nYou walk away from the cottage and into an open field.")
    print("Suddenly, a storm rolls in.")
    print("Do you:")
    print("1. Run back to the cottage")
    print("2. Find shelter under a large tree")
    choice = input("> ")
    if choice == "1":
        print("\nYou make it back to the cottage just in time. The old woman lets you in, and you are safe.")
        print("You survived your adventure!")
        sys.exit()
    elif choice == "2":
        print("\nLightning strikes the tree! You escape with minor injuries, but decide it's best to head home.")
        print("You survived, but with a story to tell!")
        sys.exit()
    else:
        print("Invalid choice. Try again.")
        open_field()

if __name__ == "__main__":
    start()
