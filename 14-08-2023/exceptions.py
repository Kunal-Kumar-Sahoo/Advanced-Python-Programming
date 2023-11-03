# Different types of Exceptions
def handle_errors():
    try:
        # ZeroDivisionError
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError")

    try:
        # TypeError
        value = "string" + 5 # data type of an object in an operation is inappropriate
    except TypeError:
        print("Caught TypeError")

    try:
        # ValueError
        num = int("abc") # Invalid argument value to a function
    except ValueError:
        print("Caught ValueError") 

    try:
        # IOError
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
    except IOError:
        print("Caught IOError")

    try:
        # IndexError
        my_list = [1, 2, 3]
        item = my_list[5]
    except IndexError:
        print("Caught IndexError")

    try:
        # KeyError
        my_dict = {"key": "value"}
        value = my_dict["nonexistent_key"]
    except KeyError:
        print("Caught KeyError")

    try:
        # NameError
        undefined_variable # Use a variable, function, or module that doesn't exist or wasn't used in a valid way
    except NameError:
        print("Caught NameError")

# Multiple Exceptions
def handle_multiple_exceptions():
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print("Result:", result)

        my_list = [1, 2, 3]
        index = int(input("Enter an index: "))
        item = my_list[index]
        print("Item at index:", item)

        my_dict = {"key1": 5, "key2": 8}
        key = input("Enter a key: ")
        value = my_dict[key]
        print("Value for key:", value)

    except (ZeroDivisionError, ValueError, TypeError):
        print("Caught an error related to division, value, or type.")

    except (IndexError, KeyError):
        print("Caught an error related to index or key.")

    except Exception as e:
        print("Caught an unknown error:", e)
    else: #else clause is executed if no exceptions occur inside the try block
        print("Operation Successfully Completed without Exceptions")
    finally: #finally block is always executed after leaving the try statement
        print("In finally...") 

# Creating Custom Exceptions for File Operation
class FileOperationError(Exception):
    def __init__(self, message):
        self.message = message

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:", content)
    except FileNotFoundError:
        raise FileOperationError("File not found") # Calling init() by passing message
    except PermissionError:
        raise FileOperationError("Permission denied") # Calling init() by passing message


if __name__ == "__main__":
    handle_errors()
    
    handle_multiple_exceptions()
    
    try:
        filename = input("Enter the filename: ")
        read_file(filename)
    except FileOperationError as e:  # using custom exception 
        print("File operation error:", e.message)
    except Exception as e:
        print("An unknown error occurred:", e)