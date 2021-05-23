# Exercise 3 : Restaurant Menu Manager
# Instructions
# The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.
# 1 Create a python file called menu_manager.py.
# 2 Create a class called MenuManager.
# 3 Create a method __init__ that instantiates an attribute called menu. The menu attributes value will be 
# all the current dishes (list of dictionaries). Each dish will be stored in a dictionary where the keys are name, price,
# spice level and gluten index (which value is a boolean).
# 4 Here is a list of the dishes currently on the menu:

    # Soup – 10 – B - False
    # Hamburger – 15 - A - True
    # Salad – 18 - A - False
    # French Fries – 5 - C - False
    # Beef bourguignon– 25 - B - True

    # Meaning: For the spice level:
    #    • A = not spicy,
    #    • B = a little spicy,
    #    • C = very spicy
    
# The dishes provided above should be the value of the menu attribute.
# 1. Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.
# 2. Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu, 
# if the dish exists then update it. If not notify the manager that the dish is not in the menu.
# 3. Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists 
# then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.
        # self.menu = menu
        # self.spice_level = spice_level
        # self.gluten_index = bool

# class MenuManager:
#     def __init__(self):
#         self.menu = {}

#     def add_item(self, **kwargs):
#         self.menu.update(kwargs)
#         print(self.menu)
                     
                     
#     def update_item(self, **kwargs):
#         name = self.menu.get("name")
#         updated_name = kwargs.get("name")
#         if name == updated_name:
#             self.menu.update(kwargs)
#             print(self.menu)
#         else:
#             print('your item is not on the menu')

      
#     def remove_item(self, **kwargs):
#         name = self.menu.get("name")
#         remove_name = kwargs.get("name")
#         if name == remove_name:
#             self.menu.clear()
#             print(self.menu)
#         else:
#             print('your item was not in the menu')
            
    
#     def __repr__(self):
#         return self.menu
    
# m1 = MenuManager()
# m1.add_item(name = 'Soup', price = 10, spice = 'B', gluten = False)
# m1.update_item(name = 'Soup', price = 10, spice = 'B', gluten = True)
# m1.remove_item(name = 'Soup', price = 10, spice = 'B', gluten = True)

# ?????????????????????????????

menu = [
    {
        'name': 'Soup',
        'price': 10,
        'spice_level': 'B',
        'gluten_index': False
    },
    {
        'name': 'Hamburger',
        'price': 15,
        'spice_level': 'A',
        'gluten_index': True
    },
    {
        'name': 'Salad',
        'price': 18,
        'spice_level': 'A',
        'gluten_index': False
    },
    {
        'name': 'French fries',
        'price': 5,
        'spice_level': 'C',
        'gluten_index': False
    },
    {
        'name': 'Beef bourguignon',
        'price': 25,
        'spice_level': 'B',
        'gluten_index': True
    },
]

class MenuManager:
    
    def __init__(self, menu):
        self.menu = menu
    
    def add_item(self, **kwargs):
        self.menu.append(new_item)
    
    def update_item(self, **item_to_update):
        for item in self.menu: 
            if item["name"] == item_to_update["name"]:
                item["price"] = item_to_update["price"]
                item["spice_level"] = item_to_update["spice_level"]
                item["gluten_index"] = item_to_update["gluten_index"]
                
                return
        print('your item is not in the list')

    def remove_item(self, name):
        for item in self.menu:
            if item["name"] == name:
                self.menu.pop(self.menu.index(item))
                

    
    def display_menu(self):
        for item in self.menu:
            print(f'{self.menu.index(item) + 1} : {item}')
        
    
# 3. Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists 
# then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.



m1 = MenuManager(menu)
# m1.update_item(name = 'Soup', price = 15, spice_level = 'A', gluten_index = True)
m1.remove_item('Soup')
print(m1.display_menu())