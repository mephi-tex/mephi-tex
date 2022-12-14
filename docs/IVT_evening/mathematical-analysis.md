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
$\newcommand{\rawOlim}[3]{\dn{{#1}\implies{#2}}{#3}}$
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

```{contents} Математический анализ  
---  
depth: 3  
```
# Математический анализ  
Преподаватель : Михайлов Владислав Дмитриевич 

Конспект : Руденький Н.В., гр. Б$22$-В$02$.

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

- Доказать, что $\left(\dfrac{m}{n}\right)^2 \neq 2$, где $\dfrac{m}{n}$ - несократимая дробь.  
	- Доказательство : Предположим, что $\left(\dfrac{m}{n}\right)^2 = 2$, тогда :  
	$m^2 = 2n^2$ Т.к. $2n^2$ - четное, то и $m^2$ - четное, а следовательно $m$ - четное. $m = 2k$, $4k^2 = 2n^2$, $2k^2 = n^2$ - следовательно: $n^2$ - четное. Получим противоречие, т.к. $\dfrac{2n^2}{2k^2}$ - сократимая дробь.  


### Сравнение вещественных чисел, их сумма и произведение  

***Определение***  
- Сравниваем поразрядно $a_{0}, b_{0}$, затем $a_{1}, b_{1}$ и т.д.  

- По аналогии сумма и произведение: $a_{0} b_{0}$, затем $a_{1} b_{1}$ и т.д.  


### Множества. Инфимум и Супремум.  
Рассмотрим произвольное числовое множество $A$, состоящее из чисел $x \in A$.   

***Определение***  
- Множество $A$ называется ограниченным сверху, если $\exists M : \forall x \in A \implies x \leq M$  

***Определение***  
- Множество $A$ называется ограниченным снизу, если $\exists m : \forall x \in A \implies x \geq m$  

***Определение***  
- Множество $A$ называется ограниченным снизу и сверху, если $\exists M, m : \forall x \in A \implies  m \leq x \leq M$  


***Определение***  
- Наименьшая граница из всех верхних граней называется точной верхней гранью $(\sup{A})$  

***Определение***  

- Наибольшая граница из всех нижних граней называется точной нижней гранью $(inf{A})$  


***Теорема***  
- Всякое ограниченное сверху множество имеет точную верхнюю грань, а всякое ограниченное снизу имеет точную нижнюю грань.  

***Определение точной верхней грани***  

- $(\forall x \in X : x \leq  M) \wedge (\forall x < M, \exists x' \in X : x' > x) \implies M = \sup{X} $  

***Определение точной нижней грани***  
- $(\forall x \in X: x \geq m) \wedge (\forall x > m, \exists x' \in X: x' < x) \implies m =inf{X}$  

***Альтернативное определение точной нижней грани***  

- $(\forall x \in X: x \geq m ) \wedge (\forall \epsilon > 0, \exists x' \in X : x' < m + \epsilon) \implies m = inf{X}$  

***Альтернативное определение точной верхней грани***  

- $(\forall x \in X : x \leq M) \wedge (\forall \epsilon > 0, \exists x' \in X: x' > M - \epsilon) \implies M = \sup{X}$  

***Упражнение***  

- Докажем, что всякое ограниченное сверху множество имеет $\sup$.   
  - Доказательство : Рассмотрим два случая:  

	1. Рассматриваемое множество не лишено неотрицательных чисел  

	2. Рассматриваемое множество содержит только отрицательные числа  

		- Пусть $(1)$, тогда $\sup{} \geq 0$. $X$ ограничено сверху $\implies x \in X : [x] \leq \sup$. Отберем из множества те числа, у которых наибольшая целая часть $\overline{x_{0}}$, остальные числа отбросим. Среди оставшихся отберем те, у которых наибольший следующий разряд, т.е. $\overline{x_{0}},\overline{x_{1}}$. И т.д. до бесконечности. Получаем число - бесконечную, вообще говоря, непериодическую десятичную дробь. $\overline{x_{0}}\overline{x_{1}}\overline{x_{2}} ... \overline{x_{n}} ... = \overline{x} \ (\sup)$  

		- Докажем, что таким образом получим точную верхнюю грань данного множества. Действительно по первой части определения $\sup$ : $\forall x \in A \implies x \leq \overline{x}$. Но это и есть $\sup$ по характеру построения числа $\overline{x}$, так как на каждой позиции для построения $\overline{x}$ бралось наибольшее число. Теперь докажем вторую часть определения $\sup : \forall x < \overline{x}, \exists x' \in A: x' > x$. Действительно, берем произвольное число (не обязательно из множества $A$) , $x < \overline{x}$, т.к. $x < \overline{x}$ на каком - то знаке из $\{\overline{x_{0}},\overline{x_{1}}, ... ,\overline{x_{n}}, ... \}$. Докажем, что $\exists x' \in A: x' > x$.  $x' \in A \implies x_{0}' \leq \overline{x_{0}}$, $x_{0}' = \overline{x_{0}} \implies$ $x_{1}' < \overline{x_{1}}$ и т.д. до позиции с номером $n$. Получим, что в элементах нашего множества есть число, у которого на $n$ - ом месте стоит $\overline{x_{n}} \implies \overline{x_{n}} > x_{n}' > x_{n}$  

		- Докажем для пункта $(2)$. Если все числа множества $A$ - отрицательные, то $\forall x \in A: x = -|x|$, тогда отбрасываем все числа у которых наименьшая целая часть модуля $\overline{x_{0}}$, затем у которых $\overline{x_{0}} \overline{x_{1}}$ и т.д. до бесконечности. Получаем бесконечную десятичную непериодическую дробь. Поставим перед числом знак $(-)$, получим $\sup$.  

***Пример***  

- $A = \{1, \dfrac{1}{2},\dfrac{1}{3}, ... \dfrac{1}{n}, ...\}$. $\sup{A} = 1, inf{A} = 0$  


### Числовая последовательность.  

***Определение***  

- Рассмотрим упорядоченный набор натуральных чисел $\{1, 2, 3, ..., n, ...\}$ и каждому из этих натуральных чисел поставим в соответствие числа: $x_{1}, x_{2}, x_{3}, ... , x_{n}, ...$. Это и есть числовая последовательность.  


***Обозначение***  
- $\{x_{n}\}$  

***Свойства***  

- Последовательность $\{x_{n}\}$ бывает ограниченной сверху, снизу и ограниченной.  

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

5. $x_{n} = 1^{\left(-1\right)^{n}}$  

6. $x_{n} = - n^2$  


- Последовательность ограничена сверху $\Longleftrightarrow \exists M: \forall n : x_{n} \leq M$  

***Определение***  
- Последовательность ограничена снизу $\Longleftrightarrow \exists m: \forall n : x_{n} \geq m$  

***Определение***  
- Последовательность ограничена $\Longleftrightarrow \exists m,M : \forall n :  m \leq x_{n} \leq M$ или в эквивалентной форме :  $\exists k , \forall n :  |x_{n}| \leq k$  

***Определение***  

- $\forall m, \exists n : |x_{n}| > m \Longleftrightarrow$ последовательность не ограничена. (не является ограниченной сверху или снизу)  

### Бесконечно большая и малая последовательность  

***Определение***  

- $\{x_{n}\}$ называется бесконечно большой $\Longleftrightarrow \left(\forall A, \exists N_{0}: \forall n > N_{0}\right) \implies |x_{n}| > A$.  

***Пример***  
- $\{1, -2, 3, -4, \dots, \left(-1\right)^{n+1} n, \dots\}$ (В отличие от неограниченной последовательности, члены бесконечно большой последовательности по модулю больше любого наперед заданного числа A, начиная с какого - то номера.)  

***Определение***  

- $\{x_{n}\}$  бесконечно малая $\Longleftrightarrow \left(\forall A, \exists N_{0}: \forall n > N_{0} \right) \implies |x_{n}| < A$.  

***Теорема***  

- Если $\{x_{n}\}$ - б. б. , то начиная с какого - то номера, после которого нет нулевых членов, для этих номеров определена бесконечно малая последовательность: $\{ \dfrac{1}{x_{n}} \}$.  
	- Доказательство : Действительно, $\{x_{n}\}$ - б. б. , $\implies \left(n > N_{0}: |x_{n}| > A\right)$, где $A$ - любое число. Тогда для этих номеров: $\dfrac{1}{x_{n}} < \dfrac{1}{A}$. Если взять произвольное $\epsilon > 0$ и $A = \dfrac{1}{\epsilon}$, то $|\dfrac{1}{x_{n}}| < \epsilon$, а это и есть определение бесконечно малой последовательности. Справедливо и обратное: Если $\{ \dfrac{1}{x_{n}} \}$ - б. м. , то начиная с какого - то номера, после которого нет нулевых членов, для этих номеров определена $\{x_{n}\}$ - б. б.  

### Монотонные последовательности  
***Определение***  
- Последовательность $\{x_{n}\}$ возрастает $\Longleftrightarrow \left(\forall n : x_{n + 1} \geq x_{n}\right)$ и строго возрастает, если $x_{n + 1} > x_{n}$. (Иногда говорят: неубывающая, строго возрастающая).   

***Определение***  
- Последовательность $\{x_{n}\}$ убывает, $\Longleftrightarrow \left(\forall n : x_{n + 1} \leq x_{n}\right)$ и строго убывает, если $x_{n + 1} < x_{n}$. (Иногда говорят: невозрастающая, строго убывающая).   

### Предел числовой последовательности  

***Формальное определение предела числовой последовательности***  

- Если последовательность приближается к числу, то это число и есть ее предел.  

***Примеры***  

1. $x_{n} = \dfrac{1}{n}, \lim{n}{\infty} \dfrac{1}{n}  = 0$  
2. $x_{n} = \dfrac{n - 1}{n}, \lim{n}{\infty} \dfrac{n - 1}{n}= 1$  

***Определение предела числовой последовательности***  

- $A = \lim{n}{\infty} {x_{n}} \Longleftrightarrow (\forall \epsilon > 0, \exists N_{\epsilon} : \forall n > N_{\epsilon}  \implies |x_{n} - A| < \epsilon)$  

***Упражнение***  

- С помощью определения докажем (1) из примера. (Т. е. найдем $N_{\epsilon}$, что $\forall n > N_{\epsilon} \implies |x_{n} - A| < \epsilon)$. Т. к. $ \lim{n}{\infty} \dfrac{1}{n} = 0 \implies (\forall \epsilon > 0, \exists N_{\epsilon} : \forall n > N_{\epsilon})  \implies |x_{n} - 0| < \epsilon \implies |\dfrac{1}{n}| < \epsilon \implies \dfrac{1}{n} < \epsilon \implies n > \dfrac{1}{\epsilon}$  
- С помощью определения докажем (2) из примера. (Т. е. найдем $N_{\epsilon}$, что $\forall n > N_{\epsilon} \implies |x_{n} - A| < \epsilon)$. Т. к. $ \lim{n}{\infty} \dfrac{n - 1}{n} = 1 \implies (\forall \epsilon > 0, \exists N_{\epsilon} : \forall n > N_{\epsilon})  \implies |x_{n} - 1| < \epsilon \implies |\dfrac{n - 1}{n} - 1| < \epsilon \implies \left|\dfrac{1}{n}\right| < \epsilon \implies n > \dfrac{1}{\epsilon}$  

### Свойства пределов  

***Теорема***  

**Последовательность, имеющая предел, называется сходящейся, иначе расходящейся.**  

- Всякая сходящаяся последовательность имеет единственный предел.  
	- Доказательство:  
		- Пусть $  \lim{n}{\infty} x_{n} = A$. Докажем единственность от противного. Предположим, что $\exists   \lim{n}{\infty} x_{n} = B$ и $A > B$. $  \lim{n}{\infty} x_{n} = A \implies  (\forall \epsilon_{1} > 0, \exists N_{\epsilon_{1} } : \forall n > N_{\epsilon_{1} }  \implies |x_{n} - A| < \epsilon_{1})$. В качестве $\epsilon_{1}$ возьмем $\dfrac{A - B}{2} \implies$  
	  
		1. $ -\dfrac{A - B}{2} < x_{n} - A < \dfrac{A - B}{2} $  
		2. $-\dfrac{A - B}{2} + A< x_{n}  < \dfrac{A - B}{2} + A$  
		3. $\dfrac{A + B}{2} < x_{n}  < \dfrac{3A - B}{2} $.  
	  
	-  $ \lim{n}{\infty} x_{n} = B \implies  (\forall \epsilon_{2} > 0, \exists N_{\epsilon_{2} } : \forall n > N_{\epsilon_{2} }  \implies |x_{n} - B| < \epsilon_{2})$. В качестве $\epsilon_{2}$ возьмем $\dfrac{A - B}{2}. $Возьмем $n > \max(N_{\epsilon_{1}}, N_{\epsilon_{2}}) \implies |x_{n} - B| < \dfrac{A - B}{2} \implies$  
		1. $-\dfrac{A - B}{2} < x_{n} - B < \dfrac{A - B}{2}$  
		2. $-\dfrac{A - B}{2} + B< x_{n}  < \dfrac{A - B}{2} + B$  
		3. $\dfrac{3B - A}{2} < x_{n}  < \dfrac{A + B}{2} $.  
	- Получим $\dfrac{A + B}{2} > x_{n} > \dfrac{A + B}{2}$. Противоречие.  

***Теорема***  

- Сходящаяся последовательность ограничена  
	- Доказательство: $\lim{n}{\infty}\{x_{n}\} = A$ $\implies (\forall \epsilon > 0, \exists N_{\epsilon}: \forall n > N_{\epsilon} \implies |x_{n} - A| < \epsilon)$. Это было бы доказательством ограниченности, если бы было верно для всех $n > 0$. Но до $N_{\epsilon}$ - конечное число членов. Если взять $M = \max(|x_{1}|, |x_{2}|, |x_{3}|, \dots, |x_{N_{\epsilon}}|, |A - \epsilon|,| A + \epsilon |)$, то $\forall n: |x_{n}| \leq M $  

***Теорема***  

- $\{x_{n}\}$ - б. м. $\implies \forall k :\{ k x_{n}\}$ - б. м.  

	- Доказательство:   
		- Действительно : т. к. $(\forall \epsilon > 0, \exists N_{\epsilon}: \forall n > N_{\epsilon} \implies |x_{n}  - 0| < \epsilon)$ . Возьмем $\epsilon = \dfrac{\epsilon}{|k|} \implies |x_{n}| < \dfrac{\epsilon}{|k|} \implies |k \cdot x_{n}| < \epsilon \implies \lim{n}{\infty} k x_{n} = 0$  

***Следствие***  

Если последовательность состоит из одного и того же члена $x_{n} = \{C, C, C, C,  \dots \}$, то $ \lim{n}{\infty} x_{n} = C$.  

***Свойства пределов, выражаемые неравенствами***  

- $(\forall n > N: x_{n} \geq y_{n}) \wedge ( \lim{n}{\infty} x_{n} = A,  \lim{n}{\infty} y_{n} = B) \implies A \geq B$  
	- Доказательство:   
		- В качестве $\epsilon$ возьмем $\dfrac{A - B}{2}$. 
		- $\forall n > N_{\epsilon_{1}}, N_{\epsilon_{1}} \implies |x_{n} - A| < \dfrac{A - B}{2} \implies \\ -\dfrac{A - B}{2} < x_{n} - A < \dfrac{A - B}{2} \implies \\   -\dfrac{A - B}{2} + A < x_{n}  < \dfrac{A - B}{2} + A \implies \\  \dfrac{3A - B}{2} < x_{n}  < \dfrac{A + B}{2} $  
		- $\forall n > N_{\epsilon_{2}} : |y_{n} - B| < \dfrac{A - B}{2} \implies \dfrac{A - B}{2} < y_{n} < \dfrac{3B - A}{2}$  
		- Получим $x_{n} < \dfrac{A + B}{2} < y_{n}$. Противоречие.  
- $(x_{n} \leq y_{n} \leq z_{n}) \wedge (\forall n > N : \lim{n}{\infty}{x_{n}} = \lim{n}{\infty}{z_{n}}) \implies \lim{n}{\infty}\{y_{n}\} = A$, причем $\lim{n}{\infty}{x_{n}} = \lim{n}{\infty}{y_{n}} = \lim{n}{\infty}{z_{n}}$   
	- Доказательство :   
		- Действительно :  
		- $(\forall \eps_{1} > 0, \exists n > N_{\eps_{1}} : |x_{n} - A| < \eps_{1})$  
		- $(\forall \eps_{2} > 0, \exists n > N_{\eps_{2}} : |z_{n} - A| < \eps_{2})$  
		- $N = \max(N_{\eps_{1}}, N_{\eps_{2}}) \implies  |x_{n} - A| < |y_{n} - A| < |z_{n} - A| \implies |y_{n} - A| < \epsilon \implies \lim{n}{\infty}{y_{n}} = A$  

***Арифметические свойства пределов сходящихся  последовательностей***  

1. $\lim{n}{\infty} \{x_{n}\} = A; \lim{n}{\infty}  \{y_{n}\} = B \implies  \lim{n}{\infty} (\{x_{n}\} + \{y_{n}\}) = A + B$  
3. $ \lim{n}{\infty} \{x_{n}y_{n}\} = AB$  
4. $ \lim{n}{\infty} \{\dfrac{x_{n}}{y_{n}}\} = \dfrac{A}{B}$  
- Докажем $(1)$  
  
	- $\lim{n}{\infty}{x_{n}} = A$, то $(\forall \epsilon > 0, \epsilon = \dfrac{\epsilon}{2}, \forall n > N_{1} : |x_{n} - A| < \dfrac{\epsilon}{2})$  
  
	- $\lim{n}{\infty}{x_{n}} = B$, то $(\forall \epsilon > 0, \epsilon = \dfrac{\epsilon}{2}, \forall n > N_{2} : |x_{n} - B| < \dfrac{\epsilon}{2})$  
	- $N = \max(N_{1}, N_{2}) \implies$ $\forall n > N : |x_{n} + y_{n} - A - B| \leq |x_{n} - A| + |y_{n} - B| < \dfrac{\epsilon}{2} +  \dfrac{\epsilon}{2} = \epsilon \implies \lim{n}{\infty} (x_{n} + y_{n}) = A + B$  
- Докажем $(2)$   
	- $ \lim{n}{\infty} x_{n} = A$, то $(\forall \epsilon_{1} > 0, \forall n > N_{\eps_{1}} : |x_{n} - A| < \epsilon_{1})$  
	- $ \lim{n}{\infty} y_{n} = B$, то $(\forall \epsilon_{2} > 0,  \forall n > N_{\eps_{2}} : |y_{n} - B| < \epsilon_{2})$  
	- $N = \max(N_{\eps_{1}}, N_{\eps_{2}}) \implies$ $\forall n > N :|x_{n}y_{n} - AB| = \\ |x_{n}y_{n} -Ay_{n} + Ay_{n} - A B| = \\ |(x_{n} - A)y_{n} + A(y_{n} - B)| \leq |x_{n} - A||y_{n}| + |A||y_{n} - B|\bigg|_{|y_{n}| < M_{y}} \leq \eps_{1} M_{y} + |A|\eps_{2}\bigg|_{\eps_{1} = \dfrac{\eps}{2|M_{y}|}}^{\eps{2} = \dfrac{\eps}{2|A|}} \implies |x_{n}y_{n} - AB| < \eps \implies \lim{n}{\infty} \left(x_{n}y_{n}\right) = AB$  

## Лекция 21.09.2022  

### Подпоследовательность  

***Определение подпоследовательности***  

- Пусть задана $\{x_{n}\}$. Возьмем $N_{1}, N_{2} > N_{1}, N_{3} > N_{2}, \dots, N_{k} > N_{k - 1}, \dots $. Получим подпоследовательность $\{x_{n_{k}}\}$.  

***Утверждение***  

 - $ \lim{n}{\infty} x_{n} = a \implies$ любая подпоследовательность $x_{n_{k}}$ тоже сходится, причем к тому же пределу.  
	- Доказательство: Действительно: $ \lim{n}{\infty} x_{n} = a \implies (\forall \epsilon > 0, \exists N_{\epsilon} : \forall n > N_{\epsilon} \implies |x_{n} - a| < \epsilon)$. Т.к при $N_{k} > N_{\epsilon}$ члены подпоследовательности входят в число членов $\{x_{n}\} \implies |x_{n_{k}} - a| < \epsilon $  

***Пример***  
1. $x_{n} = \dfrac{1 + (1)^{n}}{2}$  
	- $\{x_{2k}\} \implies 1$  
	- $\{ x_{2k + 1} \} \implies 0$  
2. $\{x_{n}\} = 1 + \sin{\dfrac{\pi n}{2}}$  
	- $\{x_{2k}\} = (1 + \sin{\pi k}) \implies 1$  
	- $\{x_{4k + 1}\} = (1 + \sin{\dfrac{\pi}{2}}) \implies 2$  
	- $\{x_{4k + 3}\} = (1 + \sin{\dfrac{3 \pi}{2}}) \implies 0$  
3. $x_{n} = n^{(-1)^{n}}$  
	- $\{x_{2k}\} \implies \infty$  
	- $\{x_{2k + 1}\} \implies 0$  

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
		4. Докажем, что $\overline{x}$ - предельная точка $\{x_{n}\}$. $\overline{x} = inf{X} \implies (\forall x \in X: x \geq \overline{x}) \wedge (\forall \epsilon > 0, \exists x' \in X : x' < \overline{x} + \epsilon) \implies $ левее $\overline{x} + \epsilon$ и правее  $\overline{x} - \epsilon$ содержится $\infty$ членов последовательности. Т. е. в $\epsilon$ - окрестности числа $\overline{x}$ содержится также $\infty$ членов. $\implies$ это и есть предельная точка. ч. т. д.  

### Критерий Коши сходимости последовательности  

***Определение фундаментальной последовательности***  

- $x_{n} $ - фундаментальная $\Longleftrightarrow$ $(\forall \epsilon > 0, \exists N_{\epsilon}, \forall n > N_{\epsilon}) \wedge (\forall p \in \NN : |x_{n + p} - x_{n}| < \epsilon)$.  

***Теорема***  
- Последовательность $\{x_{n}\}$ сходится $\Longleftrightarrow$ она фундаментальная.  
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
	- $\forall \epsilon > 0, \exists \delta > 0: \forall x \in X: 0 < |x - x_{0}| < \delta \implies |f(x) - A| < \epsilon$. Возьмем произвольную $\{x_{1}, x_{2}, \dots, x_{n}, \dots\} \in X, x_{n} \neq x_{0}, \lim{n}{\infty} {x_{n}}= x_{0}$, то есть $\forall \delta, \exists N_{\epsilon}: \forall n > N_{\epsilon} \implies |x_{n} - x_{0}| < \delta$. Что есть в определении по Коши: $0 < |x - x_{0}| < \delta \implies |f(x) - A| < \epsilon$. Получим определение сходимости $f(x_{n})$, т.к. $x_{n}$ - произвольная.  
 - $(Г \implies К)$  
	- $A = \lim{x}{x_{0}} f(x) \Longleftrightarrow (\forall \{x_{n}\} : x_{n} \in X, x_{n} \neq x_{0} \implies \lim{n}{\infty} x_{n} = x_{0}, \{f(x_{0}), f(x_{1}), \dots, f(x_{n}), \dots\} \implies \lim{n}{\infty} f(x_{n}) = A)$ . Докажем от противного: Пусть $Г \;\not\!\!\!\implies К$. Тогда $\exists \epsilon_{0} \forall \delta > 0, \exists x \in X: 0 < |x - x_{0}| < \delta \implies |f(x) - A| \geq \epsilon_{0}$. Пусть $\delta_{1} = 1$, тогда $\forall \delta > 0$ найдется $x_{1}$ из $\delta$ - окрестности точки $x_{0}$, такое, что $|f(x_{1}) - A| \geq \epsilon_{0}$. Пусть $\delta_{2} = \dfrac{1}{2}$, тогда $\forall \delta > 0$ найдется $x_{2}$ из $\delta$ - окрестности точки $x_{0}$, такое, что $|f(x_{2}) - A| \geq \epsilon_{0}$. И так далее  $\delta_{n} = \dfrac{1}{n}$, тогда $\forall \delta > 0$ найдется $x_{n}$ из $\delta$ - окрестности точки $x_{0}$, такое, что $|f(x_{n}) - A| \geq \epsilon_{0}$. Получим: $\{x_{1}, x_{2}, \dots, x_{n}, \dots\} \implies x_{0}, \{f(x_{1}),f(x_{2}), \dots, f(x_{n)}, \dots\} \;\not\longrightarrow A$  

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
		- Возьмем $\dfrac{1}{x} = \pi k, x_{k} = \dfrac{1}{\pi k} \implies 0 \implies f(x_{k}) = \sin{\pi k} \equiv 0 \implies \lim{n}{\infty} f(x_{n}) = 0$  
		- Возьмем $\dfrac{1}{x_{k}} = \left(\dfrac{\pi}{2} + 2\pi k\right), x_{k} = \left(\dfrac{2}{\pi + \pi k}\right) \implies \begin{equation*}  
	   \begin{cases}  
	    x_{k} \implies 0 \\  
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
	- Доказательство по Коши: $\forall \epsilon > 0: |\cos{x} - \cos{x_{0}| = |2 \sin{\dfrac{x - x_{0}}{2}}} \sin{\dfrac{x + x_{0}}{2} }| \leq 2|\sin{\dfrac{x - x_{0}}{2} }| \leq 2 \dfrac{|x - x_{0}|}{2}$. При $|x - x_{0}| < \delta, |\cos{x} - \cos{x_{0}}| < \epsilon \implies \delta = \epsilon$  

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
	-  Существуют конечные пределы этой функции слева и справа, они равны  
- Точка разрыва 1 - ого рода  
	- Существуют конечные пределы слева и справа в точке, но они не равны друг другу  
- Точка разрыва 2 - ого рода  
	- Все остальные точки  

***Примеры***  

- $\lim{x}{1} \dfrac{x^{2} - x - 2}{x^{2} + x - 3} = \dfrac{0}{0}$. Рассмотрим выколотую окрестность $\mathring{U}(1)$. $f(x) = \dfrac{x + 2}{x + 3} \implies \lim{x}{1} f(x) = \dfrac{3}{4}$, $x = 1$ - Устранимая точка разрыва  
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
2. $\lim{n}{\infty} \left(1 + \dfrac{1}{n}\right)^{n} = e$ (второй замечательный предел)  
3. $\lim{x}{\infty} \left(1 + \dfrac{1}{x}\right)^{x} = e$ ($x$ - произвольное)  
4. $\lim{t}{0} \left(1 + t\right)^{\dfrac{1}{t}} = e$ $\left(x = \dfrac{1}{t}\right)$  
5. $\lim{t}{0} \ln{\left(1 + t \right)}^{\dfrac{1}{t}} = \ln{(e)} = 1 \implies \lim{t}{0} \dfrac{\ln{(1 + t)}}{t} = 1$  
6. $\lim{x}{0}  \dfrac{1 - \cos{x} }{x^{2}} = \ \lim{x}{0}\ \dfrac{2\sin^{2}{(\dfrac{x}{2})}}{x^{2} } = \ \lim{x}{0} \dfrac{\dfrac{1}{2}\sin{(\dfrac{x}{2}) \sin{(\dfrac{x}{2}) } }}{\dfrac{1}{2}\dfrac{x^{2}}{2} } = \  \lim{x}{0}\ \dfrac{1}{2} \underbrace{\dfrac{\sin{(\dfrac{x}{2}) \sin{(\dfrac{x}{2}) } }}{\dfrac{x}{2} \dfrac{x}{2}}}_{1} = \dfrac{1}{2}$  
7. $\lim{x}{0} \dfrac{\sqrt[n]{1 \ + \ x} \ - \ 1}{x} = \ \lim{x}{0} \dfrac{\left(\sqrt[n]{1 \ + \ x} \ -\  1\right)\left(\left(\sqrt[n]{1 \ + \ x}\right)^{(n - 1)} + \left(\sqrt[ n]{1 \ + \ x}\right)^{(n - 2)}  + \ \dots \ + \ \left(\sqrt[n]{1 \ + \ x}\right)+ 1\right)}{x \left(\left(\sqrt[n]{1 \ + \ x}\right)^{(n - 1)} + \left(\sqrt[ n]{1 \ + \ x}\right)^{(n - 2)}  + \ \dots \ + \ \left(\sqrt[n]{1 \ + \ x}\right)+ 1\right)} = \\ \ \lim{x}{0} \dfrac{x}{x \left(\left(\sqrt[n]{1 \ + \ x}\right)^{(n - 1)} + \left(\sqrt[ n]{1 \ + \ x}\right)^{(n - 2)}  + \ \dots \ + \ \left(\sqrt[n]{1 \ + \ x}\right)+ 1\right)} = \ \dfrac{1}{n}$  

- Докажем $(1)$  
-  Рассмотрим $\lim{x}{ 0 + 0} \dfrac{\sin{(x)}}{x} \stackrel{\text{?}}{=} 1$  
	![image1](matan_pictures/matan1.jpg)  
	- $\sin{(\alpha)} = y(A)$  
	- $\cos{(\alpha)} = x(A)$  
	- $S_{OAA'} < S_{OAB'} < S_{OBB'}$  
	- $\dfrac{1}{2}\cos{(x)}\sin{(x)} < \dfrac{1}{2} \cdot 1 \cdot x < \dfrac{1}{2} \cdot 1 \cdot \tan{(x)}$  
	- $\cos{(x)}\sin{(x)} <  x < \tan{(x)}$  
	- $\cos{(x)} <  \dfrac{x}{\sin{(x)}} < \dfrac{1}{\cos{(x)}}$  
	- $\cos{(0)} \xrightarrow[n \to 0]{} 1 \implies \lim{x}{0 + 0} \dfrac{\sin{x}}{x} = 1$  
-  Рассмотрим $\lim{x}{ 0 - 0} \dfrac{\sin{(x)}}{x}$  
	- Так как $f(-x) = f(x) \implies \lim{x}{0 + 0} \dfrac{\sin{(x)}}{x} = \lim{x}{0 - 0} \dfrac{\sin(x)}{x} = \lim{x}{0} \dfrac{\sin(x)}{x} = 1$  
- Докажем $(2)$  
- $\lim{n}{\infty} (1 + \dfrac{1}{n})^{n} = 1^{\infty}$  
- Докажем, что $\exists \lim{n}{\infty} f(x_{n})$. Воспользуемся Теоремой о возрастающей, ограниченной последовательности:  
	- Ограниченность : $2 < (1 + \dfrac{1}{n})^{n} = 1 + n \cdot \dfrac{1}{n} + \dfrac{n(n- 1)}{2!} \cdot \dfrac{1}{n^{2}} + \dots = 2 + \dfrac{1}{2!}(1 - \dfrac{1}{n}) + \dfrac{1}{3!}(1 - \dfrac{1}{n})(1 - \dfrac{2}{n}) \dots \leq 2 + \dfrac{1}{2!} + \dfrac{1}{3!} + \dots < 2 + \dfrac{1}{2} + \dfrac{1}{2^{2}} + \dots < 2 + \dfrac{0.5}{1 - 0.5} = 3$  
	- Возрастание: $x_{n + 1} = (1 + \dfrac{1}{n + 1})^{n + 1} = 1 + (n + 1) \cdot \dfrac{1}{n + 1} + \dfrac{n(n + 1)}{2!} \cdot \dfrac{1}{(n + 1)^{2}} + \dots \implies x_{n + 1} > x_{n}$, так как каждое слагаемое уменьшается и число слагаемых $n + 1$  

***Определение эквивалентности функций в точке***  

- $\lim{x}{x_{0}} \dfrac{f(x)}{g(x)} = 1 \Longleftrightarrow f(x) \sim  g(x)$ ($f$ эквивалентна $g$ в $x_{0}$)  

### Эквивалентные бесконечно малые величины  
1. $\lim{x}{0} \dfrac{\sin(x)}{x} = 1 \Longleftrightarrow \sin{(x)} \sim x$  
2. $\lim{x}{0} \dfrac{\ln{(1 + x)}}{x} = 1 \Longleftrightarrow \ln{(1 + x)} \sim x$  
3. $\lim{x}{0} \dfrac{e^{x} - 1}{x} = 1 \Longleftrightarrow e^{x} - 1 \sim x$  
4. $\lim{x}{0} \dfrac{\sqrt[n]{(1 + x)} - 1}{x} = \dfrac{1}{n} \Longleftrightarrow \sqrt[n]{(1 + x)} - 1 \sim \dfrac{x}{n}$  

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
- $\overline{\lim{n}{\infty}} a_{n} \Longleftrightarrow \max{\left(\lim{n}{\infty} \{a_{n_{k}}\}\right)}$  
- $\underline{\lim{n}{\infty}} a_{n} \Longleftrightarrow \min{\left(\lim{n}{\infty} \{a_{n_{k}}\}\right)}$  

***Пример***  

- $a_{n} = 1 + \cos{(\dfrac{\pi n}{3})}$  
	- $\{a_{3k}\} = 1 + (-1)^{k} \implies (2 , 0)$   
	- $\{a_{3k + 1}\} \implies (\dfrac{1}{2} , \dfrac{7}{6})$   
	- $\{a_{3k + 2}\} \implies (\dfrac{1}{2} , \dfrac{3}{2})$   
	- $\implies \overline{\lim{n}{\infty}} a_{n} = 2, \ \underline{\lim{n}{\infty}} a_{n} = 0$  

### Раскрытие неопределенностей  
- $\lim{x}{x_{0}} (u(x)^{v(x)}); \lim{x}{x_{0}} u(x) = 1; \lim{x}{x_{0}} v(x) = \infty \implies \lim{x}{x_{0}} (u(x)^{v(x)}) = \\ \lim{x}{x_{0}} ((u(x) - 1 + 1)^{v(x)}) = \lim{x}{x_{0}} [\underbrace{(1 + \underbrace{(u - 1)}_{0})^{\dfrac{1}{u - 1}}))}_{e}]^{(u - 1)v} = e^{(u - 1)v}$  

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
	- $\lim{x}{x_{0}} \dfrac{\alpha(x)}{\beta(x)} = 1 \implies \alpha(x) \sim \beta(x), x \implies x_{0}$

***Примеры***

1.

-  $\alpha(x) = \dfrac{1}{3}x^{4} - 2x^{3} - x \  (x \implies x_{0})$
- $\beta(x) = 2x^{4} + 3x^{2} + 2x \  (x \implies x_{0})$
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
	- $\alpha \cdot \gamma = o(\beta^{2})$
	- $ f \sim C \cdot (x - x_{0})^{m},  x \longrightarrow x_{0} \implies (x - x_{0})^{m}$ - главный член $f$, причем $m$ - порядок малости.

***Пример*** 

- $f(x) = x^{3} - 3x + 2$
	- $\lim{x}{1} f = 0 \implies f$ - б. м. в $x_{0} = 1$
	- Определим порядок малости и главный член $f$
	- $f(x) = (x - 1)^{2}(x - 2)$
	- $\lim{x}{1} \dfrac{f(x)}{C \cdot (x - 1)^{m}} = 1 \implies m = 2, \ C = 3 \implies$ главный член имеет вид : $3(x - 1)^{2} + o((x - 1)^{2})$

### Сравнение бесконечно больших функций

***Определение***

- $A(x)$ - б. б. справа в $x_{0}$ $\Longleftrightarrow \exists \lim{x}{x_{0}} A(x) = + \infty \Longleftrightarrow (\forall E > 0, \ \forall \{x_{n}\} \in X, \ \exists N_{E}: \ \forall n > N_{E} \implies A(x_{n}) > E, \ x_{n} > x_{0})$
- $A(x)$ - б. б. слева в $x_{0}$ $\Longleftrightarrow \exists \lim{x}{x_{0}} A(x) = - \infty \Longleftrightarrow (\forall E > 0, \ \forall \{x_{n}\} \in X, \ \exists N_{E}: \ \forall n > N_{E} \implies A(x_{n}) < -E, \ x_{n} < x_{0})$

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
	
	- $(uv)' = \lim{\Delta x}{0} \left[ \dfrac{\Delta (uv)}{\Delta x}  = \dfrac{u(x + \Delta x)v(x + \Delta x) - u(x)v(x)}{\Delta x} = \dfrac{u(x + \Delta x)v(x + \Delta x) - u(x)v(x + \Delta x) + u(x)v(x + \Delta x) - u(x)v(x)}{\Delta x} = \dfrac{u(x + \Delta x) - u(x)}{\Delta x}v(x + \Delta x) + \dfrac{v(x + \Delta x) - v(x)}{\Delta x}u(x)  \right] = u'v + uv'$

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

## Лекция 26.10.2022

### Таблица производных 


№|f | f' 
:------:|:--------:|------:
Степенная и показательная функция||
1 | $x^{n}$     | $nx^{n - 1}$
2 |$a^{x}$     | $a^{x}\ln{a}$
3 |$e^{x}$     | $e^{x}$
4 |$x^{\alpha}, \ \alpha \in \RR$     | $\alpha x^{\alpha - 1}$
5 |$\ln{x}$     | $\dfrac{1}{x}$
6 |$\log_{a}{x}$     | $\dfrac{1}{x\ln{a}}$
Тригонометрические функции||
7 |$\sin{x}$     | $\cos{x}$   
8 |$\cos{x}$     | $- \sin{x}$
9 |$\tan{x}$     | $ \dfrac{1}{\cos^{2}{x}}$ 
10 |$\cot{x}$     | $- \dfrac{1}{\sin^{2}{x}}$ 
11 |$\arcsin{x}$     | $ \dfrac{1}{\sqrt{1 - x^{2}}}$
12 |$\arccos{x}$     | $- \dfrac{1}{\sqrt{1 - x^{2}}}$
13 |$\arctan{x}$     | $\dfrac{1}{1 + x^{2}}$
14 |$arccot{(x)}$     | $- \dfrac{1}{1 + x^{2}}$
Гиперболические функции||
15 |$sh{(x)}$     | $ch{(x)}$  
16 |$ch(x)$     | $sh(x)$ 
17 |$\tanh{x}$     | $\dfrac{1}{ch^{2}(x)}$ 
18 |$\coth{x}$     | $ - \dfrac{1}{sh^{2}(x)}$ 

***Основное тригонометрическое тождество гиперболической геометрии***

- $ch^{2}(x) - sh^{2}(x) =\left ( \dfrac{e^{x} + e^{-x}}{2} \right )^{2} - \left ( \dfrac{e^{x} - e^{-x}}{2} \right )^{2} = \dfrac{1}{4} \left(4e^{x}e^{-x} \right) = 1$

***Некоторые доказательства из таблицы производных***

- Докажем $(5)$
	- $\Delta y= y(x + \Delta x) - y(x) = \ln{(x + \Delta x)} - \ln{x} = \ln{\dfrac{x + \Delta x}{x}} = \ln{(1 + \dfrac{\Delta x}{x})} \sim \dfrac{\Delta x}{x}$ 
	- $y' = \lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x} = \lim{\Delta x}{0} \dfrac{\dfrac{\Delta y}{\Delta x}} {\Delta x} = \dfrac{1}{x}$
- Докажем $(6)$
	- $\log_{a}{x} = \dfrac{\ln{x}}{\ln{a}}$
	- $\left (\dfrac{\ln{x}}{\ln{a}} \right)' = \dfrac{1}{x\ln{a}}$
- Докажем $(2)$
	- $y = a^{x}, \ x = \log_{a}{y}$
	- $(a^{x})' = \dfrac{1}{(\log_{a}{y})'} = \dfrac{1}{\dfrac{1}{y\ln{a}}} = y\ln{a} = a^{x}\ln{a}$
- Докажем $(4)$
	- $x^{\alpha} = \left (e^{\ln{x}} \right )^{\alpha}$
	- $\left ( \left (e^{\ln{x}} \right )^{\alpha} \right ) ' = e^{\alpha\ln{x}} \left (x\ln{x} \right)' = e^{\alpha\ln{x}} \cdot \alpha \cdot \dfrac{1}{x} = \alpha x^{\alpha - 1}$
- Докажем $(9)$
	- $\tan{x} = \left (\dfrac{\sin{x}}{\cos{x}} \right )' = \dfrac{\cos{x}(\sin{x})' - \sin{x}(\cos{x})'}{\cos^{2}{x}} = \dfrac{1}{\cos^{2}{x}}$ 
- Докажем $(13)$
	- $y = \arctan{x}, \ x = \tan{y}$ 
	- $\arctan{x} = \dfrac{1}{(\tan{y})'}  = \cos^{2}{y} = \dfrac{1}{1 + \tan^{2}{y}} = \dfrac{1}{1 + x^{2}}$
- Докажем $(15)$
	- $ch(x) = \dfrac{e^{x} + e^{-x}}{2}$ 
	- $sh(x) = \dfrac{e^{x} - e^{-x}}{2}$
	- $\left (sh(x) \right )' = \left ( \dfrac{e^{x} - e^{-x}}{2} \right)' = \dfrac{1}{2}\left(e^{x} - e^{-x}(-x)' \right) = \dfrac{1}{2}\left(e^{x} + e^{-x}\right) = ch(x)$
- Докажем $(16)$
	- $\left (ch(x) \right )' = \dfrac{1}{2}\left(e^{x} - e^{-x}\right) = sh(x)$
- Докажем $(17)$
	- $\left (\tanh{x} \right )' = \left (\dfrac{sh(x)}{ch(x)} \right )' = \dfrac{ch(x)(sh(x))' - sh(x)(ch(x))'}{ch^{2}(x)} = \dfrac{1}{ch^{2}(x)}$
- Докажем $(18)$
	- $\left (\coth{x} \right )' = \left (\dfrac{ch(x)}{sh(x)} \right )' = - \dfrac{ch^{2}(x) - sh^{2}(x)}{sh^{2}(x)} = - \dfrac{1}{sh^{2}(x)}$

### Производная параметрически заданной функции
- $\begin{equation*}
  	\begin{cases}
	x = \phi{(t)} \\
	y = \psi{(t)}
	\end{cases}
    \end{equation*}$

***Пример***

- Рассмотрим уравнение окружности : $x^{2} + y^{2} = R^{2}$
	- $\begin{equation*}
  	\begin{cases}
	  x = R\cos{(t)}, \ t \in [0; 2\pi] \\
	  y = R\sin{(t)}, \ t \in [0; 2\pi] 
	  \end{cases}
    \end{equation*}$
- Пусть $x = \phi{(t)}, \ y = \psi{(t)},  \ \exists \lim{\Delta t}{0} \dfrac{\Delta x}{\Delta t} = \phi', \ \exists \lim{\Delta t}{0} \dfrac{\Delta y}{\Delta t} = \psi'$
- Рассмотрим : $\lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x}=  y'(x) = \lim{\Delta x, \ \Delta t}{0, \ 0} \dfrac{\Delta y \cdot \Delta t}{\Delta x \cdot \Delta t} = \lim{\Delta t}{0} \dfrac{\Delta y}{\Delta t} \cdot  \lim{\Delta x}{0} \dfrac{\Delta t}{\Delta x} = \dfrac{\lim{\Delta t }{0} \dfrac{\Delta y}{\Delta t}}{\lim{\Delta t }{0} \dfrac{\Delta x}{\Delta t}} = \dfrac{y'(t)}{x'(t)}$

### Производная неявно заданной функции
- $x^{2} + y^{2} = R^{2}$
- Возьмем производную от обеих частей, где $y = y(x)$:
	- $2x + 2y(x) \cdot y'(x) = 0 \implies y'(x) = - \dfrac{x}{y}$ 

### Необходимое условие существования производной

***Вспомогательное определение непрерывности***

- $f$ непрерывна в $x_{0}$ $\Longleftrightarrow$ При $\Delta x \implies 0, \ \Delta y \implies 0$.

***Доказательство***
- Действительно, возьмем $\Delta x \implies 0, \ \Delta y = y(x + \Delta x) - y(x)$. Непрерывность означает : $\forall \eps > 0, \ \exists \delta > 0 : |x - x_{0}| < \delta \implies |\Delta y| < \eps$. Следствие можно переписать в виде $|f(x + \Delta x) - f(x)| < \eps$, что и означает совпадение $f(x)$ с ее пределом.

***Теорема о существовании производной***

- $f$ имеет производную в $x$ $\implies$ $f$ - непрерывна в $x$. 

***Доказательство***

- $f$ имеет производную $f'$ в $x$ $\implies$ $f'(x)  = \lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x} \implies$ при $\Delta x \implies 0$, $\Delta y \implies 0$. Это и есть определение непрерывности $f$

### Определение дифференцируемой функции и ее дифференциала
***Обозначение дифференциала***

- $A \Delta x = dy$ или $df$

***Определение дифференцируемой функции***

- $f$ -  дифференцируема в $x$ $\Longleftrightarrow$ $\Delta y = A \Delta x + o(\Delta x)$.
- Выясним смысл $A$.
	- Разделим обе части на $\Delta x$. Получим $\dfrac{\Delta y}{\Delta x} = A + \underbrace{\dfrac{o(\Delta x)}{\Delta x}}_{\implies 0}$ 
	- $\lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x} = y'(x) = A \implies dy = y'(x) \cdot \Delta x$
- Рассмотрим $y = x$, тогда $y' = 1 \implies \Delta y = \Delta x$. $dy = y'(x)\Delta x \ \implies $ $dx = 1 \cdot \Delta x = \Delta x$.
- Перепишем : $dy = y'(x) dx \implies y'(x) = \dfrac{dy}{dx}$ (Определение производной по Коши)

***Пример***
- $y = x^{n}$
	- $dy = nx^{n - 1}dx \implies \dfrac{dy}{dx} = nx^{n - 1}$ 

### Алгебраические свойства дифференциала
1. $d(u + v) = du + dv$
2. $d(uv) = udv + vdu$
3. $d\left (\dfrac{u}{v} \right) = \dfrac{vdu - udv}{v^{2}}$

## Лекция 02.11.2022
### Необходимое и достаточное условие дифференцируемости функции в точке
- $f$ дифференцируема в $x_{0} \Longleftrightarrow \ \exists f'(x_{0})$ .

***Доказательство***

- Необходимость $\left(\implies \right)$
	- Дано : $f$ дифференцируема в $x_{0}$. Доказать, что она имеет производную в $x_{0}$. Дифференцируемость означает, что в окрестности этой точки $\Delta y = A \cdot \Delta x + o\left(\Delta x\right)$. Поделим обе части на $\Delta x$. $\lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x} = \lim{\Delta x}{0} \left(A + \dfrac{o\left(\Delta x\right)}{\Delta x}\right)$. Получим слева $f'(x_{0})$, а справа число $A$. $\dfrac{o\left(\Delta x\right)}{\Delta x} \implies 0$, при $\Delta x \implies 0 \implies A = f'(x_{0})$
- Достаточность $\left(\Longleftarrow \right)$
	- Дано $f$ имеет в $x_{0}$ производную $f'(x_{0})$. Доказать, что она дифференцируема в $x_{0}$. $\exists f'(x_{0}) = \lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x} \implies \dfrac{\Delta y}{\Delta x} = \underbrace{\lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x}}_{f'(x_{0})} + \alpha(\Delta x), \ \alpha(\Delta x) \implies 0$ при $\Delta x \implies 0 \implies \dfrac{\Delta y}{\Delta x} = f'(x_{0}) + \alpha(\Delta x) \implies \Delta y = \underbrace{f'(x_{0})\Delta x}_{dy} + \underbrace{\alpha(\Delta x)\Delta x}_{o(\Delta x)} \implies f'(x_{0}) = \dfrac{dy}{dx} \implies dy = f'(x)dx$.

***Примеры***

- Найти дифференциалы $f$
- $f(x) = xe^{x^{2}}$
	- $dy = f'(x)dx = e^{x^{2}} + 2x^{2}e^{x^{2}}dx = e^{x^{2}}\left(1 + 2x^{2}\right)dx$ 
- $d(\sin{\sqrt{x}}) = \cos{\sqrt{x}} \cdot \dfrac{1}{2\sqrt{x}}dx$

### Инвариантность формы дифференциала первого порядка
- Для $f$ дифференциал $dy = f'(x)dx$ имеет такую форму записи как в случае независимой переменной $x$, так и в случае когда $x$ - функция независимой переменной.

***Доказательство*** 
- Пусть $\phi(t)$ дифференцируема в $t$, $f(x)$ дифференцируема в $x = \phi(t)$.Тогда рассмотрим $\digamma(t) = f(\phi(t))$. $\digamma'(t) = f'(\phi(t)) \cdot \phi'(t)$. Домножим обе части на $dt \implies$ $\digamma'(t)dt = f'(\phi(t)) \underbrace{\phi'(t)dt}_{dx} \implies d \digamma = f'(\phi(t))dx$. $\phi(t) = x \implies d\digamma = dy = f'(x)dx$ - это и есть инвариантность дифференциала первого порядка.

### Производная и дифференциалы высших порядков
- $y = f(x)$, $\exists f'(x)$. Вторая производная $f$ называется производная от первой производной (если она существует в этой точке).

***Обозначение***

- $f^{(n)}(x) = (f^{(n - 1)}(x))'$
- $\dfrac{d^{n}y}{dx^{n}} = f^{(n)}(x) = \dfrac{d}{dx}\left(\dfrac{d^{n - 1}y}{dx^{n - 1}}\right)$

***Пример***
- Вычислить $n$ - ю производную функций:
- $y = \sin{x}$
	- $y' = \cos{x}, \ y'' = -\sin{x}, \ y''' = -\cos{x} \ \dots$
	- $y^{(n)}(x) = (\sin{x})^{(n)} = \dfrac{d^{n}\sin{x}}{dx^{n}} = \sin{(x + n\dfrac{\pi}{2})}$
- $y = \cos{x}$  
	- $y^{(n)} = \cos{(x + n\dfrac{\pi}{2})}$
- $y = e^{x}$
	- $(e^{x})^{(n)} = e^{x}$
- $y = a^{x}$
	- $y = (a^{x})^{(n)} = a^{x}\ln{x}$
### Формула Лейбница для $n$ - ой производной произведения функций
- $\left(uv\right)^{(n)} = \sum_\limits{k = 0}^{n} \binom{n}{k}u^{(n - k)}v^{(k)}$

### Дифференциал второго порядка и выше в других формах 
- Дифференциал второго порядка и выше не обладает свойством инвариантности, кроме одного исключения, т. е. его форма зависит от того, является ли $x$ независимой переменной $x = \phi(t)$. Пусть $f$ имеет дифференциал в $x, \ dy = f'(x)dx$, пусть уже имеется в этой точке и второй дифференциал, $x$ - независимая переменная. 
- Вычислим второй дифференциал. $d^{2}y = d(dy) = (dy)' = (f'(x)dx)'dx = y''(x)dx \cdot dx = y''(x)dx^{2}$ Для независимой переменной $dx = \Delta x$. $d^{(n)}y = y^{(n)}(x)dx^{n}$
- Пусть $x$ - зависимая переменная. $x = \phi(t)$, дифференцируемая в $t$. Из инвариантности формы первого дифференциала имеем $dy = f'(x)dx$. Берем по определению второй дифференциал этого выражения.
- $d^{2}y = d(dy) = d(f'(x)dx) = d(f'(x))dx + f'(x)d(dx) = y''(x)dx^{2} + y'd^{2}x$

### Исключение в теореме об инвариантности  формы дифференциала первого порядка
- Если $x = \phi(t)$, $\phi(t)$ - линеная функция независимой переменной, то инвариантными оказываются дифференциалы всех порядков (если существуют).

***Доказательство***
- Действительно, например при $\phi(t) = at + b, \ d^{2}y = y''(x)dx^{2} + y'(x)d^{2}x$, где $d^{2}x = d(d(x)) = d(\phi'(t)dt) = d(a)dt = 0$. Поэтому форма $d^{(n)}y = y^{(n)}dx^{n}$ имеет место в случае независимой переменной $x$, а также в случае ее линейной зависимости.

### Теорема об ограниченности функции в некоторой окрестности точки
- Функция, имеющая конечный предел в некоторой точке $x_{0}$ ограничена в некоторой окрестности $x_{0}$.

***Доказательство***

- $\forall \eps > 0 \ \exists \delta > 0: \forall x \in \mathring{U}(x_{0}) \ , \ |x - x_{0}| < \delta \implies |f(x) - b| < \eps$
- Эти неравенства можно записать:
- $|x - x_{0}| < \delta  \Longleftrightarrow x_{0} - \delta < x < x_{0} + \delta$ за вычетом $x_{0}$
- $|f(x) - b| < \eps \Longleftrightarrow b - \eps < f(x) < b + \eps$.
- Это и означает ограниченность.
- Пусть $f(x_{0}) = M$ (произвольное число), тогда для выполнения ограниченности снизу, в качестве нижней границы возьмем $\min{(M, b - \eps)}$, а для ограниченности сверху $\max{(M, b + \eps)}$.

### Теорема о сохранении знака функции в точке.
- Пусть $\exists \lim{x}{x_{0}} f(x) = b \neq 0$. 
- Докажем для $b > 0$, т. е. докажем существование окрестности $x_{0}$, в которой $f$, имеет такой же знак, что и $b$. 
	- По определению предела $x_{0} - \delta < x < x_{0} + \delta \implies b - \eps < f(x) < b + \eps$. Т. к. $\eps$ - любое, возьмем $\eps < |b|$, тогда в $\delta$ - окрестности $x_{0}$ $f(x)$ заключено между двумя положительными числами $f(x) > 0$ 

### Теорема о равенстве нулю функции в окрестности точки.
- Пусть $f$ непрерывна в $x_{0}$ и имеет разные знаки в левой и правой полуокрестностях $x_{0}$. Тогда в $f(x_{0}) = 0$.

***Доказательство***
- Действительно, по определению непрерывной функции $\forall \eps > 0 \ \exists \delta > 0: f(x_{0} + \delta) > 0$ и $f(x_{0} - \delta) < 0$. Т. к. $\exists \lim{x}{x_{0}} f(x) \implies 0 > f(x_{0} - \delta) \leq f(x) \leq f(x_{0} + \delta) > 0$. Это верно для сколь угодно малого $\delta \implies f(x_{0} + 0) = 0, \ f(x_{0} - 0) = 0 \implies f(x_{0}) = 0$.

## Лекция 09.11.2022
### Обобщение теоремы о равенстве нулю функции в окрестности точки
- Непрерывная на отрезке $x \in \left[a; b\right]$ функция, принимающая на нем значения в промежутке $y \in \left[A;B\right], \ y(a) = A, \ y(b) = B$ примет в некоторой точке этого отрезка любое промежуточное значение $C$, такое, что $A < C < B$

***Доказательство***
- Введем вспомогательную функцию $\phi(x) = f(x) - C$, тогда $\phi(x)$ примет на концах значения: $\phi(a) = f(a) - C = A - C < 0, \ \phi(b) = f(b) - C = B - C > 0$. По предыдущей теореме $\phi(x)$ непрерывна на $\left[a;b\right]$ и принимает на его концах значения разных знаков, значит найдется такая точка $c \in \left[a;b\right]$ в которой $\phi(c) = 0$. $\phi(c) - C = 0 \implies f(c) = C$

### Первая теорема Вейерштрасса о непрерывных функциях
- Функция, непрерывная на отрезке ограничена на нем.

***Доказательство***
- Предположим противное, т . е. $f(x)$ не ограничена. Это значит: какое бы положительное число мы бы не взяли, найдется точка на отрезке, в которой функция будет больше этого числа. Возьмем например число 1. На отрезке найдется число $x_{1}$, такое что $f(x_{1}) > 1$, далее возьмем число 2, найдется $x_{2}$, такое что $f(x_{2}) > 2$ и т.д. Для числа $n$ найдется $x_{n}$, такое, что $f(x_{n}) > n$ и т.д. до $\infty$. Элементы последовательности $\{x_{1}, x_{2}, \dots , x_{n}\}$ принадлежат отрезку $\left[a;b\right]$ т.е. $\{x_{n}\}$ ограничена и по теореме Больцано - Вейерштрасса: $\lim{n_{k}}{\infty} x_{n_{k}} = c \in \left[a;b\right]$, а подпоследовательность $f(x_{n_{k}})$ - не ограничена, т.е. у нее нет предела, как у подпоследовательности расходящейся последовательности. А этого не может быть, т. к. $\lim{n}{\infty} f(x_{n_{k}}) = f(c)$ - противоречие.

### Вторая теорема Вейерштрасса о непрерывных функциях
- Функция, непрерывная на отрезке, достигает на нем супремум и инфимум.

***Доказательство***
- Докажем от противного для точной верхней грани $\left(\sup f(x) = M \right)$: Пусть во всех точках  отрезка $\left[a; b\right]$  выполняется $ f(x) \neq M$. Рассмотрим вспомогательную функцию $\phi(x) = \dfrac{1}{M - f(x)}$. Т. к.  $f(x)$ - непрерывна, то и $\phi(x)$ - непрерывна на отрезке $\implies \phi(x)$ - ограничена на нем. $|\phi(x)| = \phi(x) \leq B$. Отсюда: $\dfrac{1}{M - f(x)} \leq B, \ M - f(x) \geq \dfrac{1}{B}, \ f(x) \leq M - \dfrac{1}{B} \implies M = \sup{f(x)}$

### Свойства функций, дифференцируемых на отрезке

***Понятие локального максимума и минимума функции (локального экстремума)***

- $f(x)$ имеет в точке $x_{0}$ максимум, если в некоторой окрестности этой точки выполняется $f(x) \leq f(x_{0})$ и имеет строгий максимум, если в точках окрестности $\left(x \neq x_{0} \right)$ выполняется$\ f(x) < f(x_{0})$. Аналогично для локального минимума и строгого минимума.

### Теорема Ферма
- $f(x)$, дифференцируемая в окрестности точки $x_{0}$ (включая $x_{0}$) имеет в этой точке $f'(x) = 0$, если $x_{0}$ - точка экстремума этой функции.

***Доказательство***

- Путь $x_{0}$ - максимум. $f'(x_{0}) = \lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x}$. Возьмем $\Delta x > 0$, тогда $\Delta y < 0$, т.к. $x_{0}$ - точка максимума и отношение $\dfrac{\Delta y}{\Delta x} < 0$, тогда $\lim{\Delta x}{0 + 0} \dfrac{\Delta y}{\Delta x} \leq 0$, аналогично возьмем $\Delta x < 0, \ \Delta y < 0 \implies \dfrac{\Delta y}{\Delta x} > 0 \implies \lim{\Delta x}{0 - 0} \dfrac{\Delta y}{\Delta x} \geq 0 \implies \lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x} = 0$

### Теорема Ролля
- Если $f$ дифференцируема на интервале $\left(a ; b\right)$ и непрерывна на замкнутом промежутке (включая концы) $\left[a;b\right]$ и на концах промежутка принимает одинаковые значения, то на этом отрезке найдется такая точка $\xi$ в которой $f'(\xi) = 0$.

***Доказательство***

- По предыдущим теоремам, $f$ непрерывна на отрезке, достигает на нем $\max{f} = M$ и $\min{f} = m$. Рассмотрим два случая:
- $M = m \implies f' = const$
- $M \neq m , \ f(a) = f(b) \implies$ либо $m$, либо $M$ принимаются функцией внутри отрезка. Тогда по Т. Ферма $f'$ в точке экстремума равна $0$.

### Теорема Лагранжа (о конечных приращениях)
- Пусть $f$ дифференцируема на интервале $\left(a; b\right)$ и непрерывна на $\left[a;b\right]$, принимает на концах отрезка значения $f(a) \neq f(b)$. Тогда на отрезке $\left[a;b\right]$ существует такая внутренняя точка $\xi$, в которой $f'(\xi) = \dfrac{f(b) - f(a)}{b - a}, \ f(b) > f(a)$.

***Доказательство***

- Введем вспомогательную функцию: $\digamma(x) = f(x) - f(a) - \dfrac{f(b) - f(a)}{b - a} (x - a)$
- Проверим выполнение условий теоремы Ролля для $\digamma(x)$: $\digamma(a) = f(a) - f(a) - \dfrac{f(b) - f(a)}{b - a}(a - a) = 0, \ \digamma(b) = f(b) - f(a) - \dfrac{f(b) - f(a)}{b - a}(b - a) = 0$.
- $\digamma(x)$ дифференцируема на $\left(a;b\right)$ и непрерывна на замкнутом промежутке $\left[a;b\right] \implies $ по Т. Ролля $\exists \ \xi: $ $\digamma'(\xi) = 0 \implies \digamma'(x) = f'(x) - \dfrac{f(b) - f(a)}{b - a} \implies f'(\xi) - \dfrac{f(b) - f(a)}{b - a} = 0 \implies f'(\xi) = \dfrac{f(b) - f(a)}{b - a}$.

### Теорема Коши (о конечных приращениях)
- Пусть $f$ и $g$ дифференцируемы на интревале $\left(a;b\right)$ и непрерывны на отрезке $\left[a;b\right]$, $g'(x) \neq 0$. Тогда найдется такая точка $\xi$ этого отрезка, в которой $\dfrac{f'(\xi)}{g'(\xi)} = \dfrac{f(b) - f(a)}{g(b) - g(a)}$

***Доказательство***
- Введем вспомогательную функцию $\digamma(x) = f(x) - f(a) - \dfrac{f(b) - f(a)}{g(b) - g(a)} (g(x) - g(a))$. Проверим выполнение условий теоремы Ролля:
- $\digamma(a) = 0, \ \digamma(b) = 0$, $\digamma$ - непрерывна и дифференцируема $\implies \exists \xi: \ \digamma(\xi) = 0, \ \digamma'(x) = f'(x) - \dfrac{f(b) - f(a)}{g(b) - g(a)} \cdot g'(x)$
- $f'(\xi) = \dfrac{f(b) - f(a)}{g(b) - g(a)} \cdot g(\xi) = 0 \implies \dfrac{f'(\xi)}{g'(\xi)} = \dfrac{f(b) - f(a)}{g(b) - g(a)}$

## Лекция 16.11.2022
### Правило Лопиталя
- Пусть в окрестности точки $a$ определены две бесконечно малые $f$ и $g$ (в самой точке они могут быть не определены), непрерывны и дифференцируемы в проколотой окрестности точки $a$, причем $g' \neq 0$ в этой окрестности. Тогда, $\exists \lim{x}{a} \dfrac{f(x)}{g(x)} = \ \lim{x}{a} \dfrac{f'(x)}{g'(x)}$

***Доказательство***
- $f, \ g$ - непрерывны и дифференцируемы в проколотой окрестности $a$, доопределим их пределом, равным нулю $f(a) = g(a) = 0$. Тогда они станут непрерывными на всей окрестности точки $a$. Рассмотрим последовательность $\{x_{1}, x_{2}, \dots, x_{n}, \dots\}$ таких, что $\lim{n}{\infty}{x_{n}} = a$ начиная с некоторого номера все члены последовательности будут принадлежать рассмотренной окрестности. Возьмем из них точку $x_{k}$ и рассмотрим отрезок $\left[a, x_{k}\right] \ (x_{k} > a)$. Тогда на этом отрезке $f, \ g$ непрерывны и дифференцируемы на интервале $(a , x_{k})$. На этом промежутке выполнено условие теоремы Коши о конечных приращениях, то есть $\exists \xi_{k} \in (a, x_{k})$, в которой $\dfrac{f(x_{k}) - f(a)}{g(x_{k}) - g(a)} = \dfrac{f'(\xi_{k})}{g'(\xi_{k})}$. $f(a) = g(a) = 0 \implies \dfrac{f(x_{k})}{g(x_{k})} = \dfrac{f'(\xi_{k})}{g'(\xi_{k})}$. $k \to \infty, \ x_{k} \to a \implies \xi_{k} \to a$. $\exists \lim{k}{\infty} \dfrac{f'(\xi_{k})}{g'(\xi_{k})} \implies \exists \lim{x}{a} \dfrac{f(x_{k})}{g(x_{k})} = \ \lim{x}{a} \dfrac{f'(x_{k})}{g'(x_{k})} \implies \lim{x}{a} \dfrac{f(x)}{g(x)} = \ \lim{x}{a} \dfrac{f'(x)}{g'(x)}$.

***Пример***

- Найти:  $\lim{x}{0} \dfrac{1 - \cos{x}}{x^{2}}$
	- $\lim{x}{0} \dfrac{f'(x)}{g'(x)} = \ \lim{x}{0} \dfrac{\sin{x}}{2x} = \dfrac{1}{2}$ 
- Найти:  $\lim{x}{0} \dfrac{x - \sin{x}}{x^{3}}$.
	- $\lim{x}{0} \dfrac{f'(x)}{g'(x)} = \ \lim{x}{0} \dfrac{1 - \cos{x}}{3x^{2}} = \ \lim{x}{0} \dfrac{\sin{x}}{6x} = \dfrac{1}{6}$

***Замечание***
- Правило Лопиталя применимо и на полубесконечном промежутке $x \in \left[1; + \infty \right)$, $x \to + \infty, \ f(x) \to 0, \ g(x) \to 0$. А также, для раскрытия неопределенности вида $\dfrac{\infty}{\infty}$ .

***Пример***

- $\exists \lim{x}{a} \dfrac{f(x)}{g(x)}$, но правило Лопитая не выполнено, так как $\nexists  \ \lim{x}{a} \dfrac{f'(x)}{g'(x)}$.
	- $\lim{x}{0} \dfrac{x^{2} \sin{\dfrac{1}{x}}}{\sin{x}} = \ \lim{x}{0} \dfrac{x \cdot x \cdot \sin{\dfrac{1}{x}}}{\sin{x}} = 0$
	
- Найдем предел отношения производных
	- $\lim{x}{0} \dfrac{2x\sin{\dfrac{1}{x}} + x^{2} \cos{\dfrac{1}{x}} \left(- \dfrac{1}{x^{2}}\right)}{\cos{x}}$ - не существует, $\nexists \lim{x}{0} \cos{\dfrac{1}{x}}$
	
	- $\lim{x}{0} \dfrac{e^{-x^{2}} - \cos{x}}{\ln{(1 + 3x^{2}})} = \ \lim{x}{0} \dfrac{e^{-x}(-2x) + \sin{x}}{\dfrac{1}{3}x^{2} \cdot 6x} = \\ \ \lim{x}{0} \dfrac{(-2xe^{x^{2}} + \sin{x})(1 + 3x^{2})}{6x} = \ \lim{x}{0} \dfrac{\left[-2e^{-x^{2}} - 2xe^{-x^{2}} (-2x) + \cos{x}\right] \cdot (1 + 3x^{2}) + \left[-2xe^{-x^{2}} + \sin{x}\right]6x}{6} = - \dfrac{1}{6}$
	
### Формула Тейлора

***Теорема***
- Пусть $f$ имеет в окрестности точки $a$ производные порядков до $n + 1$ включительно. Тогда в любой точке $x$ этой окрестности $f$ представима в виде :
- $f(x) = f(a) + \dfrac{f'(a)}{1!}(x - a) + \dfrac{f''(a)}{2!}(x - a)^{2} + \dots + \dfrac{f^{n}(a)}{n!}(x - a)^{n} + R_{n + 1}$ - Многочлен Тейлора $\Phi(x, a)$ с центром в точке $a$  и остаточным членом $R_{n + 1} = \left(\dfrac{x - a}{x - \xi}\right)^{p} \cdot \dfrac{\left(x - \xi\right)^{n + 1}}{n! \cdot p} \cdot f^{(n + 1)}(\xi)$, где $\xi$ - некоторая точка в окрестности точки $a$.

***Доказательство***

- Введем вспомогательную функцию $\psi(t) = f(x) - \Phi(x, t) - R_{n + 1}, t \in \left[a ;x \right]$. Запишем $R_{n + 1} = (x - t)^{p} \cdot Q(x)$. Проверим значение $\psi(t)$ на концах промежутка $t \in \left[a; x\right]$.
- $\psi(a) = f(x) - \Phi(a, a) - R_{n + 1}= 0$
- $\psi(x) = f(x) - \Phi(x, x) - R_{n + 1} = 0$.
- Условия теоремы Ролля выполнены $\implies$ $\exists \xi \in \left[a; x\right]$ ,  $\psi'(\xi) = 0$
- $\psi(t) = f(x) - f(t) - \dfrac{f'(t)}{1!}(x - С) - \dfrac{f''(t)}{2!}(x - С)^{2} - \dots - \dfrac{f^{(n)}(t)}{n!}(x - С)^{n} - (x - С)^{P} \cdot Q(x)$
- $\psi'(\xi) = - f'(\xi) - \dfrac{f''(\xi)}{1!}(x - \xi) + \dfrac{f'(\xi)}{1!} - \dfrac{f'''(\xi)}{2!}(x - \xi)^{2} + \dfrac{f''(\xi)}{1!}(x - \xi) + \dfrac{f^{(4)}(\xi)}{3!}(x - \xi)^{3} \\ \dots - \dfrac{f^{(n + 1)}(\xi)}{n!}(x - \xi)^{n} + \dfrac{f^{(n)}(\xi)}{(n - 1)!}(x - \xi)^{n - 1} + p(x - \xi)^{p - 1} \cdot Q(x)$
- $\psi'(\xi) = -\dfrac{f^{(n + 1)}(\xi)}{n!}(x - \xi)^{n} + p(x - \xi)^{p - 1} \cdot Q(x) = 0$
- $Q(x) = \dfrac{f^{(n + 1)}(\xi)}{n!} \cdot \dfrac{(x - \xi)^{n}}{p(x - \xi)^{p - 1}} = \dfrac{f^{(n + 1)}(\xi)}{n!p}(x - \xi)^{n - p + 1}$
- $R_{n + 1} = \dfrac{(x - a)^{p} \cdot f^{(n + 1)}(\xi)(x - \xi)^{n - p + 1}}{n!p} = \left(\dfrac{x - a}{x - \xi}\right)^{p} \cdot \dfrac{(x - \xi)^{n + 1}}{n!p} \cdot f^{(n + 1)}(\xi)$

***Пример***

- Разложить в точке $a$ произвольный многочлен степени $n$
- $P_{n}(x) = C_{n}x^{n} + C_{n - 1}x^{n - 1} + \cdots + C_{1}x + C_{0} = \underbrace{P(a) + \dfrac{P_{n}'(a)}{1!}(x - a) + \dfrac{P_{n}''(a)}{2!}(x - a)^{2} + \dots + \dfrac{P_{n}^{(n)}(a)}{n!}(x - a)^{n}}_{\Phi(x, a)} \implies R_{n + 1} = 0$
- $\Phi(a, a) = f(a)$
- $\Phi'(a, a) = f'(a)$
- $\Phi''(a, a) = f''(a)$
- $\Phi^{(n)}(a, a) = f^{(n)}(a)$

## Лекция 23.11.2022
### Остаточный член в трех видах
- Запишем остаточный член $R_{n + 1}$ в трех видах:
	- В форме Лагранжа при $p = n + 1$, то есть $R_{n + 1} = \dfrac{(x - a)^{n + 1}}{(n + 1)!} \cdot f^{(n + 1)}(\xi)$ 
	- В форме Коши. Введем вместо $\xi \in \left[a, x\right]$ промежуточную $\theta \in \left[0, 1\right] , p = 1$
		- $ \xi = a + \theta(x - a)$
		- $ R_{n + 1}  =  \dfrac{\left(x - a\right)}{n!} \cdot f^{(n + 1)}(\xi)(x - \xi)^{n}$
		- $x - \xi = x - a - \theta(x - a) = (x - a)(1 - \theta)$
		- $R_{n + 1} = \dfrac{(x - a)(x - a)^{n}(1 - \theta)^{n}}{n!} \cdot f^{(n + 1)}(a + \theta(x - a))$
		- $R_{n + 1} = \dfrac{(x - a)^{n + 1}(1 - \theta)^{n}}{n!} \cdot f^{(n + 1)}(a + \theta(x - a))$
	- В форме Пеано. $R_{n + 1} = o((x - a)^{n})$ 
### Доказательство формулы Тейлора с остаточным членом в форме Пеано
***Доказательство***

- Докажем $\lim{x}{a} \dfrac{R_{n + 1}}{(x - a)^{n}} = 0$
-  $ \lim{x}{a} R_{n + 1} = 0$
- Еще одно преимущество в форме Пеано - если формула Тейлора требует существования всех производных $f(x)$ до $n + 1$ порядка включительно в окрестности точки $a$, то в форме Пеано верна, при наличии $n$ - ого порядка производных в точке $a$ и $n - 1$ в окрестности $a$ .
- $\lim{x}{a} \dfrac{R_{n + 1}(x)}{(x - a)^{n}} = \dfrac{0}{0}$ - Используем правило Лопиталя. 
- $\lim{x}{a} \dfrac{(R_{n + 1}(x))'}{n(x - a)^{n - 1}} = \dfrac{0}{0}$ - Повторим $n - 1$ раз. 
- $\lim{x}{a} \dfrac{R^{(n - 1)}_{n + 1}(x) - R_{n + 1}^{(n - 1)}(a)}{n!(x - a)} = \dfrac{R^{(n)}_{n + 1}}{n!}= 0$

### Оценка остаточного члена в формуле Тейлора  
- Рассмотрим класс функций, для которых все производные любого порядка ограничены одной и той же константой $M$ в окретности точки $a$
- Используем форму Лагранжа и точку разложения возьмем $a = 0$ (Тогда формула Тейлора называется формулой Маклорена)
- $f(x) = f(0) + \dfrac{f'(0)}{1!}x + \dfrac{f''(0)}{2!}x^{2} + \dots + \dfrac{f^{(n)}(0)}{n!}x^{n} + R_{n + 1}$
- $R_{n + 1} = \dfrac{x^{n + 1}}{(n + 1)!} \cdot f^{(n + 1)}(\theta x)$
- $\left|R_{n + 1} \right| \leq \dfrac{\left|x\right|^{n + 1}}{(n + 1)!} \cdot M$

***Пример***
- $f(x) = e^{x}$. В окрестности точки $0$ все производные $e^{x}$ на отрезке $x \in \left[-r; r\right], \ M = e^{r}$
  - $\left|R_{n + 1}\right| \leq \dfrac{e^{r}\left|x\right|^{n + 1}}{(n + 1)!}$
- $f(x) = \sin{x}; \ f(x) = \cos{x}; \ M = 1$
  - $\left|R_{n + 1}\right| \leq \dfrac{|x|^{n + 1}}{(n + 1)!}$

### Формула Маклорена для некоторых элементраных функций
- $e^{x} = 1 + x + \dfrac{x^{2}}{2!} + \dfrac{x^{3}}{3!} + \dots + \dfrac{x^{n}}{n!} + R_{n + 1}$
	- $R_{n + 1} = \dfrac{x^{n + 1}}{(n + 1)!} e^{\theta x}, \ (0 \leq \theta \leq 1), \ x \in \left[-r; r\right]$
	
	- $\left|R_{n + 1}\right| \leq \dfrac{r^{n + 1}}{(n + 1)!}$
- $\sin{x}$
	- $f^{(n)}(x) = \sin{\left(x + n \cdot \dfrac{\pi}{2}\right)}$
	- $f^{(n)}(x) = 0$ - Для четных $n$
	- $n = 2k + 1$
	- $\sin{x} = x - \dfrac{x^{3}}{3!} + \dfrac{x^{5}}{5!} - \dots + (-1)^{k} \dfrac{x^{2k + 1}}{(2k + 1)!} + R_{n + 2}$
- $\cos{x}$
	- $\left(\cos{x}\right)^{(n)} = \cos{\left(x + n \cdot \dfrac{\pi}{2} \right)}$ 
	- $\cos{x} = 1 - \dfrac{x^{2}}{2!} + \dfrac{x^{4}}{4!} - \dfrac{x^{6}}{6!} \dots + \dfrac{(-1)^{k}x^{2k}}{(2k)!} + R_{n + 2}$
- $\ln{\left(1 + x\right)}$
  - $\ln{\left(1 + x\right)} = x - \dfrac{x^{2}}{2} + \dfrac{x^{3}}{3} - \dfrac{x^{4}}{4} + \dots + (-1)^{(n - 1)} \dfrac{x^{n}}{n} + R_{n + 1}$
  - $\ln'{\left(1 + x\right)} = \dfrac{1}{1 + x} \bigg|_{x = 0} = 1$
  - $\ln''{\left(1 + x\right)} = - \dfrac{1}{(1 + x)^{2}} \bigg|_{x = 0} = -1$
  - $\ln'''{\left(1 + x\right)} = \dfrac{2}{(1 + x)^{3}} \bigg|_{x = 0} = 2$
- Биноминальное разложение
	- $\left(1 + x\right)^{\alpha} = 1 + \alpha x + \dfrac{\alpha(\alpha - 1)}{2!}x^{2} + \dfrac{\alpha(\alpha - 1)(\alpha - 2)}{3!}x^{3} + \dots + \dfrac{\alpha(\alpha - 1) \dots (\alpha - n + 1)}{n!}x^{n} + R_{n + 1}$  

## Лекция 30.11.2022
### Нахождение пределов используя формулу Маклорена
- $\lim{x}{0} \dfrac{\sin{x} - x}{x^{3}} = \ \lim{x}{0} \dfrac{x - \dfrac{x^{3}}{3!} + o(x^{4}) - x}{x^{3}} = - \dfrac{1}{6}$
- $\lim{x}{0}  \dfrac{e^{- \dfrac{x^{2}}{2}} - \cos{x}}{x^{4}} = \ \lim{x}{0} \dfrac{1 - \dfrac{x^{2}}{2} + \dfrac{x^{4}}{2!\cdot 4} + o(x^{4}) - 1 - \dfrac{x^{2}}{2!} - \dfrac{x^{4}}{4!} + o(x^{4})}{x^{4}} = \dfrac{1}{8} - \dfrac{1}{24} = \dfrac{1}{12}$
- $y = \left(\cos{x} + \dfrac{x^{2}}{2}\right)^{\dfrac{1}{x(\sin{x} - 1)}}$
	- $\lim{x}{0} \ln{y} = \dfrac{\ln{\left(\cos{x} + \dfrac{x^{2}}{2}\right)}}{x(\sin{x} - x)} = \ \lim{x}{0} \dfrac{\left(1 - \dfrac{x^{2}}{2} + \dfrac{x^{4}}{4!} + o(x^{4}) + \dfrac{x^{2}}{2}\right)}{x\left(x - \dfrac{x^{3}}{3!} + o(x^{4}) - x\right)} = \ \lim{x}{0} \dfrac{\ln{\left(1 + \dfrac{x^{4}}{4!} + o(x^{4})\right)}}{-\dfrac{x^{4}}{6} + o(x^{4})} = \ \lim{x}{0} \dfrac{\dfrac{x^{4}}{4!} + o(x^{4})}{- \dfrac{x^{6}}{6} + o(x^{4})} = - \dfrac{6}{24} = - \dfrac{1}{4}$

### Убывающие и возрастающие функции
- $f(x) \uparrow \ x \in$  $\left[a; b\right]$$ \ \Longleftrightarrow$ $\forall x_{2} > x_{1} \in \left[a; b\right] \implies f(x_{2}) > f(x_{1})$
- $f(x) \downarrow \ x \in$ $\left[a; b\right]$$ \ \Longleftrightarrow$ $\forall x_{2} > x_{1} \in \left[a; b\right] \implies f(x_{2}) < f(x_{1})$
- Аналогично для неубывающей и невозрастающей.

### Монотонные функции
- Возрастающие и убывающие функции называются монотоными

### Теорема о связи знака производной с возрастанием и убыванием функци

***Теорема***

- Если у дифференцируемой на промежутке $f$ в каждой точке производная положительна, то  $f \uparrow$ на этом промежутке. Если отрицательна, то $f \downarrow$.

***Доказательство***

- Действительно, пусть $f'(x) > 0, \ x \in \left[a; b\right] \implies f$ сохраняет знак в некоторой окрестности $x$. $\dfrac{\Delta f}{\Delta x} > 0 : \Delta x > 0 \implies \Delta f > 0; \ \Delta x < 0 \implies  \Delta f < 0$. Аналогично для $f'(x) < 0$.

### Возрастание (убывание) в точке
- $x_{0}$ называется точкой возрастания, если в левой (как угодно малой) окрестности $x_{0}: f(x) < f(x_{0})$, а в правой $f(x) > f(x_{0})$. Аналогично для точки убывания.

### Утверждение о неотрицательной производной
- Если $f$ дифференцируема в окрестности $x_{0}$ и $x_{0}$ - точка возрастания $\implies f'(x_{0}) \geq 0$. 
- Если $f$ дифференцируема в окрестности $x_{0}$ и $f'(x_{0}) > 0 \implies \ x_{0}$ - точка возрастания.

***Пример***
- $f(x) = x^{3}, \ x_{0} = 0$
- $f'(x_{0}) = 0 \implies $ $x_{0}$ - точка возрастания.

### Экстремум функции 
- $x_{0} $  -  $\max$ функции $f \Longleftrightarrow$ в окрестности $x_{0}: f(x) \leq f(x_{0})$
- $x_{0}$ - строгий  $ \max$ функции $f \Longleftrightarrow$ в окрестности $x_{0}: f(x) < f(x_{0})$
- Аналогично для $\min$.

### Теорема Ферма
- $f$ дифференцируема в окрестности точки возможного экстремума $\implies f$ имеет экстремум, если $f'$ меняет знак при переходе через эту точку.

### Первое достаточное условие экстремума
- $f$ - дифференцируема в окрестности точки возможного экстремума. $f'$ меняет знак с плюса на минус $x_{0}$. Тогда$ \dfrac{\Delta f}{\Delta x} < 0, \ \Delta x > 0 \implies \Delta f > 0; \  \dfrac{\Delta f}{\Delta x} > 0, \ \Delta x < 0 \implies \Delta f < 0$. А это и значит $\max$. Аналогично для $\min$.

### Второе достаточное условие экстремума
- Если $x_{0}$ - точка возможного экстремума, $f'(x) = 0$, то $f''(x_{0}) < 0 \implies x_{0} = \max; f''(x_{0}) > 0 \implies x_{0} = \min$

***Доказательство***

- Пусть $x_{0}$ - точка возможного экстремума, $\exists f'$ в некоторой окрестности $x_{0}$. $f''(x_{0}) = \ \lim{\Delta x}{0} \dfrac{\Delta f'}{\Delta x}$. Пусть далее $f''(x_{0}) < 0$. Значит, в окрестности $x_{0}$: $\dfrac{\Delta f'}{\Delta x} < 0$. $\Delta x > 0 \implies \Delta f' < 0, \ f'(x_{0}) = 0$, то есть производная изменила знак на отрицательный, аналогично, $\Delta x < 0, \ \dfrac{\Delta f'}{\Delta x} < 0 \implies \Delta f' > 0, \ f'(x_{0}) = 0$. То есть левее $x_{0}$ производная больше нуля $\implies x_{0}$ - точка $\max$. Аналогично для $\min$.

***Пример***
- Найти $\min{f}, \ \max{f}$,  $f \uparrow, f \downarrow$.
- $f(x) = 3x^{3} - x^{2} - 2x + 5$
	- $f'(x) = 9x^{2} - 2x - 2 = 0$
	- $D = 76 \implies x_{1,2} = \dfrac{2 \pm \sqrt{76}}{18} = \dfrac{1 \pm \sqrt{19}}{9}$
	- $9x^{2} - 2x - 2 = 9(x - \dfrac{1 + \sqrt{19}}{9})(x - \dfrac{1 - \sqrt{19}}{9})$ 
	- $f''(x) = 18x - 2 = 2(9x - 1) \implies \dfrac{1 - \sqrt{19}}{9} = \max, \dfrac{1 + \sqrt{19}}{9} = \min$

## Лекция 06.12.2022
### Выпуклость и вогнутость графика функции
- Пусть дифференцируема на некотором интервале $(a;b)$ $f$ всюду на этом интервале имеет график, расположенный ниже касательной в соответствующей точке, то в этой точке график имеет выпуклость вверх, если ниже, то выпуклость вниз (вогнутость).

***Утверждение***
- Если в окрестности некоторой точки $C$ вторая производная (если существует) не меняет знака и отрицательна, то в окрестности этой точки график функции направлен выпуклостью вверх, если положительна, то вниз. Пусть в окрестности $C$ $f''(x)$ отрицательна. Напишем уравнение касательной, проведенной в этой точке.  Пусть $Y$ - ордината к касательной, а $y$ - ордината графика функции. $Y =  f(С) + f'(С)(x - С)$
- Разложим функцию $y = f(x)$ в точке $C$ по формуле Тейлора:
	- $f(x) = f(С) + f'(С)(x - С) + \dfrac{f''(\xi)}{2!}(x - С)^{2}$ 
	- $y - Y = \dfrac{f''(\xi)}{2!}(x - С)^{2}$
- $f''(\xi) < 0 \implies y - Y < 0, \ y < Y$, а это и есть определение выпуклости вверх

### Точка перегиба графика
- Если дифференцируемая в окрестности $C$ и $f$ меняет при переходе через эту точку направление выпуклости, то точка $C$ называется точкой перегиба
- Это также означает, что при переходе через $C$, $ \ f''$ (если существует) меняет знак

### Третье достаточное условие экстремума и точки перегиба
- Пусть $f$ дифференцируема в окрестности $C$ $n$ раз, а в $C$ - $(n + 1)$ раз. Если в точке $C$ производные до $n$ -ого порядка включительно равны нулю, $f^{(n + 1)}(C) \neq 0 \implies$  при $n$ - нечетном точка $C$ является точкой экстремума, а именно если  $f^{(n + 1)}(C) < 0$, то $\max$, если $f^{(n + 1)}(C) > 0$, то $\min$. Если $n$ - четное, то $C$ - точка перегиба.

***Доказательство***
- Действительно, пусть $n$ - нечетное, тогда при $f^{(n + 1)}(C) \neq 0$ для $f^{(n)}(x)$ как функции, для которой $f^{(n + 1)}$ - ее первая производная, $C$ - точка возрастания (убывания) для $f^{(n)}(x)$. Рассмотрим разложение по формуле Тейлора в точке $C$ второй производной:
	- $f''(x) = f''(C) + \dfrac{f'''(C)}{1!}(x - C) + \dots + \dfrac{f^{(n)}(C)}{n!}(x - C)^{n} + \dfrac{f^{(n + 1)}(\xi)}{(n + 1)!}(x - C)^{n + 1}$
	- Так как по условию все производные до $n$ включительно равны нулю в точке $C \implies f''(x) =\dfrac{f^{(n + 1)}(\xi)}{(n + 1)!}(x - C)^{n + 1}$
	- $f^{(n + 1)}(\xi) < 0 \implies f''(x) < 0 \implies \max$
	- $f^{(n + 1)}(\xi) > 0 \implies f''(x) > 0 \implies \min$
- Пусть $n$ - четное, $f^{(n + 1)}(\xi) \neq 0$. Разложим по формуле Тейлора $f'(x)$.
	- $f'(x) = f'(C) + \dfrac{f''(\xi)}{1!}(x - C)$. 
    - $f'(x) = \dfrac{f''(\xi)}{1!}(x - C)$. $(x - C)$ меняет знак при переходе, значит $f'(x)$ меняет знак при переходе через $C$.

### План исследования и построения графика функции
- Найти область определения функции
- Выяснить симметрию функции (четность, периодичность)
- Исследовать поведение функции вблизи границ ее области определения
- Найти точки пересечения графика с осями координат
- Найти асимптоты графика
- Вычислить производную и по ней найти промежутки возрастания (убывания), экстремум
- Найти промежутки выпуклости (вогнутости) графика и точки перегиба
- Построить график

### Определение асимптоты
- Прямая $x = a$ называется вертикальной асимптотой графика $f$ в точке $a$, если какой - либо из односторонних пределов функции в этой точке равен  $\pm \infty$.
- Прямая $y = kx + b$ называется наклонной асимптотой графика функции при $x \implies \pm \infty$, если при этом расстояние между графиком функции и асимптоты стремится к нулю.

### Необходимое и достаточное условие наклонной асимптоты
- $\lim{x}{\pm \infty} \dfrac{f(x)}{x} = k, \ \lim{x}{\pm \infty} \left(f(x) - kx\right) = b$.

***Доказательство***

- Действительно: $\lim{x}{\pm \infty} \dfrac{y_{f}}{y_{a}} = 1$
	- $\lim{x}{\pm \infty} \dfrac{f(x)}{kx + b} = 1 \Longleftrightarrow \lim{x}{\pm \infty} \dfrac{f(x)}{x} = k$
	- Стремление расстояния к нулю также означает: $(y_{f} - y_{a}) \implies 0 \implies \lim{x}{\pm \infty}\left[f(x) - (kx + b)\right] = 0 \Longleftrightarrow \lim{x}{\pm \infty}(f(x) - kx) = b$ 

### Пример исследования функции
- Исследовать $y = \dfrac{2x^{3} - 5x^{2} + 14x - 6}{4x^{2}}$
	- Область определения: $\left(-\infty; 0\right) \ \cup (0; +\infty)$ 
	- Симметрия: Отсутствует (функция общего вида)
	- Поведение вблизи границ: 
		- $\lim{x}{-\infty} \dfrac{2x^{3} -5x^{2} + 14 - 6}{4x^{2}} = -\infty$
		- $\lim{x}{+\infty} \dfrac{2x^{3} -5x^{2} + 14 - 6}{4x^{2}} = +\infty$
		- $\lim{x}{0} \dfrac{2x^{3} -5x^{2} + 14 - 6}{4x^{2}} = -\infty$
	- Точки пересечения с осями координат :
		- Решить $2x^{3} -5x^{2} + 14 - 6 = 0$
	- Асимптоты:
		- Вертикальные: $x = 0$
		- Наклонные:
		- $k = \lim{x}{\pm \infty} \dfrac{2x^{3} - 5x^{2} + 14x - 6}{4x^{3}} = \dfrac{1}{2}$
		- $b =  \lim{x}{\pm \infty} \dfrac{2x^{3} - 5x^{2} + 14x - 6}{4x^{2}} - \dfrac{x}{2} = - \dfrac{5}{4}$
		- $y = \dfrac{x}{2} - \dfrac{5}{4}$
	- Производные: 
		- $f(x) = \dfrac{1}{4}\left(2x - 5 + \dfrac{14}{x} - \dfrac{6}{x^{2}}\right)$
		- $f'(x) = \dfrac{1}{4}\left(2 - \dfrac{14}{x^{2}} + \dfrac{12}{x^{3}}\right) = \dfrac{x^{3} - 7x + 6}{2x^{3}}$
	- Промежутки $\uparrow, \ \downarrow$ , экстремум:
		- $x^{3} - 7x + 6 = 0 \implies x(x^{2} - 1) - 6(x - 1) = 0 \implies$ Корни: -3, 2.
	- Точки перегиба:
		- $f''(x) = \dfrac{1}{2} \dfrac{7(3x^{2} - 7) - (x^{3} - 7 + 6 )3x}{x^{6}} = 0$
		- $x = - \dfrac{9}{7}$ 
## Лекция 13.12.2022
### Первообразная и неопределенный интеграл
- Пусть на некотором промежутке задана $f(x)$. Первообразная для этой функции на этом промежутке называется функция дифференцирования на этом промежутке $F(x)$, такая что $F'(x) = f(x)$.
- Первообразная определена неоднозначно, т.к. если $F(x)$ - первообразная, то $F(x) + C$ - тоже первообразная.

### Теорема об отличии первообразных на постоянные на промежутке

***Теорема***

- Любые две первообразные функции $f(x)$ на данном промежутке могут отличаться только на постоянные слагаемые

***Доказательство***

- Пусть на $\left(a;b\right)$ $f(x)$ имеет первообразные $F_{1}(x)$ и $F_{2}(x)$. Докажем, что отличаются на $C$. Введем функцию $\Phi(x) = F_{1}(x) + F_{2}(x)$ в любой точке $x$. $\Phi(x)' = F_{1}(x)'  + F_{2}(x)' = f(x) - f(x) = 0$. Если $x$ - любая точка просматриваемого промежутка, то по теореме Лагранжа о конечных приращениях существует внутри промежутка точка $\xi$, что $\Phi(b) - \Phi(a) = \Phi'(\xi)(b - a)$. $\Phi(x + \Delta x) - \Phi(x) = \Phi'(\xi) \Delta x$,  $\Phi'(\xi) = 0 \implies \Phi(x + \Delta x) = \Phi(x)  \implies \Phi(x) = const \implies F_{1}(x) - F_{2}(x) = C \implies F_{1}(x) = F_{2}(x) + C$.

***Определение***
- Если известна какая - то первообразная, то совокупность всех первообразных имеет вид $F(x) + C$ и называется неопределенным интегралом

***Обозначение***
- $F(x) + C = \int f(x) dx $

### Алгебраические свойства неопределенного интеграла
- $d\left(\int f(x) dx \right) = \left( F(x) + C \right) ' dx = F'(x) dx = dF(x)$
- $\int dF = \int F'(x) dx = \int f(x) dx + C$
- $\int \left(\alpha f(x) + \beta g(x) \right) dx = \alpha \int f(x) dx + \beta \int g(x) dx$

### Таблица неопределенных интегралов
№|f(x) | F(x) 
:------:|:--------:|------:
1 |  $C$ | $Cx + C_{1}$
2 |$x^{n}$     | $\dfrac{x^{n + 1}}{n + 1} + C$ 
3 |$\dfrac{1}{x}$     | $\ln{x} + C$ 
4 |$a^{x}$     | $\dfrac{a^{x}}{\ln{a}} + C$
5 |$e^{x}$     | $e^{x} + C$
6 |$\sin{x}$     | $- \cos{x} + C$   
7 |$\cos{x}$     | $\sin{x} + C$
8 |$\dfrac{1}{\cos^{2}{x}}$     | $ \tan{x} + C$ 
9 |$- \dfrac{1}{\sin^{2}{x}}$     | $\cot{x} + C$ 
10 |$\dfrac{1}{\sqrt{1 + x^{2}}}$     | $ \arcsin{x} + C$
11 |$- \dfrac{1}{\sqrt{1 + x^{2}}}$     | $\arccos{x} + C$
12 | $\dfrac{1}{1 + x^{2}}$    | $\arctan{x} + C$  
13 |$- \dfrac{1}{1 + x^{2}}$     | $arccot{(x)} + C$ 
14 |$sh{(x)}$     | $ch{(x)} + C$ 
15 |$ch(x)$     | $sh(x) + C$ 
16 | $\dfrac{1}{\sqrt{a^{2} - x^{2}}}$ | $\arcsin{\dfrac{x}{a}} + C$
17 | $\dfrac{1}{a^{2} +x^{2}}$ | $\dfrac{1}{a} \arctan{\dfrac{x}{a}} + C$ 
18 | $\dfrac{1}{a^{2} - x^{2}}$ | $\dfrac{1}{2a} \ln{\dfrac{a + x}{a - x}} + C$ 
19 | $\dfrac{1}{\sqrt{x^{2} \pm a^{2}}}$ | $\ln{(x + \sqrt{x^{2} \pm a^{2}})}+ C$ 

### Методы интегрирования 
- Метод замены переменной
	- Пусть имеем $\int f(x) dx$, если $x = \phi(t)$, так что $dx = \phi'(t) dt$, то обозначив первообразную функции $f(\phi(t))$ через $G(t)$ получим $\int f(\phi(t)) dt = G(t) + C \implies G'(t) = f(\phi(t)) \cdot \phi(t) \implies G(t) = \int f(\phi(t))\phi'(t) dt = \int f(x) dx$ 
- Метод интегрирования по частям
	- $d(u(x) v(x)) = udv + vdu$
	- $\int d(uv) dx = \int u dv + \int v du$
	- $\int u dv = uv - \int v du$
## Лекция 20.12.2022
### Интегрирование рациональных функций
- Пусть имеем правильную несократимую дробь $\dfrac{P(x)}{Q(x)}$. Пусть далее многочлен $Q(x)$ имеет корень $x = a$ кратности $\alpha$, т. е. $Q(x) = (x - a)^{\alpha}\phi(x)$, причем $\phi(a) \neq 0$.

### Теорема о разложении дроби на простейшие
- $\dfrac{P(x)}{Q(x)} = \dfrac{A}{(x  - a)^{\alpha}\phi(x)} + \dfrac{\psi(x)}{(x - a)^{\alpha - k}\phi(x)}, \ k \geq 1$

***Доказательство***

- $\dfrac{P(x)}{Q(x)} = \dfrac{A}{(x - a)^{\alpha}\phi(x)} + \dfrac{P(x) - A\phi{(x)}}{Q(x)}\bigg|_{A = \dfrac{P(a)}{\phi(a)}} = \dfrac{\Phi(x)}{Q(x)}  = \dfrac{A}{(x - a)^{\alpha}} + \dfrac{(x - a)^{k}\psi(x)}{Q(x)} = \dfrac{A}{(x - a)^{\alpha}} + \dfrac{\psi(x)}{(x - a)^{\alpha - k}\phi(x)}$

***Замечание***
- Если $Q(x)$ имеет комплексный корень $x = u + iv$, тогда он имеет комплексно - сопряженный корень $\upline{x} = u - iv$, т. е. $Q(x) = \left(u + iv\right)\left(u - iv \right) = u^{2} + v^{2}$. Обычно этот множитель встречается в виде $Q(x) = \left(x^{2} + px + q\right)^{\alpha} \cdot \phi(x) \implies \dfrac{P(x)}{Q(x)} = \dfrac{Mx + N}{(x^{2} + px + q)^{\alpha}} + \dfrac{\psi(x)}{(x^{2} + px + q)^{\alpha - k}\phi(x)}$

***Общий вид разложения рациональной дроби на простейшие***

- $\dfrac{P(x)}{Q(x)} = \dfrac{A_{1}}{(x - a)^{\alpha}} + \dfrac{A_{2}}{(x - a)^{\alpha - 1}} + \dots + \dfrac{A_{\alpha}}{x - a} + \dfrac{B_{1}}{(x - b)^{\beta}} + \dfrac{B_{2}}{(x - b)^{\beta - 1}} + \dots + \dfrac{B_{\beta}}{x - b} + \dots + \dfrac{C_{1}}{(x - c)^{\gamma}} + \dfrac{C_{2}}{(x - c)^{\gamma - 1}} + \dfrac{C_{\gamma}}{x - c} \\ + \dfrac{M_{1}x + N_{1}}{(x^{2} + p_{1}x - q_{1})^{\delta}} +  \dfrac{M_{2}x + N_{2}}{(x^{2} + p_{1}x - q_{1})^{\delta - 1}} + \dots +  \dfrac{M_{\delta}x + N_{\delta}}{x^{2} + p_{1}x - q_{1}} + \dfrac{K_{1}x + L_{1}}{(x^{2} + p_{2}x + q_{2})^{\eps}} + \dfrac{K_{2}x + L_{2}}{(x^{2} + p_{2}x + q_{2})^{\eps - 1}} + \dots + \dfrac{K_{\eps}x + L_{\eps}}{x^{2} + p_{2}x + q_{2}}$

### Основные интегралы рациональных дробей
1. $\int \dfrac{A}{x - a} dx = A\ln{|x - a|} + C$
2. $\int \dfrac{A}{(x - a)^{\alpha}} dx = \dfrac{A(x - a)^{-\alpha + 1}}{-\alpha + 1} + C$
3. $\int \dfrac{Mx + N}{x^{2} + px + q} dx = \dfrac{M}{2} \int \dfrac{\dfrac{Mx + N}{M} \cdot 2}{x^{2} + px + q} dx = \dfrac{M}{2} \int \dfrac{2x + \dfrac{2N}{M}}{x^{2} + px + q}dx = \\ \dfrac{M}{2} \int \dfrac{2x + p - p + \dfrac{2N}{M}}{x^{2} + px + q} dx = \dfrac{M}{2} \int \dfrac{2x + p}{x^{2} + px + q} dx + \dfrac{M}{2} \int \dfrac{\dfrac{2N}{M} - p}{x^{2} + px + q} dx =  \\ \dfrac{M}{2} \int \dfrac{d(x^{2} + px)}{x^{2} + px + q} + \dfrac{M}{2} \int \dfrac{B}{x^{2} + px + q} dx = \\ \dfrac{M}{2} \ln{|x^{2} + px + q|} + \dfrac{MB}{2} \int \dfrac{dx}{x^{2} + px + q} = \dfrac{M}{2} \ln{|x^{2} + px + q|} + \dfrac{MB}{2} \int \dfrac{dx}{x^{2} + \dfrac{2px}{2} + q + \dfrac{p^{2}}{4} - \dfrac{p^{2}}{4}} = \\  \dfrac{M}{2} \ln{|x^{2} + px + q|} + \dfrac{MB}{2} \int \dfrac{dt}{t^{2} + \left(q - \dfrac{p^{2}}{4}\right)}\bigg|_{t = x + \dfrac{p}{2}} = \\  \dfrac{M}{2} \ln{|x^{2} + px + q|} + \dfrac{MB}{2} \int \dfrac{dt}{t^{2}  \pm A}\bigg|_{t = x + \dfrac{p}{2}}^{A = q - \dfrac{p^{2}}{4}}$      
В зависимости от знака в знаменателе получаем $\dfrac{M}{2} \ln{|x^{2} + px + q|} + \dfrac{MB}{4\sqrt{A}} \ln{\bigg|\dfrac{\sqrt{A} - x}{\sqrt{A} + x}}\bigg| + C$ либо $\dfrac{M}{2} \ln{|x^{2} + px + q|} + \dfrac{MB}{2\sqrt{A}} \arctan{(\dfrac{x}{\sqrt{A}})} + C$
4. $\int \dfrac{Mx + N}{(x^{2} + px + q)^{\alpha}} dx $ Решается понижением порядка с помощью рекуррентной формулы.
	-  $I_{\alpha} = \int \dfrac{dt}{(t^{2} + 1)^{\alpha}} = \int \dfrac{1 - t^{2} + t^{2}}{(t^{2} + 1)^{\alpha}} dt = \int \dfrac{dt}{(t^{2} + 1)^{\alpha - 1}} - \int \dfrac{t^{2}dt}{(t^{2} + 1)^{\alpha}} = \\ I_{\alpha - 1} - \int u dv \bigg|_{u = t}^{dv = \dfrac{tdt}{(t^{2} + 1)^{\alpha}}} = I_{\alpha - 1} -  t \cdot \dfrac{1}{2(1 - \alpha)(t^{2} + 1)^{\alpha - 1}} + \int \dfrac{1}{2(1 - \alpha)(t^{2} + 1)^{\alpha - 1}}dt = \\ I_{\alpha - 1} - \dfrac{t}{2(1 - \alpha)(t^{2} + 1)^{\alpha - 1}} + \dfrac{I_{\alpha - 1}}{2(1 - \alpha)} = - \dfrac{t}{2(\alpha - 1)(t^{2} + 1)^{\alpha - 1}} + I_{\alpha - 1} \left(\dfrac{2(1 - \alpha) + 1}{2(1 - \alpha)}\right)$

### Комплексные числа
- Комплексным числом называется упорядоченная пара действительных чисел $(a; b)$.

***Обозначение***
- $z = (a ; b)$
- $a = \Re(z)$ - действительная часть
- $b = \Im(z)$ - мнимая часть
- $i = (0, 1)$

### Алгебраические свойства комплексных чисел
- $a_{1} = a_{2} , b_{1} = b_{2} \implies z_{1} = z_{2}$
- $z_{1} + z_{2} = \left(a_{1} + a_{2}, b_{1} + b_{2}\right)$
- $z_{1}z_{2} = \left(a_{1}a_{2} - b_{1}b_{2}, a_{1}b_{2} + a_{2}b_{1}\right)$
- $z_{1} = z_{2}z \implies \dfrac{z_{1}}{z_{2}} = z$
- $z = (a, b) = (a, 0) + b(0 , 1) = a + ib$ - алгебраическая форма записи комплексного числа
### Модуль комплексного числа
- $|z| = |x + iy| = \sqrt{x^{2} + y^{2}} = \rho$

### Аргумент комплексного числа
***Обозначение***
- $0 \leq \phi \leq 2\pi \implies \phi = \arg{z} \implies  \arg{Z} = \arg{z} + 2\pi k$ 

### Тригонометрическая форма записи комплексного числа
- $z = x + iy = \rho\cos{\phi} + \rho i\sin{\phi} = \rho \left(\cos{\phi} + i\sin{\phi} \right)$
- $e^{i\phi} = \cos{\phi} + i\sin{\phi} \implies z = \rho e^{i \phi}$
- $z_{1}z_{2} = \rho_{1}\rho_{2}\left(\cos{\phi_{1}} + i \sin{\phi_{1}}\right)\left(\cos{\phi_{2}} + i \sin{\phi_{2}}\right) = \rho_{1}\rho_{2}\left(\cos{(\phi_{1} + \phi_{2}}) + i\sin{(\phi_{1} + \phi_{2})} \right)$

### Формула Муавра
- $z^{n} = \rho^{n}\left(\cos{(n\phi)} + i\sin{(n\phi)}\right)$

### Извлечение корня из комплексного числа
- $\sqrt[n]{z} = \sqrt[n]{\rho}\left(\cos{\dfrac{\phi}{n}} + i\sin{\dfrac{\phi}{n}}\right)$
- Число корней: $n$