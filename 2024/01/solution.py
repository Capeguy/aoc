left = []
right = []
totalDist = 0

with open('input.txt', 'r') as f:
    for line in f:
        a, b = line.split('   ')
        left.append(a)
        right.append(b)

left.sort()
right.sort()

for i in range(len(left)):
    totalDist += abs(int(left[i]) - int(right[i]))

print(totalDist)
