class Password:
    @staticmethod
    def is_strong(p):
        if len(p) < 8:
            return False
        has_digit = any(c.isdigit() for c in p)
        has_upper = any(c.isupper() for c in p)
        has_lower = any(c.islower() for c in p)
        return has_digit and has_upper and has_lower
