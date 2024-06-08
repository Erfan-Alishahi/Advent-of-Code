def combine(string):
    digit_list = list()
    for index, word in enumerate(string):
        if word.isdigit():
            digit_list.append((word, index))
    # sort list by index
    digit_list = sorted(digit_list, key=lambda ind: ind[1])
    # return int number
    if len(digit_list) == 1: # if there is just one digit in string
        return int(digit_list[0][0] * 2)
    elif len(digit_list) == 0: # if there is no digit in string
        return 0
    else: # if there are many digits in string
        return int(digit_list[0][0] + digit_list[-1][0])
    
# open text file 
with open(r'<.txt>') as file: # Enter text file path into <.txt>
    text = file.readlines()
# Combine line by line
Sum = 0
for string in text:
    Sum += combine(string)
print(Sum)
