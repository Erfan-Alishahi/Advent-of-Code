def combine(string):
    # first find digit numbers and their index No's
    digit_nums = list()
    for index, digit in enumerate(string):
        if digit.isdigit():
            digit_nums.append((digit, index))
    # now find word numbers and their index No's
    str_numbers = {'one': 1, 'two': 2,\
               'three': 3, 'four': 4,\
               'five': 5, 'six': 6,\
               'seven' : 7, 'eight': 8,\
                'nine': 9}
    str_numbers_word = list(str_numbers.keys())
    for index, word_digit in enumerate(string):
        sub_word = str()
        for i in range(index, len(string)):
            sub_word += string[i]
            if sub_word in str_numbers_word:
                digit_nums.append((str(str_numbers[sub_word]), index))
    # now sort list of digits and return its combine
    digit_nums = sorted(digit_nums, key=lambda ind: ind[1])
    if len(digit_nums) == 1:
        return int(digit_nums[0][0] * 2)
    elif len(digit_nums) == 0: # i there is no number in string
        return 0
    else:
        return int(digit_nums[0][0] + digit_nums[-1][0])

with open(r'<.txt>') as file: # Enter text file path into .txt
    text = file.readlines()

Sum = 0
for line in text:
    Sum += combine(line)
print(Sum)