class Calculator:
    @staticmethod
    def add(a,b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        cls.calculation_type = 'Calculation type: Arithmetic Operations'
        print(cls.calculation_type)
        return a * b