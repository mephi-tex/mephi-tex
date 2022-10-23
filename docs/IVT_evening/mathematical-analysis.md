<!-- Macros: start -->
$\newcommand{\block}[2]{\begin{#1} #2 \end{#1}}$
$\newcommand{\cases}[1]{\block{cases}{#1}}$
$\newcommand{\up}[2]{\stackrel{#1}{#2}}$
$\def\dn#1#2{\mathrel{\mathop{#2}\limits_{#1}}}$
$\def\ident{\Longleftrightarrow}$
$\def\thus{\Rightarrow}$
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
$\renewcommand{\int}{\intop}$
$\def\inf{\infty}$
$\newcommand{\lim}[2]{\dn{{#1}\rightarrow{#2}}{lim}}$
$\newcommand{\ans}[1]{\textbf{Ответ}: #1.}$
$\newcommand{\proj}[2]{\text{пр.}_{#1}{#2}}$
$\newcommand{\norm}[1]{\left \lVert #1 \right \rVert}$
$\newcommand{\ord}[1]{\operatorname{ord}(#1)}$
$\renewcommand{\gcd}{\text{НОД}}$
$\newcommand{\lcm}{\text{НОК}}$
<!-- Macros: end -->  

```{contents} Математический анализ  
---  
depth: 3  
```
# Математический анализ  
Преподаватель - Михайлов Владислав Дмитриевич  

# Литература  

- [Демидович Б. П. - "Сборник задач и упражнений по Математическому Анализу"](https://docs.google.com/gview?url=https://mephi-tex.rtfd.io/ru/latest/_static/literature/БП_ДЕМИДОВИЧ_СБОРНИК_ЗАДАЧ_И_УПРАЖНЕНИЙ_ПО_МАТЕМАТИЧЕСКОМУ_АНАЛИЗУ.pdf)  

## Лекция 07.09.2022  

### Числовые Множества. Вещественные числа.  

 ***Определение***  

- $\NN$ - Множество натуральных чисел  
- $\ZZ$ - Множество целых чисел  
- $\QQ$ - Множество рациональных чисел   
- $\RR$ - Множество вещественных чисел  

***Упражнение***  

- Доказать, что $(\dfrac{m}{n})^2 \neq 2$, где $\dfrac{m}{n}$ - несократимая дробь.  
	- Доказательство : Предположим, что $(\dfrac{m}{n})^2 = 2$, тогда :  
	$m^2 = 2n^2$ Т.к. $2n^2$ - четное, то и $m^2$ - четное, а следовательно $m$ - четное. $m = 2k$, $4k^2 = 2n^2$, $2k^2 = n^2$ - следовательно: $n^2$ - четное. Получим противоречие, т.к. $\dfrac{2n^2}{2k^2}$ - сократимая дробь.  


### Сравнение вещественных чисел, их сумма и произведение  

***Определение***  
- Сравниваем поразрядно $a_{0}, b_{0}$, затем $a_{1}, b_{1}$ и т.д.  

- По аналогии сумма и произведение: $a_{0} \dot b_{0}$, затем $a_{1}\dot b_{1}$ и т.д.  


### Множества. Инфимум и Супремум.  
Рассмотрим произвольное числовое множество $A$, состоящее из чисел $x \in A$.   

***Определение***  
- Множество $A$ называется ограниченным сверху, если $\exists M : \forall x \in A \Rightarrow x \leq M$  

***Определение***  
- Множество $A$ называется ограниченным снизу, если $\exists m : \forall x \in A \Rightarrow x \geq m$  

***Определение***  
- Множество $A$ называется ограниченным снизу и сверху, если $\exists M, m : \forall x \in A \Rightarrow  m \leq x \leq M$  


***Определение***  
- Наименьшая граница из всех верхних граней называется точной верхней гранью $(\sup{A})$  

***Определение***  

- Наибольшая граница из всех нижних граней называется точной нижней гранью $(inf{A})$  


***Теорема***  
- Всякое ограниченное сверху множество имеет точную верхнюю грань, а всякое ограниченное снизу имеет точную нижнюю грань.  

***Определение точной верхней грани***  

- $(\forall x \in X : x \leq  M) \wedge (\forall x < M \exists x' \in X : x' > x) \Rightarrow M = \sup{X} $  

***Определение точной нижней грани***  
- $(\forall x \in X x \geq m) \wedge (\forall > m, \exists x' \in X: x' < x) \Rightarrow m =inf{X}$  

***Альтернативное определение точной нижней грани***  
- $(\forall x \in X: x \geq m ) \wedge (\forall \epsilon > 0, \exists x' \in X : x' < m + \epsilon) \Rightarrow m = inf{X}$  

***Альтернативное определение точной верхней грани***  
- $(\forall x \in X : x \leq M) \wedge (\forall \epsilon > 0 \exists x' \in X: x' > M - \epsilon) \Rightarrow M = \sup{X}$  

***Упражнение***  

- Докажем, что всякое ограниченное сверху множество имеет $\sup$.   
  - Доказательство : Рассмотрим два случая:  

	1. Рассматриваемое множество не лишено неотрицательных чисел  

	2. Рассматриваемое множество содержит только отрицательные числа  

		- Пусть $(1)$, тогда точная верхняя грань больше или равна нуля. Т.к. множество ограничено сверху, то его целые части не превышают этой грани. Отберем из множества те числа, у которых наибольшая целая часть $\overline{x_{0}}$, остальные числа отбросим. Среди оставшихся отберем те, у которых наибольший следующий разряд, т.е $\overline{x_{0}},\overline{x_{1}}$. И т.д. до бесконечности. Получаем число - бесконечную, вообще говоря, непериодическую десятичную дробь. $\overline{x_{0}}\overline{x_{1}}\overline{x_{2}} ... \overline{x_{n}} ... = \overline{x} (\sup)$  

		- Докажем, что таким образом получим точную верхнюю грань данного множества. Действительно по первой части определения $\sup$ : $\forall x \in A \Rightarrow x \leq \overline{x}$. Но это и есть $\sup$ по характеру построения числа $\overline{x}$, так как на каждой позиции для построения $\overline{x}$ бралось наибольшее число. Теперь докажем вторую часть определения $\sup$. $\forall x < \overline{x}, \exists x' \in A: x' > x$. Действительно, берем произвольное число (не обязательно из множества $A$) , $x < \overline{x}$, т.к. $x < \overline{x}$ на каком - то знаке из $\overline{x_{0}},\overline{x_{1}}, ... ,\overline{x_{n}}, ... $. Докажем, что $\exists x' \in A$ , т.ч. $x' > x$. Т.к. $x' \in A$, то $x_{0}' \leq \overline{x_{0}}$, а если они равны, то $x_{1}' < \overline{x_{1}}$ и т.д. до позиции с номером $n$. Получим, что в элементах нашего множества есть число, у которого на $n$ - ом месте стоит $\overline{x_{n}}$, но $\overline{x_{n}} > x_{n} \Rightarrow x_{n}' > x_{n}$  

		- Докажем для пункта $(2)$. Если все числа множества $A$ - отрицательные, то $\forall x \in A: x = -|x|$, тогда отбрасываем все числа у которых наименьшая целая часть модуля $\overline{x_{0}}$, затем у которых $\overline{x_{0}}, \overline{x_{1}}$ и т.д. до бесконечности. Получаем бесконечную десятичную непериодическую дробь. Поставим перед числом знак $(-)$, получим $\sup$.  

***Пример***  

- $A = \{1, \dfrac{1}{2},\dfrac{1}{3}, ... \dfrac{1}{n}, ...\}$. $\sup{A} = 1, inf{A} = 0$  


### Числовая последовательность.  

***Определение***  

- Рассмотрим упорядоченный набор натуральных чисел$\{1, 2, 3, ..., n, ...\}$ и каждому из этих натуральных чисел поставим в соответствие числа: $x_{1}, x_{2}, x_{3}, ... , x_{n}, ...$. Это и есть числовая последовательность.  


***Обозначение***  
- $\{x_{n}\}$  

***Свойства***  

- Последовательность $\{x_{n}\}$ бывает ограниченной сверху, снизу и просто ограниченной.  

 1.  $\forall n: x_{n} \leq M$  
 2.  $\forall n: x_{n} \geq m$  
 3.   $\forall n: m \leq x_{n}  \leq M$  

***Пример***  

1. $\{1, \dfrac{1}{4}, \dfrac{1}{9}, ... ,\dfrac{1}{n^2}, ... \}$ - Ограничена снизу нулем, сверху единицей  
2. $\{1,-1, \dfrac{1}{4},-2, \dfrac{1}{9},-3, ... ,-n, \dfrac{1}{n^2}, ... \}$ - Не ограничена снизу.  

***Определение***  

   - Если для любой пары соседних членов последовательности выполняется $x_{k + 1} \geq x_{k}$, то последовательность неубывающая, если $x_{k + 1} > x_{k}$, то строго возрастающая. Аналогично для невозрастающей и строго убывающей.  


## Лекция 14.09.2022  


### Числовые последовательности  
- Пусть имеем для бесконечной последовательности $\{1, 2, 3, \dots , n, \dots \}$ набор соответсвующих чисел $\{x_{1}, x_{2}, x_{3}, \dots , x_{n}, \dots \}$. Получим последовательность.  

***Способы задания последовательностей***  

1. Перечислением  
2. Графически  
3. Рекуррентно  

***Примеры***  

1. $\{1, \dfrac{1}{2}, \dfrac{1}{3}, \dots, \dfrac{1}{n}, \dots\}$  

2. $\{-1, 1, -1, \dots, (-1)^n, \dots \}$  

3. $x_{n} = \dfrac{1 + (-1)^n}{2}$ - Формула общего члена  

4. Натуральный ряд - $\{1, 2, 3, 4, \dots\}$  

5. $x_{n} = 1^{(-1)^n}$  

6. $x_{n} = - n^2$  


- Последовательность называется ограниченной сверху $\Leftrightarrow \exists M: \forall n : x_{n} \leq M$  

***Определение***  
- Последовательность называется ограниченной снизу $\Leftrightarrow \exists m: \forall n : x_{n} \geq m$  

***Определение***  
- Последовательность называется ограниченной $\Leftrightarrow \exists m,M : \forall n :  m \leq x_{n} \leq M$ или в эквивалентной форме :  $\exists k , \forall n :  |x_{n}| \leq k$  

***Определение***  

- $\forall m, \exists n : |x_{n}| > m \Leftrightarrow$ последовательность не ограничена. (не является ограниченной сверху или снизу)  

### Бесконечно большая и малая последовательность  

***Определение***  

- $\{x_{n}\}$ называется бесконечно большой $\Leftrightarrow \forall A, \exists N_{0}: \forall n > N_{0} \rightarrow |x_{n}| > A$.  

***Пример***  
- $\{1, -2, 3, -4, \dots, (-1)^{n+1} \cdot n, \dots\}$ (В отличие от неограниченной последовательности, члены бесконечно большой последовательности по модулю больше любого наперед заданного числа A, начиная с какого - то номера.)  

***Определение***  

- $\{x_{n}\}$ называется бесконечно малой $\Leftrightarrow \forall A, \exists N_{0}: \forall n > N_{0} \rightarrow |x_{n}| < A$.  

***Теорема***  

- Если $\{x_{n}\}$ - б. б. , то начиная с какого - то номера, после которого нет нулевых членов, для этих номеров определена бесконечно малая последовательность: $\{ \dfrac{1}{x_{n}} \}$.  
	- Доказательство : Действительно, т.к. $\{x_{n}\}$ - б. б. , то, начиная с $n > N_{0}: |x_{n}| > A$, где $A$ - любое число. Тогда для этих номеров: $\dfrac{1}{x_{n}} < \dfrac{1}{A}$. Если взять произвольное $\epsilon > 0$ и $A = \dfrac{1}{\epsilon}$, то $|\dfrac{1}{x_{n}}| , \epsilon$, а это и есть определение бесконечно малой последовательности. Справедливо и обратное: Если $\{ \dfrac{1}{x_{n}} \}$ - б. м. , то начиная с какого - то номера, после которого нет нулевых членов, для этих номеров определена $\{x_{n}\}$ - б. б.  

### Монотонные последовательности  
***Определение***  
- Последовательность $\{x_{n}\}$ называется возрастающей, если $\forall n : x_{n + 1} \geq x_{n}$ и строго возрастающей, если $x_{n + 1} > x_{n}$. (Иногда говорят: неубывающая, строго возрастающая).   

***Определение***  
- Последовательность $\{x_{n}\}$ называется убывающей, если $\forall n : x_{n + 1} \leq x_{n}$ и строго убывающей, если $x_{n + 1} < x_{n}$. (Иногда говорят: невозрастающая, строго убывающая).   

### Предел числовой последовательности  

***Формальное определение предела числовой последовательности***  

- Если последовательность приближается к числу, то это число и есть ее предел.  

***Примеры***  

1. $x_{n} = \dfrac{1}{n}, \lim{n}{\infty} \dfrac{1}{n}  = 0$  
2. $x_{n} = \dfrac{n - 1}{n}, \lim{n}{\infty} \dfrac{n - 1}{n}= 1$  


***Определение предела числовой последовательности***  
- Число $A$ называется пределом $\{x_{n}\}$ $\Leftrightarrow (\forall \epsilon > 0, \exists N_{\epsilon} : \forall n > N_{\epsilon}  \Rightarrow |x_{n} - A| < \epsilon)$  

***Упражнение***  
- С помощью определения докажем (1) из примера. (Т. е. найдем $N_{\epsilon}$, что $\forall n > N_{\epsilon} \Rightarrow |x_{n} - A| < \epsilon)$. Т. к. $ \lim{n}{\infty} \dfrac{1}{n} = 0 \Rightarrow (\forall \epsilon > 0, \exists N_{\epsilon} : \forall n > N_{\epsilon})  \Rightarrow |x_{n} - 0| < \epsilon \Rightarrow |\dfrac{1}{n}| < \epsilon \Rightarrow \dfrac{1}{n} < \epsilon \Rightarrow n > \dfrac{1}{\epsilon}$  
- С помощью определения докажем (2) из примера. (Т. е. найдем $N_{\epsilon}$, что $\forall n > N_{\epsilon} \Rightarrow |x_{n} - A| < \epsilon)$. Т. к. $ \lim{n}{\infty} \dfrac{1}{n} = 0 \Rightarrow (\forall \epsilon > 0, \exists N_{\epsilon} : \forall n > N_{\epsilon})  \Rightarrow |x_{n} - 0| < \epsilon \Rightarrow |\dfrac{n - 1}{n} - 1| < \epsilon \Rightarrow \dfrac{1}{n} < \epsilon \Rightarrow n > \dfrac{1}{\epsilon}$  

### Свойства пределов  

***Теорема***  

**Последовательность, имеющая предел, называется сходящейся, иначе расходящейся.**  

- Всякая сходящаяся последовательность имеет единственный предел.  
	- Доказательство:  
		- Пусть $  \lim{n}{\infty} x_{n} = A$. Докажем единственность от противного. Предположим, что $\exists   \lim{n}{\infty} x_{n} = B$ и $A > B$. Т. к. , $  \lim{n}{\infty} x_{n} = A \Rightarrow  (\forall \epsilon_{1} > 0, \exists N_{\epsilon_{1} } : \forall n > N_{\epsilon_{1} }  \Rightarrow |x_{n} - A| < \epsilon_{1})$. В качестве $\epsilon_{1}$ возьмем $\dfrac{A - B}{2} \Rightarrow$  
	  
		1. $ -\dfrac{A - B}{2} < x_{n} - A < \dfrac{A - B}{2} $  
		2. $-\dfrac{A - B}{2} + A< x_{n}  < \dfrac{A - B}{2} + A$  
		3. $\dfrac{A + B}{2} < x_{n}  < \dfrac{3A - B}{2} $.  
	  
	- Т. к. $ \lim{n}{\infty} x_{n} = B \Rightarrow  (\forall \epsilon_{2} > 0, \exists N_{\epsilon_{2} } : \forall n > N_{\epsilon_{2} }  \Rightarrow |x_{n} - B| < \epsilon_{2})$. В качестве $\epsilon_{2}$ возьмем $\dfrac{A - B}{2}. $Возьмем $n > \max(N_{\epsilon_{1}}, N_{\epsilon_{2}}) \Rightarrow |x_{n} - B| < \dfrac{A - B}{2} \Rightarrow$  
		1. $-\dfrac{A - B}{2} < x_{n} - B < \dfrac{A - B}{2}$  
		2. $-\dfrac{A - B}{2} + B< x_{n}  < \dfrac{A - B}{2} + B$  
		3. $\dfrac{3B - A}{2} < x_{n}  < \dfrac{A + B}{2} $.  
	- Получим $\dfrac{A + B}{2} > x_{n} > \dfrac{A + B}{2}$. Противоречие.  

***Теорема***  

- Сходящаяся последовательность ограничена  
	- Доказательство: $\{x_{n}\}$ - сход. , $\Rightarrow (\forall \epsilon > 0, \exists N_{\epsilon}: \forall n > N_{\epsilon} \Rightarrow |x_{n} - A| < \epsilon)$. Это было бы доказательством ограниченности, если бы было верно для всех $n > 0$. Но до $N_{\epsilon}$ - конечное число членов. Если взять $M = \max(|x_{1}|, |x_{2}|, |x_{3}|, \dots, |x_{N_{\epsilon} - 1}|, A - \epsilon, A + \epsilon )$, то $\forall n: |x_{n}| \leq M $  

***Теорема***  

- $\{x_{n}\}$ - б. м. $\Rightarrow \forall k :\{ k x_{n}\}$ - б. м.  

	- Доказательство:   
		- Действительно : т. к. $(\forall \epsilon > 0, \exists N_{\epsilon}: \forall n > N_{\epsilon} \Rightarrow |x_{n}  - 0| < \epsilon)$ . Возьмем $\epsilon = \dfrac{\epsilon}{|k|} \Rightarrow |x_{n}| < \dfrac{\epsilon}{|k|} \Rightarrow |k \cdot x_{n}| < |k| \dfrac{\epsilon}{|k|} = \epsilon \Rightarrow \lim{n}{\infty} k x_{n} = 0$  

***Следствие***  

Если последовательность состоит из одного и того же члена $x_{n} = \{C, C, C, C,  \dots \}$, то $ \lim{n}{\infty} x_{n} = C$.  

***Свойства пределов, выражаемые неравенствами***  

- $(\forall n > N: x_{n} \geq y_{n}) \wedge ( \lim{n}{\infty} x_{n} = A,  \lim{n}{\infty} y_{n} = B) \Rightarrow A > B$  
	- Доказательство:   
		- В качестве $\epsilon$ возьмем $\dfrac{A - B}{2}$. $\forall n > N_{\epsilon_{1}}, N_{\epsilon_{1}} \Rightarrow |x_{n} - A| < \dfrac{A - B}{2} \Rightarrow -\dfrac{A - B}{2} < x_{n} - A < \dfrac{A - B}{2} \Rightarrow   -\dfrac{A - B}{2} + A < x_{n}  < \dfrac{A - B}{2} + A \Rightarrow  \dfrac{3A - B}{2} < x_{n}  < \dfrac{A + B}{2} $  
		- $\forall n > N_{\epsilon_{2}} : |y_{n} - B| < \dfrac{B - A}{2} \Rightarrow \dfrac{B - A}{2} < y_{n} < \dfrac{3B - A}{2}$  
		- Получим $x_{n} < \dfrac{A + B}{2} < y_{n}$. Противоречие.  
- $(x_{n} \leq y_{n} \leq z_{n}) \wedge (\forall n > N : \lim{n}{\infty}{x_{n}} = \lim{n}{\infty}{z_{n}}) \Rightarrow \{y_{n}\}$ - сходится, причем $\lim{n}{\infty}{x_{n}} = \lim{n}{\infty}{y_{n}} = \lim{n}{\infty}{z_{n}}$   
	- Доказательство :   
		- Действительно :  
		- $(\forall \epsilon > 0, \exists n > N_{1} : |x_{n} - A| < \epsilon)$  
		- $(\forall \epsilon > 0, \exists n > N_{2} : |z_{n} - A| < \epsilon)$  
		- $N = \max(N_{1}, N_{2}) \Rightarrow  |x_{n} - A| < |y_{n} - A| < |z_{n} - A| \Rightarrow |y_{n} - A| < \epsilon \Rightarrow \lim{n}{\infty}{y_{n}} = A$  

***Арифметические свойства пределов сходящихся  последовательностей***  

1. $\lim{n}{\infty} x_{n} = A; \lim{n}{\infty}  y_{n} = B \Rightarrow  \lim{n}{\infty} (x_{n} + y_{n}) = A + B$  
3. $ \lim{n}{\infty} x_{n}y_{n} = AB$  
4. $ \lim{n}{\infty} \dfrac{x_{n}}{y_{n}} = \dfrac{A}{B}$  
- Докажем $(1)$  
  1. Т. к. $\lim{n}{\infty}{x_{n}} = A$, то $(\forall \epsilon > 0, \epsilon = \dfrac{\epsilon}{2}, \forall n > N_{1} : |x_{n} - A| < \dfrac{\epsilon}{2})$  
  2. Т. к. $\lim{n}{\infty}{x_{n}} = B$, то $(\forall \epsilon > 0, \epsilon = \dfrac{\epsilon}{2}, \forall n > N_{2} : |x_{n} - B| < \dfrac{\epsilon}{2})$  
  3. Возьмем $N = \max(N_{1}, N_{2})$, тогда: $\forall n > N : |x_{n} + y_{n} - A - B| \leq |x_{n} - A| + |y_{n} - B| < \dfrac{\epsilon}{2} +  \dfrac{\epsilon}{2} = \epsilon \Rightarrow \lim{n}{\infty} (x_{n} + y_{n}) = A + B$  
- Докажем $(2)$   
  1. Т. к. $ \lim{n}{\infty} x_{n} = A$, то $(\forall \epsilon > 0, \forall n > N_{1} : |x_{n} - A| < \epsilon)$  
  2. Т. к. $ \lim{n}{\infty} x_{n} = B$, то $(\forall \epsilon > 0,  \forall n > N_{2} : |x_{n} - B| < \epsilon)$  
  3. Возьмем $N = \max(N_{1}, N_{2})$, тогда $\forall n > N : |x_{n}y_{n} - A B| = |(x_{n} - A + A)(y_{n} - B + B) - AB| \leq |x_{n}y_{n} - AB| + \dots  \implies  \lim{n}{\infty} (x_{n}y_{n}) = AB$  

## Лекция 21.09.2022  

### Подпоследовательность  

***Определение подпоследовательности***  

- Пусть задана $\{x_{n}\}$. Возьмем $N_{1}, N_{2} > N_{1}, N_{3} > N_{2}, \dots, N_{k} > N_{k - 1}, \dots $. Получим подпоследовательность $\{x_{n_{k}}\}$.  

***Утверждение***  

 - $ \lim{n}{\infty} x_{n} = a \implies$ любая подпоследовательность $x_{n_{k}}$ тоже сходится, причем к тому же пределу.  
	- Доказательство: Действительно: $ \lim{n}{\infty} x_{n} = a \implies (\forall \epsilon > 0, \exists N_{\epsilon} : \forall n > N_{\epsilon} \implies |x_{n} - a| < \epsilon)$. Т.к при $N_{k} > N_{\epsilon}$ члены подпоследовательности входят в число членов $\{x_{n}\} \implies |x_{n_{k}} - a| < \epsilon $  

***Пример***  
1. $x_{n} = \dfrac{1 + (1)^{n}}{2}$  
	- $\{x_{2k}\} \rightarrow 1$  
	- $\{ x_{2k + 1} \} \rightarrow 0$  
2. $\{x_{n}\} = 1 + \sin{\dfrac{\pi n}{2}}$  
	- $\{x_{2k}\} = (1 + \sin{\pi k}) \rightarrow 1$  
	- $\{x_{4k + 1}\} = (1 + \sin{\dfrac{\pi}{2}}) \rightarrow 2$  
	- $\{x_{4k + 3}\} = (1 + \sin{\dfrac{3 \pi}{2}}) \rightarrow 0$  
3. $x_{n} = n^{(-1)^{n}}$  
	- $\{x_{2k}\} \rightarrow \infty$  
	- $\{x_{2k + 1}\} \rightarrow 0$  

***Определение предельной точки последовательности***  

- $X_{0}$ называется предельной точкой $\{x_{n}\}$, если в любой сколь угодно малой окрестности точки содержится бесконечное число членов $\{x_{n}\}$.  

### Теорема о сходящейся подпоследовательности  
- Если $\{x_{n}\}$ имеет предельную точку, то в ней содержится сходящаяся подпоследовательность, которая имеет своим пределом эту точку.  
	- Доказательство: Действительно:   
		- Так как в $\{x_{n}\}$ имеется предельная точка $a$, то $\forall \epsilon > 0$ в $\epsilon$ - окрестности точки $a$ содержится бесконечное число членов $\{x_{n}\}$. Возьмем $\epsilon_{1} = 1$ в окрестности точки $a$, возьмем $\overline{X_{1}}$ в этой окрестности. Далее возьмем $\epsilon_{2} = \dfrac{1}{2}$ и точку $\overline{X_{2}}$ из $\epsilon_{2}$ - окрестности и т. д.  Для $\epsilon_{n} = \dfrac{1}{n}$ возьмем $\overline{X_{n}}$ из $\epsilon_{n}$ - окрестности. Получим $\{\overline{x_{n}}\}$.  
		- Докажем, что $ \lim{n}{\infty} \overline{x_{n}} = a$. $\forall \epsilon > 0$ посмотрим номера $\overline{x_{n}}$ , которые вошли в окрестность размера $\dfrac{1}{n}$, где $\dfrac{1}{n} < \epsilon$. Т. к. в нее вошла точка $x_{n}$, то в нее войдут и все дальнейшие $\overline{x_{n'}}$. Т. к. они все входят в меньшие окрестности. ч. т. д.  

### Теорема Больцано - Вейерштрасса  
- Во всякой ограниченной последовательности содержится сходящаяся  подпоследовательность.  
	- Докажем, что у ограниченной последовательности существует предельная точка  
		1. Пусть имеется $\{x_{n}\}$ -  ограниченная $\implies \exists m, M : m \leq x_{n} \leq M$.  
		2. Рассмотрим $\{X\}$, состоящее из чисел $x$, таких, что на числовой прямой они правее любой точки $x_{n} \in\{X_{n}\}$. Такое множество не пусто, т. к. по крайней мере в нем содержится $M$.  
		3. $\{X\}$ - ограничено снизу числом, меньшим или равным $m \implies \exists  \overline{x} = inf{x}$  
		4. Докажем, что $\overline{x}$ - предельная точка $\{x_{n}\}$. $\overline{x} = inf{X} \implies (\forall x \in X: x \geq m) \wedge (\forall \epsilon > 0, \exists x' \in X : x' < \overline{x} + \epsilon) \implies $ левее $\overline{x} + \epsilon$ и правее  $\overline{x} - \epsilon$ содержится $\infty$ членов последовательности. Т. е. в $\epsilon$ - окрестности числа $\overline{x}$ содержится также $\infty$ членов. $\implies$ это и есть предельная точка. ч. т. д.  

### Критерий Коши сходимости последовательности  

***Определение фундаментальной последовательности***  

- $x_{n} $ - фундаментальная $\Longleftrightarrow$ $(\forall \epsilon > 0, \exists N_{\epsilon}, \forall n > N_{\epsilon}) \wedge (\forall p \in \NN : |x_{n + p} - x_{n}| < \epsilon)$.  

***Теорема***  
- Последовательность $\{x_{n}\}$ сходится $\implies$ она фундаментальная.  
	- Необходимость $(\implies)$: $\{x_{n}\}$ - сходится. Доказать : $\{x_{n}\}$ - фундаментальная. Доказательство: $ \lim{n}{\infty} \{x_{n}\} = a$. Рассмотрим $|x_{n + p} - x_{n}|$. $|x_{n + p} - x_{n}| = |x_{n + p} - x_{n} - a + a| = |x_{n + p} - a - (x_{n} - a)| \leq \underbrace{|x_{n + p} - a|}_{\leq \dfrac{\epsilon}{2}} + \underbrace{|x_{n} - a|}_{\leq \dfrac{\epsilon}{2}} < \eps$  
	- Достаточность $(\Longleftarrow)$ : $\{x_{n}\}$ - фундаментальная. Докажем, что $\{x_{n}\}$ - сходится. Доказательство:  
		- $(\forall \epsilon > 0, \exists N_{\epsilon}, \forall n > N_{\epsilon}) \wedge (\forall p \in \NN : |x_{n + p} - x_{n}| < \epsilon)$. Перепишем в виде $-\eps < x_{n + p} - x_{n} < \eps$ (начиная с некоторого номера). До этого промежутка лишь конечное число членов $\implies$ $\{x_{n}\}$ - ограничена, тогда по Т. Больцано - Вейерштрасса в $\{x_{n}\}$ существует $\{x_{n_{k}}\}$. $\lim{n}{\infty}{x_{n_{k}}} = a$.  
		- Докажем, что $\lim{n}{\infty}{x_{n_{k}}} = a$. Рассмотрим $|x_{n} - a| = |x_{n} - x_{n_{k}} + x_{n_{k}} - a| = |x_{n} - x_{n_{k}}| + |x_{n_{k}} - a|$. Возьмем $N_{k}: (|x_{n_{k}} - a| < \dfrac{\eps}{2}, |x_{n} - x_{n_{k}}| < \dfrac{\eps}{2})$. Получим $|x_{n} - a| = |x_{n} - x_{n_{k}} + x_{n_{k}} - a| = \underbrace{|x_{n} - x_{n_{k}}|}_{< \dfrac{\eps}{2}} + \underbrace{|x_{n_{k}} - a|}_{\dfrac{\eps}{2}} < \eps$  

***Пример***  
- $\{x_{n}\} = 1 + \dfrac{1}{2} + \dfrac{1}{3} + \dots + \dfrac{1}{n}$.  
	- Докажем с помощью критерия Коши, что $x_{n}$ - расходится. Т. е. $(\exists \epsilon_{0} > 0, \forall N_{\epsilon}, \exists n > N_{\epsilon}) \wedge (\exists p \in \NN : |x_{n + p} - x_{n}| < \epsilon_{0})$. Оценим : $|x_{n + p} - x_{n}| = |1 + \dfrac{1}{2} + \dfrac{1}{3} + \dots + \dfrac{1}{n} + \dfrac{1}{n + 1} \dots \dfrac{1}{n + p} - (1 + \dfrac{1}{2} + \dfrac{1}{3} + \dots + \dfrac{1}{n})| = |\dfrac{1}{n + 1} + \dfrac{1}{n + 2} + \dots + \dfrac{1}{n + p}| \geq \dfrac{p}{n + p}$ Возьмем $p=n \implies \dfrac{p}{n + p} = \dfrac{n}{2n} = \dfrac{1}{2} = \epsilon_{0} \implies \{x_{n}\}$ - расходится. ч. т. д.  
- $\{x_{n}\} = \dfrac{\cos{x}}{1^{2}} + \dfrac{\cos{2x}}{2^{2}} + \dots + \dfrac{\cos{nx}}{n^{2}}$.  
	- Докажем сходимость $\{x_{n}\}$.  
		- Рассмотрим $|x_{n + p} - x_{n}| = |\dfrac{\cos(n + 1)x}{(n + 1)^{2}} + \dfrac{\cos(n + 2)x}{(n + 2)^{2}} + \dots + \dfrac{\cos(n + p)x}{(n + p)^{2}}| < \dfrac{p}{(n + 1)^2} < \epsilon$  

## Лекция 28.09.2022  

### Понятие функции на числовом множесте  
- Пусть на числовом множестве $X$ каждому числу $x \in X$ по какому - либо закону поставлено в соответствие число $y \in Y$. Тогда на $X$ задана функция $y = f(x)$.  
	- $f$ - характеристика функции  
	- $x$ - аргумент  
	- $y$ - значение  
	- $X$ - область определения $f$  
	- $Y$ - область значений $f$  
- Примеры:   
	- Функция Дирихле  $f(x) = \begin{equation*}  
	  \begin{cases}  
	   0, x \in \RR \backslash \QQ \\  
	   1, x \in \QQ  
	  \end{cases}  
	  \end{equation*}$  
	- $y = x^{2}$  
		- $x \in (-\infty; +\infty), y \in [0; +\infty)$  
	- $y = \sqrt{1 - x^{2}}$  
	- $y = sgn(x) = \begin{equation*}  
	   \begin{cases}  
	    1, x > 0 \\  
	    0, x = 0 \\  
	    -1, x < 0  
	   \end{cases}  
	  \end{equation*}$  
	- $f(x) = [x]$ (целая часть, не превосходящая x)  
	- $f(x) = x - [x]$  

### Ограниченные и неограниченные функции  
- Функция называется ограниченной на $[a;b] \Longleftrightarrow (\forall x \in [a;b], \exists m, M : m \leq f(x) \leq M)$.  

### Монотонные функции  
- Функция называется неубывающей на $[a;b] \Longleftrightarrow (\forall x_{1}, x_{2} \in [a;b] : x_{2} > x_{1} \implies f(x_{2}) \geq f(x_{1}))$.  
- Функция называется невозрастающей на $[a;b] \Longleftrightarrow (\forall x_{1}, x_{2} \in [a;b] : x_{2} > x_{1} \implies f(x_{2}) \leq f(x_{1}))$.  

### Предел функции в точке по Коши  
- $A = \lim{x}{x_{0}} f(x) \Longleftrightarrow (\forall \epsilon > 0, \exists \delta > 0: \forall x \in X: 0 < |x - x_{0}| < \delta \implies |f(x) - A| < \epsilon)$.  

### Предел функции в точке по Гейне  
- $A = \lim{x}{x_{0}} f(x) \Longleftrightarrow (\forall \{x_{1}, x_{2}, \dots, x_{n}, \dots\} \in X: \lim{n}{\infty} x_{n} = x_{0} \implies \lim{n}{\infty} f(x_{n}) = A)$.  

### Доказательство эквивалентности определения предела по Коши и Гейне  
- $(К \implies Г)$  
	- $\forall \epsilon > 0, \exists \delta > 0: \forall x \in X: 0 < |x - x_{0}| < \delta \implies |f(x) - A| < \epsilon$. Возьмем произвольную $\{x_{1}, x_{2}, \dots, x_{n}, \dots\} \in X, x_{n} \neq x_{0}, \lim{n}{\infty} = x_{0}$, то есть $\forall \delta, \exists N_{\epsilon}: \forall n > N_{\epsilon} \implies |x_{n} - x_{0}| < \delta$. Что есть в определении по Коши: $0 < |x - x_{0}| < \delta \implies |f(x) - A| < \epsilon$. Получим определение сходимости $f(x_{n})$, т.к. $x_{n}$ - произвольная.  
 - $(Г \implies К)$  
	- $A = \lim{x}{x_{0}} f(x) \Longleftrightarrow (\forall \{x_{n}\} : x_{n} \in X, x_{n} \neq x_{0} \implies \lim{n}{\infty} x_{n} = x_{0}, \{f(x_{0}), f(x_{1}), \dots, f(x_{n}), \dots\} \implies \lim{n}{\infty} f(x_{n}) = A)$ . Докажем от противного: Пусть $Г \;\not\!\!\!\implies К$. Тогда $\exists \epsilon_{0} \forall \delta > 0, \exists x \in X: 0 < |x - x_{0}| < \delta \implies |f(x) - A| \geq \epsilon_{0}$. Пусть $\delta_{1} = 1$, тогда $\forall \delta > 0$ найдется $x_{1}$ из $\delta$ - окрестности точки $x_{0}$, такое, что $|f(x_{1}) - A| \geq \epsilon_{0}$. Пусть $\delta_{2} = \dfrac{1}{2}$, тогда $\forall \delta > 0$ найдется $x_{2}$ из $\delta$ - окрестности точки $x_{0}$, такое, что $|f(x_{2}) - A| \geq \epsilon_{0}$. И так далее  $\delta_{n} = \dfrac{1}{n}$, тогда $\forall \delta > 0$ найдется $x_{n}$ из $\delta$ - окрестности точки $x_{0}$, такое, что $|f(x_{n}) - A| \geq \epsilon_{0}$. Получим: $\{x_{1}, x_{2}, \dots, x_{n}, \dots\} \rightarrow x_{0}, \{f(x_{1}),f(x_{2}), \dots, f(x_{n)}, \dots\} \;\not\rightarrow A$  

### Примеры доказательств, используя $\eps - \delta$  
- $y = x^{3}$  
	- $\lim{x}{0} x^{3} = 0$  
	- $\forall \epsilon > 0, \exists \delta > 0: |x - 0| < \delta \implies |f(x) - 0| < \epsilon$  
	- $|x| < \delta \wedge |f(x)| < \epsilon$  
	- $|f(x)| < \epsilon$   
	- $|x^{3}| < \epsilon$  
	- $|x| < \delta \implies |x| < \sqrt[\uproot{3}p]{\epsilon} \implies \delta = \sqrt[\uproot{3}p]{\epsilon} \implies |f(x) - A| < \epsilon$  
- $f(x) = \sin{\dfrac{1}{x}}$  
	- Докажем, что в $x_{0} = 0$ функция не имеет предела.   
		- Возьмем $\dfrac{1}{x} = \pi k, x_{k} = \dfrac{1}{\pi k} \rightarrow 0 \implies f(x_{k}) = \sin{\pi k} \equiv 0 \implies \lim{n}{\infty} f(x_{n}) = 0$  
		- Возьмем $\dfrac{1}{x_{k}} = (\dfrac{\pi}{2} + 2\pi k), x_{k} = (\dfrac{2}{\pi + \pi k}) \implies \begin{equation*}  
	   \begin{cases}  
	    x_{k} \rightarrow 0 \\  
	    f(x_{k}) \equiv 1 \\  
	    \end{cases}  
	    \end{equation*} \implies \lim{k}{\infty} f(x_{k}) = 1$  

### Непрерывные и разрывные функции  
- $f$ - непрерывна в $x_{0} \Longleftrightarrow f(x_{0}) = \lim{x}{x_{0}} f(x)$   
- Функция, непрерывная в каждой точке $[a;b]$ называется непрерывной на $[a;b]$.  
	- $p(x) = a_{n}x^{n} + a_{n - 1}x^{n - 1} + \dots + a_{1}x_{1} + a_{0}$  
	- $x^{k}$ - непрерывна в любой $x_{0}$.  
	- Возьмем алгебраическую дробь $\dfrac{P(x)}{Q(x)}$  
	- По свойству пределов $\lim{x}{x_{0}} \dfrac{P(x)}{Q(x)} = \dfrac{\lim{x}{x_{0}}P(x)}{\lim{x}{x_{0}} Q(x)} $, кроме точек, в которых знаменатель равен $0$.  
- Пример:  
	- Доказать непрерывность $y = \cos{x}$ в любой токе числовой оси.  
	- Возьмем $x_{0}$, докажем, что $\exists \lim{x}{x_{0}} \cos{x} = \cos{x_{0}}$.  
	- Доказательство по Коши: $\forall \epsilon > 0: |\cos{x} - \cos{x_{0}| = |2 \sin{\dfrac{x - x_{0}}{2}}} \sin{\dfrac{x + x_{0}}{2} }| \leq 2|\sin{\dfrac{x - x_{0}}{2} }| \leq 2 \dfrac{|x - x_{0}|}{2}$. При $|x - x_{0}| < \delta, |cos{x} - cos{x_{0}}| < \epsilon \implies \delta = \epsilon$  

## Лекция 06.10.2022  

### Непрерывность сложной функции  

***Определение сложной функции (композиции)***  

- $y = f(x), x = \phi(t)$  
	- $f(\phi(t)) = \digamma(t)$  

***Теорема о непрерывности сложной функции***  
- $f$ - определена в окрестности $x = a$, $f$ - непрерывна в $a$, $x$ - функция независимой переменной $t, x = \phi(t)$, $\phi$ - непрерывна в $\alpha$, $\Longleftrightarrow f(\phi(t))$ - непрерывна в $t = \alpha$   

***Доказательство***  

- $\digamma(t)$ - непрерывна в $t = \alpha \Longleftrightarrow \exists \lim{t}{\alpha} \digamma(t) = \digamma(\alpha)$. Так как $x = \phi(t)$ - непрерывна по условию теоремы $\implies \forall \{t_{n}\} : \lim{n}{\infty} t_{n} = \alpha, \{\phi(t_{n})\} \xrightarrow[n \to \infty]{} \phi(\alpha) = a$. При этом : $\lim{n}{\infty} f(x_{n}) = f(a)$ в силу непрерывности $f$. $(\digamma(t) = f(\phi(t))) \wedge \{\digamma(t_{n})\} = \{f(\phi(t_{n}))\} \xrightarrow[n \to \infty]{} f(\phi(\alpha)) = f(a) = \digamma(\alpha)$  

### Односторонние пределы  
- $\lim{x}{a + 0} f(x) = b \Longleftrightarrow \forall \eps > 0, \exists \delta > 0, \forall x \in X: a < x < a + \delta \implies |f(x) - b| < \eps$  
- $\lim{x}{a - 0} f(x) = b \Longleftrightarrow \forall \eps > 0, \exists \delta > 0, \forall x \in X: a - \delta< x  < a \implies |f(x) - b| < \eps$  

### Классификация точек разрыва  
- Устранимая точка разрыва  
	-  Существует конечные пределы этой функции слева и справа, они равны  
- Точка разрыва 1 - ого рода  
	- Существуют конечные пределы слева и справа в точке, но они не равны друг другу  
- Точка разрыва 2 - ого рода  
	- Все остальные точки  

***Примеры***  

- $\lim{x}{1} \dfrac{x^{2} - x - 2}{x^{2} + x - 3} = \dfrac{0}{0}$. Рассмотрим выколотую окрестность $\mathring{U}(1)$. $f(x) = \dfrac{x + 2}{x + 3} \implies \lim{x}{\to 1} f(x) = \dfrac{3}{4}$, $x = 1$ - Устранимая точка разрыва  
- $f(x) = \dfrac{1}{1 + 2^{\dfrac{1}{x}}}$. $f$ - не определена в $x = 0$.  
	- $\lim{x}{0 + 0} f(x) = 0$  
	- $\lim{x}{0 - 0} f(x) = 1$  
	- $\lim{x}{\infty} f(x) = \dfrac{1}{2}$  
	Имеем точку разрыва 1 ого рода  
- $f(x) = \dfrac{1}{x}$. В $x = 0$, $f$ - не определена. $0$ - точка разрыва 2ого рода.  
- $f(x) = \sin(\dfrac{1}{x})$. В $x = 0$ ,$f$ - не определена. Но определена в $\mathring{U}(0)$.  
$\lim{x}{0} f(x)=$ ?  
- Докажем, что предела в $x = 0$ не существует.  
	- Действительно :   
	- $x_{n} = \dfrac{1}{\pi n};\{x_{n}\} \xrightarrow[n \to \infty]{} 0; \lim{n}{\infty} f(x_{n}) = \lim{n}{\infty} \sin{(\pi n)} \equiv 0 \implies \lim{n}{\infty} f(x_{n}) = 0$  
	- $x_{n} = \dfrac{2}{\pi(4n + 1)}; \{x_{n}\} \xrightarrow[n \to \infty]{} 0; f(x_{n}) = \sin{(\dfrac{\pi}{2} (4n + 1))} = \sin{(\dfrac{\pi}{2})} \equiv 1 \implies \lim{n}{\infty} f(x_{n}) = 1$  
	- Получим, $f(x)$ - не существует в $x = 0$  

### Замечательные пределы  
1. $\lim{x}{0} \dfrac{\sin{(x)}}{x} = 1$ (первый замечательный предел)  
2. $\lim{n}{\infty} (1 + \dfrac{1}{n})^{n} = e$ (второй замечательный предел)  
3. $\lim{x}{\infty} (1 + \dfrac{1}{x})^{x} = e$ ($x$ - произвольное)  
4. $\lim{t}{0} (1 + t)^{\dfrac{1}{t}} = e$ $(x = \dfrac{1}{t})$  
5. $\lim{t}{0} \ln{(1 + t)}^{\dfrac{1}{t}} = \ln{(e)} = 1 \implies \lim{t}{0} \dfrac{ln{(1 + t)}}{t} = 1$  
6. $\lim{x}{0}  \dfrac{1 - \cos{x} }{x^{2} } = \ \lim{x}{0}\ \dfrac{2\sin^{2}{(\dfrac{x}{2})}}{x^{2} } = \ \lim{x}{0} \dfrac{\dfrac{1}{2}\sin{(\dfrac{x}{2}) \sin{(\dfrac{x}{2}) } }}{\dfrac{1}{2}\dfrac{x^{2}}{2} } = \  \lim{x}{0}\ \dfrac{1}{2} \underbrace{\dfrac{\sin{(\dfrac{x}{2}) \sin{(\dfrac{x}{2}) } }}{\dfrac{x}{2} \dfrac{x}{2}}}_{1} = \dfrac{1}{2}$  
7. $\lim{x}{0} \dfrac{\sqrt[n]{1 \ + \ x} \ - \ 1}{x} = \ \lim{x}{0} \dfrac{(\sqrt[n]{1 \ + \ x} \ -\  1)((\sqrt[\leftroot{-15} \uproot{7} n - 1]{1 \ + \ x} \ - \  1)^{(n - 1)}) \ + \ (\sqrt[\leftroot{-15} \uproot{7} n - 2]{1 \ +\  x} \ -\  1)^{(n - 2)} \ + \ \dots \ + \ (\sqrt[n]{1 \ + \ x} \ - \  1)}{x (\sqrt[\leftroot{-15} \uproot{7} n -  1]{1 \  + \  x} - 1)^{(n \ - \  1)} \ + \ (\sqrt[\leftroot{-15} \uproot{7} n - 2]{1 \ + \ x}  \ - \ 1)^{(n \ -\  2)} \ + \ \dots \ + \ \sqrt[n]{1 \ + \ x} \ - \ 1)} = \ \lim{x}{0} \dfrac{1 \ + \ x \ - \  1}{x (\sqrt[\leftroot{-15} \uproot{7} n -  1]{1 \  + \  x} - 1)^{(n \ - \  1)} \ + \ (\sqrt[\leftroot{-15} \uproot{7} n - 2]{1 \ + \ x}  \ - \ 1)^{(n \ -\  2)} \ + \ \dots \ + \ \sqrt[n]{1 \ + \ x} \ - \ 1)} = \lim{x}{0} \dfrac{1}{1 \ + 1 \ + \ \dots + \ 1} = \ \dfrac{1}{n}$  

- Докажем $(1)$  
-  Рассмотрим $\lim{x}{ 0 + 0} \dfrac{\sin{(x)}}{x} \stackrel{\text{?}}{=} 1$  
	![image1](matan_pictures/matan1.jpg)  
	- $\sin{(\alpha)} = y(A)$  
	- $\cos{(\alpha)} = y(A)$  
	- $S_{OAA'} < S_{OAB'} < S_{OBB'}$  
	- $\dfrac{1}{2}\cos{(x)}\sin{(x)} < \dfrac{1}{2} \cdot 1 \cdot x < \dfrac{1}{2} \cdot 1 \cdot \tan{(x)}$  
	- $\cos{(x)}\sin{(x)} <  x < \tan{(x)}$  
	- $\cos{(x)} <  \dfrac{x}{\sin{(x)}} < \dfrac{1}{\cos{(x)}}$  
	- $\cos{(0)} \xrightarrow[n \to 0]{} 1 \implies \lim{x}{0 + 0} \dfrac{\sin{x}}{x} = 1$  
-  Рассмотрим $\lim{x}{ 0 - 0} \dfrac{\sin{(x)}}{x}$  
	- Так как $f(-x) = f(x) \implies \lim{x}{0 + 0} \dfrac{\sin{(x)}}{x} = \lim{x}{0 - 0} \dfrac{\sin(x)}{x} = \lim{x}{0} \dfrac{sin(x)}{x} = 1$  
- Докажем $(2)$  
- $\lim{n}{\infty} (1 + \dfrac{1}{n})^{n} = 1^{\infty}$  
- Докажем, что $\exists \lim{n}{\infty} f(x_{n})$. Воспользуемся Теоремой о возрастающей, ограниченной последовательности:  
	- Ограниченность : $2 < (1 + \dfrac{1}{n})^{n} = 1 + n \cdot \dfrac{1}{n} + \dfrac{n(n- 1)}{2!} \cdot \dfrac{1}{n^{2}} + \dots = 2 + \dfrac{1}{2!}(1 - \dfrac{1}{n}) + \dfrac{1}{3!}(1 - \dfrac{1}{n})(1 - \dfrac{2}{n}) \dots \leq 2 + \dfrac{1}{2!} + \dfrac{1}{3!} + \dots < 2 + \dfrac{1}{2} + \dfrac{1}{2^{2}} + \dots < 2 + \dfrac{0.5}{1 - 0.5} = 3$  
	- Возрастание: $x_{n + 1} = (1 + \dfrac{1}{n + 1})^{n + 1} = 1 + (n + 1) \cdot \dfrac{1}{n + 1} + \dfrac{n(n - 1)}{2!} - \dfrac{1}{(n + 1)^{2}} + \dots \implies x_{n + 1} > x_{n}$, так как каждое слагаемое уменьшается и число слагаемых $n + 1$  

***Определение эквивалентности функций в точке***  

- $\lim{x}{x_{0}} \dfrac{f(x)}{g(x)} = 1 \Longleftrightarrow f(x) \sim  g(x)$ ($f$ эквивалентна $g$ в $x_{0}$)  

### Эквивалентные бесконечно малые величины  
1. $\lim{x}{0} \dfrac{\sin(x)}{x} = 1 \Longleftrightarrow \sin{(x)} \sim x$  
2. $\lim{x}{0} \dfrac{\ln{(1 + x)}}{x} = 1 \Longleftrightarrow \ln{(1 + x)} \sim x$  
3. $\lim{x}{0} \dfrac{e^{x} - 1}{x} = 1 \Longleftrightarrow e^{x} \sim x$  
4. $\lim{x}{0} \dfrac{\sqrt[n]{(1 + x)} - 1}{x} = \dfrac{1}{n} \Longleftrightarrow \sqrt[n]{(1 + x)} \sim \dfrac{x}{n}$  

## Лекция 12.10.2022  
### Система стягивающихся отрезков  
- Пусть имеем бесконечный набор точек, начал $(a_{1}, a_{2}, \dots, a_{n}, \dots)$ и концов $(b_{1}, b_{2}, \dots, b_{n}, \dots)$ системы вложенных друг в друга отрезков. $a_{1} < a_{2} <  \dots < a_{n} < b_{n} < b_{n - 1} <  \dots < b_{1}$. Причем $\lim{n}{\infty} (b_{n} - a_{n}) = 0$.  

***Утверждение***  
- Система стягивающихся отрезков имеет общую точку и притом только одну.  

***Доказательство***  
- Единственность:  
	- Предположим, что существуют две общие точки $c < d$. Тогда $\forall \ (b_{n} - a_{n}) > d - c$, так как $\lim{n}{\infty} (b_{n} - a_{n}) = 0 \implies d = c$  
- Существование:  
	- Множество левых концов ограничено сверху $b_{n}$ и монотонно возрастает $\implies \exists \ \sup{(a_{n})}$. Аналогично $\exists \ inf(b_{n}) \implies \lim{n}{\infty} a_{n} = \lim{n}{\infty} b_{n} = c$  

### Верхний и нижний пределы последовательности  
- $\overline{\lim{n}{\infty}} a_{n} \Longleftrightarrow \max(\lim{n}{\infty} \{a_{n}\})$  
- $\underline{\lim{n}{\infty}} a_{n} \Longleftrightarrow \min(\lim{n}{\infty} \{a_{n}\})$  

***Пример***  

- $a_{n} = 1 + \cos{(\dfrac{\pi n}{3})}$  
	- $\{a_{3k}\} = 1 + (-1)^{k} \rightarrow (2 , 0)$   
	- $\{a_{3k + 1}\} \rightarrow (\dfrac{1}{2} , \dfrac{7}{6})$   
	- $\{a_{3k + 2}\} \rightarrow (\dfrac{1}{2} , \dfrac{3}{2})$   
	- $\implies \overline{\lim{n}{\infty}} a_{n} = 2, \ \underline{\lim{n}{\infty}} a_{n} = 0$  

### Раскрытие неопределенностей  
- $\lim{x}{x_{0}} (u(x)^{v(x)}); \lim{x}{x_{0}} u(x) = 1; \lim{x}{x_{0}} v(x) = \infty \implies \lim{x}{x_{0}} (u(x)^{v(x)}) = \lim{x}{x_{0}} ((u(x) - 1 + 1)^{v(x)}) = \lim{x}{x_{0}} [\underbrace{(1 + \underbrace{(u - 1)}_{0})^{\dfrac{1}{u - 1}}))}_{e}]^{(u - 1)v} = e^{(u - 1)v}$  

### Определение четности и нечетности функции  

- $f$ определена на симметричном относительно начала координат промежутке $x \in (-a; a)$  

- Четная:  
	- $f(-x) = f(x)$ (график симметричен относительно $Oy$)  
- Нечетная:  
	- $f(-x) = - f(x)$  
### Обзор основных элементарных функций  
- $f(x) = x^{n}$ (степенная функция). Пусть $n \in \NN$, тогда $f$ определена на всей числовой оси, монотонно возрастает при $x \geq 0$. При $n$ - нечетном монотонна на всей числовой оси, непрерывна в любой точке. $f(-x) = f(x)$ при $n$ - четном, $f(-x) = - f(x)$ при $n$ - нечетном.  
	- $f(x) = x$ (прямая линия). $f(-x) = - f(x)$  
	- $f(x) = x^{2}$ (квадратичная функция, график: парабола). $f(-x) = f(x)$  
	- $f(x) = x^{3}$ (кубическая функция, график: кубическая парабола). $f(-x) = f(x)$  
	- $n \in \ZZ, \ n < 0 \implies f(x) = x^{(-n)} = \dfrac{1}{x^{n}}$   
	- $n \in \QQ \implies f(x) = x^{(\dfrac{m}{n})}, \ m,n \in \NN. \ f(x) = \sqrt[n]{x^{m}}$   
- $f(x) = a^{x}, \ x \in (- \infty, \infty)$  
	- $a > 1 \implies f \uparrow$  
	- $a < 1 \implies f \downarrow$  

### Понятие обратной функции  
- Пусть $ \exists f: y = f(x), \ y \in [c; d] \ , x \in (a;b)$. Если каждому $x \in (a;b)$ соответствует $y \in [c; d]$, причем каждому $y \in [c; d]$ отвечает $x \in (a;b) \ : y = f(x)$. Тогда $x = f^{-1}(y)$, $y \in [c:d]$. $f^{-1}$ называется обратной функцией для $f$.  

***Свойства обратной функции***  
- $f(f^{-1}(y)) = y$  
- $f^{-1}(f(x)) = x$  
- График обратной функции симметричен к исходной относительно биссектрисы первой и третьей четверти координатных плоскостей  
- $y = a^{x}$, $x = \log_{a}(y)$ (логарифмическая функция, обратная к показательной)  
- $y = x^{n}$, $x = \sqrt[n]{y}$  (корень $n$ - ой степени, функция, обратная к степенной)  
- Обратная функция существует только на промежутке монотонности  

## Лекция 19.10.2022 

### Сравнение бесконечно малых функций

***Определение***
- $\alpha(x_{0})$ - бесконечно малая в окрестности точки $x_{0}$ $\Longleftrightarrow \exists \lim{x}{x_{0}} \alpha(x) = 0$

- Пусть две функции $\alpha(x), \beta(x)$ определены на одном и том же множестве и являются бесконечно малыми в окрестности $x_{0}$. Тогда $\lim{x}{x_{0}} \dfrac{\alpha(x)}{\beta(x)} = 0 \implies \alpha(x)$ - бесконечно малая более высокого порядка малости, по сравнению с $\beta(x)$ в окрестности $x_{0}$,  $\alpha(x) = o(\beta(x))$. Если в качестве функции сравнения $\beta(x)$ берется $(x - x_{0})^{m}$ и $\lim{x}{x_{0}} \dfrac{\alpha(x)}{ (x - x_{0})^{m} } = C  \neq 0 \implies \alpha(x)$ имеет в точке $x_{0}$ порядок малости $m$.

- Если $\alpha(x), \beta(x)$ - б. м. :
	- $\lim{x}{x_{0}} \dfrac{\alpha(x)}{\beta(x)} = 0 \implies \alpha(x) = o(\beta(x))$
	- $\lim{x}{x_{0}} \dfrac{\alpha(x)}{\beta(x)} = C \neq 0 \implies \alpha(x), \beta(x)$ - б. м. одинакового порядка малости
	- $\lim{x}{x_{0}} \dfrac{\alpha(x)}{\beta(x)} = 1 \implies \alpha(x) \sim \beta(x), x \rightarrow x_{0}$

***Примеры***

1.

-  $\alpha(x) = \dfrac{1}{3}x^{4} - 2x^{3} - x \  (x \rightarrow x_{0})$
- $\beta(x) = 2x^{4} + 3x^{2} + 2x \  (x \rightarrow x_{0})$
	- $\lim{x}{0} \dfrac{\alpha(x)}{\beta(x)} = - \dfrac{1}{2} \implies \alpha(x), \beta(x)$ - б. м. одинакового порядка малости

2.

-  $\alpha(x) = 1 - \cos{3x}$
- $\beta(x) = \sin{x}$
	- $\lim{x}{0} \dfrac{\alpha(x)}{\beta(x)} = 0 \implies \alpha(x) = o(\beta(x))$

3.

-  $\alpha(x) = 1 - \cos{3x}$
- $\beta(x) = x$
	- $\lim{x}{0} \dfrac{1 - \cos{3x}}{x} = \dfrac{9}{2}x \implies \alpha(x)$ имеет порядок малости $2$.

### Свойства бесконечно малых величин 
- Пусть :  $\alpha = o(\beta), \ \gamma = o(\beta)$, тогда : 
	- $o(\gamma) + o(\beta) = o(\beta)$
	- $o(\beta) \pm o(\beta) = o(\beta)$
	- $\alpha \cdot \gamma = o(\beta)$
	- $ f \sim C \cdot (x - x_{0})^{m},  x \rightarrow x_{0} \implies (x - x_{0})^{m}$ - главный член $f$, причем $m$ - порядок малости.

***Пример*** 

- $f(x) = x^{3} - 3x + 2$
	- $\lim{x}{1} f = 0 \implies f$ - б. м. в $x_{0} = 1$
	- Определим порядок малости и главный член $f$
	- $f(x) = (x - 1)^{2}(x - 2)$
	- $\lim{x}{1} \dfrac{f(x)}{C \cdot (x - 1)^{m}} = 1 \implies m = 2, \ C = 3 \implies$ главный член имеет вид : $3(x - 1)^{2} + o((x - 1)^{2})$

### Сравнение бесконечно больших функций

***Определение***

- $A(x)$ - б. б. справа в $x_{0}$ $\Longleftrightarrow \exists \lim{x}{x_{0}} A(x) = + \infty \Longleftrightarrow (\forall E > 0, \ \forall \{x_{n}\} \in X, \ \exists N_{E}: \ \forall n > N_{E} \implies A(x_{n}) > E, \ x_{n} > x_{0})$
- $A(x)$ - б. б. слева в $x_{0}$ $\Longleftrightarrow \exists \lim{x}{x_{0}} A(x) = + \infty \Longleftrightarrow (\forall E > 0, \ \forall \{x_{n}\} \in X, \ \exists N_{E}: \ \forall n > N_{E} \implies A(x_{n}) > E, \ x_{n} < x_{0})$

- Пусть две функции $A(x), B(x)$ определены на одном и том же множестве и являются бесконечно большими в окрестности $x_{0}$. Если в качестве функции сравнения $B(x)$ берется $(x - x_{0})^{m}$ и $\lim{x}{x_{0}} \dfrac{\alpha(x)}{ (x - x_{0})^{m} } = C  \neq 0 \implies \alpha(x)$ имеет в точке $x_{0}$ порядок роста $m$.

- Если $A(x), B(x)$ - б. б.  :
	- $\lim{x}{x_{0}} \dfrac{A(x)}{B(x)} = C \neq 0 \implies A(x), B(x)$ - б. б. одинакового порядка роста.

### Производная и дифференциал

***Определение***

- Возьмем $x \in X, \ y = f(x)$. Дадим числу $x$ приращение $\Delta x$. Пусть в $x$ $f$ имеет значение $f(x)$, тогда в $x + \Delta x$ она будет иметь значение $f(x + \Delta x)$. $\Delta y = \Delta f = f(x + \Delta x) - f(x)$ - приращение $f$, вызванное приращением $\Delta x$. Составим отношение $\dfrac{\Delta y}{\Delta x}$. Получим: $\lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x} = y'(x)$.

***Пример***

- $y = f(x) = x^{n}$
	- $\Delta y = \Delta f = (x + \Delta x)^{n} - x^{n}$
	- $\lim{\Delta x}{0} \left[ \dfrac{\Delta y}{\Delta x} = \dfrac{(x + \Delta x)^{n} - x^{n}}{\Delta x} = \dfrac{x^{n} + nx^{n - 1}\Delta x + \dfrac{n(n - 1)}{2}x^{n - 2}\Delta x^{2} + \dots + \Delta x^{n} - x^{n}}{\Delta x} = \dfrac{nx^{n - 1}\Delta x + \dfrac{n(n - 1)}{2}x^{n - 2}\Delta x^{2} + \dots + \Delta x^{n}}{\Delta x}\right] = nx^{n - 1}$

### Арифметические свойства производной
- Пусть $\exists f'(x), g'(x)$ в $x$. Тогда :
	1. $(f \pm g)' = f' \pm g'$ 
	2. $(Cf)' = Cf'$
	3. $(f \cdot g)' = f'g + fg'$
	4. $(\dfrac{f}{g})' = \dfrac{gf' - g'f}{g^{2}}, \ $ если $g(x) \neq 0$

- Докажем $(3)$:
	- $\Delta u = u(x + \Delta x) - u(x)$
	
	- $\Delta v = v(x + \Delta x) - v(x)$
	
	- $(uv)' = \lim {\Delta x}{0} \left[ \dfrac{\Delta (uv)}{\Delta x}  = \dfrac{u(x + \Delta x)v(x + \Delta x) - u(x)v(x)}{\Delta x} = \dfrac{u(x + \Delta x)v(x + \Delta x) - u(x)v(x + \Delta x) + u(x)v(x + \Delta x) - u(x)v(x)}{\Delta x} = \dfrac{u(x + \Delta x) - u(x)}{\Delta x}v(x + \Delta x) + \dfrac{v(x + \Delta x) - v(x)}{\Delta x}u(x)  \right] = u'v + uv'$

- Докажем $(5)$:
	- Докажем : $\left( \dfrac{1}{v} \right)' = - \dfrac{v'}{v^{2}}$
	
	- $\Delta \left( \dfrac{1}{v} \right) =  \dfrac{1}{v(x + \Delta x)} -  \dfrac{1}{v} = \dfrac{v(x) - v(x + \Delta x)}{v(x + \Delta x)v(x)} = - \dfrac{\Delta v}{v(x + \Delta x) v}$
	
	- $\left(\dfrac{1}{v}\right)' = - \lim{\Delta x}{0} \dfrac{\Delta v}{v(x + \Delta x) v} = - \dfrac{v'}{v^{2}}$
	
	- $\left(\dfrac{u}{v}\right)' = \left(u \cdot \dfrac{1}{v}\right)' = u' \cdot \dfrac{1}{v} + u \cdot \left( \dfrac{1}{v}\right)' = \dfrac{u'}{v} + u\left( - \dfrac{v'}{v^{2}}\right) = \dfrac{vu' - v'u}{v^{2}}$

***Примеры***

- $y = \sin{x}$
	- $\Delta y = \sin{(x + \Delta x)} - \sin{x} = 2 \sin{\dfrac{x + \Delta x - x}{2}} \cos{\dfrac{x + \Delta x + x}{2}} = 2\sin{\dfrac{\Delta x}{2}} \cos{(x + \dfrac{\Delta x}{2})} $
	- $(\sin{x})' = \lim{\Delta x}{0}\left[ \dfrac{2\sin{\dfrac{\Delta x}{2}}\cos{(x + \dfrac{\Delta x}{2})}}{\Delta x}\right] = \cos{x}$
- $y = \cos{x}$
	- $(\cos{x})' = (\sin{(\dfrac{\pi}{2} - x)})' = -\cos{(\dfrac{\pi}{2} - x)} = -\sin{x}$

### Производная сложной функции
- Пусть $y = f(x), \ \exists f'(x), \ x = \phi(t), \ \exists \phi'(t) = x' \implies y = f(\phi(t)) = \digamma(t) $
- $\lim{\Delta x}{0} \left[ \dfrac{\Delta y}{\Delta x} \cdot \dfrac{\Delta x}{\Delta t} \right] = f'(x) \cdot \phi'(t) = f(\phi(t))' = f'(\phi(t)) \cdot \phi'(t)$

***Пример***

- $f(x) = \sin{x}, \ x = 3t^{2}$
	- $\digamma(t) = \sin{(3t^{2})}$
	- $\digamma'(t) = \cos{(3t^{2})} \cdot 6t$

### Производная обратной функции
- $y = f(x), \ x = f^{-1}(y)$
	- $\lim{\Delta x}{0} \left[ \dfrac{\Delta y}{\Delta x} = \dfrac{1}{\dfrac{\Delta x}{\Delta y}} \right] = \dfrac{1}{(f^{-1}(y))'}  = \dfrac{1}{x'(y)}$ 

***Пример***

- $y = \arcsin{x}, \ x = \sin{y}$
	- $(\arcsin{x})' = \dfrac{1}{(\sin{y})'} = \dfrac{1}{\cos{y}} = \dfrac{1}{\sqrt{1 - \sin^{2}y}} = \dfrac{1}{\sqrt{1 - x^{2}}}$ 
## Семинар 13.09.2022  
***Разбор домашней работы***  
Доказать по индукции :   

- $1^3 + \dots + n^3 = (1 + \dots + n)^2$  
- $n = 1$ : $1^3 = 1^2$ - верно $\\$   
- $1^n + \dots n^3 = (1 + \dots + n) ^2$  
- $1^3 + \dots + n^3 + (n + 1)^3 = (\dfrac{(1 + n)n}{2})^2 + (n + 1)^3$  
- $1^3 + \dots + n^3 + (n + 1)^3 = (1 + \dots + n + (n + 1))^2$  

Доказать по индукции:  

- $\dfrac{1}{2} \cdot \dfrac{3}{4} \cdot \dfrac{2n - 1}{2n} < \dfrac{1}{\sqrt{2n + 1}}$   
- $\dfrac{1}{2} \cdot \dfrac{3}{4} \cdot \dfrac{2n - 1}{2n} < \dfrac{1}{\sqrt{2n + 1}}$  
- $\dfrac{1}{2} \cdot \dfrac{3}{4} \cdot \dfrac{2n - 1}{2n}  \cdot \dfrac{2n + 1}{2n + 2} < \dfrac{1}{\sqrt{2n + 3}}$  
- $ \dfrac{1}{\sqrt{2n + 3}}  \geq \dfrac{1}{\sqrt{2n + 2}} \cdot \dfrac{2n + 1}{\sqrt{2n + 2}}$  
- $ (\sqrt{2n + 3})^2  \geq (2n + 3) \dots $  

3. Начертить график. $y = arctg{\dfrac{1}{x}}$  

4. Начертить график $y = log_{3}{(2 - 3x)}$  

***Повтор определений с лекции***  

### Точная верхняя грань ограниченного сверху множества  
***Определение точной верхней грани***  

1. $M = \sup{X} $ - наименьшая из всех верхних граней  

2. $ (\forall x \in X : x \leq M) \wedge (\forall \epsilon > 0 \exists x' \in X: x' > M - \epsilon) \Rightarrow M = \sup{X}$  

3. $(\forall x \in X : x \leq  M) \wedge (\forall x < M \exists x' \in X : x' > x) \Rightarrow M = \sup{X} $  
### Точная нижняя грань ограниченного сверху множества  
1. $m = inf{X}$ - наибольшая из всех нижних граней $X$  
2. $(\forall x \in X: x \geq m ) \wedge (\forall \epsilon > 0, \exists x' \in X : x' < m + \epsilon) \Rightarrow m = inf{X})$  
3. $(\forall x \in X x \geq m) \wedge (\forall > m, \exists x' \in X: x' < x) \Rightarrow m = inf{X}$  

***Задачи на семинаре***  

1. Доказать, что $inf(-X) = - \sup{X}$. Доказательство: $(\forall x \in X: x \leq M) \wedge (\forall \epsilon > 0 : \exists x' \in X: x' > M - \epsilon ) \Rightarrow M =\sup{X}$. Рассмотрим множество ${-X}$. $(\forall (-x) : -x \geq -M = m) \wedge (\forall \epsilon > 0 : \exists -x' \in -X: -x' < \underbrace{-M}_{m} + \epsilon = m + \epsilon \Rightarrow m = -M)$  

2. Доказать, что $\sup{(X + Y)} = \sup{X} + \sup{Y}$  
    1. $ (\forall x \in X : x \leq M_{1}) \wedge (\forall \epsilon > 0 \exists x' \in X: x' > M_{1} - \dfrac{\epsilon}{2} \Rightarrow M_{1} = \sup{X}$  
    2. $ (\forall y \in X : y \leq M_{2}) \wedge (\forall \epsilon > 0 \exists y' \in X: y' > M_{2} - \dfrac{\epsilon}{2} \Rightarrow M_2 = \sup{Y}$  
    3. $ (\forall x + y \in X + Y : x + y \leq M_{1} + M_{2}) \wedge (\forall \epsilon > 0, \exists x' + y' \in X + Y: x' + y' > M_{1} +M_{2} - \epsilon \Rightarrow M_{1} + M_{2} = \sup{(X + Y)}$  

3. Доказать, что $\sup{(XY)} = \sup{X} \cdot \sup{Y}$  
    1. $ (\forall x \in X : x \leq M_{1}) \wedge (\forall \epsilon_{1} > 0 \exists x' \in X: x' > M_{1} - \epsilon_{1}) \Rightarrow M_{1} = \sup{X}$  
    2. $ (\forall y \in Y : y \leq M_{2}) \wedge (\forall \epsilon_{2} > 0 \exists y' \in Y: y' > M_{2} - \epsilon_{2}) \Rightarrow M_2 = \sup{Y}$  
    3. $ (\forall x \cdot y \in XY : xy \leq M_{1}M_{2}) \wedge (\forall \epsilon > 0 \exists x'y' \in XY: x'y' > (M_{1} - \epsilon_{1})(M_{2} - \epsilon_{2}) = M_{1}M_{2} - \underbrace{ M_{1}\epsilon_{2} - M_{2}\epsilon_{1} + \epsilon_{1}\epsilon_{2}}_{= \epsilon} \Rightarrow M_{1}M_{2} = \sup{XY}$  

## Семинар 20.09.2022  

***Задачи на семинаре из Демидовича***   

### 43  
- Доказать, что последовательность $x_{n} = \lg(\lg{n})$ имеет бесконечный предел при $n \rightarrow \infty$ (т.е. являются бесконечно большими), определив для всякого $E > 0$ число $N = N(E)$ такое, что $|x_{n}| > E$ при $n > N$  
	- Доказательство:  
		- $|\lg(\lg{n})| > E$  
		- $|10^{\lg(\lg{n})}| > 10 ^{E}$  
		- $|\lg| > 10^{E}$   
		- $n > 10^{{10}^{E}}$  
### 44   
- Показать, что $x_{n} = n^{(-1)^n}$ $n = (1, 2 , \dots)$ не ограничена, однако не является бесконечно большой при $n \rightarrow \infty$  
	- Последовательность не ограничена, так как ее члены чередуются: $a_{2k} > 1$,  $a_{2k + 1} \leq 1$  
	- У нее отсутствует предел, по той же причине, поэтому она не является бесконечно большой.  

***Вычислить пределы:***  

### 56  

- $ \lim{n}{\infty} \left [\dfrac{1}{1 \cdot 2} + \dfrac{1}{2 \cdot 3} + \dots + \dfrac{1}{n(n + 1)}  \right ] =  \lim{n}{\infty} \left [1 - \dfrac{1}{2} + \dfrac{1}{2}  - \dfrac{1}{ 3} + \dots + \dfrac{1}{n} - \dfrac{1}{n(n + 1)}  \right ] =  \lim{n}{\infty} \left [1- \dfrac{1}{n(n + 1)}  \right ] = 1 $  

***Доказать равенства:***  

### 58  
- $ \lim{n}{\infty} \left[\dfrac{n}{2^{n}} \right] = 0$  
	- Рассмотрим представление $2^{n} = (1 + 1)^{n} = 1 + n + \dfrac{n(n-1)}{2!} + \dots > \dfrac{n(n - 1)}{2}$  
	- $\dfrac{n}{2^{n}} < \dfrac{2n}{n(n - 1)} = \dfrac{2}{(n - 1)} \implies  \lim{n}{\infty} \left[\dfrac{n}{2^{n}} \right] = 0$  

### 60  
- $\lim{n}{\infty} \left[\dfrac{n^{k}}{a^{n}} \right] = 0$  
	- Рассмотрим представление $a = (1 + \alpha)^{n} = 1 + n\alpha + \dfrac{n(n-1)}{2!}\alpha + \dots  \dfrac{n(n - 1)}{2}\alpha^2 + \dots \dfrac{n(n - 1) \dots (n - k)}{(k + 1)!}$  
	- $\dfrac{n^{k}}{a^{n}} < \dfrac{n^{k}(k + 1)!}{n(n - 1)(n - 2) \dots (n - k) \cdot \alpha^{k + 1}} = \dfrac{1}{n} \cdot \dfrac{(k + 1)!}{(1 - \dfrac{1}{n})(1 - \dfrac{2}{n}) \dots (1 - \dfrac{k}{n}) \cdot \alpha^{k + 1}} \implies \lim{n}{\infty} \left[\dfrac{n^{k}}{a^{n}} \right] = 0$  

### 61  
- $\lim{n}{\infty} \left[\dfrac{a^{n}}{n!} \right] = 0$  
	- $\dfrac{a^{n}}{n!} = \dfrac{a \cdot a \cdot \dots \cdot a}{1 \cdot 2 \cdot 3 \cdot \dots \cdot n } = \dfrac{a \cdot a \cdot \dots \cdot a}{1 \cdot 2 \cdot 3 \cdot \dots \cdot n_{0}} \cdot \dfrac{a}{n_{0} + 1} \cdot  \dfrac{a}{n_{0} + 2} \cdot \dots \cdot  \dfrac{a}{n} = M  \dfrac{a}{n_{0} + 1} \cdot  \dfrac{a}{n_{0} + 2} \cdot \dots \cdot  \dfrac{a}{n} < M (\dfrac{a}{n_{0} + 1})^{n - n_{0}} \implies \lim{n}{\infty}  \left[\dfrac{a^{n}}{n!} \right] = 0$  

### 65  
- $\lim{n}{\infty} \left [\sqrt[n]{n} \right] = 1$  
	- $(\sqrt[n]{n})^{n} = (1 + \alpha_{n})^{n}$  
	- $n = (1 + \alpha_{n})^{n} = 1 + n\alpha_{n} + \dfrac{n(n-1)}{2}\alpha_{n}^{2} + \dots > \dfrac{n(n-1)}{2}\alpha_{n}^2$  
	- $n > \dfrac{n(n-1)}{2}\alpha_{n}^2$  
	- $1 > \dfrac{n - 1}{2}\alpha_{n}^2$   
	- $\alpha_{n}^2 < \dfrac{2}{n -1}$  
	- $\alpha_{n} < \dfrac{\sqrt{2}}{\sqrt{n - 1}} \rightarrow 0 \implies \lim{n}{\infty} \left [\sqrt[n]{n} \right] = 1$  

### 77  
- Пользуясь теоремой о существовании предела монотонной и ограниченной последовательности, доказать сходимость следующих последовательностей: $x_{n} = p_{0} + \dfrac{p_{1}}{10} + \dots +  \dfrac{p_{n}}{10^{n}} $ $(n = 1, 2, \dots)$, где $p_{i}(i = 0, 1, 2, \dots)$ - целые неотрицательные числа, не превышающие $9$, начиная с $p_{i}$.  
	- Последовательность возрастает и ограничена снизу и сверху. $\implies$ она сходится.  

### Задание 1  
- Сформулировать определение последовательности, неограниченной сверху  
	- $\forall  \ M  \ ,\exists \ N \in \NN \ ,  \forall n > N : x_{n} > M$  
### Задание 2  
- Верно ли: $(x_{n} + y_{n}) \rightarrow A \implies x_{n} \rightarrow B, y_{n} \rightarrow C$  
	- Нет, например, при : $x_{n} = n, y_{n} = -n$  

### Задание 3  
- Верно ли: $\{ kx_{n}\} \rightarrow A \implies \{x_{n}\} \rightarrow B$  
	- Верно, домножение последовательности на константу не влияет на сходимость. (см. лекция 2)  

## Семинар 27.09.2022  

### 80  
- Пользуясь теоремой о существовании предела монотонной и ограниченной последовательности, доказать сходимость следующих последовательностей:  
	- $x_{n} =(1 + \dfrac{1}{2})(1 + \dfrac{1}{4}) \dots  (1 + \dfrac{1}{2^{n}})$  
	1. Покажем, что $x_{n}$ - возрастает:  
	- $x_{n + 1} > x_{n}$  
	- $(1 + \dfrac{1}{2})(1 + \dfrac{1}{4}) \dots  (1 + \dfrac{1}{2^{n}})(1 + \dfrac{1}{2^{n + 1}}) < (1 + \dfrac{1}{2})(1 + \dfrac{1}{4}) \dots  (1 + \dfrac{1}{2^{n}})$  
	- $1 + \dfrac{1}{2^{n + 1}} > 1$  
	- $\dfrac{1}{2^{n + 1}} > 0 \implies $ $x_{n} \uparrow$  
	2. Ограничение снизу:   
	- Оценим: $(\underbrace{((1 + \dfrac{1}{2^{n}})^{2^{n}})}_{e})^{\dfrac{1}{2^{n}}} = e^{\dfrac{1}{2^{n}}} < e^{(\dfrac{1}{2} + \dfrac{1}{4} + \dots+ \dfrac{1}{2^{n}})} = e^{\dfrac{\dfrac{1}{2}}{1 - \dfrac{1}{2}}} = e$  

### 85   
- Пользуясь критерием Коши, доказать сходимость следующих последовательностей:  
	- $x_{n} = 1 + \dfrac{1}{2^{2}} + \dfrac{1}{3^{2}} + \dots + \dfrac{1}{n^{2}}$  
		- Критерий Коши: $x_{n} $ - фундаментальная $\Longleftrightarrow$ $(\forall \epsilon > 0, \exists N_{\epsilon}, \forall n > N_{\epsilon} \ , \forall p \in \NN : |x_{n + p} - x_{n}| < \epsilon)$  
	- Запишем последнюю часть определения и подставим туда частичную сумму:  
	- $|\dfrac{1}{(n + 1)^{2}} + \dfrac{1}{(n + 2)^{2}} + \dots + \dfrac{1}{(n + p)^{2}}| < |\dfrac{1}{n} - \dfrac{1}{n + 1} + \dots - \dfrac{1}{n + p - 1} + \dfrac{1}{n + p - 1} - \dfrac{1}{n + p}| = \dfrac{1}{n} - \dfrac{1}{n + p} < \eps$  
	- $\dfrac{1}{n} - \dfrac{1}{n + p} < \dfrac{1}{n} < \eps$  
	- $\dfrac{1}{n} < \eps$  
	- $n > \dfrac{1}{\eps}$  
	- $N_{\eps} = \lceil{\dfrac{1}{\eps}} \rceil$  
	- $\forall n > N_{\epsilon} \ , \forall p \in \NN : |x_{n + p} - x_{n}| < \epsilon$  

## Семинар 04.10.2022  
### 404  
- Сформулировать с помощью неравенств следующие утверждения и привести соответствующие примеры:  
	- $\lim{x}{-\infty} f(x) = b \Longleftrightarrow \forall \eps > 0 \ ,\exists E > 0, \ \forall x \in X : x < - E \implies |f(x) - b| < \eps$  

### 405  
- $\lim{x}{a - 0} f(x) = \infty \Longleftrightarrow \forall E > 0 \ ,\exists \delta > 0, \ \forall x \in X :  a - \delta < x < a \implies |f(x)| > E$  

### 407  
- $\lim{x}{a} f(x) = b - 0 \Longleftrightarrow \forall \eps > 0 \ ,\exists \delta > 0, \ \forall x \in X :  |a  - x| < \delta \implies b - \eps < f(x) < \eps$  

## Семинар 11.10.2022  

### 471   
- $\lim{x}{0} \dfrac{\sin{(5x)}x}{x} = \lim{x}{0} \dfrac{5\sin{(5x)}x}{5x} = 5$  

### 474  
- $\lim{x}{0} \dfrac{1 - \cos{x}}{x^{2}} = \lim{x}{0} \dfrac{2\sin^{2}{\dfrac{x}{2}}}{x^{2}} = \dfrac{1}{2}$  

### 479   
- $\lim{x}{\dfrac{\pi}{4}} \tan{(2x)} \tan{(\dfrac{\pi}{4} - x)} = \lim{x}{\dfrac{\pi}{4}} (\dfrac{2\tan{x}}{1 - \tan^{2}{x}})(\dfrac{\tan{\dfrac{\pi}{4} - \tan{x}}}{1 - \tan{\dfrac{\pi}{4}}\tan{x}})= \lim{x}{\dfrac{\pi}{4}} \dfrac{2\tan{(x)}}{(1 - \tan{x})^{2}} = \dfrac{1}{2}$  

### 482   
- $\lim{x}{a} \dfrac{\sin{x} - \sin{a}}{x - a} = \dfrac{2\sin{(\dfrac{x - a}{2})}\cos{(\dfrac{x + a}{2})}}{x - a} = \cos{a}$  

### 506  
- $\lim{x}{0} (\dfrac{1 + x}{2 + x}) ^ {\dfrac{1 - \sqrt{x}}{1 - x}} = \dfrac{1}{2}$  
- $\lim{x}{1} (\dfrac{1 + x}{2 + x}) ^ {\dfrac{1 - \sqrt{x}}{1 - x}} = \lim{x}{1} (\dfrac{1 + x}{2 + x}) ^ {\dfrac{(1 - x)(1 + x)}{1 - x}} = \dfrac{1}{4}$  
### 514  
- $\lim{x}{0} \sqrt[x]{1 - 2x} = \lim{x}{0} ((1 + (- 2x))^{\dfrac{1}{-2x}})^{-2} = e^{-2}$  
### 517  
- $\lim{x}{0} (1 + x^{2})^{ctg{(2x)}} =  \ \lim{x}{0} ((1 + x^{2})^{\dfrac{1}{x^{2}}})^{ctg{(2x)}x^{2}} = \ \lim{x}{0} ((1 + x^{2})^{\dfrac{1}{x^{2}}})^{ctg{(2x)}x^{2}} = \ \lim{x}{0} e^{ctg{(2x)}x^{2}} = e^{0} = 1$  

### 521   
- $\lim{x}{0} \dfrac{\cos{x}}{\cos{2x}}^{\dfrac{1}{x^{2}}} = \lim{x}{0} (1 + \dfrac{\cos{x}}{\cos{2x}} - 1)^{\dfrac{1}{x^{2}}} = \lim{x}{0} (1 + \dfrac{\cos{x} - \cos{2x}}{\cos{2x}})^{\dfrac{1}{x^{2}}} = \lim{x}{0} (1 + \dfrac{2\sin{\dfrac{3x}{2}\sin{\dfrac{x}{2}}}}{\cos{2x}})^{\dfrac{1}{x^{2}}} = \ \lim{x}{0} ((1 + \dfrac{2\sin{\dfrac{3x}{2}\sin{\dfrac{x}{2}}}}{\cos{2x}})^{\dfrac{\cos{2x}}{2\sin{\dfrac{3x}{2}\sin{\dfrac{x}{2}}}}})^{\dfrac{2\sin{\dfrac{3x}{2}\sin{\dfrac{x}{2}}}}{x^{2}\cos{2x}}} = \ e^{\dfrac{3}{2}}$  

### 531   
- $\lim{x}{a} \dfrac{\ln{x} - \ln{a}}{x - a} = \lim{x}{a} \dfrac{\dfrac{x}{a} - 1 + 1}{x - a}  = \lim{x}{a} \dfrac{1 + \dfrac{x}{a} - 1}{x - a} = \dfrac{\dfrac{x}{a}}{x - a} = \dfrac{1}{a}$  

### 541  
- $\lim{x}{0} \dfrac{a^{x} - 1}{x} = \lim{x}{0} \dfrac{e^{\ln{x}} - 1}{x} =  \lim{x}{0} \dfrac{(e^{\ln{x}} - 1)\ln{a}}{x \ln{a}} = \ln{a} $  

### 595  
- $\lim{x}{1 - 0} arctg{\dfrac{1}{1 - x}}, \  \dfrac{1}{1 - x}  \xrightarrow[x \to 1 - 0]{} + \infty \implies arctg{(+ \infty)} = \dfrac{\pi}{2}$  

- $\lim{x}{1 + 0} arctg{\dfrac{1}{1 - x}}, \  \dfrac{1}{1 - x}  \xrightarrow[x \to 1 + 0]{} + \dfrac{1}{-0} \implies arctg{(- \infty)} = - \dfrac{\pi}{2}$  

### 596  
- $\lim{x}{- 0} \dfrac{1}{1 + \underbrace{e^{\dfrac{1}{x}} }_{e^{\dfrac{1}{-0}} = -\infty} }  = 1 $  
- $\lim{x}{+ 0} \dfrac{1}{1 + \underbrace{e^{\dfrac{1}{x}}}_{\infty}}  = 0$  

### 597   
- $\lim{x}{- \infty} \dfrac{\ln{(1 + \underbrace{e^{x} }_{0}) }}{x} = \dfrac{e^{x}}{x} = 0$  

## Семинар 18.10.2022
- $|\phi(x)| \leq A|\psi(x)| \implies \phi(x) = O(\psi(x)), \ x \rightarrow x_{0}$

### 650
- Пусть $x \rightarrow 0$. Доказать неравенства:
	- $2x - x^{2} = O(x)$ 
		- $|2x - x^{2}| \leq |2x| \leq 2|x|$
	- $x\sin{\dfrac{1}{x}} = O(|x|)$
		- $|x\sin{\dfrac{1}{x}}| \leq |x|$
	- $\lim{x}{0} \sqrt{x + \sqrt{x + \sqrt{x}}} \sim \sqrt[8]{x}$ 
		- $\lim{x}{0} \left[ \dfrac{\sqrt{x + \sqrt{x + \sqrt{x}}}}{\sqrt[8]{x}} = \dfrac{\sqrt{x + \sqrt{\sqrt{x}(1 + \sqrt{x})}}}{\sqrt[8]{x}} = \dfrac{\sqrt{x + \sqrt[4]{x}}}{\sqrt[8]{x}} = \dfrac{\sqrt[8]{x}}{\sqrt[8]{x}}\right] = 1 $

### 651 
- Пусть  $x \rightarrow +\infty$. Доказать неравенства:
	- $2x^{3} - 3x^{2} + 1 = O(x^{3})$ 
		- $|2x^{3} - 3x^{2} + 1| \leq 2 |x^{3}|$
	- $x + x^{2}\sin{x} = O(x^{2})$
		- $|x + x^{2}\sin{x}| \leq |x| + |x^{2}||\sin{x}| \leq |x| + |x^{2}| < 2|x^{2}|$ 
	- $\dfrac{\arctan{x}}{1 + x^{2}} = O(\dfrac{1}{x})$
		- $\left |\dfrac{\arctan{x}}{1 + x^{2}} \right| \leq \left |\dfrac{\dfrac{\pi}{2}}{1 + x^{2}} \right| \leq \left| \dfrac{\pi}{2 + 2x^{2}} \right|$
	- $\lim{x}{0} \sqrt{x + \sqrt{x + \sqrt{x}}} \sim \sqrt{x}$
		- $\lim{x}{0} \left[ \dfrac{\sqrt{x + \sqrt{x + \sqrt{x}}}}{\sqrt{x}} = \dfrac{\sqrt{x + \sqrt{x^{2}(\dfrac{1}{x} + \dfrac{\sqrt{x}}{x^{2}})}}}{\sqrt{x}} = \sqrt{1 + \sqrt{(\dfrac{1}{x} + \dfrac{\sqrt{x}}{x^{2}})}} \right] = 1 $

### 653 
- Пусть $x \rightarrow 0$. Выделить главный член и определить порядок малости относительно $x$.
	- $2x - 3x^{2} + x^{5} \sim Cx^{n}$
		- $\lim{x}{0} \left[ \dfrac{2x - 3x^{2} + x^{5}}{Cx^{n}} = \dfrac{x(2 - 3x + x^{4})}{Cx} \right] = \dfrac{2}{C} = 1 \implies m = 1; \ C = 2$
	- $\sqrt{1 - 2x} - \sqrt[3]{1 - 3x}$
		- $\dfrac{(\sqrt{1 - 2x})^{6} - (\sqrt[3]{1 - 3x})^{6}}{\sqrt[6]{1 - 6x + 12x^{2} - 8x^{3}} - \sqrt[6]{1 - 6x + 9x^{2}} } \sim 1 + \dfrac{1}{6}(-6x + 12x^{2} - 8x^{3}) - 1 + \dfrac{1}{6}(-6x + 9x^{2}) \sim 2x^{2} - \dfrac{9}{6}x^{2} = \dfrac{1}{2}x^{2}$ 
		- $\lim{x}{0} \dfrac{\dfrac{1}{2}x^{2}}{Cx^{2}} = 1 \implies m = 2; \ C = \dfrac{1}{2}$  
### 655
- Пусть $x \rightarrow 1$. Выделить главный член и определить порядок малости относительно $x - 1$.
	- $3x^{2} - 3x  + 2$ 
		- $\lim{x}{1} \dfrac{(x - 1)^{2}(x - 2)}{C(x - 1)^{m}} = 1 \implies m = 2; \ C = 1$