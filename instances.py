# python program to get the class name of an instances

# using __class__.__name__

class vehicle:
    def name(self,name):
        return name
v =vehicle()
print(v.__class__.__name__)    