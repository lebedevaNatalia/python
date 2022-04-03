src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

nums = set()
tmp = set()
for num in src:
    if num not in tmp:
        nums.add(num)
    else:
        nums.discard(num)
    tmp.add(num)

result = [num for num in src if num in nums]
print(result)