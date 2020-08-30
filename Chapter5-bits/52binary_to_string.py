def binarytostring(num):
    if num<=0 or num>=1:
        return Exception("Error")
    binary = ''
    binary+='0.'
    while num>0:
        r = num*2
        if r>=1:
            binary+='1'
            num = r-1
        else:
            binary+='0'
            num = r
        if len(binary)>=34:
            return Exception("insufficient precision")
    return binary
num1 = 0.75
num2 = 0.625
num3 = 0.3
print(binarytostring(num1),binarytostring(num2),binarytostring(num3))
    