import os


index, flag = 0, 0
in_str, ch = '', ''
lines = []
# 类别分析
dic_First = {'a': 'NUM', 'b': 'ID', 'c': 'if', 'd': 'else', 'e': 'for', 'f': 'while', 'g': 'int', 'h': 'write', 'i': 'read', 'j': '(', 'k': ')', 'l': ';', 'm': '{', 'n': '}', 'o': ',', 'p': '+', 'q': '-', 'r': '*', 's': '/', 't': '=', 'u': '>', 'v': '<', 'w': '>=', 'x': '<=', 'y': '!=', 'z': '==', 27: '注释'}
Follow_A = ['c', 'f', 'e', 'i', 'h', 'm', 'b', 'l', 'n']
Follow_C = ['n']
Follow_Q = ['c', 'f', 'e', 'i', 'h', 'm', 'b', 'l', 'n', 'd']
Follow_T = ['l', 'k', 'u', 'v', 'w', 'x', 'y', 'z']
Follow_U = ['p', 'q', 'l', 'k', 'u', 'v', 'w', 'x', 'y', 'z']
# First集
First = {'A': 'g,ε', 'B': 'g', 'C': 'c,f,e,i,h,m,b,l,ε', 'D': 'c,f,e,i,h,m,b,l', 'E': 'c', 'F': 'f', 'G': 'e', 'H': 'h', 'I': 'i', 'J': 'm', 'K': 'b', 'L': 'b', 'M': 'j,a,b', 'N': 'j,a,b', 'O': 'j,a,b', 'P': 'j,a,b', 'Q': 'd,ε', 'R': 'u,v,w,x,y,z', 'S': 'm', 'T': 'p,q,ε', 'U': 'r,s,ε'}


def err(index):
    # print(in_str.__len__())
    # print(index)
    if index == in_str.__len__():
        print("最后一行错误")
    else:
        print('错误行号：', lines[index])
    os._exit(0)


def out_range(index):
    if index == in_str.__len__():
        err(index)
    else:
        return


def S():
    global index, ch
    if ch == 'm':
        index += 1
        out_range(index)
        ch = in_str[index]
        A()
        C()
        if ch == 'n':
            print("识别成功")
        else:
            err(index)
    else:
        err(index)


def A():
    if ch == 'g':
        B()
        A()
    elif ch in Follow_A:
        return
    else:
        err(index)


def B():
    global ch, index
    if ch == 'g':
        index += 1
        out_range(index)
        ch = in_str[index]
        if ch == 'b':
            index += 1
            out_range(index)
            ch = in_str[index]
            if ch == 'l':
                index += 1
                out_range(index)
                ch = in_str[index]
            else:
                err(index)
        else:
            err(index)
    else:
        err(index)


def C():
    if ch in First['D']:
        D()
        C()
    elif ch in Follow_C:
        return
    else:
        err(index)


def D():
    global ch, index
    if ch in First['E']:
        E()
    elif ch in First['F']:
        F()
    elif ch in First['G']:
        G()
    elif ch in First['H']:
        H()
    elif ch in First['I']:
        I()
    elif ch in First['J']:
        J()
    elif ch in First['L']:
        L()
    elif ch == 'l':
        index += 1
        out_range(index)
        ch = in_str[index]
    else:
        err(index)


def E():
    global ch, index
    if ch == 'c':
        index += 1
        out_range(index)
        ch = in_str[index]
        if ch == 'j':
            index += 1
            out_range(index)
            ch = in_str[index]
            M()
            if ch == 'k':
                index += 1
                out_range(index)
                ch = in_str[index]
                D()
                Q()
            else:
                err(index)
        else:
            err(index)
    else:
        err(index)


def Q():
    global ch, index
    if ch == 'd':
        index += 1
        out_range(index)
        ch = in_str[index]
        D()
    elif ch in Follow_Q:
        return
    else:
        err(index)


def F():
    global ch, index
    if ch == 'f':
        index += 1
        out_range(index)
        ch = in_str[index]
        if ch == 'j':
            index += 1
            out_range(index)
            ch = in_str[index]
            M()
            if ch == 'k':
                index += 1
                out_range(index)
                ch = in_str[index]
                D()
            else:
                err(index)
        else:
            err(index)
    else:
        err(index)


def G():
    global ch, index
    if ch == 'e':
        index += 1
        out_range(index)
        ch = in_str[index]
        if ch == 'j':
            index += 1
            out_range(index)
            ch = in_str[index]
            K()
            if ch == 'l':
                index += 1
                out_range(index)
                ch = in_str[index]
                M()
                if ch == 'l':
                    index += 1
                    out_range(index)
                    ch = in_str[index]
                    K()
                    if ch == 'k':
                        index += 1
                        out_range(index)
                        ch = in_str[index]
                        D()
                    else:
                        err(index)
                else:
                    err(index)
            else:
                err(index)
        else:
            err(index)
    else:
        err(index)


def H():
    global ch, index
    if ch == 'h':
        index += 1
        out_range(index)
        ch = in_str[index]
        N()
        if ch == 'l':
            index += 1
            out_range(index)
            ch = in_str[index]
        else:
            err(index)
    else:
        err(index)


def I():
    global ch, index
    if ch == 'i':
        index += 1
        out_range(index)
        ch = in_str[index]
        if ch == 'b':
            index += 1
            out_range(index)
            ch = in_str[index]
            if ch == 'l':
                index += 1
                out_range(index)
                ch = in_str[index]
            else:
                err(index)
        else:
            err(index)
    else:
        err(index)


def J():
    global ch, index
    if ch == 'm':
        index += 1
        out_range(index)
        ch = in_str[index]
        C()
        if ch == 'n':
            index += 1
            out_range(index)
            ch = in_str[index]
        else:
            err(index)
    else:
        err(index)


def K():
    global ch, index
    if ch == 'b':
        index += 1
        out_range(index)
        ch = in_str[index]
        if ch == 't':
            index += 1
            out_range(index)
            ch = in_str[index]
            N()
        else:
            err(index)
    else:
        err(index)


def L():
    global ch, index
    if ch in First['K']:
        K()
        if ch == 'l':
            index += 1
            out_range(index)
            ch = in_str[index]
        else:
            err(index)
    else:
        err(index)


def M():
    if ch in First['N']:
        N()
        R()
    else:
        err(index)


def R():
    global ch, index
    if ch in First['R']:
        index += 1
        out_range(index)
        ch = in_str[index]
        N()
    else:
        err(index)


def N():
    if ch in First['O']:
        O()
        T()
    else:
        err(index)


def T():
    global ch, index
    if ch == 'p' or ch == 'q':
        index += 1
        out_range(index)
        ch = in_str[index]
        O()
        T()
    elif ch in Follow_T:
        return
    else:
        err(index)


def O():
    if ch in First['P']:
        P()
        U()
    else:
        err(index)


def U():
    global ch, index
    if ch == 'r' or ch == 's':
        index += 1
        out_range(index)
        ch = in_str[index]
        P()
    elif ch in Follow_U:
        return
    else:
        err(index)


def P():
    global ch, index
    if ch == 'j':
        index += 1
        out_range(index)
        ch = in_str[index]
        N()
        if ch == 'k':
            index += 1
            out_range(index)
            ch = in_str[index]
        else:
            err(index)
    elif ch == 'a':
        index += 1
        out_range(index)
        ch = in_str[index]
    elif ch == 'b':
        index += 1
        out_range(index)
        ch = in_str[index]
    else:
        err(index)


def recur(input_str, line_map):
    global ch
    global in_str, lines
    in_str = input_str
    ch = in_str[index]
    lines = line_map
    S()



# if __name__ == '__main__':
#     print('Recursive Decline')