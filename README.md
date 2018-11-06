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
