import customtkinter

# Assuming you have defined your functions and classes somewhere
# For example:
def light_button():
    customtkinter.set_appearance_mode("Light")

def dark_button():
    customtkinter.set_appearance_mode("Dark")

class Todo:
    def History_list(self):
        # Your implementation goes here
        pass

# Test functions
def test_light_button():
    """Test if light button sets appearance mode to light."""
    light_button()  # Call the function
    assert customtkinter.get_appearance_mode() == "Light", "Light button did not set appearance mode to 'Light'"

def test_dark_button():
    """Test if dark button sets appearance mode to dark."""
    dark_button()  # Call the function
    assert customtkinter.get_appearance_mode() == "Dark", "Dark button did not set appearance mode to 'Dark'"

def test_each_class_initialization():
    """Test if EachClass initializes components correctly."""
    app = Todo()  # Create an instance of Todo
    history_list = app.History_list()  # Call it as a method
    # You can add assertions here to check the behavior of History_list if needed

# Run tests (if you're using pytest or similar, you might not need this part)
if __name__ == "__main__":
    test_light_button()
    test_dark_button()
    test_each_class_initialization()