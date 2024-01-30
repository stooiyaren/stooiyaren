from statistics import median
idx = []
for i in range(5):
    idx.append(int(input()))
print(int(sum(idx)/len(idx)))
print(median(idx))