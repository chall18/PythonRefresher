#Prompt: Create a program that asks for the user's phone number, then prints out those numbers in words.
#Example: 1234 should return "one two three four"

def createDictionary():
    num_dict = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    return num_dict

def numPhoneToStringPhone():
    num_dict = createDictionary()
    phoneNum = input("Enter your phone number: ")
    phoneNum = phoneNum.replace("-", "") #remove dashes

    # phoneNum will come in as a string, so we can analyze each char using a for loop
    if(phoneNum.isnumeric()):
        for num in phoneNum:
            if int(num) in num_dict:
                print(num_dict[int(num)] + " ", end='')
    else:
        print("Your number's got a funky character in it. Can't work with that, sorry.")
        exit(0)

if __name__ == '__main__':
    numPhoneToStringPhone()