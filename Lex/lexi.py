import os


def readRules(filename):
    if os.path.exists(filename):
        print('规则文件存在')
        # 定义一个rules表驱动
        rules = list()
        # 打开txt文件读取规则
        with open(filename) as f:
            index = 0
            spaces = list()
            for line in f.readlines():
                # 删除最后一个'\n'符号
                line = line[0:len(line) - 1]
                arr = line.split('\t')
                rules.append(arr)

                # 可以接受other(可以接受空格)的存放起来在spaces中
                if arr[-1] != '#' and arr[-1] != 'other':
                    spaces.append(index)
                index += 1
            # 弹出最后一个终态合集
            states = rules.pop()
            # 解析出所有的终态
            states = ''.join(states)
            states = states.split(' ')
            states = states[1].split(',')
            states = list(map(int, states))
            return rules, states, spaces
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

# 前面的数字代表对应的终态
dic = {2: '标志符',
       3: '无符号整数',
       4: '无符号整数',
       5: '分界符',
       6: '运算符',
       7: '运算符',
       9: '运算符',
       12: '注释符',
       13: '错误'}

# 根据目前状态和字符查找下一状态


def findNextState(nowState, ch):
    # 最后一个是other 单独处理
    for i in range(1, len(rules[0]) - 1):
        # 将str转成int
        if ch in [str(j) for j in range(10)]:
            ch = int(ch)
        if ch in sonsOfAlphas(rules[0][i]):
            if rules[nowState][i] != '#':
                # print('目前状态', end='')
                # print(nowState)
                # print('目前字符', end='')
                # print(ch)
                # print('跳转', end='')
                # print(rules[nowState][i])

                return int(rules[nowState][i])

            else:
                return False
    # 返回符合other的状态
    if rules[nowState][len(rules[0]) - 1] != '#':
        return int(rules[nowState][len(rules[0]) - 1])

    return False

# 分析字符串


def analyse(input_string):
    pos = 0
    now_state = 1
    str_acc = ''
    while pos < len(input_string):
        if (input_string[pos] == ' ' and now_state not in space_ac) or pos == len(input_string):
            if now_state in finalStates:
                print(tplt.format(nowLine, dic[now_state], str_acc, chr(12288)))
            else:
                print(tplt.format(nowLine, '失败', str_acc, chr(12288)))
            now_state = 1
            str_acc = ''
        else:
            next_state = findNextState(now_state, input_string[pos])
            # 能跳到合法状态
            if next_state:
                str_acc += input_string[pos]
                now_state = next_state
            else:
                # 上一个是终态
                if now_state in finalStates:
                    print(tplt.format(nowLine, dic[now_state], str_acc, chr(12288)))
                    pos -= 1
                elif now_state == 1:
                    str_acc += input_string[pos]
                    print(tplt.format(nowLine, '失败', str_acc, chr(12288)))
                else:
                    print(tplt.format(nowLine, '失败', str_acc, chr(12288)))
                    pos -= 1
                str_acc = ''
                now_state = 1
        pos += 1
    if now_state in finalStates:
        print(tplt.format(nowLine, dic[now_state], str_acc, chr(12288)))
    elif now_state != 1:
        print(tplt.format(nowLine, '失败', str_acc, chr(12288)))


if __name__ == '__main__':
    # 定义全局变量
    global rules
    global finalStates
    # 可以接受空格的状态记录下来
    global space_ac
    global nowLine
    rules, finalStates, space_ac = readRules('rules.txt')
    with open('test.txt') as f:
        nowLine = 0
        for line in f.readlines():
            nowLine += 1
            print('\n\n-------------------------------------------------')
            print('识别语句:' + line[0: -1])
            print('-------------------------------------------------')
            print(tplt.format('line ', '识别状态', 'content', chr(12288)))
            analyse(line[0: -1])
            print('-------------------------------------------------')
