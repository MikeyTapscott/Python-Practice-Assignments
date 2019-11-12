#! /usr/bin/env python
import math
​
class Pi():
    
    def __init__(self, diameter, round_2):
        self.diameter=diameter
        self.round_2=round_2
        
    def calculate_pi(self):
        return round((math.pi)*((self.diameter / 2.0)**2.0),self.round_2)
​
def circle_dimensions():
    done=False
    while not done:
        try:
            values=Pi(int(raw_input('enter in the diameter of the circle: ')),int(raw_input('enter in the amount of precision: ')))
            print(values.calculate_pi())
            done=True  
        except ValueError as e:
        #error handling another date
            if e:
                print('you need to enter in both diameter and round_2 digit')
if __name__=='__main__':
    circle_dimensions()
