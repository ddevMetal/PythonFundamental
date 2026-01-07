# ============================================
# OOP - Object Oriented Programming
# ============================================
# OOP is a programming paradigm that organizes code into reusable objects
# Key Concepts: Classes, Objects, Attributes, Methods, Encapsulation

"""
LESSON STRUCTURE:
1. Class Definition (Blueprint)
2. Class Attributes (Shared by all instances)
3. Instance Attributes (Unique to each object)
4. Methods (Functions that belong to a class)
5. Creating Objects (Instances)
6. Using Objects (Calling methods and accessing attributes)
"""

# ============================================
# PART 1: CLASS DEFINITION
# ============================================
# A class is a BLUEPRINT/TEMPLATE for creating objects
# Think of it like a cookie cutter - you can make many cookies from one cutter

class Element:
    """
    Element class represents a 2D rectangular element with position and material.
    Used to demonstrate core OOP concepts.
    """
    
    # ============================================
    # PART 2: CLASS ATTRIBUTE
    # ============================================
    # Class attributes are SHARED by ALL instances of the class
    # Useful for tracking data across all objects
    id_counter = 0  # Tracks total number of elements created
    
    # ============================================
    # PART 3: CONSTRUCTOR METHOD (__init__)
    # ============================================
    # The __init__ method is called automatically when creating a new object
    # It initializes the object's attributes (properties)
    
    def __init__(self, width, height, location, material):
        """
        Constructor method - initializes a new Element object.
        
        Args:
            width (int/float): Width of the element
            height (int/float): Height of the element
            location (tuple): (x, y) coordinates of the element
            material (str): Material type (e.g., "wood", "metal")
        
        About 'self':
            - 'self' refers to the current instance of the class
            - It allows you to access attributes and methods of THIS specific object
            - Python automatically passes 'self' - you don't need to provide it when calling
        """
        # ============================================
        # PART 4: INSTANCE ATTRIBUTES
        # ============================================
        # Instance attributes are UNIQUE to each object
        # Each Element object has its own width, height, location, etc.
        self.width = width          # Object's width
        self.height = height        # Object's height
        self.location = location    # Object's position (x, y)
        self.material = material    # Object's material type
        self.id = self._generate_id()  # Unique ID for this object
        
        print(f'✓ Creating Element <ID: {self.id}> [{material}]')
    
    # ============================================
    # PART 5: INSTANCE METHODS
    # ============================================
    # Methods are functions that belong to a class
    # They can access and modify the object's attributes using 'self'
    
    def _generate_id(self):
        """
        Private method to generate unique IDs for each element.
        (Convention: methods starting with _ are intended as private/internal)
        
        Returns:
            int: Unique ID number
        """
        Element.id_counter += 1  # Increment class attribute
        return Element.id_counter
    
    def area(self):
        """
        Calculate the area of the element.
        
        Returns:
            float: Area (width × height)
        """
        return self.width * self.height
    
    def move(self, delta_x, delta_y):
        """
        Move the element by specified offsets.
        
        Args:
            delta_x (int/float): Amount to move on X axis
            delta_y (int/float): Amount to move on Y axis
        """
        old_x, old_y = self.location
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        self.location = (new_x, new_y)
        print(f'→ Element {self.id} moved from ({old_x}, {old_y}) to ({new_x}, {new_y})')
    
    def resize(self, new_width, new_height):
        """
        Resize the element to new dimensions.
        
        Args:
            new_width (int/float): New width
            new_height (int/float): New height
        """
        old_area = self.area()
        self.width = new_width
        self.height = new_height
        new_area = self.area()
        print(f'⤡ Element {self.id} resized: Area changed from {old_area} to {new_area}')
    
    def display_info(self):
        """Display all information about this element in a formatted way."""
        print(f'\n{"=" * 40}')
        print(f'ELEMENT INFO - ID: {self.id}')
        print(f'{"=" * 40}')
        print(f'Material:  {self.material}')
        print(f'Location:  {self.location}')
        print(f'Width:     {self.width}')
        print(f'Height:    {self.height}')
        print(f'Area:      {self.area()}')
        print(f'{"=" * 40}\n')
    
    def __str__(self):
        """
        Special method that defines string representation of the object.
        Called when using print() or str() on the object.
        """
        return f'Element(id={self.id}, material={self.material}, location={self.location})'
    
    def __repr__(self):
        """
        Special method for developer-friendly representation.
        Useful for debugging.
        """
        return f'Element({self.width}, {self.height}, {self.location}, "{self.material}")'


# ============================================
# PART 6: CREATING OBJECTS (INSTANCES)
# ============================================
# Objects are INSTANCES of a class
# Each object has its own unique attribute values

print('\n' + '='*50)
print('CREATING OBJECTS')
print('='*50)

# Create first element - a wooden panel
element_a = Element(width=10, height=20, location=(0, 0), material="wood")

# Create second element - a metal plate
element_b = Element(width=30, height=40, location=(5, 5), material="metal")

# Create third element - a glass window
element_c = Element(width=15, height=25, location=(10, 15), material="glass")

# ============================================
# PART 7: USING OBJECTS
# ============================================
# Access attributes and call methods on objects

print('\n' + '='*50)
print('USING OBJECTS - METHOD CALLS')
print('='*50)

# Move element_a
element_a.move(30, 500)

# Resize element_b
element_b.resize(50, 60)

# Display all element information
print('\n' + '='*50)
print('DISPLAYING OBJECT DATA')
print('='*50)

element_a.display_info()
element_b.display_info()
element_c.display_info()

# ============================================
# PART 8: ACCESSING ATTRIBUTES DIRECTLY
# ============================================
print('='*50)
print('DIRECT ATTRIBUTE ACCESS')
print('='*50)

print(f'\nElement A material: {element_a.material}')
print(f'Element B location: {element_b.location}')
print(f'Element C area: {element_c.area()}')

# ============================================
# PART 9: CLASS ATTRIBUTE ACCESS
# ============================================
print(f'\nTotal elements created: {Element.id_counter}')

# ============================================
# PART 10: STRING REPRESENTATIONS
# ============================================
print('\n' + '='*50)
print('STRING REPRESENTATIONS')
print('='*50)

print(f'\nUsing print(): {element_a}')
print(f'Using repr(): {repr(element_b)}')

# ============================================
# KEY TAKEAWAYS
# ============================================
"""
1. CLASS = Blueprint/Template (defines structure and behavior)
2. OBJECT = Instance (actual thing created from the blueprint)
3. ATTRIBUTES = Properties/Data (what the object HAS)
4. METHODS = Functions (what the object CAN DO)
5. self = Reference to the current instance
6. Class attributes = Shared by all instances
7. Instance attributes = Unique to each object
"""