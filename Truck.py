from oop_assignment_001.car import Car
class Truck(Car):
    def __init__(self,color='',max_speed=0,acceleration=0,tyre_friction=0,max_cargo_weight=0):
        self._max_cargo_weight = max_cargo_weight
        self._load = 0
        super().__init__(color,max_speed,acceleration,tyre_friction)
        
    
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    
    def load(self,cargo_weight):
        if cargo_weight<0:
            raise ValueError('Invalid value for cargo_weight')
        elif self._load + cargo_weight >= self._max_cargo_weight:
            print('Cannot load cargo more than max limit: {}'.format(self._max_cargo_weight))
        elif self._current_speed == False:
            self._load += cargo_weight
        else:
            print('Cannot load cargo during motion')
            
            
    def unload(self,cargo_weight):
        if cargo_weight<0:
            raise ValueError('Invalid value for cargo_weight')
        elif self._current_speed == False:
            self._load -= cargo_weight
        else:
            print('Cannot unload cargo during motion')
        
        
    def sound_horn(self):
        if self._is_engine_started == True:
            print('Honk Honk')
        else:
            print('Start the engine to sound_horn')
            
    
            
    
            
    
        
    
        
        
            
        
            
        
            
    
        
        
            
    
        

    
        
