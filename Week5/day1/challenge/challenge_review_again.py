

class Farm:
    def __init__(self, farm):
        self.farm = farm
        self.animal_list = {}
    
    
    def add_animal(self, animal, amount = 1):
        self.animal_list[animal] = amount
        for item in self.animal_list:
            if item["animal"] == animal:
                item[animal] += 1
            
        # print(self.animal_list)
        
    def __repr__(self):
        return self.animal_list
        
    def get_info(self):
        print(f"{self.farm}'s farm\n\n {self.animal_list} \n\n E-I-E-I-0!")
        
        
        
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
