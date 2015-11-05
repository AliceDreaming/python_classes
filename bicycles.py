import random

class Bicycles(object):
    def __init__(self, modelName, weight, cost):
        self.modelName = modelName
        self.weight = weight
        self.cost = cost
    
class BikeShop(object):
    def __init__(self, name, inventory, margin):
        self.name = name
        self.inventory = inventory
        self.margin = margin
        self.sales_volumn={}
    
    def sell_bike(self, bikeModel):
        if(bikeModel in self.sales_volumn):
            self.sales_volumn[bikeModel] += 1
        else:
            self.sales_volumn[bikeModel] = 1
        self.inventory[bikeModel] -= 1
        
        #return the price of the bike model
        return bikeModel.cost*(1+0.2)
        
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
            print(bike.modelName,self.inventory[bike])
        
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
    #Create a bicycle shop that has 6 different bicycle models in stock. 
    bike_model_A = Bicycles('model_A', 20, 100)
    bike_model_B = Bicycles('Model_B', 18, 200)
    bike_model_C = Bicycles('model_C', 22, 500)
    bike_model_D = Bicycles('Model_D', 19, 800)
    bike_model_E = Bicycles('model_E', 25, 1000)
    bike_model_F = Bicycles('Model_F', 15, 1600)
    
    inventory = {   bike_model_A: 10,
                    bike_model_B: 10,
                    bike_model_C: 10,
                    bike_model_D: 10,
                    bike_model_E: 10,
                    bike_model_F: 10,
                    }
    
    #The shop should charge its customers 20% over the cost of the bikes.                
    bikeshop = BikeShop("Sunshine", inventory, 0.2)
    
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
        print(bike.modelName)
        
    print("Jorge can afford these bikes:")
    for bike in jorge_affordable_bikes:
        print(bike.modelName)
    
    print("Sooraj can afford these bikes: ")
    for bike in sooraj_affordable_bikes:
        print(bike.modelName)
    
    print("Print the initial inventory of the bike shop for each bike it carries.")
    bikeshop.print_inventory()
    
    alice_choice = random.choice(alice_affordable_bikes)
    jorge_choice = random.choice(jorge_affordable_bikes)
    sooraj_choice = random.choice(sooraj_affordable_bikes)
    
    print("Alice buy bike {}".format(alice_choice.modelName))
    Alice.buy_bike(bikeshop.sell_bike(alice_choice))
    
    print("Jorge buy bike {}".format(jorge_choice.modelName))
    Jorge.buy_bike(bikeshop.sell_bike(jorge_choice))
    
    print("Sooraj buy bike {}".format(sooraj_choice.modelName))
    Sooraj.buy_bike(bikeshop.sell_bike(sooraj_choice))
    
    print("print out the bicycle shop's remaining inventory for each bike")
    bikeshop.print_inventory()
    
    print("Profit get from selling bikes for {} is {}".format(bikeshop.name, bikeshop.calc_profit()))
    
    
    
if(__name__ == '__main__'):
    main()