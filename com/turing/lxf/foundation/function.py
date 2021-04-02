
def transchar(para_str):
    if type(para_str) == str:
        str_1 = para_str.replace('a', 'h')
        str_2 = str_1.replace('b', 'i')
        return str_2
    else:
        return False

print(type('str'))