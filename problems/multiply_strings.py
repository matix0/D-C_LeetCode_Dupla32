class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def karatsuba(x,y):
            if x < 10 or y < 10:
                return x * y
            n = max(len(str(x)), len(str(y)))
            k = n // 2

            x1, x0 = divmod(x, 10 ** k)
            y1, y0 = divmod(y, 10 ** k)

            a = karatsuba(x1,y1)
            c = karatsuba(x0,y0)
            b = karatsuba(x0 + x1, y0 + y1) - a - c

            return (10 ** (2 * k) * a) + (10 ** k * b) + c 
        
        if not num1 or not num2:
            return "0"

        return str(karatsuba(int(num1), int(num2)))


