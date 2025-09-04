# Global variable
global_var = "I am a global variable"
class VariableDemo:
    def __init__(self, value):
        # Instance variable (local to the object)
        self.instance_var = value
    def show_variables(self):
        # Local variable inside the method
        local_var = "I am a local variable"
        
        print(local_var)            # Accessing local variable
        print(self.instance_var)    # Accessing instance variable (object-level)
        print(global_var)           # Accessing global variable
# Create an object of the class
demo = VariableDemo("I am an instance variable")
# Call the method to display variables

demo.show_variables()
