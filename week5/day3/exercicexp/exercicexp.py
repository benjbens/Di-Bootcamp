# Exercice 1 

# def abs():
#     """ 
#     it help the user
#     """


# print(abs.__doc__)
        
# def int():
#     """
#     returns the int of the type
#     """

# print(int.__doc__)

# def input():
#     """
#     it ask the user 
#     """

# print(input.__doc__)

# Exercice 2 




class Currency:
    def __init__(self, type_of, amount):

        self.amount = amount 
        self.type_of = type_of


    def __str__(self):
        return f'{self.amount} {self.type_of}'

    def __int__(self):
        return int(self.amount)

    def __repr__(self):
        return f'{self.amount} {self.type_of}'

    def __add__(self, other):
        if (self.type_of) == (other.type_of):
            return self.amount + other.amount
        else:
            raise ValueError

    def __iadd__(self, other):
        if (self.type_of) == (other.type_of):
            return f"{self.amount + other.amount} {self.type_of}"
        else:
            raise ValueError

    


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)



print(c1)
