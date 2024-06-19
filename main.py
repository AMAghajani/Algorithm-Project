from CreateAutomata import ComputeTF, ConvertToInt
from FindPattern import GetAllString
from os import listdir, mkdir, path
from shutil import move
#'C8A2B' 35 '1A9FE' 22 '0D8F7' 21 '14B59' 16 '1AAFE' 12 '08C92' 10 '18FD3' 8 'BA673' 9 '21588' 5 '17F82' 4 '1C5B2' 3 '5F6D1' 2
patterns = [
    '015CD',
    '139FE',
    '01DAE',
    '0ADB7',
    '1C61F',
    'FAFED',
    'D7FF2',
    'C1FB2',
    '9E413',
    '026AB',
    '1451A',
    '019D6',
    '119D5',
    '01B5A',
    '01DEC',
    '55FA5',
    '011ED',
    '012FD'
]

def Search(folder_name, TFs):
    files = [file for file in listdir(folder_name)]
    malware_folder = 'Malware'
    if not path.exists(malware_folder):
        mkdir(malware_folder)
    count = 0
    for file in files:
        all_string = GetAllString(folder_name + '\\' + file)
        n = len(all_string)
        state = 0
        flag = False
        for TF in TFs:
            for i in range(n):
                state = TF[state][ConvertToInt[all_string[i]]]
                if state == 5:
                    move(folder_name + '\\' + file, malware_folder + '\\' + file)
                    count += 1
                    flag = True
                    break
            if flag:
                break
    print(str(count) + ' detected malware files were transferred from ' + folder_name + ' to Malware folder.')
 
 
if __name__ == '__main__':
    TFs = [ComputeTF(pattern) for pattern in patterns]
    folder_name = input('Please enter folder name: ')
    Search(folder_name, TFs)
 