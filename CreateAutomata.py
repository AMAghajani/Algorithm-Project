alphabets_size = 16
patterntern_size = 5
ConvertToInt = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15
}

def GetNextState(pattern, corrent_state, a):
    if corrent_state < patterntern_size and a == ConvertToInt[pattern[corrent_state]]:
        return corrent_state + 1 
    i=0
    for next_state in range(corrent_state, 0, -1):
        if ConvertToInt[pattern[next_state - 1]] == a:
            while(i < next_state - 1):
                if pattern[i] != pattern[corrent_state - next_state + 1 + i]:
                    break
                i += 1
            if i == next_state - 1:
                return next_state
    return 0
 
def ComputeTF(pattern):
    TF = [[0 for i in range(alphabets_size)] for j in range(patterntern_size + 1)]
    for state in range(patterntern_size + 1):
        for a in range(alphabets_size):
            TF[state][a] = GetNextState(pattern, state, a)
    return TF
 
