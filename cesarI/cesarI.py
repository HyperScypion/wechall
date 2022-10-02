def cesar(string: str, key: int):
    list_of_strings = string.split(" ")
    for l in list_of_strings:
        for char in l:
            index = ord(char) - ord('A')
            print(chr(((index - key) % 26) + 65), end = '')
        print(end='\n')


if __name__ == "__main__":
    string = "JXU GKYSA RHEMD VEN ZKCFI ELUH JXU BQPO TEW EV SQUIQH QDT OEKH KDYGKU IEBKJYED YI DUHVQDDQCXWF"
    #  Solution NERFANNAMHGP
    cesar(string, -10)
