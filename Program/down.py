class NewT():
    def __init__(self,value):
        global newT_num
        self.value = value
        self.name = 'T' + str(newT_num)
        newT_num += 1
    def __str__(self):
        return self.name
    def __repr__(self):
        return '\nname:{:10}value:{:5}'.format(self.name,self.value)
    def isdigit(self):
        return False

class label():
    def __init__(self, value=None):
        self.value = value

class Sequence():
    def __init__(self,action,p1= '_',p2 = '_',result='_'):
        self.action = action
        self.p1 = p1
        self.p2 = p2
        self.result = result
    def __str__(self):
        return '\n{:5}{:10}{:10}{:10}'.format(str(self.action),str(self.p1),str(self.p2),str(self.result))
    def __repr__(self):
        # return '\n:  ' +str(self.action) +  '  p1:  ' + str(self.p1) + '  p2  ' + str(self.p2) + '    ' + str(self.result)
        return '\n{:5}{:10}{:10}{:10}'.format(str(self.action),str(self.p1),str(self.p2),str(self.result))


class element():
    def __init__(self, symbol, value, line, type=None):
        self.symbol = symbol
        self.value = value
        self.line = line
        dic = {'NUM':'a','ID':'b','if':'c','else':'d','for':'e','while':'f','int':'g','write':'h','read':'i','(':'j',')':'k',';':'l','{':'m','}':'n',',':'o','+':'p','-':'q','*':'r','/':'s','=':'t','>':'u','<':'v','>=':'w','<=':'x','!=':'y','==':'z','注释':1,'#':'#'}
        dic = dict(zip(dic.values(),dic.keys()))
        self.type = dic[symbol]
    def __str__(self):
        return '\n符号:' + self.symbol + '\t值:' + self.value + '\t行数:' + str(self.line) + '\t类型:' + self.type
    def __repr__(self):
        return '\n符号:' + self.symbol + '\t值:' + self.value + '\t行数:' + str(self.line) + '\t类型:' + self.type

class MyException(Exception):
    def __init__(self,line,need,now):
        err = 'Line {} is not legal Expected {} Before {}'.format(line,now,need)
        Exception.__init__(self,err)
        self.line = line
        self.need = need
        self.now = now

class Pro():
    def __readRules(self,filename):
        with open(filename) as f:
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
            return dic

    def createSymbolList(self, input_str, map_list, map_line):
        # 词法分析给出的所有元素
        self.list = []
        for i,ch in enumerate(input_str):
            self.list.append(element(ch,map_list[i],map_line[i]))
        print(self.list)
        # 符号表
        self.chart = dict()
        self.seq_list = list()
        self.seq_num = 0
        global newT_num
        newT_num = 0
        self.temp_list = list()

    def analysis(self, filename):
        # 读取规则获得rule表
        self.rule = self.__readRules(filename)
        self.ch = self.list.pop(0)
        self._S()

    def FIRST(self,symbol,ch):
        if ch in self.rule[symbol]:
            return True
        return False

    def FOLLOW(self,symbol,ch):
        if ch in self.rule[symbol] and self.rule[symbol][ch].split('->')[1] == '':
            return True
        return False

    def getNextch(self):
        self.ch = self.list.pop(0)

    def _op(self,op,p1,p2):
        if op == '+':
            return p1 + p2
        elif op == '-':
            return p1 - p2
        elif op == '*':
            return p1 * p2
        elif op == '/':
            return p1 // p2

    def __VALUE(self,op,p1,p2):
        p1_t = 0
        p2_t = 0
        t0 = 0
        if isinstance(p1,NewT):
            p1_t = p1.value
        elif p1.isdigit():
            p1_t = p1
        else:
            p1_t = self.chart[p1]
        if isinstance(p2,NewT):
            p2_t = p2.value
        elif p2.isdigit():
            p2_t = p2
        else:
            p2_t = self.chart[p2]
        if p1.isdigit() and p2.isdigit():
            t0 = self._op(op,p1_t,p2_t)
        else:
            t0 = NewT(self._op(op,p1_t,p2_t))
        self.seq_list.append(Sequence(action=op,p1=p1,p2=p2,result=t0))
        self.seq_num += 1
        self.temp_list.append(t0)
        return t0

    def _err(self, line= None, need = None, now = None):
        raise (MyException(line,need,now))

    def _S(self):
        if self.ch.symbol == 'm':
            self.getNextch()
            self._A()
            self._C()
            if self.ch.symbol == 'n':
                print('识别成功')
                print('符号表\n' + str(self.chart))
                print('序列表: 数量是='+str(self.seq_num))
                print('临时变量表')
                print(self.temp_list)
                print(self.seq_list)
            else:
                self._err()
        else:
            self._err()

    def _A(self):
        # First
        if self.FIRST('B',self.ch.symbol):
            self._B()
            self._A()
        elif self.FOLLOW('A',self.ch.symbol):
            return
        else:
            self._err()

    def _B(self):
        if self.ch.symbol == 'g':
            self.getNextch()
            if self.ch.symbol == 'b':
                # 获得名字添加符号表
                name = self.ch.value
                self.getNextch()
                if self.ch.symbol == 'l':
                    self.chart[name] = 0
                    self.getNextch()
                else:
                    self._err()
            else:
                self._err()
        else:
            self._err()

    def _C(self):
        if self.FIRST('D',self.ch.symbol):
            self._D()
            self._C()
        elif self.FOLLOW('C',self.ch.symbol):
            return
        else:
            self._err()

    def _D(self):
        if self.FIRST('E',self.ch.symbol):
            self._E()
        elif self.FIRST('F',self.ch.symbol):
            self._F()
        elif self.FIRST('G',self.ch.symbol):
            self._G()
        elif self.FIRST('I',self.ch.symbol):
            self._I()
        elif self.FIRST('H',self.ch.symbol):
            self._H()
        elif self.FIRST('J',self.ch.symbol):
            self._J()
        elif self.FIRST('L',self.ch.symbol):
            self._L()
        elif self.ch.symbol == 'l':
            self.getNextch()
        else:
            self._err()

    def _E(self):
        if self.ch.symbol == 'c':
            self.getNextch()
            if self.ch.symbol == 'j':
                self.getNextch()
                self._M()
                if self.ch.symbol == 'k':
                    self.getNextch()
                    self._D()
                    self._Q()
                else:
                    self._err
            else:
                self._err()
        else:
            self._err()

    def _Q(self):
        if self.ch.symbol == 'd':
            self.getNextch()
            self._D()
        elif self.FOLLOW('Q',self.ch.symbol):
            return
        else:
            self._err()

    def _F(self):
        if self.ch.symbol == 'f':
            self.getNextch()
            if self.ch.symbol == 'j':
                self.getNextch()
                self._M()
                if self.ch.symbol == 'k':
                    self.getNextch()
                    self._D()
                else:
                    self._err()
            else:
                self._err()
        else:
            self._err()

    def _G(self):
        if self.ch.symbol == 'e':
            self.getNextch()
            if self.ch.symbol == 'j':
                self.getNextch()
                self._K()
                if self.ch.symbol == 'l':
                    self.getNextch()
                    self._M()
                    if self.ch.symbol == 'l':
                        self.getNextch()
                        self._K()
                        if self.ch.symbol == 'k':
                            self._D()
                        else:
                            self._err()
                    else:
                        self._err()
                else:
                    self._err()
            else:
                self._err()
        else:
            self._err()

    def _H(self):
        if self.ch.symbol == 'h':
            self.getNextch()
            self._N()
            if self.ch.symbol == 'l':
                self.getNextch()
            else:
                self._err()
        else:
            self._err()

    def _I(self):
        if self.ch.symbol == 'i':
            self.getNextch()
            if self.ch.symbol == 'b':
                self.getNextch()
                if self.ch.symbol == 'l':
                    self.getNextch()
                else:
                    self._err()
            else:
                self._err()
        else:
            self._err()

    def _J(self):
        if self.ch.symbol == 'm':
            self.getNextch()
            self._C()
            if self.ch.symbol == 'n':
                self.getNextch()
            else:
                self._err()
        else:
            self._err()

    def _K(self):
        if self.ch.symbol == 'b':
            name = self.ch.value
            self.getNextch()
            if self.ch.symbol == 't':
                self.getNextch()
                value = self._N()
                if name in self.chart:
                    self.chart[name] = value
                    self.seq_list.append(Sequence(action='=',p1=value,result=name))
                    self.seq_num += 1
                else:
                    self._err()
            else:
                self._err()
        else:
            self._err()

    def _L(self):
        if self.FIRST('K',self.ch.symbol):
            self._K()
            if self.ch.symbol == 'l':
                self.getNextch()
            else:
                self._err()
        else:
            self._err()

    def _M(self):
        if self.FIRST('N',self.ch.symbol):
            self._N()
            self._R()
        else:
            self._err()

    def _R(self):
        if self.ch.symbol == 'u':
            self.getNextch()
            self._N()
        elif self.ch.symbol == 'v':
            self.getNextch()
            self._N()
        elif self.ch.symbol == 'w':
            self.getNextch()
            self._N()
        elif self.ch.symbol == 'x':
            self.getNextch()
            self._N()
        elif self.ch.symbol == 'z':
            self.getNextch()
            self._N()
        elif self.ch.symbol == 'y':
            self.getNextch()
            self._N()
        else:
            self._err()

    def _N(self):
        if self.FIRST('O',self.ch.symbol):
            p = self._O()
            t = self._T(p)
            print('N返回了一个\t' + str(t) )
            return t
        else:
            self._err()

    def _T(self,p):
        if self.ch.symbol == 'p':
            self.getNextch()
            r = self._O()
            t0 = self.__VALUE('+',p,r)
            # t0 = p + r
            # print ('加法操作' + str(p) + '+' + str(r) +  '=' + str(t0))
            # self.seq_list.append(Sequence(action='+',p1=p,p2=r,result=t0))
            # self.seq_num += 1
            t = self._T(t0)
            return t
        elif self.ch.symbol == 'q':
            self.getNextch()
            r = self._O()
            t0 = self.__VALUE('-',p,r)
            # t0 = p - r
            # print ('减法操作' + str(p) + '-' + str(r) +  '=' + str(t0))
            # self.seq_list.append(Sequence(action='-',p1=p,p2=r,result=t0))
            # self.seq_num += 1
            t = self._T(t0)
            return t
        elif self.FOLLOW('T',self.ch.symbol):
            t = p
            return t
        else:
            self._err()

    def _O(self):
        if self.FIRST('P',self.ch.symbol):
            p = self._P()
            t = self._U(p)
            return t
        else:
            self._err()

    def _U(self,p):
        if self.ch.symbol == 'r':
            self.getNextch()
            r = self._P()
            t0 = self.__VALUE('*',p,r)
            # t0 = p * r
            # print ('乘法操作' + str(p) + '*' + str(r) +  '=' + str(t0))
            # self.seq_list.append(Sequence(action='*',p1=p,p2=r,result=t0))
            # self.seq_num += 1
            t = self._U(t0)
            return t
        elif self.ch.symbol == 's':
            self.getNextch()
            r = self._P()
            t0 = self.__VALUE('/',p,r)
            # t0 = p//r
            # print ('除法操作' + str(p) + '/' + str(r) +  '=' + str(t0))
            # self.seq_list.append(Sequence(action='/',p1=p,p2=r,result=t0))
            # self.seq_num += 1
            t = self._U(t0)
            return t
        elif self.FOLLOW('U',self.ch.symbol):
            t = p
            return t
        else:
            self._err()

    def _P(self):
        if self.ch.symbol == 'j':
            self.getNextch()
            t = self._N()
            p = t
            if self.ch.symbol == 'k':
                self.getNextch()
                return p
            else:
                self._err()
        elif self.ch.symbol == 'a':
            p = int(self.ch.value)
            self.getNextch()
            return p
        elif self.ch.symbol == 'b':
            p = self.ch.value
            self.getNextch()
            return p
        else:
            self._err()






