# Write a program to do distance addition using OOP

class Distance:
    def __init__(self, feet, inches): # Constructor
        self.__feet = feet
        self.__inches = inches

        if self.__inches >= 12:
            '''Ensure data is correct'''
            self.__feet += self.__inches // 12
            self.__inches %= 12

    def __str__(self):
        '''Returns string representation of the distance'''
        return f'{self.__feet}\' {self.__inches}"'
    
    def getter(self):
        '''Returns feet and inches outside the class'''
        return self.__feet, self.__inches
    
    def __add__(self, dist):
        '''Operator overriding'''
        feet, inches = dist.getter()
        return Distance(self.__feet + feet, self.__inches + inches)
    
if __name__ == '__main__':
    feet, inches = map(int, input('Enter feets and inches for distance 1: ').split())
    d1 = Distance(feet, inches)
    
    feet, inches = map(int, input('Enter feets and inches for distance 2: ').split())
    d2 = Distance(feet, inches)
    
    feet, inches = map(int, input('Enter feets and inches for distance 3: ').split())
    d3 = Distance(feet, inches)

    print('Sum of all the three distances:', d1 + d2 + d3)