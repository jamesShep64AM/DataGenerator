import random
f = open("orders.csv","w")

burgersMenu = {"Rev's Burger":5.59,
           "Double Stach Cheese Burger":8.79,
           "Classic Burger": 5.49,
           "Bacon Cheeseburger":6.99}

burgersComboPrice = 1.90

basketsMenu = {"Three Tender Basket":6.79,
           "Four Steak Finger Basket":8.39}

basketsComboPrice = 1.10

sandwichesMenu = {"Gig 'em Patty Melt": 6.29,
              "Howdy Spicy Ranch Chicken Strip":6.99,
              "Classic Crispy Chicket Tender Sandwich":5.79,
              "Grilled Chicken Tender Sandwich":5.79,
              "Grilled Cheese":3.49}

gigPattyMeltComboPrice = 1.80
sandwichesComboPrice = 1.90

shakesNSweetMenu = {"Aggie Shake":3.14,
                "Double Scoop Ice Cream Cup":3.79,
                "Chocolate Chip Chunk Cookie":2.11,
                "Chocolate Fudge Brownie":2.11}

saucesMenu = {"Gig 'Em Sauce":.69,
          "Buffalo":.69,
          "Ranch":.69,
          "BBQ Sauce":.69,
          "Honey Mustard":.69,
          "Spicy Ranch":.69}

sidesMenu = {"Seasoned Fries":1.5,
         "Tator Tots":1.5,
         "Onion Rings":1.98,
         "Kettle Chips":1.25}

beveragesMenu = {"Medium Fountain Drink":2.25,
             "Large Fountain Drink":2.45,
             "Drip Coffee":2.29,
             "Cold Brew":3.65}

customerNames = [
    "Liam",
    "Olivia",
    "Noah",
    "Emma",
    "Oliver",
    "Ava",
    "Elijah",
    "Charlotte",
    "William",
    "Sophia",
    "James",
    "Amelia",
    "Benjamin",
    "Isabella",
    "Lucas",
    "Mia",
    "Henry",
    "Evelyn",
    "Alexander",
    "Harper"
]

managers = ["Zach","Xavier","Victor"]

employees = ["Quency","Wyat","Emily","Ryan","Trist","Yorn","Uno"]

#items for stock
sauces = ["ketchup","mustard","ranch"]
cookingIngredients = ["oil","butter","flour","salt","eggs","milk","sugar"]
seasonings = ["peper","paprika"]
meats = ["chicken tenders","ground beef","steak"]
toppings = ["bacon","american cheese","shredded cheese","lettuce"]
breads = ["burger bun","sanwich loaf"]
sides = ["potatoes","onions","chips"]
containers = ["baskets","bags","wrappers","foil"]
desserts = ["chocolate ice cream","vanilla ice cream","strawberry icecream","chocolate chips"]
drinks = ["water bottles","soda syrup","soda water","tea","coffee beans"]

#todo:
#   Write orders to file
#       ~figure out the format to do this
#   Generate modifications for the orders 
#       ~How are we going to do modifications in the data base


#order could have multiple people so we should probally havea serpate generatePersonOrder, and generate order
#Don't put much effort into making the orders realistic, I dont think it really matters. 
#Make sure to have a none for each order section 

#generate order, order is dictionary with array menu (key,value) pairs. 
#Each key has value of an array that can have none,one, or multiple items
def generatePersonOrder():
    order = {"entre":[],"makeCombo":[],"sweets":[],"sauces":[],"sides":[],"beverages":[]}
    entreChoice = random.randint(1,4)
    match entreChoice:
        case 1:
            order["entre"].append(random.choice(list(burgersMenu.items())))
            order["entre"].append(random.choice(list(burgersMenu.items())))
        case 2:
            order["entre"].append(random.choice(list(basketsMenu.items())))
        case 3:
            order["entre"].append(random.choice(list(sandwichesMenu.items())))
        case 4:
            order["entre"] = []
    
    if(order["entre"]):
        for _ in range(len(order["entre"])):   
            print(len(order["entre"])) 
            comboChoice = random.randint(1,10)
            if(comboChoice <= 8):
                order["makeCombo"].append(True)
            else:
                order["makeCombo"].append(False)
        
    sweetsChoice = random.randint(1,10)
    if(sweetsChoice <= 3):
        order["sweets"].append(random.choice(list(shakesNSweetMenu.items())))
    else:
        order["sweets"] = []

    sauceChoice = random.randint(1,3)
    match sauceChoice:
        case 1:
            order["sauces"].append(random.choice(list(saucesMenu.items())))
        case 2:
            order["sauces"].append(random.choice(list(saucesMenu.items())))
            order["sauces"].append(random.choice(list(saucesMenu.items())))
        case 3:
            order["sauces"].append(())

    sideChoice = random.randint(1,3)
    match sideChoice:
        case 1:
            order["sides"].append(random.choice(list(sidesMenu.items())))
        case 2:
            order["sides"].append(random.choice(list(sidesMenu.items())))
            order["sides"].append(random.choice(list(sidesMenu.items())))
        case 3:
            order["sides"].append(())

    beverageChoice = random.randint(1,3)
    match beverageChoice:
        case 1:
            order["beverages"].append(random.choice(list(beveragesMenu.items())))
        case 2:
            order["beverages"].append(random.choice(list(beveragesMenu.items())))
            order["beverages"].append(random.choice(list(beveragesMenu.items())))
        case 3:
            order["beverages"].append(())
    return order

print(generatePersonOrder())



#Probaly need to generate different order modifications

#Need a function to generate times for the orders, weight for more during certain times

#Add function for generating deliveries. Probally do this is a seperate .csv file

