# 词法分析、语法分析
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
# 语义分析
## 前置工作
### 添加动作
```
@name-def: 将变量名放入符号表中
@BRF： 结果为假时跳转到指定标号的四元式
@BR： 结果为真时跳转到指定标号的四元式
@SETlabel： 设置标号（用于判断，循环语句的跳转）
@IN： 将从键盘获取的值赋给指定变量
@OUT： 将变量的值输出到控制台
@LOOK： 查符号表
@LOAD： 加载符号表中的值
@LOADI： 加载常量
@GT： 比较两个变量或值的大小，若p1>p2返回真
@LES： 比较两个变量或值的大小，若p1<p2返回真
@GE:  比较两个变量或值的大小，若p1<=p2返回真
@LE: 比较两个变量或值的大小，若p1>=p2返回真
@EQ: 比较两个变量或值的大小，若p1==p2返回真
@NOTEQ:  比较两个变量或值的大小，若p1!=p2返回真
@ADD:  返回p1+p2
@SUB： 返回p1-p1
@MULT： 返回p1*p2
@DIV： 返回p1/p2
```
### 添加属性
```
1) <program> → {<declaration_list><statement_list>}
2) <declaration_list> → <declaration_list><declaration_stat> | ε

3）<declaration_stat >↑n → int ID↑n@name-def↓n；

4) <statement_list> → <statement_list><statement>| ε
5) <statement> → <if_stat>|<while_stat>|<for_stat>|<read_stat>

6）<if_stat> →  if(<bool_expression>↑r)@BRF↓'j',0,_ ,↑label1
                            <statement> @BR↓'j',_,_ ,↑label2   @SETlabel↓label1  
                            [else<statement>]@SETlabel↓label2
7）<while_stat> → while @SETlabel↓label1 
                                (<bool_expression >↑r) @BRF↓'j',0,_↑label2
                                < statement >@BR↓'j',0,_↑label1 @SETlabel↓label2
8）<for_stat> → for (<assignment_expression >;      
                                @SETlabel↑label1
                                 < bool _expression >↑r;     
                                @BRF↓'j',0,_,label2@BR↓'j',0,_,label3@SETlabel↑label4
                                 < assignment_expression >@BR↓'j',0,_,label1)     
                                @SETlabel↓label3 
                                <statement>@BR↓'j',_,_,label4@SETlabel↓label2
9）<write_stat> → write < arithmetic_expression >↑t@OUT↑t;                                
10）<read_stat> → read ID↑n LOOK↓n↑d @IN
11) <compound_stat> → {<statement_list>}
12）< assignment_expression >↑n,t  →  ID↑n@LOOK↓n↑d = <arithmetic_expression >↑t
13) <assignment_stat> → <assignment_expression>;
14）<bool_expression>↑t  →   <arithmetic_expression> ↑r R↑t↓r
    R↑t↓r    →     > <arithmetic_expression>↑p@GT↓r,p↑t       | 
                   < <arithmetic_expression>↑p@LES↓r,p↑t      | 
                   >= <arithmetic_expression>↑p@GE↓r,p↑t      | 
                   <= <arithmetic_expression>↑p@LE↓r,p↑t      | 
                   == <arithmetic_expression>↑p@EQ↓r,p↑t      | 
                   != <arithmetic_expression>↑p@NOTEQ↓r,p↑t
15）<arithmetic_expression>↑t → <term>↑r T↓r↑t
     T↓r↑t     →    +<term>↑p @ADD↓r,p,t0   T↓t0↑t  |
                    -<term>↑p @SUB ↓r,p,t0   T↓t0↑t |
                    ε
16）<term >↑t  →    <factor>↑r U↓r↑t
     U↓r↑t     →    *<factor>↑p @MULT↓r,p,t0   U↓t0↑t  |   
                    /<factor>↑p @DIV↓r,p,t0    U↓t0↑t  |
                    ε                            
17）<factor>↑p → (<arithmetic_expression>↑t)  | 
                 ID↑n @LOOK↓n↑d @LOAD↓d       |  
                 NUM↑i@LOADI↓i

```
### 符号化的属性文法
```
3） B↑n →   g b↑n@name-def↓n l  
6） E   →   c j M↑r k @BRF↓'j',0,_ ,↑label1D@BR↓'j',_,_ ,↑label2   @SETlabel↓label1  Q@SETlabel↓label2
            Q → d D | ε
7） F   →   f@SETlabel↓label1
            j M↑r k@BRF↓'j',0,_↑label2
            D@BR↓'j',0,_↑label1 @SETlabel↓label2    
8)  G   →   e j K l @SETlabel↑label1
            M↑r l@BRF↓'j',0,_,label2@BR↓'j',_,_,label3@SETlabel↑label4
            K@BR↓'j',_,_label1 k @SETlabel↓label3 
            D@BR↓'j',_,_,label4@SETlabel↓label2
9） H   →   h N↑t;@OUT           
10）I   →   i ID↑n LOOK↓n↑d @IN
12）K↑n,t→  b↑n @LOOK↓n↑d  t N↑t@STO↓d @POP
14) M↑t →   N ↑r R↑t↓r
    R↑t↓r → u N↑p@GT↓r,p↑t    | 
            v N↑p@LES↓r,p↑t   | 
            w N↑p@GE↓r,p↑t    | 
            x N↑p@LE↓r,p↑t    | 
            z N↑p@EQ↓r,p↑t    | 
            y N↑p@NOTEQ↓r,p↑t
15）N↑t →   O↑rT↓r↑t
    T↓r↑t → p O↑p @ADD↓r,p,t0  T ↓t0↑t  |
            q O↑p @SUB ↓r,p,t0  T ↓t0↑t |
            ε
16）O↑t →   P↑r U↓r↑t
    U↓r↑t → r P↑p @MULT↓r,p,t0 U↓t0↑t  |
            s P↑p @DIV↓r,p,t0  U↓t0↑t  |
            ε                        
17）P↑p →   j N↑t k               |
            a↑n @LOOK↓n↑d @LOAD↓d |
            b↑i@LOADI↓i
```

