class Pokemon:
    running=''
    swimming=''
    sound=''
    flying=''
    
    def __init__(self,name,level=1):
        self._name=name
        self._level=level
        self._master=None
        
        if self._name=='':
            raise ValueError('name cannot be empty')
        
        if self._level<=0:
            raise ValueError('level should be > 0')
        
    @property
    def master(self):
        if self._master == None:
            print('No Master')
        else:
            return self._master

    @property
    def name(self):
        return self._name
        
    @property    
    def level(self):
        return self._level
    
    def __str__(self):
        return ("{} - Level {}".format(self._name,self._level))
 
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    @classmethod
    def run(cls):
        print(cls.running)
        
    @classmethod
    def swim(cls):
        print(cls.swimming)
        
    @classmethod
    def fly(cls):
        print(cls.flying)

class Pikachu(Pokemon):
    sound="Pika Pika"
    running="Pikachu running..."
    
    def attack(self):
        print("Electric attack with {} damage".format((self._level)*10))
        self._level += 1
        
 
class Squirtle(Pokemon):
    sound="Squirtle...Squirtle"
    running="Squirtle running..."
    swimming="Squirtle swimming..."
    
    def attack(self):
        print("Water attack with {} damage".format((self._level)*9))
        self._level += 1

class Pidgey(Pokemon):
    sound="Pidgey...Pidgey"
    flying="Pidgey flying..."
         
    def attack(self):
        print("Air attack with {} damage".format((self._level)*5))
        self._level +=1

class Swanna(Pokemon):
    sound="Swanna...Swanna"
    flying="Swanna flying..."
    swimming="Swanna swimming..."
    
    def attack(self):
        print("Water attack with {} damage".format((self._level)*9))
        print("Air attack with {} damage".format((self._level)*5))
        self._level += 1

class Zapdos(Pokemon):
    sound="Zap...Zap"
    flying="Zapdos flying..."
    
    def attack(self):
        print("Electric attack with {} damage".format((self._level)*10))
        print("Air attack with {} damage".format((self._level)*5))
        self._level += 1
        
class Island:
    list1 = []
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs,pokemon_left_to_catch=0):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = pokemon_left_to_catch
        self.list2 = []
        self.list1.append(self)
        
    @property
    def name(self):
        return self._name
        
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
    
    def __str__(self):
        return ('{} - {} pokemon - {} food'.format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs))
    
    def add_pokemon(self,object):
        if self._pokemon_left_to_catch < self._max_no_of_pokemon:
            self._pokemon_left_to_catch+=1
        else:
            print('Island at its max pokemon capacity')
            
    @classmethod
    def get_all_islands(cls):
        return cls.list1
        

class Trainer(Island):
    def __init__(self,name):
        self._name = name
        self._experience = 100
        self._food_in_bag = 0
        self._max_food_in_bag = 10 * self._experience
        self._current_island = None
        self.list3 = []
        
    @property
    def name(self):
        return self._name
    
    @property
    def experience(self):
        return self._experience
        
    @property
    def food_in_bag(self):
        return self._food_in_bag
    
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
        
    @property
    def current_island(self):
        if self._current_island == None:
            print('You are not on any island')
        else:
            return self._current_island
    
    def __str__(self):
        return ('{}'.format(self._name))
        
    def move_to_island(self,island):
        self._current_island = island
        
    def get_my_pokemon(self):
        return self.list3
        
    def collect_food(self):
        if self._current_island == None:
            print('Move to an island to collect food')
        elif self._current_island._total_food_available_in_kgs<self._max_food_in_bag:
            self._food_in_bag = self._current_island._total_food_available_in_kgs
            self._current_island._total_food_available_in_kgs=0
        elif self._food_in_bag!=self._max_food_in_bag:
            self._current_island._total_food_available_in_kgs-=self._max_food_in_bag
            self._food_in_bag = self._max_food_in_bag
            
    def catch(self,pokemon):
        if self._experience >= 100*pokemon.level:
            self.list3.append(pokemon)
            print('You caught {}'.format(pokemon.name))
            self._experience+=pokemon.level*20
            pokemon._master = self
        else:
            print('You need more experience to catch {}'.format(pokemon.name))
 
