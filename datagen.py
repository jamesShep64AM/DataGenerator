import random
f = open("orders.csv","w")

burgersMenu = ["Rev's Burger",
           "Double Stach Cheese Burger",
           "Classic Burger",
           "Bacon Cheeseburger"]

burgersComboPrice = 1.90

basketsMenu = ["Three Tender Basket",
           "Four Steak Finger Basket"]

basketsComboPrice = 1.10

sandwichesMenu = ["Gig 'em Patty Melt",
              "Howdy Spicy Ranch Chicken Strip",
              "Classic Crispy Chicket Tender Sandwich",
              "Grilled Chicken Tender Sandwich",
              "Grilled Cheese"]


shakesNSweetMenu = {"Aggie Shake",
                "Double Scoop Ice Cream Cup",
                "Chocolate Chip Chunk Cookie",
                "Chocolate Fudge Brownie"}

saucesMenu = ["Gig 'Em Sauce",
          "Buffalo",
          "Ranch",
          "BBQ Sauce",
          "Honey Mustard",
          "Spicy Ranch"]

sidesMenu = ["Seasoned Fries",
         "Tator Tots",
         "Onion Rings",
         "Kettle Chips"]

beveragesMenu = ["Medium Fountain Drink",
             "Large Fountain Drink",
             "Drip Coffee",
             "Cold Brew"]

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
            order["entre"].append(random.choice(burgersMenu))
            order["entre"].append(random.choice(burgersMenu))
        case 2:
            order["entre"].append(random.choice(burgersMenu))
        case 3:
            order["entre"].append(random.choice(burgersMenu))
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
        order["sweets"].append(random.choice(shakesNSweetMenu))
    else:
        order["sweets"] = []

    sauceChoice = random.randint(1,3)
    match sauceChoice:
        case 1:
            order["sauces"].append(random.choice(saucesMenu))
        case 2:
            order["sauces"].append(random.choice(saucesMenu))
            order["sauces"].append(random.choice(saucesMenu))
        case 3:
            order["sauces"].append("")

    sideChoice = random.randint(1,3)
    match sideChoice:
        case 1:
            order["sides"].append(random.choice(sidesMenu))
        case 2:
            order["sides"].append(random.choice(sidesMenu))
            order["sides"].append(random.choice(sidesMenu))
        case 3:
            order["sides"].append("")

    beverageChoice = random.randint(1,3)
    match beverageChoice:
        case 1:
            order["beverages"].append(random.choice(beveragesMenu))
        case 2:
            order["beverages"].append(random.choice(random.choice(beveragesMenu)))
            order["beverages"].append(random.choice(random.choice(beveragesMenu)))
        case 3:
            order["beverages"].append("")
    return order

print(generatePersonOrder())



#Probaly need to generate different order modifications

#Need a function to generate times for the orders, weight for more during certain times

#Add function for generating deliveries. Probally do this is a seperate .csv file

