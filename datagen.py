import random
f = open("data.csv","w")

burgersMenu = {"Rev's Burger":5.59,
           "Double Stach Cheese Burger":8.79,
           "Classic Burger": 5.49,
           "Bacon Cheeseburger":6.99}

burgersComboPrice = 1.90

baskets = {"Three Tender Basket":6.79,
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


#Need to create functions to create orders with all of the values. Use random.choice
#Probaly need to generate different order modifications

#Need a function to generate times for the orders, weight for more during certain times

#Add function for generating deliveries. Probally do this is a seperate .csv file

