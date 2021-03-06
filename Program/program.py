def readRules():
    with open('ll1.txt') as f:
        # 去掉最后的 '\n'
        ter_list = f.readline()[:-1].split('\t')
        dic = dict()
        for line in f.readlines():
            line_list = line[:-1].split('\t')
            line_dic = dict()
            for index, rule in enumerate(line_list):
                if rule != '' and index != 0:
                    line_dic[ter_list[index]] = rule
            dic[line_list[0]] = line_dic
        return dic, 'S'


def analysize(input_str):
    symbolStack = '#' + startSymbol
    pos = 0
    while pos < len(input_str):
        ch = input_str[pos]
        print('当前字符:' + ch)
        print('剩下字符' + input_str[pos:])
        if ch in rule[symbolStack[-1]]:
            res = rule[symbolStack[-1]][ch]
            print('识别的结果:' + res)
            if res == 'Q->dD' and input_str[pos+1] == 'n':
                res = 'Q->'
            symbolStack = symbolStack[:-1] + res[::-1][:-3]
            print('符号栈:' + symbolStack)
            while symbolStack[-1] == ch:
                symbolStack = symbolStack[:-1]
                # print('符号栈:' + symbolStack)
                pos += 1
                if pos >= len(input_str):
                    break
                ch = input_str[pos]
            if symbolStack != '' and symbolStack[-1] not in rule:
                # print(input_str[pos] + '终结符匹配失败')
                dealError(1, input_str[pos],pos, symbolStack[-1])
                break
        else:
            # print('非终结符里没有这个去处')
            dealError(2,input_str[pos],pos,symbolStack[-1],rest = input_str[pos:])
            break
    if symbolStack == '':
        print('识别成功')

# 类别分析
dic = {'NUM':'a','ID':'b','if':'c','else':'d','for':'e','while':'f','int':'g','write':'h','read':'i','(':'j',')':'k',';':'l','{':'m','}':'n',',':'o','+':'p','-':'q','*':'r','/':'s','=':'t','>':'u','<':'v','>=':'w','<=':'x','!=':'y','==':'z','注释':1,'#':'#'}
dic = dict(zip(dic.values(),dic.keys()))

def dealError(code,now,pos, need, rest = ''):
    if pos < len(map_line):
        count = 0
        while True:
            pos -= 1
            if map_line[pos] == map_line[pos+1]:
                # print(len(dic[now]))
                count += 1
            else:
                break
        print('出现语法错误的行号:' +str(map_line[pos] + 1) + '列数' + str(count+1))
    else:
        print('出现语法错误的行号:最后一行')
    if code == 1:
        print('Expected:    ' + dic[need] + '   Before:    ' + dic[now] )
    # elif code == 2:
    #     s = ''
    #     print(need + ' 产生式无法产生 ' + dic[now])
    #     print('剩余未识别' + rest)


def pro(input_str, m_list, line_map):
    global rule
    global startSymbol
    global map_list
    global map_line
    map_line = line_map
    map_list = m_list
    rule, startSymbol = readRules()
    analysize(input_str)


if __name__ == '__main__':
    global rule
    global startSymbol
    rule, startSymbol = readRules()
    analysize('i*i+i#')
