def Bbit(i):
    output = ''
    for j in range(3, -1, -1):
        output += '1' if i & (1 << j) else '0'
    return output

hexa = '1E06079861E79F99FE079861E79F8'
binary = ''

for i in range(len(hexa)):
    num = int(hexa[i], 16)
    binary += Bbit(num)

print(binary)
