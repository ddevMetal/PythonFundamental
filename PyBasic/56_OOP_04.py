# OOP - Inheritance
class Element:
    
    def __init__(self):
        # This base constructor runs for all elements unless overridden
        print('Element __init__ executed.')
        self.category = self.category_name() # Use a method to get class name
    
    def category_name(self):
        # Returns the name of the current class (e.g., 'Wall', 'Floor')
        return self.__class__.__name__
    
    def move(self):
        print(f'Moving {self.category_name()}.')
    
    def rotate(self):
        print(f'Rotating {self.category_name()}.')
        
    def scale(self):
        print(f'Scaling {self.category_name()}.')


# Child Class Inherited from Parent Class
class Wall(Element):
    def __init__(self):
        # Use super() to run the Parent's (Element) initialization code first
        super().__init__() 
        print('Wall __init__ executed.')

    def move(self):
        # Override the parent's move method with specific logic
        print('Moving Wall based on Line.')

class Floor(Element):
    def __init__(self):
        # Calls the Parent constructor to ensure 'self.category' is set up
        super().__init__()
        print('Floor __init__ executed.')
            
    def move(self):
        # Override the parent's move method with specific logic
        print('Moving Floor based on Point.')


# Object instances
# Creating these will now trigger both Element and specific child __init__ methods
wall_a = Wall()
floor_a = Floor()

print("-" * 10)
wall_a.move()   # Executes the overridden version in Wall
floor_a.move()  # Executes the overridden version in Floor
wall_a.rotate() # Executes the inherited version from Element
