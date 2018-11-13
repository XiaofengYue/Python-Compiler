from Lex.lexi import lex
from Program.program import pro


if __name__ == '__main__':
    lex('test.txt')
    input_str = ''
    map_list = list()
    with open('lex.txt') as f:
        for line in f.readlines():
            line = line[:-1].split('\t')
            if line[0].isalpha():
                input_str += line[0]
                map_list.append(line[1])
    pro(input_str + '#', map_list)
