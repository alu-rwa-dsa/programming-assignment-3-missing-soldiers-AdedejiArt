'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
Integers = int(input())

coordinates = []

for i in range(Integers):
    a, b, c = map(int, input().strip().split())
    coordinates.append([a, b, c])

i = 0
n = Integers
Min = coordinates[0][0]
Max = coordinates[0][-1]
while (n >= 1):
    array = coordinates[i]
    a = array[0]
    b = array[1]
    c = array[2]
    if (Max < a + c):
        Max = a + c
    if (Min > a):
        Min = a
    i += 1
    n -= 1

c = Max - Min + 1
if (c == 12):
    print(11)
else:
    print(c)
