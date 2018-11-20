from Program.down import Pro


def _op(op, P1, P2):
    p1 = 0
    p2 = 0
    if P1 in p.temp_list:
        for i, t in enumerate(p.temp_list):
            if t.name == str(P1):
                p1 = t.value
    elif P1 in p.chart:
        p1 = p.chart[P1]
    else:
        p1 = int(P1)
    if P2 in p.temp_list:
        for i, t in enumerate(p.temp_list):
            if t.name == str(P2):
                p2 = t.value
    elif P2 in p.chart:
        p2 = p.chart[P2]
    else:
        p2 = int(P2)

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
    print(type(index))
    while index != len(p.seq_list):
        item = p.seq_list[int(index)]
        if item.action == '=':
            index += 1
            if item.p1 in p.temp_list:
                for i, t in enumerate(p.temp_list):
                    if t.name == str(item.p1):
                        p.chart[item.result] = p.temp_list[i].value
            else:
                p.chart[item.result] = item.p1
        elif item.action == 'j=' or item.action == 'j':
            index = item.result.value
        else:
            index += 1
            if item.result in p.chart:
                p.chart[item.result] = _op(item.action, item.p1, item.p2)
            elif item.result in p.temp_list:
                for i,t in enumerate(p.temp_list):
                    if t.name == str(item.result):
                        p.temp_list[i].value = _op(item.action, item.p1, item.p2)


    print('测试抽象机是否将值赋给了符号表与临时变量表')
    print(p.chart)
    print(p.temp_list)


if __name__ == '__main__':
    VM()