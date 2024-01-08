'''


#----------------------------------------#
Define a custom exception class which takes a string message as attribute.

Hints:

To define a custom exception, we need to define a class inherited from Exception.

'''

class CustomExeption(Exception):
    msg = 'explanation of the error'
    def __init__(self, msg):
        self.msg = msg
    def show(self):
        return print(self.msg)
error = CustomExeption("something wrong")
error.show()
