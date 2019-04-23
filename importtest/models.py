
COUNT = 365


class BaseModule :
    def __init__(self):
        self.name = 'init'
    def forword(self):
        self.input = 3

    def backward(self):
        pass

    def compute(self,a , b):
        return a + b



