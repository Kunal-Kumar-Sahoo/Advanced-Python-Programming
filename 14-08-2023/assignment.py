class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Insufficient funds: You tried to withdraw ${amount}, but your balance is only ${balance}.")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."
    except IOError as e:
        return f"An IOError occurred: {e}"

def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            return True
    except PermissionError:
        return "Permission denied: Unable to write to file."
    except IOError as e:
        return f"An IOError occurred: {e}"

def perform_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except TypeError as e:
        return f"TypeError: {e}"

def perform_indexing(data_list, index):
    try:
        value = data_list[index]
        return value
    except IndexError:
        return "Index out of range."
    except TypeError as e:
        return f"TypeError: {e}"

def convert_to_int(string):
    try:
        integer_value = int(string)
        return integer_value
    except ValueError:
        return "Invalid input. Cannot convert to integer."

def open_socket(host, port):
    try:
        # Simulate opening a socket connection
        print(f"Opened socket connection to {host} on port {port}")
    except ConnectionError:
        return "Connection error: Unable to establish a socket connection."

def main():
    try:
        option = int(input("Choose an option:\n1. Read from file\n2. Write to file\n3. Perform division\n4. Indexing\n5. Convert to integer\n6. Open socket\n"))
        
        if option == 1:
            filename = input("Enter filename to read from: ")
            content = read_file(filename)
            print("File content:", content)
        elif option == 2:
            filename = input("Enter filename to write to: ")
            content = input("Enter content to write: ")
            success = write_to_file(filename, content)
            if success:
                print("Write successful.")
            else:
                print("Write failed.")
        elif option == 3:
            num1 = float(input("Enter numerator: "))
            num2 = float(input("Enter denominator: "))
            result = perform_division(num1, num2)
            print("Result of division:", result)
        elif option == 4:
            data_list = [10, 20, 30]
            index = int(input("Enter index to access: "))
            value = perform_indexing(data_list, index)
            print("Value at index:", value)
        elif option == 5:
            input_string = input("Enter a value to convert to integer: ")
            int_value = convert_to_int(input_string)
            print("Converted integer value:", int_value)
        elif option == 6:
            host = input("Enter host: ")
            port = int(input("Enter port: "))
            open_socket(host, port)
        else:
            print("Invalid option.")
    
    except ValueError:
        print("Invalid input. Please enter a valid option or value.")

if __name__ == "__main__":
    main()
