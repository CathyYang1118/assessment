def Read (txtname):
    PCode = []
    PDes = []
    PRet = []
    File = open(txtname,'r')
    num = 0
    for i in range(0,27):
        j = File.readline()
        if i % 3 == 0:
            PCode.append(j[:-1])
        elif i % 3 == 1:
            PDes.append(j[:-1])
        else:
            PRet.append(float(j[:-1]))
    print('PCode:',PCode,'PDes:',PDes,'PRet:',PRet)
    File.close()
    return PCode

def Pro(PCode,Code):
    Result = -1
    i = 0
    while Result == -1:
        if PCode[i] == Code:
            Result = i+1
            return Result
        elif i == len(PCode)-1:
            return Result
        else:
            i += 1

print(Pro(Read('2.txt'),'0005'))
