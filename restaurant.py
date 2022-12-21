class Restuarant:
    """A simple attempt to model a restuaramt"""
    def __init__(self, rest_name, cusine_type):
        """Initialize name and cusine attributes"""
        self.rest_ = rest_name
        self.cusine_type = cusine_type

    def describe_restuarant(self):
        """Print establishment name and cusine in response to a command"""
        print(f"The name of the restuarant is {self.rest_name} and it serves {self.cusine_type}.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over.")
