MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

stop = False
money = 0
while stop == False:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        stop = True
        
    elif choice == "report":
        print(f"Water : {resources['water']} ml")
        print(f"Milk : {resources['milk']} ml")
        print(f"Coffee : {resources['coffee']} gm")
        print(f"Money : ${money}")
    else:  
      resource_value = 0
      total_coins = 0
      for single_value in resources:
        if resources[single_value] >= MENU[choice]['ingredients'][single_value]:
          resource_value += 0
        else:
          resource_value += 1
          print(f"There is not enough {single_value}")
  
      if resource_value == 0:
        print("Please Insert coins")
        quarters = float(input("How many quarters? : ")) * 0.25
        dimes = float(input("How many dimes? : ")) * 0.10
        nickles = float(input("How many nickles? : " )) * 0.05
        pennies = float(input("How many pennies? : ")) * 0.01
        
        total_coins = round(quarters + dimes + nickles + pennies,2)
  
      if resource_value == 0:
        if total_coins >= MENU[choice]['cost']:
  
          for new_single_value in resources:
            resources[new_single_value] -= MENU[choice]['ingredients'][new_single_value]
          money += MENU[choice]['cost']
          
          give_them = round(total_coins - MENU[choice]['cost'] , 2)
          print(f"Here is ${give_them} in change.")
          print(f"Here is your {choice}. Enjoy!")
          
        elif total_coins < MENU[choice]['cost']:
          print("Sorry that's not enough money. Money refunded.")
          

      
