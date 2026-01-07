# ============================================
# OOP - INHERITANCE
# ============================================
# Inheritance allows a class to inherit attributes and methods from another class
# Parent Class (Base/Super class) → Child Class (Derived/Sub class)

# ============================================
# PARENT CLASS (BASE CLASS)
# ============================================
class Element:
    """Base class for all architectural elements"""
    
    def get_class_name(self):
        """
        Returns the name of the current class.
        Uses __class__.__name__ to dynamically get the class name.
        """
        return self.__class__.__name__
    
    def move(self):
        """Default move behavior for all elements"""
        print(f'Moving {self.get_class_name()}.')
              
    def rotate(self):
        """Default rotate behavior for all elements"""
        print(f'Rotating {self.get_class_name()}.')
        
    def scale(self):
        """Default scale behavior for all elements"""
        print(f'Scaling {self.get_class_name()}.')


# ============================================
# CHILD CLASSES (DERIVED CLASSES)
# ============================================
# Child classes inherit all methods from parent but can override them

class Wall(Element):
    """
    Wall inherits from Element.
    Overrides move() method with custom behavior.
    """
    def move(self):
        """Custom move behavior for walls - overrides parent method"""
        print('Moving Wall based on Line (start and end points).')


class Floor(Element):
    """
    Floor inherits from Element.
    Overrides move() method with custom behavior.
    """
    def move(self):
        """Custom move behavior for floors - overrides parent method"""
        print('Moving Floor based on Point (boundary points).')


# ============================================
# CREATING INSTANCES
# ============================================
wall_a = Wall()
floor_a = Floor()

print('\n' + '='*50)
print('INHERITANCE DEMONSTRATION')
print('='*50 + '\n')

# ============================================
# METHOD CALLS - POLYMORPHISM IN ACTION
# ============================================

# Overridden methods (custom behavior for each child)
print('--- Overridden Methods (Custom Behavior) ---')
wall_a.move()      # Uses Wall's custom move() method
floor_a.move()     # Uses Floor's custom move() method

print()

# Inherited methods (same behavior from parent)
print('--- Inherited Methods (From Parent Element) ---')
wall_a.rotate()    # Uses Element's rotate() method
floor_a.rotate()   # Uses Element's rotate() method
wall_a.scale()     # Uses Element's scale() method     
floor_a.scale()    # Uses Element's scale() method

# ============================================
# KEY CONCEPTS
# ============================================
"""
1. INHERITANCE: Wall and Floor inherit from Element
2. METHOD OVERRIDING: Child classes override move() with custom behavior
3. METHOD INHERITANCE: rotate() and scale() are inherited as-is
4. POLYMORPHISM: Same method name (move) behaves differently for different objects
5. super().__method__: Can call parent's method from child (not shown here)
"""