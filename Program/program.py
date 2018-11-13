def readRules():
    with open('ll1.txt') as f:
        ter_list = f.readline()[:-1].split('\t')
        dic = dict()
        for line in f.readlines():
            line_list = line[:-1].split('\t')
            line_dic = dict()
            for index, rule in enumerate(line_list):
                if rule != '' and index != 0:
                    line_dic[ter_list[index]] = rule
            dic[line_list[0]] = line_dic
        return dic, 'E'


def analysize(input_str):
    symbolStack = '#' + startSymbol
    pos = 0
    while pos < len(input_str):
        ch = input_str[pos]
        print('当前字符:' + ch)
        res = rule[symbolStack[-1]][ch]
        print('识别的结果:' + res)
        if res:
            symbolStack = symbolStack[:-1] + res[::-1][:-2]
            print('符号栈:' + symbolStack)
            if symbolStack[-1] == ch:
                pos += 1
                symbolStack = symbolStack[:-1]
                print('符号栈:' + symbolStack)
        else:
            print('error')
    if startSymbol == '':
        print('成功')
    else:
        print('error')


def pro():
    global rule
    global startSymbol
    rule, startSymbol = readRules()
    analysize('i*i+i#')


if __name__ == '__main__':
    global rule
    global startSymbol
    rule, startSymbol = readRules()
    analysize('i*i+i#')
