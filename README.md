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
