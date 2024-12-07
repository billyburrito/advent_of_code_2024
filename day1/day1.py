first = []
second = []
data = []
sum = 0
part2 = 0

with open('input') as fp:
    for line in fp:
        data = line.split()
        first.append(data[0])
        second.append(data[1])

first.sort()
second.sort()

for x in range(len(first)):
    if int(second[x]) > int(first[x]):
        sum += int(second[x]) - int(first[x])
    else:
        sum += int(first[x]) - int(second[x])

    # part 2
    part2 += int(first[x]) * second.count(first[x])


print("part one: "+str(sum))
print("part two: "+str(part2))