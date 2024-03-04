

def question_5(string): #invert
    return string[::-1]

def question_5_v2(string):
    res_str = ''
    l = len(string) - 1
    for s in range(l, -1, -1):
        res_str += string[s]
    return res_str


print(question_5('meu nome é victor'))
print(question_5_v2('meu nome é victor'))