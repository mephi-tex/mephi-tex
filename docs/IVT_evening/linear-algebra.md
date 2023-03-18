<!-- Macros: start -->
$\newcommand{\block}[2]{\begin{#1} #2 \end{#1}}$
$\newcommand{\cases}[1]{\block{cases}{#1}}$
$\newcommand{\up}[2]{\stackrel{#1}{#2}}$
$\def\dn#1#2{\mathrel{\mathop{#2}\limits_{#1}}}$
$\def\ident{\Longleftrightarrow}$
$\def\thus{\rightarrow}$
$\newcommand{\set}[1]{ \{ #1 \} }$
$\newcommand{\bigset}[1]{ \left \{ #1 \right \} }$
$\newcommand{\bracs}[1]{ ( #1 ) }$
$\newcommand{\bigbracs}[1]{ \left ( #1 \right ) }$
$\newcommand{\bkets}[1]{\langle #1 \rangle}$
$\newcommand{\bigbkets}[1]{\left \langle #1 \right \rangle}$
$\newcommand{\mat}[1]{\block{Vmatrix}{#1}}$
$\newcommand{\det}[1]{\block{vmatrix}{#1}}$
$\newcommand{\pmat}[1]{\block{pmatrix}{#1}}$
$\newcommand{\emat}[1]{\block{matrix}{#1}}$
$\renewcommand{\geq}{\geqslant}$
$\renewcommand{\leq}{\leqslant}$
$\newcommand{\upline}[1]{\overline{#1}}$
$\newcommand{\dnline}[1]{\underline{#1}}$
$\def\ex{\exists}$
$\def\exo{\ex!}$
$\renewcommand{\fal}{\forall}$
$\renewcommand{\int}{\intop}$
$\def\inf{\infty}$
$\renewcommand{\tg}{\tan}$
$\renewcommand{\phi}{\varphi}$
$\renewcommand{\epsilon}{\varepsilon}$
$\def\alp{\alpha}$
$\def\lam{\lambda}$
$\def\gam{\gamma}$
$\def\eps{\epsilon}$
$\def\sig{\sigma}$
$\newcommand{\NN}{\mathbb{N}}$
$\newcommand{\ZZ}{\mathbb{Z}}$
$\newcommand{\RR}{\mathbb{R}}$
$\newcommand{\CC}{\mathbb{C}}$
$\newcommand{\FF}{\mathbb{F}}$
$\newcommand{\QQ}{\mathbb{Q}}$
$\newcommand{\EE}{\mathbb{E}}$
$\newcommand{\UU}{\mathcal{U}}$
$\newcommand\E{\mathbbold{e}}$
$\newcommand\F{\mathbbold{f}}$
$\newcommand\G{\mathbbold{g}}$
$\newcommand{\rawOlim}[3]{\dn{{#1}\rightarrow{#2}}{#3}}$
$\newcommand{\lim}[2]{\rawOlim{#1}{#2}{lim}}$
$\newcommand{\uplim}[2]{\rawOlim{#1}{#2}{\upline{lim}}}$
$\newcommand{\dnlim}[2]{\rawOlim{#1}{#2}{\dnline{lim}}}$
$\newcommand{\norm}[1]{\left \lVert #1 \right \rVert}$
$\newcommand{\ord}[1]{\operatorname{ord}(#1)}$
$\newcommand{\ans}[1]{\textbf{Ответ}: #1.}$
$\renewcommand{\gcd}{\text{НОД}}$
$\newcommand{\lcm}{\text{НОК}}$
$\newcommand{\proj}[2]{\text{пр.}_{#1}{#2}}$
$\newcommand{\U}[2]{U_{#1}(#2)}$
<!-- Macros: end -->  

# Линейная алгебра  

```{contents} Линейная алгебра  
---  
depth: 3  
```
Преподаватель : Михайлов Владислав Дмитриевич 

Конспект : Руденький Н.В., Б$22$-В$71$.

## Лекция 15.02.2023
### Теорема об обратимости матриц
- $A^{-1}$ - обратная, если $A^{-1}A =AA^{-1} = E$
- Теорема: $A$ обратима тогда и только тогда, когда $det{A} \neq 0, \ A^{-1} = \dfrac{1}{det{A}}\begin{pmatrix}
  A_{11} & A_{21} & \dots & A_{n1} \\
  A_{12} & A_{22} & \dots & A_{n2} \\
  \dots  & \dots & \dots & \dots\\
  A_{1n} & A_{2n} & \dots & A_{nn}
  \end{pmatrix}$
- Доказательство:
	- Необходимость: Пусть $\exists A^{-1}: A^{-1}A = E, \ det{AB} = det{A} \cdot det{B} \implies det{A^{-1}} \cdot det{A} = det{E} = 1 \implies det{A} \neq 0$
	- Достаточность: Докажем, что $A^{-1}$ обратная к $A, \ det{A} \neq 0$.
	- $AA^{-1} =\dfrac{1}{\Delta} \begin{pmatrix}
  a_{11} & a_{12} & \dots & a_{1n} \\
  a_{21} & a_{22} & \dots & a_{2n} \\
  \dots  & \dots & \dots & \dots\\
  a_{n1} & a_{n2} & \dots & a_{nn}
  \end{pmatrix} \begin{pmatrix}
  A_{11} & A_{21} & \dots & A_{n1} \\
  A_{12} & A_{22} & \dots & A_{n2} \\
  \dots  & \dots & \dots & \dots\\
  A_{1n} & A_{2n} & \dots & A_{nn}
  \end{pmatrix} = E$
	-   Предположим, что существует другая обратная матрица $\ A^{-1} = X , \ Y: AY = YA = E$
	- $X = X(AY) = XE = X(AY) = (XA)Y = EY = Y$
### Свойства обратных матриц
- $(A^{-1})^{-1} = A$ 
- $(AB)^{-1} =B^{-1}A^{-1}$
- $(A^{T})^{-1} = (A^{-1})^{T}$
	- Докажем $(1)$
	- $A^{-1}A = E$
	- $A^{-1}AA^{-1} = (A^{-1}A)A^{-1} = EA^{-1}$
	- Докажем $(2)$
	- $(AB)B^{-1}A^{-1} \ ? \ E$
	- $A(BB^{-1})A^{-1} = AEA^{-1} = AA^{-1} = E$
### Вычисление обратных матриц
- По определению
- Элементарными преобразованиями
### Утверждение об элементарных преобразованиях
- Каждое элементарное преобразование есть умножение исходной матрицы на некую невырожденную матрицу, а именно:
- Перемена мест строк (столбцов)
	- $\rho = E - B_{ii} - B_{jj} + B_{ij} + B_{ji}, \ B_{ii}$ , где $b_{ij} = 0, b_{ii} = 1$
- Умножение $i$ - строки на $\lambda$
	- $\rho = E - (1 - \lambda)B_{ii}$
- Сложение $i, j$ - строк
	- $\rho = E + B_{ij}$ 
- Переход от $A$ к $E$ есть последовательность операций : $\rho_{s}\rho_{s-1}\dots\rho_{1}A = E$
- $\rho_{s}\rho_{s-1}\dots\rho_{1}AA^{-1} = EA^{-1}$
- $\rho_{s}\rho_{s-1}\dots\rho_{1} = A^{-1}$

### Теорема о ранге матрицы
- $rg{(A)} = r$
- Если в матрице $A$ есть минор $k$ порядка отличный от нуля, а все окаймляющие его миноры равны нулю, то $rg(A) = k$

## Лекция 01.03.2023
### Теорема о базисном миноре
- Любая строка базисного минора есть линейная комбинация базисных строк
  - Докажем, что любая строка есть линейная комбинация базисных строк. Если cтрока базисная, то данное утверждение очевидно. Возьмем произвольную строку не обязательно входящую в базисный минор. Для удобства будем считать, что базисный минор порядка $r$ в левом верхнем углу матрицы. Разложим определитель по правому столбцу.
	- $ \begin{vmatrix}
  a_{11} & a_{12} & \dots & a_{1r} & a_{1j} \\
  a_{21} & a_{22} & \dots & a_{2r}  & a_{2j}  \\
  \dots  & \dots & \dots & \dots  & \dots  \\
  a_{r1} & a_{r2} & \dots & a_{rr}   & a_{rj} \\
  a_{k1} & a_{k2} & \dots & a_{kr}  & a_{kj} 
  \end{vmatrix} = a_{1j}A_{1j} + a_{2j}A_{2j} + \dots + a_{kj}A_{kj} = a_{1j}C_{1} + a_{2j}C_{2} + \dots + a_{kj}C_{kj} = 0$
  - Получим, что произвольная строка выражается через линейную комбинацию базисных.

### Следствие из теоремы о базисном миноре
- Определитель матрицы равен $0$ тогда и только тогда, когда его строки линейно зависимы
- Доказательство:
	- Необходимость: $det{A} = 0 \implies$ строки $A$ линейно зависимы.
	- Достаточность : строки линейно зависимы $\implies$ $det{A} = 0$

### Системы линейных алгебраический уравнений 
- $\begin{equation*}
 \begin{cases}
   a_{11}x_{1} + a_{12}x_{2}  + \dots + a_{1n}x_{n}   = b_{1} \\
   a_{11}x_{1} + a_{11}x_{1}  + \dots + a_{1n}x_{n}   = b_{2} \\
   \dots  \dots  \dots  \dots \dots \dots \dots \dots \dots\dots \dots    \\
   a_{m1}x_{1} + a_{m2}x_{2}  + \dots + a_{mn}x_{n}   = b_{n} \\
   \end{cases}
  \end{equation*}$
- Набор чисел называется решением, если при подстановке в систему образуется тождество. В этом случае система совместна
-  Две системы эквивалентны, если множества их решений совпадают

### Совместность однородной системы
 - $\left(b_{1}=b_{2} \dots = b_{m} = 0\right)$ Всегда совместна, так как имеется одно решение $\left(x_{1}=x_{2} \dots = x_{m} = 0\right)$

### Теорема Кронекера - Капелли
- Система совместна тогда и только тогда, когда ранг основной матрицы системы равен рангу расширенной матрицы
	- $A = \begin{pmatrix}
  a_{11} & a_{22} & a_{13} & \dots & a_{1n} \\
  a_{21} & a_{22} & a_{23} & \dots & a_{2n} \\
  \dots & \dots & \dots  & \dots & \dots \\
  a_{m1} & a_{m2} & a_{m3} & \dots & a_{mn} \\
  \end{pmatrix}$
	- $\overline{A} = \begin{pmatrix}
  a_{11} & a_{22} & a_{13} & \dots & a_{1n} & b_{1} \\
  a_{21} & a_{22} & a_{23} & \dots & a_{2n} & b_{2}  \\
  \dots & \dots & \dots  & \dots & \dots & \dots \\
  a_{m1} & a_{m2} & a_{m3} & \dots & a_{mn} & b_{m}  \\
  \end{pmatrix}$
- Доказательство 
	- Необходимость: система имеет решение, тогда существует набор чисел $x_{1} = c_{1}, x_{2} = c_{2}, \dots, x_{n} = c_{n}$. Тогда при подстановке в систему обращаются в тождество
	- $\begin{pmatrix}
	  a_{11} \\
	  \dots \\
	  a_{m1}  \\
	  \end{pmatrix} c_{1} + \begin{pmatrix}
	  a_{12} \\
	  \dots \\
	  a_{m2}  \\
	  \end{pmatrix} c_{2} + \dots + \begin{pmatrix}
	  a_{1n} \\
	  \dots \\
	  a_{mn}  \\
	  \end{pmatrix} c_{n} = \begin{pmatrix}
	  b_{1} \\
	  \dots \\
	  b_{m}  \\
	  \end{pmatrix}$. Это означает, что столбец $B$ есть линейная комбинация столбцов матрицы $A \implies rgA = rg\overline{A}$
	-  Достаточность: дано $rang{A} = rang{\overline{A}}$. Доказать, что система совместна, то есть если добавление столбца свободных членов не меняет ранга расширенной матрицы, то этот столбец есть линейная комбинация столбцов $A$. А это значит, что существуют ненулевое число $c_{j}$

### Правило Крамера
- Рассмотрим квадратную систему с отличным от нуля определителем (Система Крамера)
	- $\begin{equation*}
	 \begin{cases}
    a_{11}x_{1} + a_{12}x_{2}  + \dots + a_{1n}x_{n}   = b_{1}  & | & A_{1j}\\
    a_{21}x_{1} + a_{21}x_{2}  + \dots + a_{2n}x_{n}   = b_{2}  & | & A_{2j}\\
    \dots + \dots  + \dots + \dots   + \dots =& | & \dots \\
    a_{n1}x_{1} + a_{n2}x_{2}  + \dots + a_{nn}x_{n}   = b_{n} & | & A_{nj} \\
    \end{cases}
    \end{equation*}$
	- $x_{1}(a_{11} A_{1j} + a_{21} A_{2j} + \dots + a_{n1} A_{nj}) + \dots + x_{n}(a_{1n}A_{1j} + a_{2n}A_{2j} + \dots + a_{nn}A_{nj}) = \underbrace{b_{1} A_{1j} + b_{2} A_{2j} + \dots + b_{n}A_{nj}}_{\Delta j}$
	- $x_{j} \Delta = \Delta_{j} \implies x_{j} = \dfrac{\Delta_{j}}{\Delta}$

### Исследование системы. Общее решение однородных и неоднородных систем
- Пусть $rg{A} = r < n$. Без ограничения общности будем считать, что $r$ уравнений, входящих в базисный минор и $r$ неизвестных находятся в левом верхнем углу.
	- $\begin{equation*}
	 \begin{cases}
    a_{11}x_{1} + a_{12}x_{2}  + \dots + a_{1r}x_{r}  =   - a_{1_r+1}x_{r + 1} - a_{2, r + 2}x_{r + 2}  -  \dots - a_{1n}x_{n} + b_{1} \\
    a_{21}x_{1} + a_{22}x_{2}  + \dots + a_{2r}x_{r}  =  -  a_{2, r+1}x_{r + 1} - a_{2, r + 2}x_{r + 2}  -  \dots - a_{2n}x_{n} + b_{2} \\
    \dots  \dots   \dots  \dots  \dots   \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \\
    a_{r1}x_{1} + a_{r2}x_{2}  + \dots + a_{rr}x_{r}  = -   a_{r, r+1}x_{r + 1}   -  a_{2, r+2}x_{r + 2} - \dots - a_{rn}x_{n} + b_{r} \\
    \end{cases}
    \end{equation*}$
	- Получим систему Крамера, которая имеет единственное решение, поскольку свободным переменным можно придавать любые значения, то решений бесконечно много
	- $\bigg|\{x_{r + 1}, x_{r + 2}, \dots, x_{n}\}\bigg|= n - r \implies n - r $ линейно независимых наборов свободных переменных. Все они и называются ФСР.
	- Нормальная ФСР состоит из единиц и нулей: $X_{1} = \begin{pmatrix}
	 x_{1} \\
     \dots \\
     x_{r} \\
     1 \\
     0 \\
     0 \\
     \dots \\
     \end{pmatrix}; \  X_{2} =  \begin{pmatrix}
     x_{1} \\
     \dots \\
     x_{r} \\
     0 \\
     1 \\
     0\\
     \dots \\
     \end{pmatrix}; \ X_{3} = \begin{pmatrix}
     x_{1} \\
     \dots \\
     x_{r} \\
     0 \\
     0 \\
     1\\
     \dots \\
     \end{pmatrix};  \ \dots; \ X_{n - r} = \begin{pmatrix}x_{1} \\
     \dots \\
     x_{r} \\
     0 \\
     0 \\
     \dots \\
	  1 \\
	  \end{pmatrix}$
- Если сложить все решения ФСР с произвольными коэффициентами, то получим общее решение соответствующей однородной системы: $X = c_{1}X_{1} + \dots + c_{n -r}X_{n-r}$
### Общее решение неоднородной системы
- Общее решение неоднородной системы $X_{ОРНС} = X_{ЧРНС} + X_{ОРОС}$

## Лекция 15.03.2023

### Метод Гаусса решения систем линейных алгебраических уравнений 
- $\begin{cases}
     a_{11}x_{1}  + a_{12}x_{2} \dots a_{1n}x_{n} = b_{1} \\
     a_{21}x_{1}  + a_{22}x_{2} \dots a_{2n}x_{n} = b_{2} \\
     \dots \\
     a_{m1}x_{1} + a_{m2}x_{2} \dots a_{mn}x_{n} = b_{m}
     \end{cases}$
	- Элементарными преобразованиями приводим расширенную матрицу системы к виду:
	- $\begin{pmatrix}
	1  & a_{12}  & \dots & a_{1n} \ | b_{1} \\
	0  & 1 & \dots & a_{2n}' \ | b_{2}' \\
	\dots & \dots & \dots & \dots \\
	0  & \dots & a_{m-1n}'  & a_{mn}' \ | b_{m}' \\
    0  & \dots & \dots &\dots  | 0  \\
    \end{pmatrix}$
	- $a_{mn}' = a_{m-1n}' = 0 \neq b_{m}' \implies$ Система несовместна
	- $a_{m-1n}' = 0, a_{mn}' \neq 0 \implies$ У системы только одно решение
	- $a_{m-1n}' \neq 0, a_{mn}' \neq 0 \implies $ У системы больше одного решения

### Линейные пространства

***Обозначение***

- $\RR^{n}$

***Определение***

- Множество элементов любой природы называется линейным пространством этих элементов, если эти элементы подчиняются двум требованиям:
	- Для любой пары элементов определен элемент этого же пространства, называемый суммой этих элементов, так что выполняется 4 аксиомы для $\vec{a}, \vec{b}, \vec{c} \in \RR^{n}$:
		- $\vec{a} + \vec{b} = \vec{b} + \vec{a}$
		- $(\vec{a} + \vec{b}) + \vec{c} = \vec{a} + (\vec{b} + \vec{c})$
		- $\forall \vec{a}: \vec{a} + \vec{0} = \vec{a}$
		- $\forall \vec{a} \in \RR^{n} \ \exists \vec{a}': \vec{a}' + \vec{a} = \vec{0}$
	- На данном множестве определена операция умножения элемента пространства на число, со следующими свойствами:
		- $(\lambda \mu)\vec{a} = \lambda(\mu \vec{a})$ 
		- $(\lambda + \mu)\vec{a} = \lambda \vec{a} + \mu \vec{a}$
		- $\lambda(\vec{a} + \vec{b}) = \lambda \vec{a} + \lambda \vec{b}$
		- $\vec{a} \cdot 1 = \vec{a}$

- Примеры
	- $\RR^{2}$ по сложению и умножению
	- Пространство функций заданных и непрерывных на $\left[a;b\right]$
	- Пространство упорядоченных наборов чисел $a = \left(x_{1}, x_{2}, \dots, x_{n}\right)$
	- Пространство всех многочленов $P_{n}(x), \deg{P} \leq n$

### Некоторые свойства $\RR^{n}$ 
- Единственность нулевого элемента
	- Предположим, что есть два различных нулевых элемента $\vec{0_{1}}, \ \vec{0_{2}} \in \RR^{n}$. Взяв за нулевой элемент $\vec{0_{1}}$, за произвольный $\vec{0_{2}}:$  $\vec{0_{2}} + \vec{0_{1}} = \vec{0_{2}}$. Наоборот:  $\vec{0_{2}}: \vec{0_{1}} + \vec{0_{2}} = \vec{0_{1}} \implies \vec{0_{1}} = \vec{0_{2}}$
- Единственность противоположного элемента для любого элемента $\vec{a} \in \RR^{n}$. 
  - Пусть имеется два различных противоположных элемента для одного и того же $\vec{a} \in \RR^{n}: \vec{a} + \vec{b_{1}} = \vec{0}$ и $\vec{a} + \vec{b_{2}} = \vec{0} \implies$$\vec{b_{1}} = \vec{b_{1}} + \vec{0} = \vec{b_{1}} + (\vec{a} + \vec{b_{2}})= (\vec{b_{1}} + \vec{a}) + \vec{b_{2}} = \vec{0} + \vec{b_{2}} = \vec{b_{2}}$

- Нулевой элемент получается умножением любого элемента $a \in \RR^{n}$ на число $0 \in \RR$.
  - $0 \cdot \vec{a} = \vec{a} \cdot 0 + \vec{0} = \vec{a} \cdot 0 + \vec{a} + \vec{a}' = \vec{a} \cdot 0 + \vec{a} \cdot \vec{1} + \vec{a}' = \vec{a} \left(0 + \vec{1}\right) + \vec{a}' = \vec{a} \cdot 1 + \vec{a}' = \vec{a} + \vec{a}' = \vec{0}$
- Получение противоположного элемента для любого $\vec{a} \in \RR^{n}$ с заданной операцией сложения элементов.
  - Докажем, что  $\vec{a}' = \left(-1\right)\vec{a}$
  - $\left(-1\right)\vec{a} = \left(-1\right)\vec{a} + \vec{0} = \left(-1\right) \vec{a} + \vec{a} + \vec{a}' = (-1 + 1) \vec{a} + \vec{a}' = 0 \vec{a} + \vec{a}' = \vec{0} + \vec{a}' = \vec{a}'$

### Базис и размерность $\RR^{n}$
- Совокупность элементов $\vec{e}_{1}, \vec{e_{2}}, \dots, \vec{e_{n}} \in \RR^{n}$ называется линейно независимой, если $ \lambda_{1}\vec{e_{1}} +  \lambda_{2}\vec{e}_{2} +  \lambda_{n} \vec{e_{n}} = 0 \implies $ $\lambda_{1} = \lambda_{2} = \lambda_{3} = \dots = \lambda_{n} = 0$. 
