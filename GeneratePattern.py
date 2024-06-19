malware_address = 'part1\\Released\\Released\\Train\\Malware Sample\\'
benign_address = 'part1\\Released\\Released\\Train\\Benign\\1 '

def Compute(characters, all_string_of_benign):
    permutions = characters.copy()
    with open('GeneratedPatterns.txt', 'w') as file:
        for i in range(2,6):
            perm = permutions.copy()
            for p in perm:
                for char in characters:
                    permutions.append(p + char)
                permutions.remove(p)
            print('=========' + str(i) + '=========')
            if i == 5: 
                for pp in permutions:
                    if CheckBenign(pp, all_string_of_benign):
                        file.write(pp)
                        file.write('\n')
                        print(pp)
    return permutions

def CheckBenign(string, all_string_of_benign):
    r = False
    for i in range(900):
        all_string = all_string_of_benign[i]
        if string in all_string:
            r = False
            break
        else:
            r = True
    return r

def GetAllString(filename):
    line = 32 
    result = ''
    with open(filename, mode="rb") as file:
        while True:
            chunk = file.read(line).hex()    
            if not chunk:
                break
            result += chunk
    return result.upper()



if __name__ == "__main__":
    print('=========Start=========')
    all_string_of_benign = [GetAllString(benign_address + '(' + str(i) + ')') for i in range(1, 901)]
    print(Compute(['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'], all_string_of_benign))