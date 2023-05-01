from restaurant import ItalianRestaurant, AmericanRestaurant


if __name__ == "__main__":
    italian_restaurant = ItalianRestaurant()  # Italian restaurant is created
    pizza = italian_restaurant.get_pizza()  # get a pizza concrete product
    beverage = italian_restaurant.get_beverage()  # get a beverage concrete product
    print(pizza.prepare())  # Output: Preparing Margherita Pizza
    print(beverage.serve())  # Output: Serving Coke

    american_restaurant = AmericanRestaurant()  # American restaurant is created
    pizza = american_restaurant.get_pizza()  # get a pizza concrete product
    beverage = american_restaurant.get_beverage()  # get a beverage concrete product
    print(pizza.prepare())  # Output: Preparing Pepperoni Pizza
    print(beverage.serve())  # Output: Serving Pepsi
