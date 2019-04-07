class OperationSingleton:
    __instance = None

    ADD_OPERATION = 1
    SUBSTRACT_OPERATION = 2
    MULTIPLY_OPERATION = 3
    DIVIDE_OPERATION = 4

    @classmethod
    def __getInstance(cls):
        return cls._instance

    @classmethod
    def getInstance(cls, *args, **kargs):
        if not cls.__instance:
            cls.__instance = cls(*args, **kargs)
        return cls.__instance

    def operate(self, operatorType, firstNumber, secondNumber):
        answer = 0
        operator = None

        if operatorType == OperationSingleton.ADD_OPERATION:
            answer = firstNumber + secondNumber
            operator = "+"
        elif operatorType == OperationSingleton.SUBSTRACT_OPERATION:
            answer = firstNumber - secondNumber
            operator = "-"
        elif operatorType == OperationSingleton.MULTIFLY_OPERATION:
            answer = firstNumber * secondNumber
            operator = "*"
        elif operatorType == OperationSingleton.DIVIDE_OPERATION:
            answer = firstNumber / secondNumber
            operator = "/"
        result = str(firstNumber) + operator + str(secondNumber) + "=" + str(answer)

        self.printResult(result)

    def printResult(self, result):
        print(result)

class Client:
    def main(self):
        calculatorSingleton = OperationSingleton.getInstance()

        firstNumber = 100
        secondNumber = 20

        calculatorSingleton.operate(OperationSingleton.ADD_OPERATION, firstNumber, secondNumber)
        calculatorSingleton.operate(OperationSingleton.SUBSTRACT_OPERATION, firstNumber, secondNumber)
        calculatorSingleton.operate(OperationSingleton.MULTIPLY_OPERATION, firstNumber, secondNumber)
        calculatorSingleton.operate(OperationSingleton.DIVIDE_OPERATION, firstNumber, secondNumber)

client = Client()
client.main()