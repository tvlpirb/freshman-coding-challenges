# given a list which contains numbers, find the indices of the two numbers in
# the list which sum to the target
# https://leetcode.com/problems/two-sum
def twoSum(nums, target):
    index = 0
    nextIndice = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i,j]

# given a string, reverse it in place
# https://leetcode.com/problems/reverse-string
def reverseString(s):
    amount_pop = len(s)
    s.extend(s[::-1])
    for i in range(amount_pop):
        s.pop(0)


# Reverse a number given a signed integer, if reversing it causes it to be out
# of the range [-2^31,2^31-1] then return 0
# https://leetcode.com/problems/reverse-integer/
def reverseNumber(x):
    revNumber = 0
    temp = abs(x)
    while temp > 0:
        remainder = temp % 10
        revNumber = (revNumber * 10) + remainder
        temp = temp // 10
    if x < 0:
        revNumber = revNumber * -1
    if not((-2)**31 <= revNumber <= (2)**31-1):
        return 0
    return revNumber
