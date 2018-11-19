
class symbolChart():
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def __str__(self):
        return '变量名:' + self.name + '    值:' + str(self.value)

    def __repr__(self):
        return '变量名:' + self.name + '    值:' + str(self.value)


class MyList():
    def __init__(self):
        e1 = element('S', 'S')
        e2 = element('#', '#')
        self.list = [e1, e2]
        self.stack_B = []
        self.chart = []

    def out(self, ch):
        e = self.list[0]
        self.list.pop(0)
        if e.final:
            # 真正结束
            if e.symbol == e.ele:
                print(e.symbol + '这个产生式结束了')
                if e.symbol == 'B':
                    # 加入符号表
                    print('\t定义了一个变量\t' + self.stack_B[0])
                    c = symbolChart(self.stack_B[0])
                    self.chart.append(c)
                    self.stack_B.pop(0)
            else:
                print('遇见这个也相当于是最后一个啦' + ch)
                self.out(self.list[0].ele)
        else:
            if e.symbol == 'B' and e.ele == 'b':
                self.stack_B.append(ch)

    def addRes(self, res):
        print(res)
        self.symbol = res[0]
        self.list.pop(0)
        pos = -1 * len(self.list)
        for index, ele in enumerate(res.split('->')[1]):
            ele = element(ele, self.symbol)
            if index == len(res.split('->')[1]) - 1:
                ele.final = True
            self.list.insert(pos, ele)
        self.list.insert(pos, element(self.symbol, self.symbol, True))
        if res.split('->')[1] == '':
            self.out(res[0])

    def __str__(self):
        return '符号栈:' + str(self.list)

    def __repr__(self):
        return '符号栈:' + str(self.list)

    def __getattr__(self, attr):
        if attr == 'first':
            return self.list[0]

    def __len__(self):
        return len(self.list)


class element():
    def __init__(self, ele, symbol, final=False):
        self.ele = ele
        self.symbol = symbol
        self.final = final

    def __str__(self):
        return self.ele + self.symbol + str(self.final)

    def __repr__(self):
        return self.ele
