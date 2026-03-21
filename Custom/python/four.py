# frequency character check by dictionary

def char_freq(str):
    freq={}
    for ch in str:
        freq[ch]=freq.get(ch, 0)+1
    return freq

print(char_freq("banana"))