# Global variable for tracking files
fileAmount = 0

def makeFile():
    global fileAmount  # Need to declare global to modify it
    fileAmount = fileAmount + 1  # Fixed assignment operator
    print(f"You now have {fileAmount} files.")  # Used f-string for proper string formatting

def openFile():
    global fileAmount
    if fileAmount == 0:
        print("You don't have any files.")
        return
    try:
        print(f"You have {fileAmount} files.")
        response = int(input("What file would you like to open? (Enter number): "))
        if response > fileAmount:
            print("You don't have that many files.")
        else:
            print("Opening file", response)
            print("You do realize this is not the final version.")
    except ValueError:
        print("Please enter a valid number.")

def mainMenu():
    while True:  # Added loop to prevent recursion errors
        print("\nMain Menu:")
        allFeatures = ["New File (NF)", "Open File (OF)", "Online Multiplayer (OF)", "Exit (E)"]
        for currentFeature in allFeatures:
            print(currentFeature)
        
        option = input("Choose an option: ").upper()
        
        if option == "NF":
            if fileAmount < 3:  # Fixed logic (was >= which prevented file creation)
                makeFile()
            else:
                print("Maximum file limit (3) reached!")
        elif option == "OF":
            if fileAmount == 0:
                response = input("You don't have any files. Would you like to make a file? (yes/no): ")
                if response.lower() == "yes":
                    makeFile()
                    openFile()
            else:
                openFile()
        elif option == "OM":
            print("Online multiplayer is not supported in this version. Remember, this is a conceptual Python title screen, not")
        elif option == "E":
            print("Ok, bye. Not like there is anything to do in this game.")
            break
        else:
            print("That is not an option, moron.")

def main():
    print("_" * 80)
    print("\nCIRCLE TALES")
    input("Press Enter to play...")
    mainMenu()

if __name__ == "__main__":
    main()