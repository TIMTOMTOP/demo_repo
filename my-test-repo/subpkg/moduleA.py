class Parent:
    """
    A simple parent class
    """
    def __init__(self):
        self.value = 42

def top_level_func(a, b):
    """
    A function defined at the module level
    """
    return a + b

class Child(Parent):
    """
    Child class inherits from Parent
    """
    def child_method(self, x):
        """
        Demonstrate a method that calls a top-level function
        """
        print("child_method called with:", x)
        print("Parent's value is:", self.value)
        # Call the module-level function
        return top_level_func(1, 2)