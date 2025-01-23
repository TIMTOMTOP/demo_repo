def helper_function():
    """
    Helper function in moduleB
    """
    print("Helper function from moduleB called")

class AnotherClass:
    """
    Another simple class
    """
    def another_method(self):
        # This method calls helper_function
        helper_function()