class Difference:
    diff=[]
#     maximumDifference=0
    def __init__(self, a):
        self.__elements = a
#         self.diff=[]
    def computeDifference(self):
        diff=[]
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                diff.append(a[i]-a[j])
        self.maximumDifference=max(diff)


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

