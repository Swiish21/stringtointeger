import re

# Lists for number words (order matters)
units = [
    "zero", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten", "eleven",
    "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen"
]

tens = [
    "", "", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
]

scales = {
    "hundred": 100,
    "thousand": 1000,
    "million": 1000000,
    "billion": 1000000000,
    "trillion": 1000000000000
}

# Build numwords dictionary to help the code understand strings
numwords = {word: idx for idx, word in enumerate(units)}
numwords.update({word: idx * 10 for idx, word in enumerate(tens) if word})
numwords.update(scales)

def text2int(textnum):
    """
    Convert a number written in English words to an integer.
    """
    textnum = textnum.lower().replace("-", " ")
    textnum = textnum.replace(" and ", " ")
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

# Test cases
print(text2int("one hundred twenty three"))  # 123
print(text2int("two thousand five hundred"))  # 2500
print(text2int("one million two hundred thirty four thousand five hundred sixty seven"))  # 1234567
print(text2int("one hundred and five"))  # 105
