class Mathamatics:
    def __init__(self, m, n):
        self.m = m
        self.n = n
    def gcd(self):
        i = min(self.m,self.n)
        while i>0:
            if self.m%i == 0 and self.n%i == 0:
                return i
            else:
                i = i-1
gcd1=Mathamatics(20, 24)
print(gcd1.gcd())
