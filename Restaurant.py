class Restaurant():
    """餐厅类练习"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant():
        print("The name of restaurant is " + self.restaurant_name.title())
        print("The cuisine type of this restaurant is " +
              self.cuisine_type.title())


my_restaurant = Restaurant('bai ri wu qian nian', 'zashi')
