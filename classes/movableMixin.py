from classes.robot import *

class MovableMixin(Robot):
    def MOVE(self,x,y):
        print("I moving")
        self.x = x
        self.y = y

    def WHERE(self):
        print(f"im at {self.x,self.y}")



