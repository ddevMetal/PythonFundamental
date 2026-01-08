
# # class
# class Element:
#     id_count = 0                               # class variable   
    
#     def __init__(self, w, h, loc, mat):
#         self.width = w                           
#         self.height = h
#         self.location = loc
#         self.material = mat
#         self.id = self.generate_id()           # attribute for the instance
        
    
    
#     def generate_id(self):
#         Element.id_count += 1
#         return Element.id_count
        
#     def print_data(self):
#         print()
#         print(f'Element ID: {self.id}')
#         print(f'Material: {self.material}')
#         print(f'Location: {self.location}')
#         print(f'Width: {self.width}')
#         print(f'Height: {self.height}')
#         print(3*'-')
        
#     def move(self, x, y):
#         print(f'Moving element to new location: [{x}, {y}]')
#         old_x = self.location[0]
#         old_y = self.location[1]
#         self.location[0] = old_x + x
#         self.location[1] = old_y + y
        
#     def __repr__(self):     # repr <-- string representation of the object
#         return f'Element(ID: {self.id}, Material: {self.material}, Location: {self.location}, Width: {self.width}, Height: {self.height})'

      
    
# # Object instance based on template 
# elem_a = Element(10, 20 , [4,5], 'Stone')
# elem_b = Element(15, 25 , [1,2], 'Wood')

# elem_a.print_data()
# elem_b.print_data()

# print(elem_a)    # calls __repr__ method
# print(elem_b)    # calls __repr__ method


# OOP - Inheritance
class Element:
    
    def __init__(self):
        print('Element __init__ executed.')
        self.category = self.category()
    
    def category(self):
        return self.__class__.__name__
    
    def move(self):
        print(f'Moving {self.category()}.')
    
    def rotate(self):
        print(f'Rotating {self.category()}.')
        
    def scale(self):
        print(f'Scaling {self.category()}.')


# Child Class Inherited from Parent Class
class Wall(Element):
    def __init__(self):
        super().__init__()
        print('Wall __init__ executed.')

class Floor(Element):
    def __init__(self):
        super().__init__()
        print('Floor __init__ executed.')


# Object instance based on template 
wall_a = Wall()
floor_a = Floor()

wall_a.move()
floor_a.move()
