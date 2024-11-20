class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def abs(self):
        print((self.x**2+self.y**2+self.z**2)**0.5)
    def summa(self,other):
        a=(Vector(self.x+other.x,self.y+other.y,self.z+other.z))
        print(a.x,a.y,a.z)
    def difference(self,other):
        a=Vector(self.x-other.x,self.y-other.y,self.z-other.z)
        print(a.x,a.y,a.z)
    def dot_product(self,other):
        print(self.x*other.x+self.y*other.y+self.z*other.z)

    def mult(self,other):
        a=Vector(self.x*other,self.y*other,self.z*other)
        print(a.x,a.y,a.z)

v=Vector(3,45,5)
a=Vector(1,2,3)
v.dot_product(a)