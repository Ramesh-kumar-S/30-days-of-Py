# n=int(input())
# f=[]
# for i in range(1,n):
#     if n%i==0:
#         f.append(i)
# f.append(n)
# print(f)

# f=[i for i in range(1,n) if n%i==0 ]
# f.append(n)
# print(f)

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        f=[i for i in range(1,n) if n%i==0 ]
        f.append(n)
        return sum(f)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)