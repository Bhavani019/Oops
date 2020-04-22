from oop_assignment_001.car import Car
import math
class RaceCar(Car):
    def __init__(self,color='',max_speed=0,acceleration=0,tyre_friction=0):
        self._nitro = 0
        super().__init__(color,max_speed,acceleration,tyre_friction)
        
        
    @property
    def nitro(self):
        return self._nitro
    

    def accelerate(self):
        if self._is_engine_started==True:
            if self._nitro>0:
                value = math.ceil(self._acceleration*30/100)
                self._nitro-=10
                if self._current_speed+self._acceleration+value < self._max_speed:
                    self._current_speed +=  self._acceleration+value
                else:
                    self._current_speed = self._max_speed
            else:
                self._current_speed+=self._acceleration
                if self._current_speed>self._max_speed:
                    self._current_speed = self._max_speed
        else:
            print('Start the engine to accelerate')
                
        
    def apply_brakes(self):
        if self._current_speed>=(self._max_speed//2):
            self._nitro += 10
        if self._current_speed > self._tyre_friction:
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed = 0
            
        
    def sound_horn(self):
        if self._is_engine_started == True:
            print('Peep Peep\nBeep Beep')
        else:
            print('Start the engine to sound_horn')
    
    
            
    
            
    
            
    
        
    
        
        
            
        
            
        
            
    
        
        
            
    
        

    
        
