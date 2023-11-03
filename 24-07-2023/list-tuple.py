if __name__ == '__main__':
    # Take input from the user
    _input = map(int, input('Enter sequence of numbers: ').split())

    # Convert the same input to list and tuple
    _list = list(_input)
    _tuple = tuple(_list)

    print(f'List: {_list}')
    print(f'Tuple: {_tuple}')

    try:
        # Check the mutability of lists and tuples.
        print('Changing first element of both the data type to 69')
        _list[0] = 69
        print(f'New list: {_list}')
        _tuple[0] = 69
        print(f'New tuple: {_tuple}')
    except Exception as e:
        print(f'Error: {e}')