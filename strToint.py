import re

numwords = {}

#dictionaries for the number words

units = {
    "zero", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten", "eleven",
    "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen"
}

tens = {
    "", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
}

scales = ["hundred", "thousand", "million", "billion", "trillion"]

for idx, word in enumerate(units):
    numwords[word] = idx
    
for idx, word in enumerate(tens):
    numwords[word] = idx * 10
    
numwords["hundred"] = 100
numwords["thousand"] = 1000
numwords["million"] = 1000000
numwords["billion"] = 1000000000
numwords["trillion"] = 1000000000000

def text2int(textnum):
    textnum = textnum.lower().replace("-", " ")
    current = result = 0
    
    for word in textnum.split():
        if word not in numwords:
            raise ValueError(f"Unknown number word: {word}")
        
        scale = numwords[word]
        
        if scale == 100:
            current *= scale
        elif scale >= 1000:
            current *= scale
            result += current
            current = 0
        else:
            current += scale
            
    return result + current

    
    
#test cases
print(text2int("one hundred twenty three"))  # 123
print(text2int("two thousand five hundred"))  # 2500
print(text2int("one million two hundred thirty four thousand five hundred sixty seven"))  # 1234567