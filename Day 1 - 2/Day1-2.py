file = open('input.txt', 'r')
readFile = file.readlines()
print(readFile)
total = 0


def getFirstNum():
    for i in range(len(line)):
        substr = line[i:]
        for num in digits:
            if substr.startswith(num):
                print("First:", digits[num])

                return digits[num]


def getLastNum():
    for i in range(len(line), -1, -1):
        substr = (line[i:])
        for num in digits:
            if substr.startswith(num):
                print("Last:", digits[num])
                return digits[num]


for i in readFile:
    digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
    }
    line = i.removesuffix("\n")
    print(line)
    first = 0
    last = 0

    print(line)
    first = getFirstNum()
    last = getLastNum()
    # for char in line:
    #     if str.isnumeric(char):
    #         first = char
    #         print("First:",first)
    #         break
    #
    # for char in reversed(line):
    #     if str.isnumeric(char):
    #         last = char
    #         print("Last:",last)
    #
    #         break

    lineSum = first + '' + last
    print(lineSum)
    total = total + int(lineSum)
print(total)
