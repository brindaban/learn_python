class Complex_No:

    def __init__(self,real,imaginary):
        self.__realNo = real
        self.__imaginaryNo = imaginary

    def getReal(self):
        return self.__realNo

    def getImaginary(self):
        return self.__imaginaryNo

    def add(self,other):
        return Complex_No(self.__realNo + other.__realNo, self.__imaginaryNo + other.__imaginaryNo)
