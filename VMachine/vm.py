from Program.down import Pro


def find_value(name):
    value = 0
    if name in p.temp_list:
        for i, t in enumerate(p.temp_list):
            if t.name == str(name):
                value = t.value
    elif name in p.chart:
        value = p.chart[name]
    else:
        value = int(name)
    return value


def _op(op, P1, P2):
    p1 = find_value(P1)
    p2 = find_value(P2)

    if op == '+':
        return p1 + p2
    elif op == '-':
        return p1 - p2
    elif op == '*':
        return p1 * p2
    elif op == '/':
        return p1 // p2
    elif op == '>':
        if p1 > p2:
            return 1
        return 0
    elif op == '<':
        if p1 < p2:
            return 1
        return 0
    elif op == '==':
        if p1 == p2:
            return 1
        return 0
    elif op == '>=':
        if p1 >= p2:
            return 1
        return 0
    elif op == '<=':
        if p1 <= p2:
            return 1
        return 0
    elif op == '!=':
        if p1 != p2:
            return 1
        return 0


def VM(chart,newT,sequence):
    global p
    p = Pro()
    p.chart = chart
    p.temp_list = newT
    p.seq_list = sequence
    # 测试使用，将符号表与临时变量表的value置为0
    for i in p.chart.keys():
        p.chart[i] = 0
    for i in range(p.temp_list.__len__()):
        p.temp_list[i].value = 0

    print('-------------------------------------')
    index = 0
    while index < len(p.seq_list):
        item = p.seq_list[int(index)]
        if item.action == '=':
            index += 1
            if item.p1 in p.temp_list:
                for i, t in enumerate(p.temp_list):
                    if t.name == str(item.p1):
                        p.chart[item.result] = p.temp_list[i].value
            else:
                p.chart[item.result] = item.p1
        elif item.action == 'j=':
            flag = find_value(item.p2)
            if flag == item.p1:
                index = item.result.value
            else:
                index += 1
        elif item.action == 'j':
            index = item.result.value
        else:
            index += 1
            if item.result in p.chart:
                p.chart[item.result] = _op(item.action, item.p1, item.p2)
            elif item.result in p.temp_list:
                for i,t in enumerate(p.temp_list):
                    if t.name == str(item.result):
                        p.temp_list[i].value = _op(item.action, item.p1, item.p2)

    print('将抽象机结果赋给了符号表与临时变量表')
    print(p.chart)
    print(p.temp_list)


if __name__ == '__main__':
    VM()