import math
class circle:
    #area=0
    def __init__(self,r):

        if r<0:
            raise RuntimeError("Invalid Radius")
        else:
            self.rad=r
    def area(self):
        return (math.pi*self.rad**2)
#area=3.14*circle.rad**2
try:
    c1=circle(int(input("Enter the radius:")))
    print(c1.area())
except RuntimeError as ex:
    print (ex,'hell')
