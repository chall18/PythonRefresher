#Prompt: Write a program that allows the user to input what unit of measurement they want to input their weight in
#(kg or lbs), then convert that to the opposite unit.
def kilosToLbs(kilos):
    return kilos*2.2

def lbsToKilos(pounds):
    return pounds*0.45

unit = input("Enter weight unit of choice (kg or lbs): ")
if(unit != "kg" and unit != "lbs"):
    print("Unacceptable input given. Please try again.")
    exit(-1)

print("Unit chosen is " + unit)
weight = float(input("Enter weight: "))
print("Weight in " + unit + " is ", weight)

if(unit == "kg"):
    print("Weight in kg is ", lbsToKilos(weight))
elif(unit == "lbs"):
    print("Weight in lbs is ", kilosToLbs(weight))