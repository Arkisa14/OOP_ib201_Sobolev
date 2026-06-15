class Temperature:
    @staticmethod
    def c_to_f(c):
        return round(c * 9 / 5 + 32, 2)
    
    @staticmethod
    def f_to_c(f):
        return round((f - 32) * 5 / 9, 2)