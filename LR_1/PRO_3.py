Armstr = []
for i in range(100, 10000):
    nums = [int(j) for j in str(i)]
    p = sum([ j ** (len(nums)) for j in nums])
    if i == p:
        Armstr.append(i)
print(Armstr)