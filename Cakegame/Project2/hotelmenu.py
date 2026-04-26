#define the  items of the menu
menu={
    "Coffee": 100,
    "Tea": 50,
    "Sandwich": 120,
    "Burger": 150,
    "Pizza": 250,
    "Fries": 80,
    "Cake": 90,
    "Brownie": 110,
}
#greet
print("Welcome to hackalicious bakehouse")
print("Coffee: Rs100\nTea: Rs50\nSandwich: Rs120\nBurger: Rs150\nPizza: Rs250\nFries: Rs80\nCake: Rs90\nBrownie: Rs110")
order_total = 0
item_1 = input("Would you like to take anything?\n") 
if item_1 in menu:
    order_total += menu[item_1] #0+50
    print(f"Your item  {item_1} has been added:)")
else:
    print(f"Ordered item{item_1} is not available yet!")
another_order=input(f"Do you like to order anything else?(Yes/No)\n")
if another_order=="Yes":
    item_2=input(f"What would you like to order?")
    if item_2 in menu:
        order_total += menu[item_2] 
        print(f"Your order has been added!")
    else:
        print(f"Ordered item is not available yet!")
print(f"The amount to pay is {order_total}:\n Thanks for visiting:)")        
              