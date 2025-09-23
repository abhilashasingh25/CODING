# python program to get the class name of an instance

# using type() and __name__attribute

class vehicle:
    def name(self,name):
        return name
    
v= vehicle()

print(type(v).__name__)