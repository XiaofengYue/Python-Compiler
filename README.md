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
数字 NUM	a
字母开头后接任意字母或数字（保留字除外）	ID b
if	if	c
else	else	d
for	for	e
while	while	f
int	int	g
write	write	h
read	read	i
（	（	j
）	）	k
；	；	l
｛	｛	m
｝	｝	n
，	，	o
＋	＋	p
－	－	q
＊	＊	r
／	／	s
＝	＝	t
＞	＞	u
＜	＜	v
＞＝	＞＝	w
＜＝	＜＝	x
！＝	！＝	y
＝＝	＝＝	z
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
1) S → m AC n
2) A → AB|ε
3) B → g b l
4) C → CD|ε
5) D → E|F|G|I|H|J|L|l
6) E → c j M k D | c j M k D d D
7) F → f j M k D
8) G → e j K l M l K k D
9) H → h N l
10) I → i b l
11) J → m C n
12) K → b t N
13) L → K l
14) M → N u N | N v N | N w N | N x N | N z N | N y N
15) N → N p O | N q O | O
16) O → O r P | O s P | P
17) P → j N k | a | b

#提取左公因子、消除左递归
1) S → m AC n
2) A → BA|ε
3) B → g b l
4) C → DC|ε
5) D → E|F|G|I|H|J|L|l
6) E → c j M k D Q
   Q → d D | ε
7) F → f j M k D
8) G → e j K l M l K k D
9) H → h N l
10) I → i b l
11) J → m C n
12) K → b t N
13) L → K l
14) M → N R
    R → u N | v N | w N | x N | z N | y N
15) N → O T
    T → p O T | q O T | ε
16) O → P U
    U → r P U | s P U | ε 
17) P → j N k | a | b
```
