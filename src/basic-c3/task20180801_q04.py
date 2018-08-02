nums = range(1, 41)
s = list(filter(lambda x: x % 3 == 0 or x // 10 == 3, nums))
print(s)
