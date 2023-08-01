#Prompt: Write a program that will ask the user the year they were born, calculate the user's age, then
#print the result to terminal
import datetime


def CalculateUserAge():
    userYear = input("What year were you born?\n")
    #convert input to # we can work with
    userYear = int(userYear)
    #Grab current year
    currentYear = datetime.date.today().year
    userAge = currentYear - userYear;
    print("You are ",userAge," years old.")

#CalculateUserAge()

#Prompt: Ask a user their weight (in pounds), convert it to kg, and print to terminal
def ConvertLbsToKg():
    weightInLbs = float(input("Input weight in lbs: "))
    #1 kg = 2.2 lbs
    weightInKilos = weightInLbs/2.2
    #"{:.2f}".format(num)
    print("Weight in kilos: ", "{:.2f}".format(weightInKilos))

ConvertLbsToKg()