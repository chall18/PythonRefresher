#Prompt: Write a program to calculate the total cost of all the items in a shopping cart, then print the sum to terminal
import random

def populateShoppingCart():
    items = 10
    print("Shopping cart items: ")
    shoppingCart = []
    for item in range(items):
        price = round(random.uniform(1, 100), 2)
        shoppingCart.append(price)
    print(*shoppingCart)
    return shoppingCart

def calculateCartTotal():
    shoppingCart = populateShoppingCart()
    total = 0
    for item in shoppingCart:
        total += item
    print("Shopping cart total is: $", round(total, 2))


if __name__ == '__main__':
    calculateCartTotal()