from Lex.lexi import lex
from Program.down import Pro
from VMachine.vm import VM

if __name__ == '__main__':
    map_line = lex('test.txt')
    input_str = ''
    map_list = list()
    with open('lex.txt') as f:
        for line in f.readlines():
            line = line[:-1].split('\t')
            if line[0].isalpha():
                input_str += line[0]
                map_list.append(line[1])
    # pro(input_str + '#', map_list, line_map)
    # p(input_str + '#', map_list, map_line)
    p = Pro()
    p.createSymbolList(input_str, map_list, map_line)
    p.analysis('ll1.txt')
    # 抽象机
    vm = VM(p.chart, p.temp_list, p.seq_list)