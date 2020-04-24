class Animal:
    sound_by_animal=""
    make_breathe=""
    feed_grow=0
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        if age_in_months != 1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        if required_food_in_kgs <= 0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        else:
            self._required_food_in_kgs=required_food_in_kgs
        self._breed=breed
        
    @property
    def age_in_months(self):
        return self._age_in_months
    
    @property
    def breed(self):
        return self._breed 
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    @classmethod
    def breathe(cls):
        print(cls.make_breathe)
    
    @classmethod
    def make_sound(cls):
        print(cls.sound_by_animal)
        
    
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.feed_grow    
        
class Deer(Animal):
    sound_by_animal="Buck Buck"
    make_breathe="Breathe in air"
    feed_grow=2
    
class Lion(Animal):
    sound_by_animal="Roar Roar"
    make_breathe="Breathe in air"
    feed_grow=4
    def hunt(self,hunt_animal):
        kill='Deer'
        hunting(hunt_animal,kill)
    
    
class Shark(Animal):
    sound_by_animal="Shark Sound"
    make_breathe="Breathe oxygen from water"
    feed_grow=8
    def hunt(self,hunt_animal):
        kill='GoldFish'
        hunting(hunt_animal,kill)
    
    
class GoldFish(Animal):
    sound_by_animal="Hum Hum"
    make_breathe="Breathe oxygen from water"
    feed_grow=0.2
    
class Snake(Animal):
    sound_by_animal="Hiss Hiss"
    make_breathe="Breathe in air"
    feed_grow=0.5
    def hunt(self,hunt_animal):
        kill='Deer'
        hunting(hunt_animal,kill)

class Zoo(Deer,Lion,Shark,GoldFish,Snake):
    total_animals=[]
    def __init__(self):
        self.store_animals = []
        self._reserved_food_in_kgs=0
        
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs += food
        
    def add_animal(self,animal):
        self.store_animals.append(animal)
        self.total_animals.append(animal)
    
    def count_animals(self):
        return len(self.store_animals)
    
    def feed(self,animal):
        if self._reserved_food_in_kgs > 0:
            self._reserved_food_in_kgs -= animal.required_food_in_kgs
            animal.grow()
    def required_food_in_kgs(self):
        return self.required_food_in_kgs
            
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.total_animals)
        
    @staticmethod
    def count_animals_in_given_zoos(zoos):
        count=0
        for zoo in zoos:
            count+=zoo.count_animals()
        return count
    
    @property
    def reserved_food_in_kgs(self):
        return  self._reserved_food_in_kgs
        
def hunting(animal,kill):
    count1=0
    count = 0
    for i in animal.store_animals:
        if i.__class__==Deer:
            count =1
            animal.store_animals.remove(i)
        elif i.__class__==GoldFish:
            count1 =1
            animal.store_animals.remove(i)
                
        if count==0 and kill=='Deer':
            print('No deers to hunt')
        elif count1==0 and kill=='GoldFish':
            print('No GoldFish to hunt')
        
