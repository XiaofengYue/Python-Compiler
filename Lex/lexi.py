import os


def readRules(filename):
    if os.path.exists(filename):
        print('规则文件存在')
        # 定义一个rules表驱动
        rules = list()
        # 打开txt文件读取规则
        with open(filename) as f:
            for line in f.readlines():
                # 删除最后一个'\n'符号
                line = line[0:len(line) - 1]
                arr = line.split('\t')
                rules.append(arr)

            # 弹出最后一个终态合集
            states = rules.pop()
            # 解析出所有的终态
            states = ''.join(states)
            states = states.split(' ')
            states = states[1].split(',')
            states = list(map(int, states))
            return rules, states
    else:
        print('请检查规则文件是否存在')
        return False


# 根据str获得子集
def sonsOfAlphas(str):
    if str == '[a-z]':
        return [chr(i) for i in range(ord('a'), ord('z') + 1)]
    elif str == '[A-Z]':
        return [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    elif str == '[1-9]':
        return [i for i in range(1, 10)]
    elif str == '0':
        return [0]
    elif str == 'other':
        return ['other']
    else:
        list_l = list()
        for i in str:
            list_l.append(i)
        return list_l


tplt = "{0:^10}|{1:{3}^10}|{2:{3}^10}"
# 前面的数字代表对应的终态 留给自己看的
# dic = {2: 'ID',3: 'NUM',4: 'NUM',5: '分界符',6: '运算符',7: '运算符',9: '运算符',12: '注释符'}
# 保留字
reserved = ['if', 'else', 'for', 'while', 'int', 'write', 'read']
# 类别分析
dic = {'NUM':'a','ID':'b','if':'b','else':'d','for':'e','while':'f','int':'g','write':'h','read':'i','(':'j',')':'k',';':'l','{':'m','}':'n',',':'o','+':'p','-':'q','*':'r','/':'s','=':'t','>':'u','<':'v','>=':'w','<=':'x','!=':'y','==':'z','注释':27}


def writeIn(str_acc, now_state):
    with open('lex.txt', 'a+') as f:
        if now_state == 2 and str_acc not in reserved:
            name = 'ID'
        elif now_state == 3 or now_state == 4:
            name = 'NUM'
        elif now_state == 12:
            name = '注释'
        else:
            name = str_acc
        f.write(str(dic[name]) + '\t' + str_acc + '\n')
# 根据目前状态和字符查找下一状态


def findNextState(nowState, ch):
    # 最后一个是other 单独处理
    for i in range(1, len(rules[0]) - 1):
        # 将str转成int
        if ch in [str(j) for j in range(10)]:
            ch = int(ch)
        if ch in sonsOfAlphas(rules[0][i]):
            if rules[nowState][i] != '#':
                return int(rules[nowState][i])
            else:
                return False
    # 如果表驱动other 对应的下一跳不是#（说明可以接受）
    if rules[nowState][len(rules[0]) - 1] != '#':
        # 返回nextState
        return int(rules[nowState][len(rules[0]) - 1])
    return False


def analyse(input_string):
    now_state = 1
    str_acc = ''
    index = 0
    while index < len(input_string):
        ch = input_string[index]
        next_state = findNextState(now_state, ch)
        if next_state:
            str_acc += ch
            now_state = next_state
        else:
            if now_state in finalStates:
                writeIn(str_acc, now_state)
            else:
                print(tplt.format(100, '失败', str_acc, chr(12288)))
            # 状态和接收字符串置为初始态和空
            now_state = 1
            str_acc = ''
            # 直到寻找下一个可被接收的字符跳出
            while True:
                next_state = findNextState(1, ch)
                if next_state:
                    now_state = next_state
                    str_acc = ch
                    break
                # 忽略空格和回车的报错（他们仅仅是为了格式）
                elif ch != ' ' and ord(ch) != 10:
                    print(tplt.format(100, '失败', ch, chr(12288)))
                index += 1
                if index >= len(input_string):
                    break
                ch = input_string[index]
        index += 1
    # 读完字符串后最后需要进行判断
    if now_state in finalStates:
        writeIn(str_acc, now_state)
    elif now_state != 1:
        print('here')
        print(tplt.format(100, '失败', str_acc, chr(12288)))


def lex(filename):
    # 定义全局变量
    global rules
    global finalStates
    rules, finalStates = readRules('rules.txt')
    with open(filename) as f:
        analyse(f.read())

if __name__ == '__main__':
    # 定义全局变量
    global rules
    global finalStates
    rules, finalStates = readRules('rules.txt')
    with open('test.txt') as f:
        analyse(f.read())
