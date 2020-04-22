import math
class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        if type(real_part) is str and type(imaginary_part) is str:
            raise ValueError('Invalid value for real and imaginary part')
        
        if type(real_part) is str:
            raise ValueError('Invalid value for real part')
        else:
            self.real_part = real_part
        
        if type(imaginary_part) is str:
            raise ValueError('Invalid value for imaginary part')
        else:
            self.imaginary_part = imaginary_part
        
        
    def __str__(self):
        return ('{}+{}i'.format(self.real_part,self.imaginary_part))
        
    def conjugate(self):
        return ComplexNumber(self.real_part,-self.imaginary_part)
        
    def __add__(self,other):
        return ComplexNumber(self.real_part + other.real_part,self.imaginary_part + other.imaginary_part)
    
    def __sub__(self,other):
        return ComplexNumber(self.real_part - other.real_part,self.imaginary_part - other.imaginary_part)
        
    def __mul__(self,other):
        real = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        imaginary = self.imaginary_part * other.real_part + self.real_part * other.imaginary_part
        return ComplexNumber(real,imaginary)
        
    def __truediv__(self,other):
        self_real,self_imaginary,other_real,other_imaginary = self.real_part, self.imaginary_part, other.real_part,other.imaginary_part
        r = float(other_real**2 + other_imaginary**2)   
        return ComplexNumber((self_real*other_real + self_imaginary*other_imaginary)/r, (self_imaginary*other_real - self_real*other_imaginary)/r)
      
    def __abs__(self):
        return round(math.sqrt(self.real_part**2 + self.imaginary_part**2),3)
        
    def  __eq__(self,other):
        if self.real_part == other.real_part and self.imaginary_part == other.imaginary_part:
           return True
        else:
           return False
            
            
            
