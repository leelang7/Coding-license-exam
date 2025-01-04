f = open('sample.txt', 'r')
lines = f.readlines()
f.close()

sum = 0
for line in lines:
    sum += int(line)

print(sum)
average = sum / len(lines)
print(len(lines))
print(average)

f = open('sample_1.txt', 'w')
f.write(str(average))
f.close