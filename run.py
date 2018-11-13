from Lex.lexi import lex
from Program.program import pro


if __name__ == '__main__':
    lex('test.txt')
    input_str = ''
    with open('lex.txt') as f:
        for line in f.readlines():
            input_str += line[0]
    pro(input_str+'#')
