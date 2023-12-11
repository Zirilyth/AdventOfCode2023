


file = open('input.txt', 'r')
readFile = file.readlines()
print(readFile)
total = 0
for i in readFile:
    print("Entered For\n")
    line = i.removesuffix("\n")
    print(line)
    first = ''
    last = ''
    for char in line:
        if str.isnumeric(char):
            first = char
            break

    for char in reversed(line):
        if str.isnumeric(char):
            last = char
            break

    lineTotal = first + '' + last
    total = total + int(lineTotal)
print(total)