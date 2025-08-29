import math


class Calculator:
    def __init__(self):
        
        self.buttons = [
            ('c', 'ce', 'mrc', 'm-', 'm+'),
            ('7', '8', '9', '%', 'sqrt'),
            ('4', '5', '6', chr(215), chr(247)),
            ('1', '2', '3', '+', '-'),
            ('0', '.', '+/-', '=')
        ]
        
        self.ndigits = 12
        self.start_zero = '0'
        self.error = 'error'
        
    def evaluate(self, expr: str):
        try:
            result = eval(self.translate_expr(expr))
            return self.format_result(result)
        except Exception:
            return self.error.capitalize()
        
    def format_result(self, result: int | float) -> str:
        if len(str(result)) > self.ndigits:
            result = round(result, self.ndigits)
        if str(result).endswith('.0'):
            result = int(result)
        return str(result)
    
    def translate_expr(self, expr: str) -> str:
        trans_table = ''.maketrans({chr(215): '*', chr(247): '/'})
        return expr.translate(trans_table).lower()
    
    def negate_number(self, number: int | float) -> str:
        try:
            return self.format_result(-float(number))
        except Exception:
            return self.error.capitalize()
        
    def compute_sqrt(self, number: int | float) -> str:
        try:
            return self.format_result(math.sqrt(number))
        except Exception:
            return self.error.capitalize()