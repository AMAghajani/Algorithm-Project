from os import listdir, mkdir, path

malware_address = 'part1\\Released\\Released\\Train\\Malware Sample\\'
benign_address = 'part1\\Released\\Released\\Train\\Benign\\1 '

def Compute(characters):
    permutions = characters.copy()
    for i in range(5):
        perm = permutions.copy()
        for p in perm:
            for char in characters:
                new = str(p) + str(char)
                permutions.append(new)
            permutions.remove(p)
        for pp in permutions:
            if CheckBenign(pp):
                print(pp)
    return permutions

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

def CheckBenign(string):
    for i in range(1, 901):
        benign_file_path = benign_address + '(' + str(i) + ')'
        all_string = GetAllString(benign_file_path)
        if string in all_string:
            print(i)
    
def CheckMalware(malware_number, string, number_of_malwares):
    malware_folder_path = malware_address + str(malware_number) + '\\' + str(malware_number)
    count = 0
    n = number_of_malwares + 1
    for i in range(1, n):
        malware_file_path = malware_folder_path + ' (' + str(i) + ')'
        all_string = GetAllString(malware_file_path)
        if string in all_string:
            count += 1   
        else:
            print(i)     
    print(str(malware_number) + ': ' + string + ' ---> ' + str(count) + ' of ' + str(number_of_malwares))

def Check(malware_number, string, number_of_malwares):
    CheckBenign(string)
    print('==========')
    CheckMalware(malware_number, string, number_of_malwares)

def GetBestPattern(malware_number, patterns, number_of_malwares):
    malware_folder_path = malware_address + str(malware_number) + '\\'
    files = [file for file in listdir(malware_folder_path)]
    all_string_of_malware = [GetAllString(malware_folder_path + file) for file in files]
    max = 0
    n = len(patterns)
    j = 0
    best_pattern = ''
    while j < n:
        count = 0
        p = patterns[j]
        for i in range(number_of_malwares):
            all_string = all_string_of_malware[i]
            if p in all_string:
                count += 1
        if count > max:
            max = count
            best_pattern = p
            print('=========' + p + '=========')
            if max == number_of_malwares:
                break
        print(str(j) + ': ' + str(max) + '    ' + best_pattern)
        if j < 11000:
            j += 1
        else:
            j += 1
    print(str(malware_number) + ': ' + best_pattern + ' ---> ' + str(max) + ' of ' + str(number_of_malwares))
        
def GetAllPatterns(filename): 
    result = []
    with open(filename) as file:
        for i in range(221787):
            chunk = file.readline() 
            result.append(chunk.rstrip())
    return result



if __name__ == "__main__":

    #1: 015CD ---> 100.00 %
    #2: 139FE ---> 98.25 %
    #3: 01DAE ---> 100.00 %
    #4: 0ADB7 ---> 100.00 %
    #5: 1C61F ---> 100.00 %
    #6: FAFED ---> 66.25 %
    #7: FAFED ---> 66.14 %
    #8: FAFED ---> 65.75 %
    #9: D7FF2 ---> 82.13 %
    #10: C1FB2 ---> 53.63 %
    #11: 9E413 ---> 87.25 %
    #12: 026AB ---> 100.00 %
    #13: 1451A ---> 100.00 %
    #14: 019D6 ---> 100.00 %
    #15: 119D5 ---> 100.00 %
    #16: 01B5A ---> 100.00 %
    #17: 01DEC ---> 100.00 %
    #18: 55FA5 ---> 99.75 %
    #19: 011ED ---> 100.00 %
    #20: 012FD ---> 100.00 %
    # Check(8, 'FAFED', 400)
    patterns = GetAllPatterns('GeneratedPatterns.txt')
    #GetBestPattern('bottleneck', patterns, 2)

    GetBestPattern(1, patterns, 400)
    # GetBestPattern(2, patterns, 400)
    # GetBestPattern(3, patterns, 400)   
    # GetBestPattern(4, patterns, 400)
    # GetBestPattern(5, patterns, 322)
    # GetBestPattern(6, patterns, 400)
    # GetBestPattern(7, patterns, 319)
    # GetBestPattern(8, patterns, 400)
    # GetBestPattern(9, patterns, 319)
    # GetBestPattern(10, patterns, 358)
    # GetBestPattern(11, patterns, 400)
    # GetBestPattern(12, patterns, 193)
    # GetBestPattern(13, patterns, 400)
    # GetBestPattern(14, patterns, 25)
    # GetBestPattern(15, patterns, 70)
    # GetBestPattern(16, patterns, 400)
    # GetBestPattern(17, patterns, 400)
    # GetBestPattern(18, patterns, 400)
    # GetBestPattern(19, patterns, 400)
    # GetBestPattern(20, patterns, 400)
