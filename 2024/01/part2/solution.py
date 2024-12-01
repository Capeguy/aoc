left = []
right = []
similarity = 0
occurrenceCache = {}

with open('input.txt', 'r') as f:
    for line in f:
        a, b = line.split('   ')
        left.append(int(a))
        right.append(int(b))

def getOccurrenceCount(list, number):
    if number in occurrenceCache:
        return occurrenceCache[number]
    count = 0
    for i in list:
        if i == number:
            count += 1
    occurrenceCache[number] = count
    return count

for i in range(len(left)):
    similarity += getOccurrenceCount(right, left[i]) * left[i]

print(similarity)
