class Integer:

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if isinstance(float_value, float):
            return cls(int(float_value))
            
        return "value is not a float"
    
    
    @classmethod
    def from_roman(cls, value):
        roman_numerals = {"I" : 1,
                  "V" : 5,
                  "X" : 10,
                  "L" : 50,
                  "C" : 100,
                  "D" : 500,
                  "M" : 1000
                  }

        int_value = 0

        for i in range(len(value)):
            if value[i] in roman_numerals:
                    if i + 1 < len(value) and roman_numerals[value[i]] < roman_numerals[value[i + 1]]:
                        int_value -= roman_numerals[value[i]]
                    else:
                        int_value += roman_numerals[value[i]]

        return cls(int_value)
    
    @classmethod
    def from_string(cls, value):
        if str(value).isdigit():
            return cls(int(value))
        return "wrong type"
        

        
