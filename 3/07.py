class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
    
    def __call__(self, x):
        result = 0
        power = 1
        for coeff in self.coefficients:
            result += coeff * power
            power *= x
        return result
    
    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = []
        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(coeff1 + coeff2)
        return Polynomial(new_coeffs)