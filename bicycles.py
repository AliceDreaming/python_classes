import random

material_list=['aluminum', 'carbon', 'steel']

class Wheel(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
    
class Frame(object):
    def __init__(self, material, weight, cost):
        self.material = material
        self.weight = weight
        self.cost = cost
        
class Bicycles(object):
    def __init__(self, name, wheel, frame):
        self.name = name
        self.front_wheel = wheel
        self.back_wheel = wheel
        self.frame = frame
        self.manufaturer=''
        self.weight = self.front_wheel.weight + self.back_wheel.weight + self.frame.weight
        self.cost = self.front_wheel.cost + self.back_wheel.cost + self.frame.cost
    
    def copy(self, manufaturer):
        new_bike = Bicycles(self.name, self.front_wheel, self.frame)
        new_bike.manufaturer = manufaturer
        return new_bike
        
class BicycleManufacturer(object):
    def __init__(self, name, models, margin):
        self.name = name
        self.models = models
        self.margin = margin
        self.sales_volumn={}
        for bike in models:
            self.sales_volumn[bike] = 0
        
    def produce_bicycles(self, bike):
        return bike.copy(self.name)
            
    def sell_bike(self, bike, amount):
        if(bike in self.models):
            new_bike = self.produce_bicycles(bike)
            new_bike.cost += bike.cost * self.margin
            self.sales_volumn[bike] += amount
            return new_bike
        else:
            print("Manufaturer {} doesn't provide bike model {}".format(self.name, bike.name))
     
    def calc_profit(self):
        profit = 0
        for bike in self.sales_volumn.keys():
            profit += bike.cost * self.sales_volumn[bike] * self.margin
        return profit
    
class BikeShop(object):
    def __init__(self, name, margin):
        self.name = name
        self.inventory = {}
        self.margin = margin
        self.sales_volumn={}
    
    def purchase_bike(self, manufaturer, bike, amount):
        new_bike = manufaturer.sell_bike(bike, amount)
        if(new_bike in self.inventory):
            self.inventory[new_bike] += amount
        else:
            self.inventory[new_bike] = amount
        
    def sell_bike(self, bikeModel):
        if(bikeModel in self.sales_volumn):
            self.sales_volumn[bikeModel] += 1
        else:
            self.sales_volumn[bikeModel] = 1
        self.inventory[bikeModel] -= 1
        
        #return the price of the bike model
        return bikeModel.cost*(1 + self.margin)
        
    #calculate how much profit has got from selling bikes
    def calc_profit(self):
        profit = 0
        for bike in self.sales_volumn.keys():
            profit += bike.cost * self.sales_volumn[bike] * self.margin
        
        return profit    
        
    def affordable_bikes(self, budget):
        affordableBike = []
        for bike in self.inventory.keys():
            if(budget >= bike.cost * (1 + self.margin)):
                affordableBike.append(bike)
        return affordableBike   
    
    def print_inventory(self):
        for bike in self.inventory.keys():
            print(bike.name,self.inventory[bike])
        
class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def buy_bike(self, cost):
        # Decrease the budget
        print("cost of the bike is: {}".format(cost))
        self.budget -= cost
        print("The left budget is {}".format(self.budget))

def main():
    
    wheel_type_A = Wheel('wheel_A', 10, 40)
    wheel_type_B = Wheel('wheel_B', 12, 200)
    wheel_type_C = Wheel('wheel_C', 5, 400)
    
    frame_al = Frame(material_list[0], 20, 100)
    frame_carbon = Frame(material_list[1], 15, 400)
    frame_steel = Frame(material_list[2], 25, 40)
    
    #Create a bicycle shop that has 6 different bicycle models in stock.
    bike_model_A = Bicycles('model_A', wheel_type_A, frame_steel)
    bike_model_B = Bicycles('Model_B', wheel_type_A, frame_al)
    bike_model_C = Bicycles('model_C', wheel_type_B, frame_al)
    bike_model_D = Bicycles('Model_D', wheel_type_B, frame_carbon)
    bike_model_E = Bicycles('model_E', wheel_type_C, frame_al)
    bike_model_F = Bicycles('Model_F', wheel_type_C, frame_carbon)
    
    models_manufaturer_A=[bike_model_A, bike_model_B, bike_model_C]
    manufaturer_A = BicycleManufacturer('manufaturer_A', models_manufaturer_A, 0.15)
    
    models_manufaturer_B=[bike_model_D, bike_model_E, bike_model_F]
    manufaturer_B = BicycleManufacturer('manufaturer_B', models_manufaturer_B, 0.15)
    
    #The shop should charge its customers 20% over the cost of the bikes.                
    bikeshop = BikeShop("Sunshine", 0.2)
    bikeshop.purchase_bike(manufaturer_A, bike_model_A, 5)
    bikeshop.purchase_bike(manufaturer_A, bike_model_B, 5)
    bikeshop.purchase_bike(manufaturer_A, bike_model_C, 5)
    bikeshop.purchase_bike(manufaturer_B, bike_model_D, 5)
    bikeshop.purchase_bike(manufaturer_B, bike_model_E, 5)
    bikeshop.purchase_bike(manufaturer_B, bike_model_F, 5)
    
    #Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
    Alice = Customer('Alice', 200)
    Jorge = Customer('Jorge', 500)
    Sooraj = Customer('Sooraj', 1000)
    
    print('Print the name of each customer')
    print(Alice.name)
    print(Jorge.name)
    print(Sooraj.name)
    
    print("Print a list of the bikes offered by the bike shop that they can afford given their budget")
    alice_affordable_bikes = bikeshop.affordable_bikes(Alice.budget);
    jorge_affordable_bikes = bikeshop.affordable_bikes(Jorge.budget);
    sooraj_affordable_bikes = bikeshop.affordable_bikes(Sooraj.budget);
    
    print("Alice can afford these bikes:")
    for bike in alice_affordable_bikes:
        print(bike.name)
        
    print("Jorge can afford these bikes:")
    for bike in jorge_affordable_bikes:
        print(bike.name)
    
    print("Sooraj can afford these bikes: ")
    for bike in sooraj_affordable_bikes:
        print(bike.name)
    
    print("Print the initial inventory of the bike shop for each bike it carries.")
    bikeshop.print_inventory()
    
    alice_choice = random.choice(alice_affordable_bikes)
    jorge_choice = random.choice(jorge_affordable_bikes)
    sooraj_choice = random.choice(sooraj_affordable_bikes)
    
    print("Alice buy bike {}".format(alice_choice.name))
    Alice.buy_bike(bikeshop.sell_bike(alice_choice))
    
    print("Jorge buy bike {}".format(jorge_choice.name))
    Jorge.buy_bike(bikeshop.sell_bike(jorge_choice))
    
    print("Sooraj buy bike {}".format(sooraj_choice.name))
    Sooraj.buy_bike(bikeshop.sell_bike(sooraj_choice))
    
    print("print out the bicycle shop's remaining inventory for each bike")
    bikeshop.print_inventory()
    
    print("Profit get from selling bikes for bike shop {} is {}".format(bikeshop.name, bikeshop.calc_profit()))
    print("Profit get from selling bikes for manufaturer {} is {}".format(manufaturer_A.name, manufaturer_A.calc_profit()))
    print("Profit get from selling bikes for manufaturer {} is {}".format(manufaturer_B.name, manufaturer_B.calc_profit()))
    
if(__name__ == '__main__'):
    main()