<!-- Macros: start -->
$\def\ident{\Longleftrightarrow}$
$\def\thus{\Rightarrow}$
$\newcommand{\braket}[1]{\langle #1 \rangle}$
$\newcommand{\block}[2]{\begin{#1} #2 \end{#1}}$
$\newcommand{\cases}[1]{\block{cases}{#1}}$
$\newcommand{\wrapmat}[2]{\block{#1}{#2}}$
$\newcommand{\mat}[1]{\wrapmat{Vmatrix}{#1}}$
$\newcommand{\det}[1]{\wrapmat{vmatrix}{#1}}$
$\newcommand{\pmat}[1]{\wrapmat{pmatrix}{#1}}$
$\newcommand{\upline}[1]{\overline{#1}}$
$\newcommand{\dnline}[1]{\underline{#1}}$
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

- $\mathbb{N}$ - Множество натуральных чисел
- $\mathbb{Z}$ - Множество целых чисел
- $\mathbb{Q}$ - Множество рациональных чисел 
- $\mathbb{R}$ - Множество вещественных чисел


***Упражнение***
Доказать, что $(\dfrac{m}{n})^2 \neq 2$, где $\dfrac{m}{n}$ - несократимая дробь.


***Доказательство***
Предположим, что $(\dfrac{m}{n})^2 = 2$, тогда :
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
- Наименьшая граница из всех верхних граней называется точной верхней гранью $(sup{A})$


***Определение***
Наибольшая граница из всех нижних граней называется точной нижней гранью $(inf{A})$


***Теорема***
- Всякое ограниченное сверху множество имеет точную верхнюю грань, а всякое ограниченное снизу имеет точную нижнюю грань.

***Определение точной верхней грани***

$(\forall x \in X : x \leq  M) \wedge (\forall x < M \exists x' \in X : x' > x) \Rightarrow M = sup{X} $

***Определение точной нижней грани***
- $(\forall x \in X x \geq m) \wedge (\forall > m, \exists x' \in X: x' < x) \Rightarrow m = inf{X}$

***Альтернативное определение точной нижней грани***
- $(\forall x \in X: x \geq m ) \wedge (\forall \epsilon > 0, \exists x' \in X : x' < m + \epsilon) \Rightarrow m = inf(X)$

***Альтернативное определение точной верхней грани***
- $(\forall x \in X : x \leq M) \wedge (\forall \epsilon > 0 \exists x' \in X: x' > M - \epsilon) \Rightarrow M = sup{X}$

***Упражнение***
Докажем, что всякое ограниченное сверху множество имеет $sup$. 
Доказательство : Рассмотрим два случая

1. Рассматриваемое множество не лишено неотрицательных чисел

2. Рассматриваемое множество содержит только отрицательные числа

- Пусть $(1)$, тогда точная верхняя грань больше или равна нуля. Т.к. множество ограничено сверху, то его целые части не превышают этой грани. Отберем из множества те числа, у которых наибольшая целая часть $\overline{x_{0}}$, остальные числа отбросим. Среди оставшихся отберем те, у которых наибольший следующий разряд, т.е $\overline{x_{0}},\overline{x_{1}}$. И т.д. до бесконечности. Получаем число - бесконечную, вообще говоря, непериодическую десятичную дробь. $\overline{x_{0}}\overline{x_{1}}\overline{x_{2}} ... \overline{x_{n}} ... = \overline{x} (sup)$

- Докажем, что таким образом получим точную верхнюю грань данного множества. Действительно по первой части определения $sup$ : $\forall x \in A \Rightarrow x \leq \overline{x}$. Но это и есть $sup$ по характеру построения числа $\overline{x}$, так как на каждой позиции для построения $\overline{x}$ бралось наибольшее число. Теперь докажем вторую часть определения $sup$. $\forall x < \overline{x}, \exists x' \in A: x' > x$. Действительно, берем произвольное число (не обязательно из множества $A$) , $x < \overline{x}$, т.к. $x < \overline{x}$ на каком - то знаке из $\overline{x_{0}},\overline{x_{1}}, ... ,\overline{x_{n}}, ... $. Докажем, что $\exists x' \in A$ , т.ч. $x' > x$. Т.к. $x' \in A$, то $x_{0}' \leq \overline{x_{0}}$, а если они равны, то $x_{1}' < \overline{x_{1}}$ и т.д. до позиции с номером $n$. Получим, что в элементах нашего множества есть число, у которого на $n$ - ом месте стоит $\overline{x_{n}}$, но $\overline{x_{n}} > x_{n} \Rightarrow x_{n}' > x_{n}$

- Докажем для пункта $(2)$. Если все числа множества $A$ - отрицательные, то $\forall x \in A: x = -|x|$, тогда отбрасываем все числа у которых наименьшая целая часть модуля $\overline{x_{0}}$, затем у которых $\overline{x_{0}}, \overline{x_{1}}$ и т.д. до бесконечности. Получаем бесконечную десятичную непериодическую дробь. Поставим перед числом знак $(-)$, получим $sup$.
***Пример***

- $A = \{1, \dfrac{1}{2},\dfrac{1}{3}, ... \dfrac{1}{n}, ...\}$. $sup{A} = 1, inf{A} = 0$


### Числовая последовательность.

***Определение***

- Рассмотрим упорядоченный набор натуральных чисел$\{1, 2, 3, ..., n, ...\}$ и каждому из этих натуральных чисел поставим в соответствие числа: $x_{1}, x_{2}, x_{3}, ... , x_{n}, ...$. Это и есть числовая последовательность.


***Обозначение*** - $\{x_{n}\}$

***Свойства***

Последовательность $\{x_{n}\}$ бывает ограниченной сверху, снизу и просто ограниченной.

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
Пусть имеем для бесконечной последовательности $\{1, 2, 3, \dots , n, \dots \}$ набор соответсвующих чисел $\{x_{1}, x_{2}, x_{3}, \dots , x_{n}, \dots \}$. Получим последовательность.

***Способы задания последовательностей***

1. Перечислением
2. Графически
3. Рекуррентно

***Примеры***

1. $\{1, \frac{1}{2}, \frac{1}{3}, \dots, \frac{1}{n}, \dots\}$

2. $\{-1, 1, -1, \dots, (-1)^n, \dots \}$

3. $x_{n} = \frac{1 + (-1)^n}{2}$ - Формула общего члена

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

- Если $\{x_{n}\}$ - б. б. , то начиная с какого - то номера, после которого нет нулевых членов, для этих номеров определена бесконечно малая последовательность: $\{ \frac{1}{x_{n}} \}$. Доказательство : Действительно, т.к. $\{x_{n}\}$ - б. б. , то, начиная с $n > N_{0}: |x_{n}| > A$, где $A$ - любое число. Тогда для этих номеров: $\frac{1}{x_{n}} < \frac{1}{A}$. Если взять произвольное $\epsilon > 0$ и $A = \frac{1}{\epsilon}$, то $|\frac{1}{x_{n}}| , \epsilon$, а это и есть определение бесконечно малой последовательности. Справедливо и обратное: Если $\{ \frac{1}{x_{n}} \}$ - б. м. , то начиная с какого - то номера, после которого нет нулевых членов, для этих номеров определена $\{x_{n}\}$ - б. б.

### Монотонные последовательности
***Определение***
- Последовательность $\{x_{n}\}$ называется возрастающей, если $\forall n : x_{n + 1} \geq x_{n}$ и строго возрастающей, если $x_{n + 1} > x_{n}$. (Иногда говорят: неубывающая, строго возрастающая). 

***Определение***
- Последовательность $\{x_{n}\}$ называется убывающей, если $\forall n : x_{n + 1} \leq x_{n}$ и строго убывающей, если $x_{n + 1} < x_{n}$. (Иногда говорят: невозрастающая, строго убывающая). 

### Предел числовой последовательности

***Формальное определение предела числовой последовательности***

- Если последовательность приближается к числу, то это число и есть ее предел.

***Примеры***
1. $x_{n} = \frac{1}{n}, \lim\limits_{n \rightarrow \infty}{\frac{1}{n}} = 0$
2. $x_{n} = \frac{n - 1}{n}, \lim\limits_{n \rightarrow \infty}{\frac{n - 1}{n}} = 1$


***Определение предела числовой последовательности***
- Число $A$ называется пределом $\{x_{n}\}$ $\Leftrightarrow (\forall \epsilon > 0, \exists N_{\epsilon} : \forall n > N_{\epsilon}  \Rightarrow |x_{n} - A| < \epsilon)$

***Упражнение***
- С помощью определения докажем (1) из примера. (Т. е. найдем $N_{\epsilon}$, что $\forall n > N_{\epsilon} \Rightarrow |x_{n} - A| < \epsilon)$. Т. к. $\lim\limits_{n \rightarrow \infty}{\frac{1}{n}} = 0 \Rightarrow (\forall \epsilon > 0, \exists N_{\epsilon} : \forall n > N_{\epsilon})  \Rightarrow |x_{n} - 0| < \epsilon \Rightarrow |\frac{1}{n}| < \epsilon \Rightarrow \frac{1}{n} < \epsilon \Rightarrow n > \frac{1}{\epsilon}$
- С помощью определения докажем (2) из примера. (Т. е. найдем $N_{\epsilon}$, что $\forall n > N_{\epsilon} \Rightarrow |x_{n} - A| < \epsilon)$. Т. к. $\lim\limits_{n \rightarrow \infty}{\frac{1}{n}} = 0 \Rightarrow (\forall \epsilon > 0, \exists N_{\epsilon} : \forall n > N_{\epsilon})  \Rightarrow |x_{n} - 0| < \epsilon \Rightarrow |\frac{n - 1}{n} - 1| < \epsilon \Rightarrow \frac{1}{n} < \epsilon \Rightarrow n > \frac{1}{\epsilon}$

### Свойства пределов

***Теорема***

**Последовательность, имеющая предел, называется сходящейся, иначе расходящейся.**

1. Всякая сходящаяся последовательность имеет единственный предел.
- Доказательство: Пусть $ \lim\limits_{n \rightarrow \infty}{x_{n}} = A$. Докажем единственность от противного. Предположим, что $\exists  \lim\limits_{n \rightarrow \infty}{x_{n}} = B$ и $A > B$. Т. к. , $ \lim\limits_{n \rightarrow \infty}{x_{n}} = A \Rightarrow  (\forall \epsilon_{1} > 0, \exists N_{\epsilon_{1} } : \forall n > N_{\epsilon_{1} }  \Rightarrow |x_{n} - A| < \epsilon_{1})$. В качестве $\epsilon_{1}$ возьмем $\frac{A - B}{2} \Rightarrow -\frac{A - B}{2} < x_{n} - A < \frac{A - B}{2} \Rightarrow   -\frac{A - B}{2} + A< x_{n}  < \frac{A - B}{2} + A \Rightarrow   \frac{A + B}{2} < x_{n}  < \frac{3A - B}{2} $.
- Т. к. $ \lim\limits_{n \rightarrow \infty}{x_{n}} = B \Rightarrow  (\forall \epsilon_{2} > 0, \exists N_{\epsilon_{2} } : \forall n > N_{\epsilon_{2} }  \Rightarrow |x_{n} - B| < \epsilon_{2})$. В качестве $\epsilon_{2}$ возьмем $\frac{A - B}{2}. $Возьмем $n > \max(N_{\epsilon_{1}}, N_{\epsilon_{2}}) \Rightarrow |x_{n} - B| < \frac{A - B}{2} \Rightarrow -\frac{A - B}{2} < x_{n} - B < \frac{A - B}{2} \Rightarrow   -\frac{A - B}{2} + B< x_{n}  < \frac{A - B}{2} + B \Rightarrow   \frac{3B - A}{2} < x_{n}  < \frac{A + B}{2} $. Получим $\frac{A + B}{2} > x_{n} > \frac{A + B}{2}$. Противоречие.

***Теорема***

**Сходящаяся последовательность ограничена**

- Доказательство: $\{x_{n}\}$ - сход. , $\Rightarrow (\forall \epsilon > 0, \exists N_{\epsilon}: \forall n > N_{\epsilon} \Rightarrow |x_{n} - A| < \epsilon)$. Это было бы доказательством ограниченности, если бы было верно для всех $n > 0$. Но до $N_{\epsilon}$ - конечное число членов. Если взять $M = \max(|x_{1}|, |x_{2}|, |x_{3}|, \dots, |x_{N_{\epsilon} - 1}|, A - \epsilon, A + \epsilon )$, то $\forall n: |x_{n}| \leq M $

***Теорема***

$\{x_{n}\}$ - б. м. $\Rightarrow \forall k :\{ k x_{n}\}$ - б. м.

- Доказательство: Действительно : т. к. $(\forall \epsilon > 0, \exists N_{\epsilon}: \forall n > N_{\epsilon} \Rightarrow |x_{n}  - 0| < \epsilon)$ . Возьмем $\epsilon = \frac{\epsilon}{|k|} \Rightarrow |x_{n}| < \frac{\epsilon}{|k|} \Rightarrow |k \cdot x_{n}| < |k| \frac{\epsilon}{|k|} = \epsilon \Rightarrow \lim\limits_{n \rightarrow \infty}{k x_{n}} = 0$

***Следствие***

Если последовательность состоит из одного и того же члена $x_{n} = \{C, C, C, C,  \dots \}$, то $\lim\limits_{n \rightarrow \infty}{x_{n}} = C$.

***Свойства пределов, выражаемые неравенствами***

1. $(\forall n > N: x_{n} \geq y_{n}) \wedge (\lim\limits_{n \rightarrow \infty}{x_{n}} = A, \lim\limits_{n \rightarrow \infty}{y_{n}} = B) \Rightarrow A > B$
- Доказательство: 
  1. В качестве $\epsilon$ возьмем $\frac{A - B}{2}$. $\forall n > N_{\epsilon_{1}}, N_{\epsilon_{1}} \Rightarrow |x_{n} - A| < \frac{A - B}{2} \Rightarrow -\frac{A - B}{2} < x_{n} - A < \frac{A - B}{2} \Rightarrow   -\frac{A - B}{2} + A < x_{n}  < \frac{A - B}{2} + A \Rightarrow  \frac{3A - B}{2} < x_{n}  < \frac{A + B}{2} $
  2. $\forall n > N_{\epsilon_{2}} : |y_{n} - B| < \frac{B - A}{2} \Rightarrow \frac{B - A}{2} < y_{n} < \frac{3B - A}{2}$
  3. Получим $x_{n} < \frac{A + B}{2} < y_{n}$. Противоречие.
2. $(x_{n} \leq y_{n} \leq z_{n}) \wedge (\forall n > N : \lim\limits_{n \rightarrow \infty}{x_{n}} = \lim\limits_{n \rightarrow \infty}{z_{n}}) \Rightarrow \{y_{n}\}$ - сходится, причем $\lim\limits_{n \rightarrow \infty}{x_{n}} = \lim\limits_{n \rightarrow \infty}{y_{n}} = \lim\limits_{n \rightarrow \infty}{z_{n}}$ 
- Доказательство : 
  1. Действительно : $1)  (\forall \epsilon > 0, \exists n > N_{1} : |x_{n} - A| < \epsilon) \\ 2) (\forall \epsilon > 0, \exists n > N_{2} : |z_{n} - A| < \epsilon) \\  \Rightarrow N = \max(N_{1}, N_{2}) \Rightarrow  |x_{n} - A| < |y_{n} - A| < |z_{n} - A| \Rightarrow |y_{n} - A| < \epsilon \Rightarrow \lim\limits_{n \rightarrow \infty}{y_{n}} = A$

***Арифметические свойства пределов сходящихся  последовательностей***
1. $\lim\limits_{n \rightarrow \infty}{x_{n}} = A; \lim\limits_{n \rightarrow \infty}{y_{n}} = B \Rightarrow \lim\limits_{n \rightarrow \infty}{(x_{n} + y_{n})} = A + B$
2. $\lim\limits_{n \rightarrow \infty}{x_{n}y_{n}} = AB$
3. $\lim\limits_{n \rightarrow \infty}{\frac{x_{n}}{y_{n}}} = \frac{A}{B}$
- Докажем $(1)$
  1. Т. к. $\lim\limits_{n \rightarrow \infty}{x_{n}} = A$, то $(\forall \epsilon > 0, \epsilon = \frac{\epsilon}{2}, \forall n > N_{1} : |x_{n} - A| < \frac{\epsilon}{2}$
  2. Т. к. $\lim\limits_{n \rightarrow \infty}{x_{n}} = B$, то $(\forall \epsilon > 0, \epsilon = \frac{\epsilon}{2}, \forall n > N_{2} : |x_{n} - B| < \frac{\epsilon}{2}$
  3. Возьмем $N = \max(N_{1}, N_{2})$, тогда $\forall n > N : |x_{n} + y_{n} - A - B| \leq |x_{n} - A| + |y_{n} - B| < \frac{\epsilon}{2} +  \frac{\epsilon}{2} = \epsilon \Rightarrow \lim\limits_{n \rightarrow \infty}{(x_{n} + y_{n})} = A + B$
- Докажем $(2)$ 
  1. Т. к. $\lim\limits_{n \rightarrow \infty}{x_{n}} = A$, то $(\forall \epsilon > 0, \forall n > N_{1} : |x_{n} - A| < \epsilon$
  2. Т. к. $\lim\limits_{n \rightarrow \infty}{x_{n}} = B$, то $(\forall \epsilon > 0,  \forall n > N_{2} : |x_{n} - B| < \epsilon$
  3. Возьмем $N = \max(N_{1}, N_{2})$, тогда $\forall n > N : |x_{n}y_{n} - A B| = |(x_{n} - A + A)(y_{n} - B + B)| \leq |x_{n}y_{n} - AB| + \underbrace{|x_{n} - A|y_{n}}_{< \frac{\epsilon}{2}} + \underbrace{|y_{n} - B|x_{n}}_{< \frac{\epsilon}{2}} + \dots  \Rightarrow \lim\limits_{n \rightarrow \infty}{(x_{n}y_{n})} = A + B$
## Семинар 13.02.2022
***Разбор домашней работы***
Доказать по индукции : 

- $1^3 + \dots + n^3 = (1 + \dots + n)^2$
- $n = 1$ : $1^3 = 1^2$ - верно $\\$ 
- $1^n + \dots n^3 = (1 + \dots + n) ^2$
- $1^3 + \dots + n^3 + (n + 1)^3 = (\frac{(1 + n)n}{2})^2 + (n + 1)^3$
- $1^3 + \dots + n^3 + (n + 1)^3 = (1 + \dots + n + (n + 1))^2$

Доказать по индукции:

- $\frac{1}{2} \cdot \frac{3}{4} \cdot \frac{2n - 1}{2n} < \frac{1}{\sqrt{2n + 1}}$ 
- $\frac{1}{2} \cdot \frac{3}{4} \cdot \frac{2n - 1}{2n} < \frac{1}{\sqrt{2n + 1}}$
- $\frac{1}{2} \cdot \frac{3}{4} \cdot \frac{2n - 1}{2n}  \cdot \frac{2n + 1}{2n + 2} < \frac{1}{\sqrt{2n + 3}}$
- $ \frac{1}{\sqrt{2n + 3}}  \geq \frac{1}{\sqrt{2n + 2}} \cdot \frac{2n + 1}{\sqrt{2n + 2}}$
- $ (\sqrt{2n + 3})^2  \geq (2n + 3) \dots $

3. Начертить график. $y = arctg{\frac{1}{x}}$

4. Начертить график $y = log_{3}{(2 - 3x)}$

***Повтор определений с лекции***

### Точная верхняя грань ограниченного сверху множества
***Определение точной верхней грани***

1. $M = sup{X} $ - наименьшая из всех верхних граней

2. $ (\forall x \in X : x \leq M) \wedge (\forall \epsilon > 0 \exists x' \in X: x' > M - \epsilon) \Rightarrow M = sup{X}$

3. $(\forall x \in X : x \leq  M) \wedge (\forall x < M \exists x' \in X : x' > x) \Rightarrow M = sup{X} $
### Точная нижняя грань ограниченного сверху множества
1. $m = inf(X)$ - наибольшая из всех нижних граней $X$
2. $(\forall x \in X: x \geq m ) \wedge (\forall \epsilon > 0, \exists x' \in X : x' < m + \epsilon) \Rightarrow m = inf(X)$
3. $(\forall x \in X x \geq m) \wedge (\forall > m, \exists x' \in X: x' < x) \Rightarrow m = inf{X}$

***Задачи на семинаре***

1. Доказать, что $inf(-X) = - sup(X)$. Доказательство: $(\forall x \in X: x \leq M) \wedge (\forall \epsilon > 0 : \exists x' \in X: x' > M - \epsilon ) \Rightarrow M =sup{X}$. Рассмотрим множество ${-X}$. $(\forall (-x) : -x \geq -M = m) \wedge (\forall \epsilon > 0 : \exists -x' \in -X: -x' < \underbrace{-M}_{m} + \epsilon = m + \epsilon \Rightarrow m = -M)$
2. Доказать, что $sup{X + Y} = sup{X} + \sup{Y}$
    1. $ (\forall x \in X : x \leq M_{1}) \wedge (\forall \epsilon > 0 \exists x' \in X: x' > M_{1} - \frac{\epsilon}{2} \Rightarrow M_{1} = sup{X}$
    2. $ (\forall y \in X : y \leq M_{2}) \wedge (\forall \epsilon > 0 \exists y' \in X: y' > M_{2} - \frac{\epsilon}{2} \Rightarrow M_2 = sup{X}$
    3. $ (\forall x + y \in X + Y : x + y \leq M_{1} + M_{2}) \wedge (\forall \epsilon > 0, \exists x' + y' \in X + Y: x' + y' > M_{1} +M_{2} - \epsilon \Rightarrow M_{1} + M_{2} = sup{X}$

3. Доказать, что $sup{XY} = sup{X} \cdot \sup{Y}$
    1. $ (\forall x \in X : x \leq M_{1}) \wedge (\forall \epsilon_{1} > 0 \exists x' \in X: x' > M_{1} - \epsilon_{1}) \Rightarrow M_{1} = sup{X}$
    2. $ (\forall y \in X : y \leq M_{2}) \wedge (\forall \epsilon_{2} > 0 \exists y' \in X: y' > M_{2} - \epsilon_{2}) \Rightarrow M_2 = sup{X}$
    3. $ (\forall x \cdot y \in XY : xy \leq M_{1}M_{2}) \wedge (\forall \epsilon > 0 \exists x'y' \in XY: x'y' > (M_{1} - \epsilon_{1})(M_{2} - \epsilon_{2}) = M_{1}M_{2} - \underbrace{ M_{1}\epsilon_{2} - M_{2}\epsilon_{1} + \epsilon_{1}\epsilon_{2}}_{= \epsilon} \Rightarrow M_{1}M_{2} = sup{X}$