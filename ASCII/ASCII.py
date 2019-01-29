numbers = [84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 98, 97, 97, 98, 105, 97, 101, 100, 104, 110, 99, 103]

string = ""
second_list = []
for number in numbers:
    second_list.append(chr(number))

print(string.join(second_list))
