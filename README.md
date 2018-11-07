# 词法分析
## 规则
```
1、标识符:字母打头，后接任意字母或数字。 
2、保留字:标识符的子集，包括 if, else, for, while, int, write,read。
3、无符号整数:由数字组成，但最高位不能为 0，允许一位的 0。 
4、分界符:(、)、;、{、}、, 
5、运算符:+、-、*、/、=、<、>、>=、<=、!=、== 
6、注释符:/* */
```
## 自动机状态转换图
![Image text](https://github.com/XiaofengYue/Python-Compiler/blob/master/img-folder/%E8%87%AA%E5%8A%A8%E6%9C%BA.png)
## 单词分类方案
```
输入	分类	类别码
数字 NUM	1
字母开头后接任意字母或数字（保留字除外）	ID 2
if	if	3
else	else	4
for	for	5
while	while	6
int	int	7
write	write	8
read	read	9
（	（	10
）	）	11
；	；	12
｛	｛	13
｝	｝	14
，	，	15
＋	＋	16
－	－	17
＊	＊	18
／	／	19
＝	＝	20
＞	＞	21
＜	＜	22
＞＝	＞＝	23
＜＝	＜＝	24
！＝	！＝	25
＝＝	＝＝	26
／＊　　＊／	注释符	27
```
## 语法规则
```
1) <program> → {<declaration_list><statement_list>}
2) <declaration_list> → <declaration_list><declaration_stat> | ε
3) <declaration_stat> → int ID;
4) <statement_list> → <statement_list><statement>| ε
5) <statement> → <if_stat>|<while_stat>|<for_stat>|<read_stat>
|<write_stat>|<compound_stat> |<assignment_stat>|;
6) <if_stat> → if (<bool_expression >) <statement >
| if (<bool_expression>) <statement >else < statement >
7) <while_stat> → while (<bool_expression>) < statement >
8) <for_stat> → for (<assignment_expression>; <bool_expression>;
<assignment_ expression >)<statement>
9) <write_stat> → write < arithmetic_expression >;
10) <read_stat> → read ID;
11) <compound_stat> → {<statement_list>}
12) <assignment_expression> → ID=<arithmetic_expression>
13) <assignment_stat> →<assignment_expression>;
14) <bool_expression>→<arithmetic_expression> > <arithmetic_expression>
|<arithmetic_expression> < <arithmetic_expression> |<arithmetic_expression> >= <arithmetic_expression> |<arithmetic_expression> <= <arithmetic_expression> |<arithmetic_expression> == <arithmetic_expression> |<arithmetic_expression> != <arithmetic_expression>
15) <arithmetic_expression> → <arithmetic_expression>+<term> |< arithmetic_expression>-<term>
|< term >
16) < term > → < term >*<factor>|< term >/<factor>|< factor >
17) < factor > → (<arithmetic_expression>)|ID|NUM
```
## 构造LL(1)文法
### 前期准备
```
S <program>
A <declaration_list>
B <declaration_stat>
C <statement_list>
D <statement>
E <if_stat>
F <while_stat>
G <for_stat>
H <write_stat>
I <read_stat>
J <compound_stat>
K <assignment_expression>
L <assignment_stat>
M <bool_expression>
N <arithmetic_expression>
O <term>
P <factor>

#将语法规则符号化
1) S → 13 AC 14
2) A → AB|ε
3) B → 7 2 12
4) C → CD|ε
5) D → E|F|G|I|H|J|L|12
6) E → 3 10 M 11 D | 3 10 M 11 D 4 D
7) F → 6 10 M 11 D
8) G → 5 10 K 12 M 12 K 11 D
9) H → 8 N 12
10) I → 9 2 12
11) J → 13 C 14
12) K → 2 20 N
13) L → K 12
14) M → N 21 N | N 22 N | N 23 N | N 24 N | N 26 N | N 25 N
15) N → N 16 O | N 17 O | O
16) O → O 18 P | O 19 P | P
17) P → 10 N 11 | 1 | 2

#提取左公因子、消除左递归
1) S → 13 AC 14
2) A → BA|ε
3) B → 7 2 12
4) C → DC|ε
5) D → E|F|G|I|H|J|L|12
6) E → 3 10 M 11 D e
   e → 4 D | ε
7) F → 6 10 M 11 D
8) G → 5 10 K 12 M 12 K 11 D
9) H → 8 N 12
10) I → 9 2 12
11) J → 13 C 14
12) K → 2 20 N
13) L → K 12
14) M → N m
    m → 21 N | 22 N | 23 N | 24 N | 26 N | 25 N
15) N → O n
    n → 16 O n | 17 O n | ε
16) O → P o
    o → 18 P o | 19 P o | ε 
17) P → 10 N 11 | 1 | 2
```
