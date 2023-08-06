def startCar():
    print("Car started...Ready to go!")
def stopCar():
    print("Stopping car now.")

def printMenuOptions():
    print("start - to start the car\nstop - to stop the car\nquit - to exit\n")
def startGame(carStatus):
    choice = ""
    while(True):
        choice = input("> ").lower()
        if(choice == "start"):
            if(carStatus == 0):
                print("Car is already running...")
            else:
                startCar()
                carStatus = 0
        elif(choice == "stop"):
            if(carStatus == 1):
                print("Car is already stopped...")
            else:
                stopCar()
                carStatus = 1
        elif(choice == "help"):
            printMenuOptions()
        elif(choice == "quit"):
            print("Exiting program...")
            exit(0)
        else:
            print("That isn't a menu option. Try again.")


if __name__ == '__main__':
    carStatus = 1
    startGame(carStatus)