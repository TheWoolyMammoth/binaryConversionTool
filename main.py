'''
conversionTool.py
purpose:
convert the following:
- binary to decimal number(positive only) <- primary
- decimal to binary number (binary only) <- primary
- binary to hexadecimal number - optional
- hexadecimal to binary number - optional
- decimal to hexadecimal - optional
- hexadecimal to decimal - optional
'''

def binaryToDecimal(binaryNum):
    power = len(binaryNum)
    decimalNum = 0
    for bit in binaryNum:
        power -= 1
        if bit == '1':
            decimalNum += (2 ** power)
    return decimalNum

def decimalToBinary(decimalNum):
    binaryArray = []
    remainder = decimalNum
    while True:
        if remainder > 0:
            if remainder % 2 == 0:
                binaryArray.insert(0, '0')
            elif remainder % 2 == 1:
                binaryArray.insert(0, '1')
        else:
            break
        remainder = remainder // 2
        # print(remainder)
    binaryString = ''.join(binaryArray)
    # print(binaryString)
    return binaryString

def twosCompliment():
    # used for converting a negative decimal number to binary
    # not sure I will use but keeping here just in case
    return None
# Optional side bits

def binaryToHex(decimalNum):
    # split into nibbles (1-4 bits), calculate the decimal and then convert to its hex form

    return None

def hexToBinary():
    return None

def decimalToHex():
    return None

def hexToDecimal():
    return None


test1 = ('1101',13)
test2 = ('1111',15)
test3 = ('10101',21)
test4 = ('110010101010001',25937)
tests = [test1,test2,test3,test4]

for test in tests:
    if binaryToDecimal(test[0]) == test[1]:
        print('pass')
    else:
        print('fail')

for test in tests:
    if decimalToBinary(test[1]) == test[0]:
        print('pass')
    else:
        print('fail')
