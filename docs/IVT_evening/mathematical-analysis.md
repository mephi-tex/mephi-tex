<!-- Macros: start -->
$\def\ident{\Longleftrightarrow}$
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

## Числовые Множества. Вещественные числа.

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


## Сравнение вещественных чисел, их сумма и произведение

***Определение***
- Сравниваем поразрядно $a_{0}, b_{0}$, затем $a_{1}, b_{1}$ и т.д.

- По аналогии сумма и произведение: $a_{0} \dot b_{0}$, затем $a_{1}\dot b_{1}$ и т.д.


## Множества. Инфимум и Супремум.
Рассмотрим произвольное числовое множество $A$, состоящее из чисел $x \in A$. 

***Определение***
- Множество $A$ называется ограниченным сверху, если $\exists M : \forall x \in A \Rightarrow x \leq M$

***Определение***
 -Множество $A$ называется ограниченным снизу, если $\exists m : \forall x \in A \Rightarrow x \geq m$

***Определение***
-Множество $A$ называется ограниченным снизу, если $\exists M, m : \forall x \in A \Rightarrow  m \leq x \leq M$


***Определение***
- Наименьшая граница из всех верхних граней называется точной верхней гранью $(sup{A})$


***Определение***
Наибольшая граница из всех нижних граней называется точной нижней гранью $(inf{A})$


***Теорема***
- Всякое ограниченное сверху множество имеет точную верхнюю грань, а всякое ограниченное снизу имеет точную нижнюю грань.


***Определение точной верхней грани***
- $(\forall x \in A \Rightarrow x \leq M) \wedge (\forall x < M , \exists x' \in A : x < x' \leq M) \Rightarrow M = sup{A}$


***Определение точной нижней грани***
- $(\forall x \in A \Rightarrow x \geq m) \wedge (\forall \epsilon > 0, \exists x' \in A \Rightarrow m \leq x' < m + \epsilon) \Rightarrow m = inf{A}$

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


## Числовая последовательность.

***Определение***

- Рассмотрим упорядоченный набор натуральных чисел$\{1, 2, 3, ..., n, ...\}$ и каждому из этих натуральных чисел поставим в соответсвие числа: $x_{1}, x_{2}, x_{3}, ... , x_{n}, ...$. Это и есть числовая последовательность.


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