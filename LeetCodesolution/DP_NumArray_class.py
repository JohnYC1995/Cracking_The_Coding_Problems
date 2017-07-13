class NumArray(object):
    def __init__(self, nums):
        self.library = [0]
        for item in nums:
            self.library += [self.library[-1] + item]

    def sumRange(self, i, j):
        return self.library[j+1]-self.library[i]

if __name__ == '__main__':
    test = NumArray([1,2,3,4])
    print(test.sumRange(1,2))
