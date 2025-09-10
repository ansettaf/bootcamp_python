import math

class TinyStatistician:
    def mean(self, x):
        if not x:
            return None
        s = 0.0
        n = 0
        for v in x:
            s += v
            n += 1
        return s / n

    def median(self, x):
        if not x:
            return None
        s = sorted(x)
        n = len(s)
        mid = n // 2
        if n % 2 == 1:
            return float(s[mid])
        else:
            return (s[mid-1] + s[mid]) / 2.0

    def quartiles(self, x):
        if not x:
            return None
        s = sorted(x)
        n = len(s)
        def median_of_list(lst):
            m = len(lst)
            if m == 0:
                return None
            mid = m // 2
            if m % 2 == 1:
                return float(lst[mid])
            else:
                return (lst[mid-1] + lst[mid]) / 2.0
        if n % 2 == 0:
            lower = s[:n//2]
            upper = s[n//2:]
        else:
            lower = s[:n//2]
            upper = s[n//2+1:]
        return [median_of_list(lower), median_of_list(upper)]

    def var(self, x):
        if not x:
            return None
        mu = self.mean(x)
        s = 0.0
        n = 0
        for v in x:
            s += (v - mu) ** 2
            n += 1
        return s / n

    def std(self, x):
        v = self.var(x)
        if v is None:
            return None
        return math.sqrt(v)
