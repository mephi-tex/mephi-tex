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

```{contents} Математический анализ  
---  
depth: 3  
```
# Математический анализ  
Преподаватель: Михайлов Владислав Дмитриевич 

Конспект : Руденький Н. В. 

Группа: Б$22$-В$71$.

# Литература  

- [Демидович Б. П. - "Сборник задач и упражнений по Математическому Анализу"](https://docs.google.com/gview?url=https://mephi-tex.rtfd.io/ru/latest/_static/literature/БП_ДЕМИДОВИЧ_СБОРНИК_ЗАДАЧ_И_УПРАЖНЕНИЙ_ПО_МАТЕМАТИЧЕСКОМУ_АНАЛИЗУ.pdf)  

## Лекция 07.09.2022  

### Обозначения числовых множеств  

- $\NN$ - Множество натуральных чисел  
- $\ZZ$ - Множество целых чисел  
- $\QQ$ - Множество рациональных чисел   
- $\RR$ - Множество вещественных чисел
- $\CC$ - Множество комплексных чисел  


### Определение ограниченности множества чисел
- Рассмотрим произвольное числовое множество $A$, состоящее из чисел $x \in A$.   

  - Множество $A$ называется ограниченным сверху, если $\exists M : \forall x \in A \implies x \leq M$  

  - Множество $A$ называется ограниченным снизу, если $\exists m : \forall x \in A \implies x \geq m$  

  - Множество $A$ называется ограниченным снизу и сверху, если $\exists M, m \ \forall x \in A \implies  m \leq x \leq M$ 


### Определение точной верхней и нижней граней числового множества
- Наименьшая граница из всех верхних граней называется точной верхней гранью $(\sup{A})$  

- Наибольшая граница из всех нижних граней называется точной нижней гранью $(inf{A})$  

- Всякое ограниченное сверху множество имеет точную верхнюю грань, а всякое ограниченное снизу имеет точную нижнюю грань.  

***Определение точной верхней грани***  

- $(\forall x \in X : x \leq  M) \wedge (\forall x < M, \exists x' \in X : x' > x) \implies M = \sup{X} $  
- $(\forall x \in X : x \leq M) \wedge (\forall \epsilon > 0, \exists x' \in X: x' > M - \epsilon) \implies M = \sup{X}$  

***Определение точной нижней грани***  

- $(\forall x \in X: x \geq m) \wedge (\forall x > m, \exists x' \in X: x' < x) \implies m =inf{X}$  
- $(\forall x \in X: x \geq m ) \wedge (\forall \epsilon > 0, \exists x' \in X : x' < m + \epsilon) \implies m = inf{X}$  

### Теорема о наличии супремума (инфимума) в ограниченном сверху (снизу) множестве 

- Рассмотрим два случая:

  - Рассматриваемое множество не лишено неотрицательных чисел  

  - Рассматриваемое множество содержит только отрицательные числа  

    - Пусть $(1)$, тогда $\sup{} \geq 0$. $X$ ограничено сверху $\implies x \in X : [x] \leq \sup$. Отберем из множества те числа, у которых наибольшая целая часть $\overline{x_{0}}$. Среди оставшихся отберем те, у которых наибольший следующий разряд, т.е. $\overline{x_{0}},\overline{x_{1}}$. И т.д. до бесконечности. Получаем  бесконечную, непериодическую десятичную дробь. $\overline{x_{0}}\overline{x_{1}}\overline{x_{2}} ... \overline{x_{n}} ... = \overline{x} \ (\sup)$  
    - Докажем, что таким образом получим точную верхнюю грань данного множества. Действительно по первой части определения $\sup$ : $\forall x \in A \implies x \leq \overline{x}$. Но это и есть $\sup$ по характеру построения числа $\overline{x}$, так как на каждой позиции для построения $\overline{x}$ бралось наибольшее число. Теперь докажем вторую часть определения $\sup : \forall x < \overline{x}, \exists x' \in A: x' > x$. Действительно, берем произвольное число (не обязательно из множества $A$) , $x < \overline{x}$, т.к. $x < \overline{x}$ на каком - то знаке из $\{\overline{x_{0}},\overline{x_{1}}, ... ,\overline{x_{n}}, ... \}$. Докажем, что $\exists x' \in A: x' > x$.  $x' \in A \implies x_{0}' \leq \overline{x_{0}}$, $x_{0}' = \overline{x_{0}} \implies$ $x_{1}' < \overline{x_{1}}$ и т.д. до позиции с номером $n$. Получим, что в элементах нашего множества есть число, у которого на $n$ - ом месте стоит $\overline{x_{n}} \implies \overline{x_{n}} > x_{n}' > x_{n}$  
    - Докажем для пункта $(2)$. Если все числа множества $A$ - отрицательные, то $\forall x \in A: x = -|x|$, тогда таким же алгоритмом получаем бесконечную непериодическую десятичную дробь с наименьшими по модулю разрядами. Поставим перед числом знак $(-)$, получим $\sup$.  

### Пример ограниченного множества

- $A = \{1, \dfrac{1}{2},\dfrac{1}{3}, ... \dfrac{1}{n}, ...\} \implies$ $\sup{A} = 1, inf{A} = 0$  


### Определение числовой последовательности.  

- Рассмотрим упорядоченный набор натуральных чисел $\{1, 2, 3, ..., n, ...\}$ и каждому из этих натуральных чисел поставим в соответствие числа: $x_{1}, x_{2}, x_{3}, ... , x_{n}, ...$. Это и есть числовая последовательность.  

### Обозначение числовой последовательности.

- $\{x_{n}\}$  

### Определение ограниченной последовательности 
 - $\forall n: x_{n} \leq M$ - Ограничена сверху
 -  $\forall n: x_{n} \geq m$  - Ограничена снизу
 - $\forall n: m \leq x_{n}  \leq M \ \or \ $$\exists k  \ \forall n :  |x_{n}| \leq k$  - Ограничена снизу и сверху
 - $\forall k \ \exists n : |x_{n}| > k$ - Не ограничена

### Примеры ограниченной и неограниченной последовательностей

- $\{1, \dfrac{1}{4}, \dfrac{1}{9}, ... ,\dfrac{1}{n^2}, ... \}$ - Ограничена  

- $\{1,-1, \dfrac{1}{4},-2, \dfrac{1}{9},-3, ... ,-n, \dfrac{1}{n^2}, ... \}$ - Не ограничена

### Определение возрастающей и убывающей последовательностей

   - Если для любой пары соседних членов последовательности выполняется $x_{k + 1} \geq x_{k}$, то последовательность неубывающая, если $x_{k + 1} > x_{k}$, то строго возрастающая. Аналогично для невозрастающей и строго убывающей.  


## Лекция 14.09.2022  


### Способы задания числовых последовательностей 
- Перечислением  

- Графически  

- Рекуррентно  

### Различные примеры числовых последовательностей

- $\{1, \dfrac{1}{2}, \dfrac{1}{3}, \dots, \dfrac{1}{n}, \dots\}$  

- $\{-1, 1, -1, \dots, (-1)^n, \dots \}$  

- $x_{n} = \dfrac{1 + (-1)^n}{2}$ 

- $\{1, 2, 3, 4, \dots\}$  

- $x_{n} = 1^{\left(-1\right)^{n}}$  

- $x_{n} = - n^2$  

### Определение бесконечно большой и малой последовательностей  

- $\{x_{n}\}$ - бесконечно большая $\Longleftrightarrow \left(\forall A \ \exists N \in \NN: \forall n > N\right) \implies |x_{n}| > A$.  

- $\{x_{n}\}$ -  бесконечно малая $\Longleftrightarrow \left(\forall A \ \exists N: \forall n > N \right) \implies |x_{n}| < A$.  

### Теорема о существовании бесконечно малой и большой последовательностей

- Если $\{x_{n}\}$ - бесконечно большая , то для нее определена бесконечно малая последовательность $\{ \dfrac{1}{x_{n}} \}$ и наоборот. 
	-  $\{x_{n}\}$ - бесконечно большая $\implies \left(\forall A  \ \exists N \in \NN : \forall n > N : |x_{n}| > A\right)$ Тогда для этих номеров: $\dfrac{1}{x_{n}} < \dfrac{1}{A}$. Если взять произвольное $\epsilon > 0$ и $A = \dfrac{1}{\epsilon}$, то $\bigg|\dfrac{1}{x_{n}}\bigg| < \epsilon$, а это и есть определение бесконечно малой последовательности. 

### Определение монотонной последовательности  
- Последовательность $\{x_{n}\}$ монотонно возрастает, если: $\left(\forall n \in \NN : x_{n + 1} \geq x_{n}\right)$ и строго монотонно возрастает, если $x_{n + 1} > x_{n}$.

- Последовательность $\{x_{n}\}$ монотонно убывает, если : $\left(\forall n \in \NN : x_{n + 1} \leq x_{n}\right)$ и строго монотонно убывает, если $x_{n + 1} < x_{n}$.

### Определение предела числовой последовательности  

$A \ = \ \lim{n}{\infty} {x_{n}} \Longleftrightarrow (\forall \epsilon > 0 \ \exists N(\eps) \in \NN \ \forall n > N(\eps)  : |x_{n} - A| < \epsilon)$  

### Примеры пределов

- $x_{n} = \dfrac{1}{n} \implies \lim{n}{\infty} \dfrac{1}{n}  = 0 \implies \forall \epsilon > 0 \ \exists N(\epsilon) \in \NN \ \forall n > N(\epsilon)  : \bigg|x_{n} - 0\bigg| =  \bigg|\dfrac{1}{n}\bigg| = \dfrac{1}{n} < \epsilon \implies n > \dfrac{1}{\epsilon}$
- $x_{n} = \dfrac{n - 1}{n} \implies \lim{n}{\infty} \dfrac{n - 1}{n} = 1 \implies (\forall \epsilon > 0 \ \exists N(\epsilon) \in \NN \ \forall n > N(\epsilon)  \implies \big|x_{n} - 1\big| = \bigg|\dfrac{n - 1}{n} - 1\bigg| = \left|\dfrac{1}{n}\right| < \epsilon \implies n > \dfrac{1}{\epsilon}$  

### Теорема о единственности предела сходящейся последовательности 

- Всякая сходящаяся последовательность имеет единственный предел.  
	
	-   $\lim{n}{\infty} x_{n} = A$. Допустим: $\exists   \lim{n}{\infty} x_{n} = B,$ $A > B$. 
	
	- $  \lim{n}{\infty} x_{n} = A \implies \forall \epsilon_{1} > 0 \ \exists N(\epsilon_{1}) \in \NN \ \forall n > N(\epsilon_{1} )  : |x_{n} - A| < \epsilon_{1};$  $\epsilon_{1} =$ $\dfrac{A - B}{2} \implies \dfrac{A + B}{2} < x_{n}  < \dfrac{3A - B}{2} $.  
	
	- $\lim{n}{\infty} x_{n} = B \implies  \forall \epsilon_{2} > 0 \ \exists N(\epsilon_{2}) \in \NN \ \forall n > N(\epsilon_{2})  : |x_{n} - B| < \epsilon_{2}; \ \epsilon_{2} = \dfrac{A - B}{2} \implies \dfrac{3B - A}{2} < x_{n}  < \dfrac{A + B}{2} $.  
	
	- $\forall n > \max(N(\epsilon_{1}), N(\epsilon_{2})) : $ $\dfrac{A + B}{2} > x_{n} > \dfrac{A + B}{2}$.  

### Теорема об ограниченности сходящейся последовательности

- Сходящаяся последовательность ограничена  
  -  $\lim{n}{\infty}\{x_{n}\} = A;$ $K = \max(|x_{1}|, |x_{2}|, |x_{3}|, \dots, |x_{N(\epsilon)}|, |A - \epsilon|,| A + \epsilon |) \implies$ $\forall n > N(\eps): |x_{n}| \leq K$  

### Свойства пределов, выражаемые неравенствами

- $\left(\forall n > N(\eps): x_{n} \geq y_{n}\right) \wedge \left( \lim{n}{\infty} x_{n} = A,  \lim{n}{\infty} y_{n} = B\right) \implies A \geq B$  
	- $\epsilon_{1} = \dfrac{A - B}{2} \implies \forall n > N(\epsilon_{1}) : |x_{n} - A| < \dfrac{A - B}{2}  \implies \dfrac{3A - B}{2} < x_{n}  < \dfrac{A + B}{2} $  
	- $\epsilon_{2} = \dfrac{A - B}{2} \implies \forall n > N(\epsilon_{2}) : |y_{n} - B| < \dfrac{A - B}{2} \implies \dfrac{A - B}{2} < y_{n} < \dfrac{3B - A}{2}$  
	- $\forall n > \max(N(\eps_{1}), N(\eps_2)) : x_{n} < \dfrac{A + B}{2} < y_{n}$. 
- $(\forall n > N(\eps):x_{n} \leq y_{n} \leq z_{n}) \wedge (\lim{n}{\infty}\{x_{n}\} \ = \ \lim{n}{\infty}\{z_{n}\} = A) \implies \lim{n}{\infty}\{y_{n}\} = A $   
	- $\forall \eps_{1} > 0 \ \exists N(\eps_{1}) \ \forall n > N(\eps_{1}) : |x_{n} - A| < \eps_{1}$  
	- $\forall \eps_{2} > 0 \ \exists N(\eps_{2}) \ \forall n > N(\eps_{2}) : |x_{n} - A| < \eps_{2}$   
	- $\forall n > N = \max(N(\eps_{1}), N(\eps_{2})) :  |x_{n} - A| < |y_{n} - A| < |z_{n} - A| \implies |y_{n} - A| < \epsilon \implies \lim{n}{\infty}{y_{n}} = A$  

### Арифметические свойства пределов сходящихся последовательностей

- $\lim{n}{\infty} \{x_{n}\} = A; \lim{n}{\infty}  \{y_{n}\} = B $

  - $\lim{n}{\infty} \left(\{x_{n}\} + \{y_{n}\}\right) = A + B$  

  - $ \lim{n}{\infty} \{\{x_{n}\}\{y_{n}\}\} = AB$  

  - $ \lim{n}{\infty} \{\dfrac{x_{n}}{y_{n}}\} = \dfrac{A}{B}$  

- Докажем $(1)$  
  
	- $\lim{n}{\infty}{x_{n}} = A \Longleftrightarrow$ $(\forall \epsilon > 0 \ \exists N_{1}(\eps) \in \NN \ \forall n > N_{1}(\eps) : |x_{n} - A| < \dfrac{\epsilon}{2})$  
  
	- $\lim{n}{\infty}{x_{n}} = B \Longleftrightarrow$ $(\forall \epsilon > 0 \ \exists N_{2}(\eps) \in \NN \ \forall n > N_{2}(\eps) : |x_{n} - B| < \dfrac{\epsilon}{2})$  
	- $N = \max(N_{1}(\eps), N_{2}(\eps)) \implies \forall n > N : |x_{n} + y_{n} - A - B| \leq |x_{n} - A| + |y_{n} - B| < \dfrac{\epsilon}{2} +  \dfrac{\epsilon}{2} = \epsilon$  
- Докажем $(2)$   
	- $ \lim{n}{\infty} x_{n} = A \Longleftrightarrow $ $(\forall \epsilon_{1} > 0 \ \exists N(\eps_{1}) \in \NN \ \forall n > N(\eps_{1}) : |x_{n} - A| < \epsilon_{1})$  
	- $ \lim{n}{\infty} y_{n} = B \Longleftrightarrow$ $(\forall \epsilon_{2} > 0 \ \exists N(\eps_{2}) \in \NN \ \forall n > N(\eps_{2}) : |x_{n} - A| < \epsilon_{2})$  
	- $N = \max(N(\eps_{1}), N(\eps_{2})) \implies \forall n > N :\bigg|x_{n}y_{n} - AB\bigg| = \\ \bigg|x_{n}y_{n} -Ay_{n} + Ay_{n} - A B\bigg| = \\ \bigg|(x_{n} - A)y_{n} + A(y_{n} - B)\bigg| \leq \bigg|x_{n} - A\bigg|\bigg|y_{n}\bigg| + \bigg|A\bigg|\bigg|y_{n} - B\bigg| < \eps_{1} M_{y} + \bigg|A\bigg|\eps_{2} \implies \eps_{1} = \dfrac{\eps}{2\bigg|M_{y}\bigg|} , \eps{2} = \dfrac{\eps}{2\bigg|A\bigg|} \implies \\ \bigg|x_{n}y_{n} - AB\bigg| < \eps$  

## Лекция 21.09.2022  

### Определение подпоследовательности  

- Пусть задана $\{x_{n}\}$. Удалим из нее все члены кроме $x_{k}$ без изменения порядка. Получим подпоследовательность $\{x_{n_{k}}\}$.  

###  Утверждение о сходимости подпоследовательности 

$\lim{n}{\infty} \{x_{n}\} = A \implies  \lim{n}{\infty} \{x_{n_{k}}\} = A $ 
-  $\lim{n}{\infty} \{x_{n}\} = A$. При $N_{k} > N_{\epsilon}$ члены подпоследовательности входят в число членов $\{x_{n}\} \implies |x_{n_{k}} - A| < \epsilon $  

### Примеры подпоследовательностей 

1. $x_{n} = \dfrac{1 + (-1)^{n}}{2}$  
	- $\{x_{n_{2k}}\} \rightarrow 1$  
	- $\{ x_{n_{2k + 1} } \} \rightarrow 0$  
2. $\{x_{n}\} = 1 + \sin{\dfrac{\pi n}{2}}$  
	- $\{x_{n_{2k} }\} = (1 + \sin{\pi k}) \rightarrow 1$  
	- $\{x_{n_{4k + 1} }\} = (1 + \sin{\dfrac{\pi}{2}}) \rightarrow 2$  
	- $\{x_{n_{4k + 3}}\} = (1 + \sin{\dfrac{3 \pi}{2}}) \rightarrow 0$  
3. $x_{n} = n^{(-1)^{n}}$  
	- $\{x_{n_{2k}}\} \rightarrow \infty$  
	- $\{x_{n_{2k + 1}}\} \rightarrow 0$  

### Определение предельной точки последовательности

- $X$ называется предельной точкой $\{x_{n}\}$, если в любой сколь угодно малой окрестности точки содержится бесконечное число членов $\{x_{n}\}$.  

### Теорема о сходящейся подпоследовательности  
-  $\{x_{n}\}$ имеет предельную точку $X \implies \exists \{x_{n_{k}}\} : \lim{n}{\inf} \{x_{n_{k}}\} = X$ 
	- Так как в $\{x_{n}\}$ имеется предельная точка $X$, то $\forall \epsilon > 0$ в $\epsilon$ - окрестности точки $X$ содержится бесконечное число членов $\{x_{n}\}$. Возьмем  $\overline{X_{1}}$ из $\epsilon_{1}$ окрестности точки $X$. Далее возьмем $\epsilon_{2} < \eps_{1}$ и точку $\overline{X_{2}}$ из $\epsilon_{2}$ - окрестности и т. д.  для $\epsilon_{n} < \eps_{n - 1}$ возьмем $\overline{X_{n}}$ из $\epsilon_{n}$ - окрестности. Получим $\{\overline{X_{n}}\}$.  
	- Докажем, что $ \lim{n}{\infty} \{\overline{X_{n}}\} = X$. Рассмотрим все точки, которые вошли в $\eps_{n}$ окрестность точки $X$. В нее вошла точка $\overline{X_{n}}$,следовательно, в нее войдут и все дальнейшие точки с большими номерами.

### Теорема Больцано - Вейерштрасса  
- Во всякой ограниченной последовательности содержится сходящаяся  подпоследовательность.  
	- Докажем, что у ограниченной последовательности $\{x_{n}\}$ существует предельная точка  
		- Рассмотрим множество $X$ такое,  что $\forall x \in X \ \forall x' \in\{x_{n}\} : x > x' $
		
		- $\forall x \in X: x > x' \geq m \implies \exists  \overline{x} = inf{X} \implies \overline{x}$ - предельная точка.

### Определение фундаментальной последовательности

- $\forall \epsilon > 0 \ \exists N_{\epsilon} \ \forall n > N_{\epsilon} \ \forall p \in \NN : |x_{n + p} - x_{n}| < \epsilon \implies $  $\{x_{n}\} $ - фундаментальная 
### Критерий Коши сходимости последовательности  
- $\lim{n}{\inf}$ $\{x_{n}\} = A$  тогда и только тогда, когда она фундаментальная.  
	- Необходимость: $\bigg|x_{n + p} - x_{n}\bigg| = \bigg|x_{n + p} - x_{n} - A + A\bigg| = \bigg|x_{n + p} - A - \left(x_{n} - A\right)\bigg| \leq \underbrace{\bigg|x_{n + p} - A\bigg|}_{\leq \dfrac{\epsilon}{2}} + \underbrace{\bigg|x_{n} - a\bigg|}_{\leq \dfrac{\epsilon}{2}} < \eps$
	- Достаточность:  
	  - $\forall \epsilon > 0 \ \exists N_{\epsilon} \in \NN \ \forall n > N_{\epsilon} \ \forall p \in \NN : \bigg|x_{n + p} - x_{n}\bigg| < \epsilon \implies$  $-\eps + x_{n + p} < x_{n} < \eps + x_{n + p} \implies$ $\{x_{n}\}$ - ограничена$\implies \exists \ \{x_{n_{k}}\}$. $\lim{n}{\infty}\{x_{n_{k}}\} = A$  
	  -  $\bigg|x_{n_{k}} - A\bigg| = \bigg|x_{n_k} - x_{n} + x_{n} - A\bigg| \leq  \underbrace{\bigg|x_{n_{k}} - x_{n}\bigg|}_{< \dfrac{\eps}{2}} + \underbrace{\bigg|x_{n} - A\bigg|}_{< \dfrac{\eps}{2}} < \eps$  

### Применение Критерия Коши сходимости последовательности

- $\{x_{n}\} = 1 + \dfrac{1}{2} + \dfrac{1}{3} + \dots + \dfrac{1}{n}$.  
	- $|x_{n + p} - x_{n}| = \bigg|1 + \dfrac{1}{2} + \dfrac{1}{3} + \dots + \dfrac{1}{n} + \dfrac{1}{n + 1} \dots \dfrac{1}{n + p} - \left(1 + \dfrac{1}{2} + \dfrac{1}{3} + \dots + \dfrac{1}{n}\right)\bigg| = \bigg|\dfrac{1}{n + 1} + \dfrac{1}{n + 2} + \dots + \dfrac{1}{n + p}\bigg| \geq \dfrac{p}{n + p}$  $p=n \implies \dfrac{p}{n + p} = \dfrac{n}{2n} = \dfrac{1}{2} = \epsilon \implies \lim{n}{\inf}\{x_{n}\} = \inf$ 
- $\{x_{n}\} = \dfrac{\cos{x}}{1^{2}} + \dfrac{\cos{2x}}{2^{2}} + \dots + \dfrac{\cos{nx}}{n^{2}}$.  
	-  $|x_{n + p} - x_{n}| = \bigg|\dfrac{\cos(n + 1)x}{(n + 1)^{2}} + \dfrac{\cos(n + 2)x}{(n + 2)^{2}} + \dots + \dfrac{\cos(n + p)x}{(n + p)^{2}}\bigg| < \dfrac{p}{(n + 1)^2} < \epsilon$  

## Лекция 28.09.2022  

### Понятие функции на числовом множесте  
- Пусть на числовом множестве $X$ каждому числу $x \in X$ по какому - либо закону поставлено в соответствие число $y \in Y$. Тогда на $X$ задана функция $y = f(x)$.  
	- $f$ - характеристика функции  
	- $x$ - аргумент функции $f$
	- $y$ - значение  функции $f$
	- $X$ - область определения функции $f$
	- $Y$ - область значений функции $f$
	
### Примеры функций на числовом множестве
-  $f(x) = \begin{equation*}  
	  \begin{cases}  
	   0, x \in \RR \backslash \QQ \\  
	   1, x \in \QQ  
	  \end{cases}  
	  \end{equation*}$  
- $y = x^{2}$     
- $y = sgn(x) = \begin{equation*}  
	   \begin{cases}  
	    1, x > 0 \\  
	    0, x = 0 \\  
	    -1, x < 0  
	   \end{cases}  
	  \end{equation*}$  
- $f(x) = [x]$ (целая часть, не превосходящая x) 

### Определение ограниченной и неограниченной функций  
- Функция называется ограниченной на $[a;b]$, если :$ (\forall x \in [a;b] \ \exists m, M : m \leq f(x) \leq M)$.  
- Функция называется неограниченной на $\left[a;b\right]$, если :$ (\forall x \in [a;b] \ \exists K: \ |f(x)| > K)$.  

### Монотонные функции  
- Функция называется неубывающей на $[a;b] $, если: $ (\forall x_{1}, x_{2} \in [a;b] : x_{2} > x_{1} \implies f(x_{2}) \geq f(x_{1}))$.  
- Функция называется невозрастающей на $[a;b] $, если: $ (\forall x_{1}, x_{2} \in [a;b] : x_{2} > x_{1} \implies f(x_{2}) \leq f(x_{1}))$.  

### Предел функции в точке по Коши  
- $A  \ =  \ \lim{x}{x_{0}} f(x) \Longleftrightarrow \forall \epsilon > 0 \ \exists \delta(\eps) > 0 \ \forall x \in X: |x - x_{0}| < \delta \implies |f(x) - A| < \epsilon$.  

### Предел функции в точке по Гейне  
- $A = \lim{x}{x_{0}} f(x) \Longleftrightarrow (\forall \{x_{n} \in X: x_{n} \neq x_{0}\} : \lim{n}{\infty} \{x_{n}\} = x_{0} \implies \lim{n}{\infty} f(x_{n}) = A)$.  

### Доказательство эквивалентности определения предела по Коши и Гейне  
- $(К \implies Г)$  
	- Рассмотрим произвольную $\{x_{n} \in X: x_{n} \neq x_{0}\}, \lim{n}{\infty} \{x_{n}\} = x_{0} \implies $ $\forall \delta > 0 \ \exists N(\delta) \in \NN \ \forall n > N_{\delta} : |x_{n} - x_{0}| < \delta \implies |f(x_{n}) - A| < \epsilon$. 
 - $(Г \implies К)$  
	-  Пусть $Г \;\not\!\!\!\implies К$. Тогда $\exists \epsilon > 0 \ \forall \delta(\eps) > 0 \ \exists x \in X: |x - x_{0}| < \delta \implies |f(x) - A| \geq \epsilon$. Рассмотрим $x_{1}$ из $\delta_{1}$ - окрестности точки $x_{0}$,  что $|f(x_{1}) - A| \geq \eps$.Рассмотрим $x_{2}$ из  $\delta_{2} < \delta_{1}$ - окрестности точки $x_{0}$,  что $|f(x_{2}) - A| \geq \eps$. И так далее возьмем $x_{n}$ из $\delta_{n} < \delta_{n - 1}$ - окрестности точки $x_{0}$, такое, что $|f(x_{n}) - A| \geq \eps$. Получим: $\{x_{1}, x_{2}, \dots, x_{n}, \dots\} \rightarrow x_{0}, \{f(x_{1}),f(x_{2}), \dots, f(x_{n}), \dots\} \;\not\longrightarrow A$  

### Примеры доказательств, используя $\eps - \delta$  
- $f(x) = x^{3}$  
	- $\lim{x}{0} f(x) = 0$  
	- $\forall \epsilon > 0 \ \exists \delta(\eps) > 0: |x - 0| < \delta \implies |f(x) - 0| < \epsilon$  
	- $|x| < \delta \ ; |f(x)| < \epsilon$  
	- $|x^{3}| < \epsilon \implies |x| < \sqrt[\uproot{3}3]{\epsilon} \implies \delta = \sqrt[\uproot{3}p]{\epsilon} $  

### Определение непрерывной функции  
- $f$  непрерывна в $x_{0} \in \left[a;b\right] \Longleftrightarrow f(x_{0})\ = \ \lim{x}{x_{0}} f(x)$   

## Лекция 06.10.2022  

### Определение сложной функции (композиции)  

- $y = f(x), x = \phi(t)$  
	- $f(\phi(t)) = F(t)$  

### Теорема о непрерывности сложной функции  

- $f$  определена и непрерывна в окрестности $x_{0}$,  $x = \phi(t)$, $\phi$ определена и непрерывна в окрестности $t_{0}$ $\implies f(\phi(t)) = F(t)$ - непрерывна в окрестности $t_{0}$   
  - $F(t)$ - непрерывна в окрестности $t_{0} \implies \lim{t}{t_{0}} F(t) = F(t_{0})$. Так как $x = \phi(t)$ - непрерывна по условию теоремы $\implies \forall \{t_{n}, t_{n} \neq t_{0}\} : \lim{n}{\infty} \{t_{n}\} = t_{0}, \{\phi(t_{n})\} \xrightarrow[n \to \infty]{} \phi(t_{0}) = x_{0}$. $\lim{n}{\infty} f(x_{n}) = f(x_{0}) \implies F(t) = f(\phi(t))) ; \{F(t_{n})\} = \{f(\phi(t_{n}))\} \xrightarrow[n \to \infty]{} f(\phi(t_{0})) = f(x_{0}) = F(t_{0})$  


### Определение односторонних пределов  
- $\lim{x}{a + 0} f(x) = b \Longleftrightarrow \forall \eps > 0 \ \exists \delta(\eps) > 0 \ \forall x \in X: a < x < a + \delta \implies |f(x) - b| < \eps$  
- $\lim{x}{a - 0} f(x) = b \Longleftrightarrow \forall \eps > 0 \ \exists \delta(\eps) > 0 \ \forall x \in X: a - \delta< x  < a \implies |f(x) - b| < \eps$  

### Классификация точек разрыва  
- Устранимая точка разрыва  
	-  Существуют конечные пределы этой функции слева и справа, они равны  
- Точка разрыва 1 - ого рода  
	- Существуют конечные пределы слева и справа в точке, но они не равны друг другу  
- Точка разрыва 2 - ого рода  
	- Все остальные точки  

### Замечательные пределы  
- $\lim{x}{0} \dfrac{\sin{(x)}}{x} = 1$  

- $\lim{n}{\infty} \left(1 + \dfrac{1}{n}\right)^{n} = e$   

- $\lim{x}{\infty} \left(1 + \dfrac{1}{x}\right)^{x} = e$  

- $\lim{x}{0} \left(1 + x\right)^{\dfrac{1}{x}} = e$

- $\lim{x}{0} \ln{\left(1 + x \right)}^{\dfrac{1}{x}} = \ln{(e)} = 1 \implies \lim{x}{0} \dfrac{\ln{(1 + x)}}{x} = 1$  

- $\lim{x}{0}  \dfrac{1 - \cos{x} }{x^{2}} = \ \lim{x}{0}\ \dfrac{2\sin^{2}{(\dfrac{x}{2})}}{x^{2} }  = \  \lim{x}{0}\ \dfrac{1}{2} \underbrace{\dfrac{\sin{(\dfrac{x}{2}) \sin{(\dfrac{x}{2}) } }}{\dfrac{x}{2} \dfrac{x}{2}}}_{1} = \dfrac{1}{2}$  

- $\lim{x}{0} \dfrac{\sqrt[n]{1 \ + \ x} \ - \ 1}{x} = \ \lim{x}{0} \dfrac{\left(\sqrt[n]{1 \ + \ x} \ -\  1\right)\left(\left(\sqrt[n]{1 \ + \ x}\right)^{(n - 1)} + \left(\sqrt[ n]{1 \ + \ x}\right)^{(n - 2)}  + \ \dots \ + \ \left(\sqrt[n]{1 \ + \ x}\right)+ 1\right)}{x \left(\left(\sqrt[n]{1 \ + \ x}\right)^{(n - 1)} + \left(\sqrt[ n]{1 \ + \ x}\right)^{(n - 2)}  + \ \dots \ + \ \left(\sqrt[n]{1 \ + \ x}\right)+ 1\right)} = \\ \ \lim{x}{0} \dfrac{x}{x \left(\left(\sqrt[n]{1 \ + \ x}\right)^{(n - 1)} + \left(\sqrt[ n]{1 \ + \ x}\right)^{(n - 2)}  + \ \dots \ + \ \left(\sqrt[n]{1 \ + \ x}\right)+ 1\right)} = \ \dfrac{1}{n}$  

- Докажем $(1)$  
  - Рассмотрим $\dfrac{\sin{(x)}}{x} $    
  - $\sin{(\alpha)} = y(A)$  
  - $\cos{(\alpha)} = x(A)$  
  - $S_{OAA'} < S_{OAB'} < S_{OBB'}$  
  - $\dfrac{1}{2}\cos{(x)}\sin{(x)} < \dfrac{1}{2} \cdot 1 \cdot x < \dfrac{1}{2} \cdot 1 \cdot \tan{(x)}$  
  - $\cos{(x)}\sin{(x)} <  x < \tan{(x)}$  
  - $\cos{(x)} <  \dfrac{x}{\sin{(x)}} < \dfrac{1}{\cos{(x)}}$  
  - $\cos{(0)} \xrightarrow[x \to 0+0]{} 1 \implies \lim{x}{0 + 0} \dfrac{\sin{x}}{x} = 1$  

- Рассмотрим $\lim{x}{ 0 - 0} \dfrac{\sin{(x)}}{x}$  
  -  $\sin(-x) = -\sin(x) \implies \lim{x}{0 + 0} \dfrac{\sin{(x)}}{x} = \lim{x}{0 - 0} \dfrac{\sin(x)}{x} = \lim{x}{0} \dfrac{\sin(x)}{x} = 1$  
- Докажем $(2)$  
  - Воспользуемся Теоремой о возрастающей и ограниченной сверху последовательности:  
  - Ограниченность : $2 < (1 + \dfrac{1}{n})^{n} = 1 + n \cdot \dfrac{1}{n} + \dfrac{n(n- 1)}{2!} \cdot \dfrac{1}{n^{2}} + \dots = 2 + \dfrac{1}{2!}(1 - \dfrac{1}{n}) + \dfrac{1}{3!}(1 - \dfrac{1}{n})(1 - \dfrac{2}{n}) \dots \leq 2 + \dfrac{1}{2!} + \dfrac{1}{3!} + \dots < 2 + \dfrac{1}{2} + \dfrac{1}{2^{2}} + \dots < 2 + \dfrac{0.5}{1 - 0.5} = 3$  
  - Возрастание: $x_{n + 1} = (1 + \dfrac{1}{n + 1})^{n + 1} = 1 + (n + 1) \cdot \dfrac{1}{n + 1} + \dfrac{n(n + 1)}{2!} \cdot \dfrac{1}{(n + 1)^{2}} + \dots \implies x_{n + 1} > x_{n}$, так как каждое слагаемое уменьшается и число слагаемых $n + 1$  

### Определение эквивалентности функций в точке  

- $\lim{x}{x_{0}} \dfrac{f(x)}{g(x)} = 1 \implies f(x) \sim  g(x)$ 

### Эквивалентные бесконечно малые величины  
1. $\lim{x}{0} \dfrac{\sin(x)}{x} = 1 \implies \sin{(x)} \sim x$  
2. $\lim{x}{0} \dfrac{\ln{(1 + x)}}{x} = 1 \implies \ln{(1 + x)} \sim x$  
3. $\lim{x}{0} \dfrac{e^{x} - 1}{x} = 1 \implies e^{x} - 1 \sim x$  
4. $\lim{x}{0} \dfrac{\sqrt[n]{(1 + x)} - 1}{x} = \dfrac{1}{n} \implies \sqrt[n]{(1 + x)} - 1 \sim \dfrac{x}{n}$  

## Лекция 12.10.2022  
### Теорема о существовании и единственности общей точки системы стягивающихся отрезков  
- Пусть имеем бесконечный набор точек $\{a_{1}, a_{2}, \dots, a_{n}, \dot\}$ и концов $\{b_{1}, b_{2}, \dots, b_{n}, \dots\}$ системы вложенных друг в друга отрезков. $a_{1} < a_{2} <  \dots < a_{n} < \dots  < b_{n} < b_{n - 1} <  \dots < b_{1}$. Причем $\lim{n}{\infty} \{b_{n} - a_{n}\} = 0$.  

- Система стягивающихся отрезков имеет общую точку и притом только одну.  

  - Существование:  
    - Множество левых концов ограничено сверху $b_{n}$ и монотонно возрастает $\implies \exists \ \sup{\{a_{n}\}}$. Аналогично $\exists \ inf\{b_{n}\} \implies \lim{n}{\infty} a_{n} = \lim{n}{\infty} b_{n} = C$  


  - Единственность:  
  	- Вытекает из единственности пределов.


### Определение верхнего и нижнего пределов последовательности  
- $\overline{\lim{n}{\infty}} a_{n} = \max{\left(\lim{n}{\infty} \{a_{n_{k}}\}\right)}$  
- $\underline{\lim{n}{\infty}} a_{n} = \min{\left(\lim{n}{\infty} \{a_{n_{k}}\}\right)}$  

### Раскрытие неопределенности вида $1^{\inf}$  
- $\lim{x}{x_{0}} (u(x)^{v(x)}); \lim{x}{x_{0}} u(x) = 1; \lim{x}{x_{0}} v(x) = \infty \implies \lim{x}{x_{0}} (u(x)^{v(x)}) = \\ \lim{x}{x_{0}} ((u(x) - 1 + 1)^{v(x)}) = \lim{x}{x_{0}} [\underbrace{(1 + \underbrace{(u - 1)}_{0})^{\dfrac{1}{u - 1}}))}_{e}]^{(u - 1)v} = e^{(u - 1)v}$  

### Определение четности и нечетности функции  

- $f$ определена на симметричном относительно начала координат промежутке $x \in X$  
- $f$ четная, если: $\forall x \in X : f(-x) = f(x)$  
- $f$ четная, если: $\forall x \in X: f(-x) = - f(x)$  
### Понятие обратной функции  
- Пусть $ \exists f(x): \ y \in [c; d] \ , x \in [a;b]$.  Тогда $\exist f^{-1}(y)$.

### Свойства обратной функции

- $f(f^{-1}(y)) = y$  
- $f^{-1}(f(x)) = x$  
- График обратной функции симметричен к исходной относительно биссектрисы первой и третьей четверти координатных плоскостей  
- $y = a^{x}$, $x = \log_{a}(y)$ (логарифмическая функция)  
- $y = x^{n}$, $x = \sqrt[n]{y}$  (корень $n$ - ой степени)  
- Обратная функция существует только на промежутке монотонности  

## Лекция 19.10.2022 

### Сравнение бесконечно малых функций

- Пусть две функции $\alpha(x), \beta(x)$ определены на одном и том же множестве и являются бесконечно малыми в окрестности $x_{0}$. 

  - Тогда $\lim{x}{x_{0}} \dfrac{\alpha(x)}{\beta(x)} = 0 \implies \alpha(x)$ - бесконечно малая более высокого порядка малости, по сравнению с $\beta(x)$ в окрестности $x_{0}$,  $\alpha(x) = o(\beta(x))$.

  -  Если в качестве функции сравнения $\beta(x)$ берется $(x - x_{0})^{m}$ и $\lim{x}{x_{0}} \dfrac{\alpha(x)}{ (x - x_{0})^{m} } = C  \neq 0 \implies \alpha(x)$ имеет в точке $x_{0}$ порядок малости $m$.


  - $\lim{x}{x_{0}} \dfrac{\alpha(x)}{\beta(x)} = 0 \implies \alpha(x) = o(\beta(x))$
  - $\lim{x}{x_{0}} \dfrac{\alpha(x)}{\beta(x)} = C \neq 0 \implies \alpha(x), \beta(x)$ - б. м. одного порядка малости
  - $\lim{x}{x_{0}} \dfrac{\alpha(x)}{\beta(x)} = 1 \implies \alpha(x) \sim \beta(x), x \implies x_{0}$

### Свойства бесконечно малых функций 
-  $\alpha = o(\beta), \ \gamma = o(\beta)$, тогда : 
	- $o(\gamma) + o(\beta) = o(\beta)$
	
	- $\alpha \cdot \gamma = o(\beta^{2})$
	
	- $ f \sim C \cdot (x - x_{0})^{m},  x \rightarrow x_{0} \implies (x - x_{0})^{m}$ - главный член $f$,  $m$ - порядок малости.
	
### Производная и дифференциал

***Определение***

- Возьмем $x \in X, \ y = f(x)$. Дадим числу $x$ приращение $\Delta x$. Пусть в $x$ $f$ имеет значение $f(x)$, тогда в $x + \Delta x$ она будет иметь значение $f(x + \Delta x)$. $\Delta y = \Delta f = f(x + \Delta x) - f(x)$ - приращение $f$, вызванное приращением $\Delta x$. Составим отношение $\dfrac{\Delta y}{\Delta x}$. Получим: $\lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x} = y'(x)$.

***Пример***

- $y = f(x) = x^{n}$
	- $\Delta y = \Delta f = (x + \Delta x)^{n} - x^{n}$
	- $\lim{\Delta x}{0} \left[ \dfrac{\Delta y}{\Delta x} = \dfrac{(x + \Delta x)^{n} - x^{n}}{\Delta x} = \dfrac{x^{n} + nx^{n - 1}\Delta x + \dfrac{n(n - 1)}{2}x^{n - 2}\Delta x^{2} + \dots + \Delta x^{n} - x^{n}}{\Delta x} = \dfrac{nx^{n - 1}\Delta x + \dfrac{n(n - 1)}{2}x^{n - 2}\Delta x^{2} + \dots + \Delta x^{n}}{\Delta x}\right] = nx^{n - 1}$

### Арифметические свойства производной
- Пусть $\exists f'(x), g'(x)$ в $x_{0}$. :
	- $(f \pm g)' = f' \pm g'$ 
	
	- $(Cf)' = Cf'$
	
	- $(f \cdot g)' = f'g + fg'$
	
	- $\left(\dfrac{f}{g}\right)' = \dfrac{gf' - g'f}{g^{2}}, \ $  $g(x) \neq 0$
	
- Докажем $(3)$:
	- $\Delta u = u(x + \Delta x) - u(x)$
	
	- $\Delta v = v(x + \Delta x) - v(x)$
	
	- $(uv)' = \lim{\Delta x}{0} \dfrac{\Delta (uv)}{\Delta x}  = \dfrac{u(x + \Delta x)v(x + \Delta x) - u(x)v(x)}{\Delta x} = \dfrac{u(x + \Delta x)v(x + \Delta x) - u(x)v(x + \Delta x) + u(x)v(x + \Delta x) - u(x)v(x)}{\Delta x} = \\ = \dfrac{u(x + \Delta x) - u(x)}{\Delta x}v(x + \Delta x) + \dfrac{v(x + \Delta x) - v(x)}{\Delta x}u(x) = u'v + uv'$

- Докажем $(5)$:
	- Докажем : $\left( \dfrac{1}{v} \right)' = - \dfrac{v'}{v^{2}}$
	
	- $\Delta \left( \dfrac{1}{v} \right) =  \dfrac{1}{v(x + \Delta x)} -  \dfrac{1}{v} = \dfrac{v(x) - v(x + \Delta x)}{v(x + \Delta x)v(x)} = - \dfrac{\Delta v}{v(x + \Delta x) v(x)}$
	
	- $\left(\dfrac{1}{v}\right)' = - \lim{\Delta x}{0} \dfrac{\Delta v}{\Delta x \cdot v(x + \Delta x) v(x)} = - \dfrac{v'}{v^{2}}$
	
	- $\left(\dfrac{u}{v}\right)' = \left(u \cdot \dfrac{1}{v}\right)' = u' \cdot \dfrac{1}{v} + u \cdot \left( \dfrac{1}{v}\right)' = \dfrac{u'}{v} + u\left( - \dfrac{v'}{v^{2}}\right) = \dfrac{vu' - v'u}{v^{2}}$

### Производная сложной функции
- $y = f(x), x = \phi(t)$
- $\lim{\Delta t}{0} \left[ \dfrac{\Delta y}{\Delta x} \cdot \dfrac{\Delta x}{\Delta t} \right] = f'(x) \cdot \phi'(t) = f'(\phi(t)) = f'(\phi(t)) \cdot \phi'(t)$

### Производная обратной функции
- $y = f(x)$
	- $\lim{\Delta y}{0} \left[\dfrac{\Delta y}{\Delta x} = \dfrac{1}{\dfrac{\Delta x}{\Delta y}}\right] = \dfrac{1}{(f^{-1}(y))'}  = \dfrac{1}{x'(y)}$ 

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

- Рассмотрим уравнение окружности : $x^{2} + y^{2} = R^{2}$
	- $\begin{equation*}
  	\begin{cases}
	  x = R\cos{(t)}, \ t \in [0; 2\pi] \\
	  y = R\sin{(t)}, \ t \in [0; 2\pi] 
	  \end{cases}
    \end{equation*}$
- Пусть $x = \phi{(t)}, \ y = \psi{(t)},  \ \exists \lim{\Delta t}{0} \dfrac{\Delta x}{\Delta t} = \phi', \ \exists \lim{\Delta t}{0} \dfrac{\Delta y}{\Delta t} = \psi'$
- Рассмотрим : $\lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x} = \lim{\Delta x, \ \Delta t}{0, \ 0} \dfrac{\Delta y \cdot \Delta t}{\Delta x \cdot \Delta t} = \lim{\Delta t}{0} \dfrac{\Delta y}{\Delta t} \cdot  \lim{\Delta x}{0} \dfrac{\Delta t}{\Delta x} = \dfrac{\lim{\Delta t }{0} \dfrac{\Delta y}{\Delta t}}{\lim{\Delta t }{0} \dfrac{\Delta x}{\Delta t}} = \dfrac{y'(t)}{x'(t)}$

### Производная неявно заданной функции
- $x^{2} + y^{2} = R^{2}$
- $2x + 2y \cdot y' = 0 \implies y'(x) = - \dfrac{x}{y}$ 

### Определение непрерывности в терминах приращений

- $f$ непрерывна в $x_{0}$ , если $\Delta x \rightarrow 0 \implies \ \Delta y \rightarrow 0$.
  -  $\forall \eps > 0 \ \exists \delta(\eps) > 0 \ \forall x \in X : |x - x_{0}| = |\Delta x| < \delta \implies |f(x_{0} + \Delta x) - f(x_{0})| = |\Delta y| < \eps $. 


### Необходимое условие существования производной

- $\exist f'(x_{0}) \implies$ $f$ непрерывна в $x_{0}$. 
  -  $f'(x)  = \lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x} \implies \Delta x \rightarrow 0 \implies \Delta y = 0$


### Определение дифференциала функции
- $dy=   \Delta y = C\Delta x + o(\Delta x)$

### Алгебраические свойства дифференциала функции
1. $d(u + v) = du + dv$
2. $d(uv) = udv + vdu$
3. $d\left (\dfrac{u}{v} \right) = \dfrac{vdu - udv}{v^{2}}$

## Лекция 02.11.2022
### Необходимое и достаточное условие дифференцируемости функции в точке
- $f$ дифференцируема в $x_{0}$ тогда и только тогда, когда $ \ \exists f'(x_{0})$ .

  - Необходимость:
  	-  $\Delta y = C\Delta x + o\left(\Delta x\right) \implies \lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x} = \lim{\Delta x}{0} \left(C + \dfrac{o\left(\Delta x\right)}{\Delta x}\right) = f'(x_{0}) = C$. 

  - Достаточность:
  	- $f'(x_{0}) = \lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x} =  C \implies \Delta y =  C\Delta X + o(\Delta x) = f'(x_{0})\Delta x + o(\Delta x) \implies \Delta y  = \underbrace{f'(x_{0})\Delta x}_{dy} + o(\Delta x) \implies dy = f'(x)dx$


### Инвариантность формы дифференциала первого порядка
- $dy = f'(x)dx$ имеет такую форму записи как в случае независимой переменной $x$, так и в случае зависимой.
  - Пусть $\phi(t)$ дифференцируема в окрестности $t_{0}$, $f(x)$ дифференцируема в окрестности $x_{0} = \phi(t_{0})$.Тогда рассмотрим в окрестности $t_{0} :F(t) = f(\phi(t))$. $F'(t) = f'(\phi(t)) \cdot \phi'(t)$ $ \implies F'(t)dt = f'(\phi(t)) \underbrace{\phi'(t)dt}_{dx} \implies d F = f'(\phi(t))dx$. 


### Производная и дифференциалы высших порядков
-  Производная $n$ - ого порядка в $x_{0}$ $f$ называется производная от производной порядка $n - 1$ (если она существует в $x_{0}$).

- $\dfrac{d^{n}y}{dx^{n}} = f^{(n)}(x) = \dfrac{d}{dx}\left(\dfrac{d^{n - 1}y}{dx^{n - 1}}\right)$

### Формула Лейбница для $n$ - ой производной произведения функций
- $\left(uv\right)^{(n)} = \displaystyle\sum_\limits{k = 0}^{n} \binom{n}{k}u^{(n - k)}v^{(k)}$

### Дифференциал второго порядка и выше 
- Дифференциал второго порядка и выше обладает свойством инвариантности в зависимости от того, является ли $x$ независимой переменной $x = \phi(t)$ или не является.
- Вычислим второй дифференциал для зависимой переменной: $d^{2}y = d(dy) = d(f'(x)dx) = d(f'(x))dx + f'(x)d(dx) = f''(x)dx^{2} + f'd^{2}x$ Для независимой переменной: $d^{(2)}y = d(dy) = d(f'(x)dx) = f''(x)dx^{2}$

### Теорема об ограниченности функции в некоторой окрестности точки
- Функция, имеющая конечный предел в некоторой точке $x_{0}$ ограничена в некоторой окрестности $x_{0}$.

  - $|x - x_{0}| < \delta  \implies x_{0} - \delta < x < x_{0} + \delta$

  - $|f(x) - A| < \eps \implies A - \eps < f(x) < A + \eps$.


### Теорема о сохранении знака функции в точке.
- Пусть $\exists \lim{x}{x_{0}} f(x) = A \neq 0$.  
  - $x_{0} - \delta < x < x_{0} + \delta \implies A - \eps < f(x) < A + \eps$.  $\eps : \eps < \big|A\big| \implies f(x)$ сохраняет знак в $x_{0}$

### Теорема о равенстве нулю функции в окрестности точки.
- Пусть $f$ непрерывна в $x_{0}$ и имеет разные знаки в левой и правой полуокрестностях $x_{0}$. Тогда в $f(x_{0}) = 0$.
  -  $\forall \eps > 0 \ \exists \delta(\eps) > 0 \ \forall x \in X:|x - x_{0}| < \delta \implies |f(x) - f(x_{0})| < \eps ; f(x_{0} + \delta) > 0 \and f(x_{0} - \delta) < 0$. Т. к. $ 0 > f(x_{0} - \delta) \leq f(x) \leq f(x_{0} + \delta) > 0 \implies f(x_{0}) = 0$.


## Лекция 09.11.2022
### Обобщение теоремы о равенстве нулю функции в окрестности точки
- Непрерывная на отрезке $x \in \left[a; b\right]$ функция, принимающая на нем значения в промежутке $y \in \left[A;B\right], \ y(a) = A, \ y(b) = B$ примет в некоторой точке этого отрезка любое промежуточное значение $C:$ $A < C < B$
  - Введем вспомогательную функцию $\phi(x) = f(x) - C$, тогда $\phi(x)$ примет на концах значения: $\phi(a) = f(a) - C = A - C < 0, \ \phi(b) = f(b) - C = B - C > 0$. По предыдущей теореме $\phi(x)$ непрерывна на $\left[a;b\right]$ и принимает на его концах значения разных знаков, значит найдется такая точка $c \in \left[a;b\right]$ в которой $\phi(c) = 0$. $\phi(c) - C = 0 \implies f(c) = C$


### Первая теорема Вейерштрасса о непрерывных функциях
- Функция, непрерывная на отрезке ограничена на нем.
  - Допустим $f(x)$ не ограничена. Рассмотрим число $x_{n_{1}}:$ $f(x_{n_{1}}) > n_{1}$,  $f(x_{n_{2}}) > n_{2} > n_{1}$, $f(x_{n_{k}}) > n_{k} > n_{k - 1}$ $ \dots$Элементы последовательности $\{x_{1}, x_{2}, \dots , x_{n_{k}}, \dots\}$ принадлежат отрезку $\left[a;b\right]$ , $\{x_{n_{k}}\}$ ограничена и по теореме Больцано - Вейерштрасса: $\lim{n_{k}}{\infty} x_{n_{k}} = c \in \left[a;b\right]$, но $\nexists \lim{x}{x_{n_{k}}}f(x_{n_{k}})$ по построению. Однако, $\lim{x}{x_{n_{k}}} f(x_{n_{k}}) = f(c)$ по определению непрерывной функции.


### Вторая теорема Вейерштрасса о непрерывных функциях
- Функция, непрерывная на отрезке, достигает на нем супремум и инфимум.
  - Пусть во всех точках  отрезка $\left[a; b\right]$  выполняется $ f(x) \neq M = \sup{f}$. Рассмотрим вспомогательную функцию $\phi(x) = \dfrac{1}{M - f(x)}$ $;f(x)$  непрерывна $\implies$ $\phi(x)$  непрерывна на отрезке $\implies \phi(x)$  ограничена на нем. $\implies \exists M' :  \phi(x) < M'$ $;\dfrac{1}{M - f(x)} < M'; \ M - f(x) > \dfrac{1}{M'}; \ f(x) < M - \dfrac{1}{M'} \implies M \neq \sup{f(x)}$


### Понятие локального максимума и минимума функции (локального экстремума)

- $f(x)$ имеет в точке $x_{0}$ максимум, если в некоторой окрестности этой точки выполняется $f(x) \leq f(x_{0})$ и имеет строгий максимум, если в точках окрестности $\left(x \neq x_{0} \right)$ выполняется$\ f(x) < f(x_{0})$. Аналогично для локального минимума и строгого минимума.

### Теорема Ферма
- $f(x)$, дифференцируемая в окрестности точки $x_{0}$ и  $f'(x_{0}) = 0$, если $x_{0}$ - точка экстремума этой функции.
  - Путь $x_{0}$ - точка максимума. $f'(x_{0}) = \lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x}$. Положим $\Delta x > 0 \implies \Delta y < 0\implies \lim{\Delta x}{0 + 0} \dfrac{\Delta y}{\Delta x} \leq 0$, положим $\Delta x < 0 \implies \Delta y < 0 \implies \dfrac{\Delta y}{\Delta x} > 0 \implies \lim{\Delta x}{0 - 0} \dfrac{\Delta y}{\Delta x} \geq 0 \implies \lim{\Delta x}{0} \dfrac{\Delta y}{\Delta x} = 0$


### Теорема Ролля
- $f$ дифференцируема на $\left(a ; b\right)$ и непрерывна на $\left[a;b\right]$ , $f(a) = f(b) \implies$  $\exists \xi \in [a; b]: f'(\xi) = 0$.

  -  $f$  достигает на $[a; b]$ $\max{f} = M$ и $\min{f} = m$. 

  - $M = m \implies f'(\xi) = const$

  - $M \neq m  \implies$  $f'(\xi) = 0$


### Теорема Лагранжа (о конечных приращениях)
- $f$ дифференцируема на  $\left(a; b\right)$ и непрерывна на $\left[a;b\right];f(a) \neq f(b) \implies \exists \xi \in [a; b] :f'(\xi) = \dfrac{f(b) - f(a)}{b - a}, \ f(b) > f(a)$.

  - Рассмотрим: $F(x) = f(x) - f(a) - \dfrac{f(b) - f(a)}{b - a} (x - a)$

  - $F(a) = f(a) - f(a) - \dfrac{f(b) - f(a)}{b - a}(a - a) = F(b) = f(b) - f(a) - \dfrac{f(b) - f(a)}{b - a}(b - a) = 0 \implies \exists \ \xi: F'(\xi) = 0 \implies \\ \implies F'(x) = f'(x) - \dfrac{f(b) - f(a)}{b - a} \implies f'(\xi) - \dfrac{f(b) - f(a)}{b - a} = 0 \implies f'(\xi) = \dfrac{f(b) - f(a)}{b - a}$.


### Теорема Коши (о конечных приращениях)
-  $f$ и $g$ дифференцируемы на $\left(a;b\right)$ и непрерывны на  $\left[a;b\right]$, $g'(x) \neq 0 \implies \exists \xi \in [a;b]: \dfrac{f'(\xi)}{g'(\xi)} = \dfrac{f(b) - f(a)}{g(b) - g(a)}$

  - Рассмотрим $F(x) = f(x) - f(a) - \dfrac{f(b) - f(a)}{g(b) - g(a)} (g(x) - g(a))$.

  - $F(a) = F(b) = 0 \implies \exists \xi: \ F(\xi) = 0, \ F'(x) = f'(x) - \dfrac{f(b) - f(a)}{g(b) - g(a)} \cdot g'(x)$

  - $f'(\xi) = \dfrac{f(b) - f(a)}{g(b) - g(a)} \cdot g(\xi) \implies \dfrac{f'(\xi)}{g'(\xi)} = \dfrac{f(b) - f(a)}{g(b) - g(a)}$


## Лекция 16.11.2022
### Правило Лопиталя
- Пусть $f$ и $g$   непрерывны и дифференцируемы в проколотой окрестности точки $x_{0},$$g' \neq 0 \implies \exists \lim{x}{x_{0}} \dfrac{f(x)}{g(x)} = \ \lim{x}{a} \dfrac{f'(x)}{g'(x)}$
  - Доопределим их пределом, равным нулю. Тогда они станут непрерывными на всей окрестности точки $x_{0}$. Рассмотрим последовательность $\{x_{1}, x_{2}, \dots, x_{n}, \dots\}$ таких, что $\lim{n}{\infty}{x_{n}} = x_{0}$ начиная с некоторого номера все члены последовательности будут принадлежать рассмотренной окрестности. Возьмем из них точку $x_{k}$ и рассмотрим отрезок $\left[a, x_{k}\right] \ (x_{k} > a)$. Тогда на этом отрезке $f, \ g$ непрерывны и дифференцируемы на интервале $(a , x_{k})$. На этом промежутке выполнено условие теоремы Коши о конечных приращениях, то есть $\exists \xi_{k} \in (a, x_{k})$, в которой $\dfrac{f(x_{k}) - f(a)}{g(x_{k}) - g(a)} = \dfrac{f'(\xi_{k})}{g'(\xi_{k})}$. $f(a) = g(a) = 0 \implies \dfrac{f(x_{k})}{g(x_{k})} = \dfrac{f'(\xi_{k})}{g'(\xi_{k})}$. $k \to \infty, \ x_{k} \to a \implies \xi_{k} \to a$. $\exists \lim{k}{\infty} \dfrac{f'(\xi_{k})}{g'(\xi_{k})} \implies \exists \lim{x}{a} \dfrac{f(x_{k})}{g(x_{k})} = \ \lim{x}{a} \dfrac{f'(x_{k})}{g'(x_{k})} \implies \lim{x}{a} \dfrac{f(x)}{g(x)} = \ \lim{x}{a} \dfrac{f'(x)}{g'(x)}$.


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
- Возрастающие и убывающие функции называются монотонными

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
- Пусть дифференцируема на некотором интервале $(a;b)$ $f$ всюду на этом интервале имеет график, расположенный ниже касательной в соответствующей точке, то в этой точке график имеет выпуклость вверх, если выше, то выпуклость вниз (вогнутость).

***Утверждение***
- Если в окрестности некоторой точки $C$ вторая производная (если существует) не меняет знака и отрицательна, то в окрестности этой точки график функции направлен выпуклостью вверх, если положительна, то вниз. Пусть в окрестности $C$ $f''(x)$ отрицательна. Напишем уравнение касательной, проведенной в этой точке.  Пусть $Y$ - ордината к касательной, а $y$ - ордината графика функции. $Y =  f(С) + f'(С)(x - С)$
- Разложим функцию $y = f(x)$ в точке $C$ по формуле Тейлора:
	- $f(x) = f(С) + f'(С)(x - С) + \dfrac{f''(\xi)}{2!}(x - С)^{2}$ 
	- $y - Y = \dfrac{f''(\xi)}{2!}(x - С)^{2}$
- $f''(\xi) < 0 \implies y - Y < 0, \ y < Y$, а это и есть определение выпуклости вверх

### Точка перегиба графика
- Если дифференцируемая в окрестности $C$ и $f''$ меняет при переходе через эту точку направление выпуклости, то точка $C$ называется точкой перегиба

### Третье достаточное условие экстремума и точки перегиба
- Пусть $f$ дифференцируема в окрестности $C$ $n$ раз, а в $C$ - $(n + 1)$ раз. Если в точке $C$ производные до $n$ -ого порядка включительно равны нулю, $f^{(n + 1)}(C) \neq 0 \implies$  при $n$ - нечетном точка $C$ является точкой экстремума, а именно если  $f^{(n + 1)}(C) < 0$, то $\max$, если $f^{(n + 1)}(C) > 0$, то $\min$. Если $n$ - четное, то $C$ - точка перегиба.

***Доказательство***
- Действительно, пусть $n$ - нечетное, тогда при $f^{(n + 1)}(C) \neq 0$ для $f^{(n)}(x)$ как функции, для которой $f^{(n + 1)}$ - ее первая производная, $C$ - точка возрастания (убывания) для $f^{(n)}(x)$. Рассмотрим разложение по формуле Тейлора в точке $C$ второй производной:
	- $f''(x) = f''(C) + \dfrac{f'''(C)}{1!}(x - C) + \dots + \dfrac{f^{(n)}(C)}{n!}(x - C)^{n} + \dfrac{f^{(n + 1)}(\xi)}{(n + 1)!}(x - C)^{n + 1}$
	- Так как по условию все производные до $n$ включительно равны нулю в точке $C \implies f''(x) =\dfrac{f^{(n + 1)}(\xi)}{(n + 1)!}(x - C)^{n + 1}$
	- $f^{(n + 1)}(\xi) < 0 \implies f''(x) < 0 \implies \max$
	- $f^{(n + 1)}(\xi) > 0 \implies f''(x) > 0 \implies \min$
- Пусть $n$ - четное, $f^{(n + 1)}(\xi) \neq 0$. Разложим по формуле Тейлора $f''(x)$.
	- $f''(x) = \dfrac{f^{(n + 1)}(\xi)}{(n + 1)!}(x - C)^{(n + 1)}$. 
    - $f''(x) = \dfrac{f^{(n + 1)}(\xi)}{(n + 1)!}(x - C)^{(n + 1)}$. $(x - C)$ меняет знак при переходе, значит $f''(x)$ меняет знак при переходе через $C$.

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

- Пусть на $\left(a;b\right)$ $f(x)$ имеет первообразные $F_{1}(x)$ и $F_{2}(x)$. Докажем, что отличаются на $C$. Введем функцию $\Phi(x) = F_{1}(x) + F_{2}(x)$ в любой точке $x$. $\Phi'(x) = F_{1}'(x)  + F_{2}'(x) = f(x) - f(x) = 0$. Если $x$ - любая точка просматриваемого промежутка, то по теореме Лагранжа о конечных приращениях существует внутри промежутка точка $\xi$, что $\Phi(b) - \Phi(a) = \Phi'(\xi)(b - a)$. $\Phi(x + \Delta x) - \Phi(x) = \Phi'(\xi) \Delta x$,  $\Phi'(\xi) = 0 \implies \Phi(x + \Delta x) = \Phi(x)  \implies \Phi(x) = const \implies F_{1}(x) - F_{2}(x) = C \implies F_{1}(x) = F_{2}(x) + C$.

***Определение***
- Если известна какая - то первообразная, то совокупность всех первообразных имеет вид $F(x) + C$ и называется неопределенным интегралом

***Обозначение***
- $F(x) + C = \displaystyle\int f(x) dx $

### Алгебраические свойства неопределенного интеграла
- $d\left(\displaystyle\int f(x) dx \right) = \left( F(x) + C \right) ' dx = F'(x) dx = dF(x)$
- $\displaystyle\int dF = \displaystyle\int F'(x) dx = \displaystyle\int f(x) dx + C$
- $\displaystyle\int \left(\alpha f(x) + \beta g(x) \right) dx = \alpha \displaystyle\int f(x) dx + \beta \displaystyle\int g(x) dx$

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
	- Пусть имеем $\displaystyle\int f(x) dx$, если $x = \phi(t)$, так что $dx = \phi'(t) dt$, то обозначив первообразную функции $f(\phi(t))$ через $G(t)$ получим $\displaystyle\int f(\phi(t)) dt = G(t) + C \implies G'(t) = f(\phi(t)) \cdot \phi(t) \implies G(t) = \displaystyle\int f(\phi(t))\phi'(t) dt = \displaystyle\int f(x) dx$ 
- Метод интегрирования по частям
	- $d(u(x) v(x)) = udv + vdu$
	- $\displaystyle\int d(uv) dx = \displaystyle\int u dv + \displaystyle\int v du$
	- $\displaystyle\int u dv = uv - \displaystyle\int v du$
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
1. $\displaystyle\int \dfrac{A}{x - a} dx = A\ln{|x - a|} + C$
2. $\displaystyle\int \dfrac{A}{(x - a)^{\alpha}} dx = \dfrac{A(x - a)^{-\alpha + 1}}{-\alpha + 1} + C$
3. $\displaystyle\int \dfrac{Mx + N}{x^{2} + px + q} dx = \dfrac{M}{2} \displaystyle\int \dfrac{\dfrac{Mx + N}{M} \cdot 2}{x^{2} + px + q} dx = \dfrac{M}{2} \displaystyle\int \dfrac{2x + \dfrac{2N}{M}}{x^{2} + px + q}dx = \\ \dfrac{M}{2} \displaystyle\int \dfrac{2x + p - p + \dfrac{2N}{M}}{x^{2} + px + q} dx = \dfrac{M}{2} \displaystyle\int \dfrac{2x + p}{x^{2} + px + q} dx + \dfrac{M}{2} \displaystyle\int \dfrac{\dfrac{2N}{M} - p}{x^{2} + px + q} dx =  \\ \dfrac{M}{2} \displaystyle\int \dfrac{d(x^{2} + px)}{x^{2} + px + q} + \dfrac{M}{2} \displaystyle\int \dfrac{B}{x^{2} + px + q} dx = \\ \dfrac{M}{2} \ln{|x^{2} + px + q|} + \dfrac{MB}{2} \displaystyle\int \dfrac{dx}{x^{2} + px + q} = \dfrac{M}{2} \ln{|x^{2} + px + q|} + \dfrac{MB}{2} \displaystyle\int \dfrac{dx}{x^{2} + \dfrac{2px}{2} + q + \dfrac{p^{2}}{4} - \dfrac{p^{2}}{4}} = \\  \dfrac{M}{2} \ln{|x^{2} + px + q|} + \dfrac{MB}{2} \displaystyle\int \dfrac{dt}{t^{2} + \left(q - \dfrac{p^{2}}{4}\right)}\bigg|_{t = x + \dfrac{p}{2}} = \\  \dfrac{M}{2} \ln{|x^{2} + px + q|} + \dfrac{MB}{2} \displaystyle\int \dfrac{dt}{t^{2}  - A}\bigg|_{t = x + \dfrac{p}{2}}^{A = - q + \dfrac{p^{2}}{4}} = \dfrac{M}{2} \ln{|x^{2} + px + q|} + \dfrac{MB}{4\sqrt{A}} \ln{\bigg|\dfrac{\sqrt{A} - x}{\sqrt{A} + x}}\bigg| + C$
4. $\displaystyle\int \dfrac{Mx + N}{(x^{2} + px + q)^{\alpha}} dx $ Решается понижением порядка с помощью рекуррентной формулы.
	-  $I_{\alpha} = \displaystyle\int \dfrac{dt}{(t^{2} + A)^{\alpha}} = \displaystyle\int \dfrac{A - t^{2} + t^{2}}{(t^{2} + A)^{\alpha}} dt = \displaystyle\int \dfrac{dt}{(t^{2} + A)^{\alpha - 1}} - \displaystyle\int \dfrac{t^{2}dt}{(t^{2} + A)^{\alpha}} = \\ I_{\alpha - 1} - \displaystyle\int u dv \bigg|_{A = -C} = I_{\alpha - 1} - \dfrac{t}{2(C - \alpha)(t^{2} + C)^{\alpha - 1}} + \displaystyle\int \dfrac{dt}{2(C - \alpha)(t^{2} + C)^{\alpha - 1}} = \\ I_{\alpha - 1} - \dfrac{t}{2(C - \alpha)(t^{2} + C)^{\alpha - 1}} + \dfrac{I_{\alpha - 1}}{2(C - \alpha)} = - \dfrac{t}{2(\alpha - C)(t^{2} + C)^{\alpha - 1}} + I_{\alpha - 1} \left(\dfrac{2(C - \alpha) + 1}{2(C - \alpha)}\right)$

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

## Лекция 08.02.2023
### Определенный интеграл
- На отрезке $\left[a;b\right]$ задана $f$, $a = x_{0} < x_{1} < x_{2} < \dots < x_{n-1} < x_{n} = b$
- $\left[x_{i -1};x_{i}\right]$ - $i$ - отрезок разбиения
- Внутри каждого отрезка разбиения возьмем произвольную точку $\xi_{i}$
- $\sigma = f(\xi_{1})\Delta x_{1} + f(\xi_{2})\Delta x_{2} + \dots +f(\xi_{n})\Delta x_{n}= \sum\limits_{i = 1}^{n} f(\xi_{i})\Delta x_{i}$
- $T$ - разбиение, $t$ - выбранный отрезок и точка $\xi$
- $\Delta = \max{\left|\Delta x_{i}\right|}$ - характеристика $T$
- Определенным интегралом называется $\lim{\Delta}{0}\sigma = I = \displaystyle\int\limits_{a}^{b} f(x)dx$
- $f$ имеет интеграл на $\left[a;b\right] \implies$ она интегрируема
### Ограниченность интегрируемой функции на отрезке
- $f$ интегрируема на $\left[a;b\right] \implies$ она ограничена на нем

***Доказательство***
- Предположим противное, т.е. $f$ интегрируема, но не ограничена $\implies$ в интегральной сумме $f$ обращается в $\inf$ на некотором $\Delta x \implies \lim{\Delta}{0}\sigma = \inf$
### Верхняя и нижняя интегральная суммы
- $S = M_{1}\Delta x_{1} + M_{2}\Delta x_{2} + \dots +M_{n}\Delta x_{n} = \sum\limits_{i = 1}^{n} M_{i}\Delta x_{i} \ , M_{i} = \sup_{\left[x_{i - 1}, x_{i}\right]}{f(x)}$ - Верхняя интегральная сумма
- $s = m_{1}\Delta x_{1} + m_{2}\Delta x_{2} + \dots +m_{n}\Delta x_{n} = \sum\limits_{i = 1}^{n} m_{i}\Delta x_{i} \ , m_{i} = inf_{\left[x_{i - 1}, x_{i}\right]}{f(x)}$ - Нижняя интегральная сумма
- $s \leq f(\xi_{i})\Delta x_{i} \leq S \implies s \leq \sigma \leq S$

### Свойства интегральных сумм
- Если к данному $T$ добавить $t$, то у получившегося разбиения $T'$: $S' \leq S$, $s \leq s'$
	- $T: S = M_{i}\Delta x_{i}$
	- $T': S' = M'\Delta x' + M_{i}\Delta x_{i}$
	- Отсюда следует, что это утверждение верно при добавлении $p$ точек
- Для двух произвольных разбиений $T'$ и $T''$ выполняется: $s' \leq S''$, $s'' \leq S'$
	- Возьмем $T$, состоящее из точек разбиения $T'$ и $T''$. Его можно рассматривать как разбиение, полученное из $T'$ добавлением $T''$, при этом $s' \leq s$ и $S \leq S'$. Аналогично, его можно рассматривать как получившееся из $T''$ добавлением $T'$, при этом $s'' \leq s$ и $S \leq S''$.
	- $s' \leq s \leq S \leq S''$
	- Это свойство показывает, что все нижние интегральные суммы $s$ ограничены сверху множеством верхних интегральных сумм, значит имеет точную верхнюю грань $\underline{I} = \sup{s}$ - нижний интеграл Дарбу, $\upline{I} = inf{S}$
- $\underline{I} \leq \upline{I}$
	- Действительно, предположим противное $\upline{I} \leq \underline{I} \implies \upline{I} - \underline{I} > 0$. Возьмем $\eps = \upline{I} - \underline{I}$. По определению точных граней: $\exists S: S < \upline{I} + \eps$ и $\exists s: s > \underline{I} - \eps$. Положим $\eps = \dfrac{\eps}{2}$
	- $S - s < \upline{I} - \underline{I} + \eps$
	- $S - s < -\eps + \eps = 0$
	- $S  < s$ Получим противоречие.
- Пусть разбиение $T'$ получено из $T$ добавлением некоторого произвольного $p$ точек разбиения. Пусть далее $M = \sup_{\left[a;b\right]}{f(x)}, \ m = inf_{\left[a;b\right]}{f(x)} \implies S - S' \leq \left(M - m \right) p \Delta$
	- Докажем для $p = 1$.
	- $S - S'' \leq \left(M - m\right) \Delta$. Так как добавление одной точки произведено на некотором частичном отрезке $\left[x_{i-1}, x_{i}\right]$, то рассмотрим изменение интегральных сумм на этом фрагменте.
	- $\Delta x' + \Delta x'' = \Delta x$
	- $S - S' = M_{i}\Delta x_{i} - M'_{i}\Delta x' - M''_{i}\Delta x'' = \\ M_{i}\left(\Delta x' + \Delta x'' \right) - M'_{i}\Delta x' - M''_{i}\Delta x'' \leq M\left(\Delta x' + \Delta x''\right) - m\left(\Delta x' + \Delta x''\right) = \left(M - m\right)\Delta x' + \left(M - m \right)\Delta x'' = \\ \left(M - m\right)\Delta x$ 
### Лемма Дарбу
- $\lim{\Delta}{0} S = \upline{I}$, $\lim{\Delta}{0} s = \underline{I}$
- Докажем $\lim{\Delta}{0} S = \upline{I}$
	-  $\upline{I} = inf(S) \implies \forall \eps \ \exists T^{\star}: S^{\star} - \upline{I} < \dfrac{\eps}{2}$
	- Рассмотрим все разбиение, $\Delta < \delta: T, \ \delta = \dfrac{\eps}{2\left(M - m\right)p}$ ; $M$ = $\max_{\left[a; b\right]}{f}$; $m$ = $\min_{\left[a; b\right]}{f}$; $p$ - число точек в $T^{\star}$
	- Добавим к $T$ точки $T^{\star}$, получим $T', S' \implies S - S' \leq \left(M - m\right)p\Delta \leq \left(M - m\right)p\dfrac{\eps}{2(M - m)p} = \dfrac{\eps}{2}$ 
	- Добавим к $T^{\star}$ точки $T$, получим $T'$, $S' \implies S - S^{\star} \leq \dfrac{\eps}{2}$
	- $\upline{I} \leq S' \leq S^{\star}$
	- $ S' - \upline{I} \leq S^{\star} - \upline{I} < \dfrac{\eps}{2}$
	- $S - S' + S' - \upline{I} \leq \dfrac{\eps}{2} + \dfrac{\eps}{2}$
	- $S - \upline{I} < \eps \implies \lim{\Delta}{0} = \upline{I}$

## Лекция 15.02.2023
### Необходимое и достаточное условие интегрируемости функции на отрезке
- Необходимость
- Дано : $\exists I = \displaystyle\int_\limits{a}^{b} f(x)dx = \lim{\Delta}{0} \sigma$ $, \forall \eps > 0 \ \exists \delta > 0 : \Delta < \delta \rightarrow \left|I - \sigma\right| < \eps$
- Доказать: $\forall \eps > 0 \ \exists T: S - s < \eps$
	- $S - s = S - \sigma_{i} + \sigma_{i} - I + I - \sigma_{k} + \sigma_{k} - S \leq \left|S - \sigma_{i}\right| + \left|\sigma_{i} - I\right| + \left|I - \sigma_{k}\right| + \left|\sigma_{k} - S\right| \leq \dfrac{\eps}{4} + \dfrac{\eps}{4} + \dfrac{\eps}{4} + \dfrac{\eps}{4} = \eps$
- Достаточность
- Дано: $\forall \eps > 0 \ \exists T: S - s < \eps$
- Доказать: $\exists I = \displaystyle\int_\limits{a}^{b} f(x)dx = \lim{\Delta}{0} \sigma$ $, \forall \eps > 0 \ \exists \delta > 0 : \Delta < \delta \rightarrow \left|I - \sigma\right| < \eps$
	- $\upline{I} = \lim{\Delta}{0}S \implies S - \upline{I} < \dfrac{\eps}{2}$
	- $\underline{I} = \lim{\Delta}{0}s \implies S - \underline{I} < \dfrac{\eps}{2}$
	- $S - \upline{I} + \underline{I} - s < \eps \implies \upline{I} - \underline{I} < \eps$
	- $\lim{\Delta}{0} \upline{I} = \underline{I} = I$
	- $s < \sigma < S \implies \lim{\Delta}{0} \sigma = I$

### Некоторые классы интегрируемых функций
- Непрерывная на отрезке функция интегрируема на нем
	- Доказательство: $f(x)$  непрерывна на $\left[a; b\right] \implies$ она равномерно непрерывна на $\left[a; b\right]$ по Теореме Кантора.
	- $S - s = \displaystyle\sum\limits_{i = 1}^{n}\left(M_{i} - m_{i}\right)\Delta x_{i} \leq \dfrac{\eps}{b - a}\sum\limits_{i = 1}^{n}\Delta x_{i} = \eps$
	- В силу равномерной непрерывности $\forall \eps > 0 \ \exists \delta > 0: \Delta < \delta \implies \left|f(x_{i}) - f(x_{i}')\right| < \eps$, где $x_{i} - x_{i}' < \delta$
- Монотонная и определенная на отрезке функция интегрируема на нем
	- Доказательство : Для монотонно возрастающей
	- $\Delta < \delta = \dfrac{\eps}{f(b) - f(a)}$
	- $S - s = \displaystyle\sum\limits^{n}_{i = 1}\left(M_{i} - m_{i}\right)\Delta x_{i} \leq \Delta  \sum\limits_{i = 1}^{n}\left(M_{i} - m_{i}\right) = \Delta \left(f(x_{1}) - f(a) + f(x_{2}) - f(x_{1}) + \dots + f(b)\right) = \Delta \left(f(b) - f(a)\right) < \eps$ 
- Пример : $f(x) = \begin{equation*}  
	  \begin{cases}  
		   0, x \in \RR \backslash \QQ \\  
		   1, x \in \QQ  
	  \end{cases}  
	  \end{equation*}$
- $x \in \QQ  : \sigma = 1 \cdot \Delta x_{1} + 1  \cdot \Delta x_{2} + \dots + 1 \cdot \Delta x_{n} = b - a, \ \lim{\Delta}{0} \sigma = b - a$
- $x \in \RR \backslash \QQ : \sigma = 0 \cdot \Delta x_{1} + 0  \cdot \Delta x_{2} + \dots + 0 \cdot \Delta x_{n} = 0, \ \lim{\Delta}{0} \sigma = 0$
### Теорема о среднем
- Пусть $f(x)$ интегрируема на $\left[a;b\right]$. Тогда $\exists \mu \ \left(m < \mu < M\right): \displaystyle\int\limits_{a}^{b} f(x) dx = \mu\left(b - a\right)$
	- Доказательство: 
	- $f(x)$ интегрируема $\implies$ она ограничена: $m \leq f(x) \leq M$ 
	- $m\left(b - a\right) \leq \displaystyle\int\limits_{a}^{b} f(x) dx \leq M\left(b - a\right)$
	- $m \leq \dfrac{\displaystyle\int\limits_{a}^{b} f(x) dx}{\left(b - a\right)} \leq M \implies \dfrac{\displaystyle\int\limits_{a}^{b} f(x) dx}{\left(b - a\right)} = \mu \implies \displaystyle\int\limits_{a}^{b} f(x) dx = \mu\left(b - a\right)$
### Следствие из теоремы о среднем
- $f(x)$ непрерывна на $\left[a;b\right] \implies \xi \in \left[a;b\right] : f(\xi) = \mu \implies \displaystyle\int\limits_{a}^{b} f(x) dx = f(\xi)(b - a)$

## Лекция 22.02.2023
### Интеграл с переменным верхним пределом
- Пусть $f(x)$ непрерывна на $\left[a; b\right]$ и существует интеграл $\displaystyle\int\limits_{a}^{b} f(x) dx$, а также для любой точки $C$ этого интервала существует интеграл $\displaystyle\int\limits_{C}^{x} f(t) dt$ 
- Тогда функция верхнего предела $F(x) = \displaystyle\int\limits_{C}^{x} f(t) dt$ является первообразной на $\left[a;b\right]$ для $f(x)$
- Доказательство
	- $\Delta F = F(x + \Delta x) - F(x)$
	- Надо доказать, что $\lim{\Delta x}{0} \dfrac{\Delta F}{\Delta x} = f(x)$ то есть $\forall \eps > 0 \ \exists \delta > 0: \forall \ |\Delta x| < \delta \ \implies \left|\dfrac{\Delta F}{\Delta x} - f(x)\right| < \eps$
	- $F(x) = \displaystyle\int\limits_{C}^{x} f(t) dt$
	- $F(x + \Delta x) = \displaystyle\int\limits_{C}^{x + \Delta x} f(t) dt$
	- $F(x + \Delta x) - F(x) = \displaystyle\int\limits_{C}^{x + \Delta x} f(t) dt - \displaystyle\int\limits_{C}^{x} f(t) dt = \displaystyle\int\limits_{C}^{x} f(t) dt + \displaystyle\int\limits_{x}^{x + \Delta x} f(t) dt - \displaystyle\int\limits_{C}^{x} f(t) dt = f(\xi) \Delta x$
- Если в предыдущей теореме $f(x)$ как непрерывную функцию заменить на требование только лишь интегрируемости, то можно доказать, что $F(x)$ будет непрерывной функцией на $\left[a;b\right]$
- Действительно: $F(x + \Delta x) - F(x) = \Delta F = \displaystyle\int\limits_{x}^{x + \Delta x} f(t) dt = \mu \Delta x$
### Формула Ньютона - Лейбница
- Возьмем в качестве $C$ точку $a$, тогда $F(x) = \displaystyle\int\limits_{a}^{x} f(t) dt \implies F(a) = \displaystyle\int\limits_{a}^{a} f(t) dt = 0 \implies F(x) = \displaystyle\int\limits_{a}^{x} f(t) dt + F(a)$.
- $F(b) = \displaystyle\int\limits_{a}^{b} f(t) dt + F(a)$  $\implies \displaystyle\int\limits_{a}^{b} f(x) dx = F(b) - F(a)$

***Пример***

- $\displaystyle\int\limits_{0}^{\pi} \sin{x} dx = - \cos{\pi} + \cos{0} = 1 + 1 = 2$
- Обычно найдя первообразную пишут: $\displaystyle\int\limits_{a}^{b} f(x) dx = F(x)\bigg|^{b}_{a} = F(b) - F(a)$

### Теорема о замене переменной в определенном интеграле

- Пусть на $\left[a;b\right]$ задана непрерывная $f(x)$ имеющая на этом промежутке $F(x)$, так что $\displaystyle\int\limits_{a}^{b} f(x) dx = F(b) - F(a)$. Пусть далее отрезок $\left[\alpha; \beta\right]$ будет областью определения дифференцируемой на нем функции $x = \phi(t). \ t \in \left[\alpha; \beta\right], \ \left[a ; b\right]$ - область значений этой функции, причем $\phi(\alpha) = a, \ \phi(\beta) = b \implies F(x)$ - первообразная для $f(\phi(t))\phi'(t), \ \displaystyle\int\limits_{a}^{b} f(x) dx = F(\phi(\beta)) - F(\phi(\alpha))$
- Доказательство :
	- $\dfrac{d}{dt} \left[F(\phi(t))\right] = F'(\phi(t))\phi'(t) = f(\phi(t))\phi'(t) \implies \displaystyle\int\limits_{\phi(\alpha)}^{\phi(\beta)} f(\phi(t))\phi'(t) dt  =\displaystyle\int\limits_{a}^{b} f(x) dx = F(\phi(t))\bigg|^{\phi(\beta)}_{\phi(\alpha)} = F(\phi(\beta)) - F(\phi(\alpha)) = F(b) - F(a)$

***Пример***

- $\displaystyle\int\limits_{1}^{2} \dfrac{\ln{x}}{x} dx\bigg|^{x = e^{t}}_{dx = e^{t} dt} = \displaystyle\int\limits_{0}^{\ln{2}} tdt  = \dfrac{t^{2}}{2}\bigg|^{\ln{2}}_{0}$

### Метод интегрирования по частям в определенном интеграле
- Теорема: Пусть на $\left[a; b\right]$ заданы дифференцируемые функции $u(x), \ v(x)$, причем существует интеграл $\displaystyle\int\limits_{a}^{b} v(x) du(x).$ $\exists \ \displaystyle\int\limits_{a}^{b} u(x) dv(x) = u(x)v(x)\bigg|^{b}_{a} - \displaystyle\int\limits_{a}^{b} v(x) du(x)$ 
	- Доказательство: $d\left[u(x) v(x)\right] = u(x)dv(x) + v(x)du(x)$
	- $\displaystyle\int\limits_{a}^{b} d\left[u(x) v(x)\right] = \displaystyle\int\limits_{a}^{b} u(x)dv(x) + \displaystyle\int\limits_{a}^{b} v(x)du(x)$
	- $u(x) v(x)\bigg|^{b}_{a} = \displaystyle\int\limits_{a}^{b} u(x)dv(x) + \displaystyle\int\limits_{a}^{b} v(x)du(x) \implies \displaystyle\int\limits_{a}^{b} u(x)dv(x) = u(x)v(x)\bigg|^{b}_{a} - \displaystyle\int\limits_{a}^{b} v(x)du(x)$. Эти интегралы существуют по условию теоремы.

***Пример*** 
- $\displaystyle\int\limits_{1}^{2} \ln{x}dx$.
	-  $\ln{x} = u(x), \ du = \dfrac{dx}{x}$
	- $\displaystyle\int\limits_{1}^{2} \ln{x}dx = x \ln{x}\bigg|^{2}_{1} - \displaystyle\int\limits_{1}^{2} x\dfrac{1}{x}dx = x\ln{x}\bigg|^{2}_{1} - \displaystyle\int\limits_{1}^{2} dx = x\ln{x}\bigg|^{2}_{1} - x\bigg|^{2}_{1}$
- $\displaystyle\int\limits_{0}^{1} x\arctan{x}dx$
	- Положим $\arctan{x} = u(x)$
	- $\dfrac{1}{2}\displaystyle\int\limits_{0}^{1} \arctan{x}dx^{2} = \dfrac{1}{2}x^{2}\arctan{x}\bigg|^{1}_{0} - \dfrac{1}{2}\displaystyle\int\limits_{0}^{1}  \dfrac{x^{2}}{1 + x^{2}}dx = \dfrac{\pi}{8} - \dfrac{1}{2}\displaystyle\int\limits_{0}^{1} \dfrac{x^{2}}{1 + x^{2}}dx = \dfrac{\pi}{8} - \dfrac{1}{2}\left(x - \arctan{x}\right)\bigg|^{1}_{0} = \dfrac{\pi}{8} - \dfrac{1}{2}\left(1 - \dfrac{\pi}{4}\right)$

### Применения определенного интеграла 
- Вычисление площади плоской фигуры
	- Геометрический смысл определенного интеграла : площадь криволинейной трапеции $\left(f(x) \geq 0\right)$. $\displaystyle\int\limits^{b}_{a} f(x) dx = S$. Найдем площадь плоской фигуры, ограниченной замкнутой линией, такой что любая прямая, параллельная оси $Oy$ и пересекающая эту фигуру пересекает ее только два раза: при входе через нижнюю границу $y = \phi(x)$ и при выходе через внешнюю границу $y = \psi(x)$. Крайняя левая точка имеет координату $a$, а крайняя правая $b$. Причем: $\phi(x), \ \psi(x)$ интегрируемы на $\left[a; b\right]$. Рассмотрим $\displaystyle\int\limits^{b}_{a} \psi(x) dx = S_{1}$ (площадь криволинейной трапеции, расположенной под кривой $y = \psi(x)$. Площадь под кривой $\phi(x): S_{2} =\displaystyle\int\limits^{b}_{a} \phi(x) dx  \implies S = S_{1} - S_{2}$. Если условие пересечения фигуры прямой, параллельной оси $Oy$ не выполняется, то площадь бывает возможным вычислить разбив фигуру на части для которых это условие выполняется.

***Пример***
- Найти площадь кольца: 
	- В силу симметрии фигуры достаточно найти площадь ее четвертой части в первой четверти.
	- Уравнения внутренней окружности: $x^{2} + y^{2} = r^{2}, \ x^{2} + y^{2} = R^{2}$. В первой четверти $y > 0, \ x > 0 \implies y_{1} = \sqrt{R^{2} - x^{2}} \ y_{2} = \sqrt{r^{2} - x^{2}}$. 
	- $S = \left(\displaystyle\int\limits_{0}^{R} \left(\sqrt{R^{2} - x^{2}} \right)dx - \displaystyle\int\limits_{0}^{r} \left(\sqrt{r^{2} - x^{2}} \right)dx\right)\bigg|^{x = R\cos{\phi}}_{dx = - R\sin{\phi}d\phi} = \\ - \displaystyle\int\limits_{0}^{\dfrac{\pi}{2}} \left(R^{2}\sin^{2}{\phi} \right)d\phi + \displaystyle\int\limits_{0}^{\dfrac{\pi}{2}} \left(r^{2}\sin^{2}{\psi} \right)d\psi = R^{2} \displaystyle\int\limits_{0}^{\dfrac{\pi}{2}} \sin^{2}{\phi}d\phi - r^{2}\displaystyle\int\limits_{0}^{\dfrac{\pi}{2}} \sin^{2}{\psi} d\psi = \dfrac{\pi}{4}\left(R^{2} - r^{2}\right)$

## Лекция 01.03.2023
### Вычисление длины кривой
- Дана кривая на отрезке $\left[a;b\right]$ . Разобъем кривую на отрезки, устремим число точек деления к бесконечности. $\Delta = \max{(\Delta l_{i})}$ - характеристика разбиения. $\Delta \rightarrow 0$. Если длина ломаной при стремлении $n \rightarrow \inf$ имеет предел, то кривая называется спрямляемой, а этот предел называется длиной кривой. Рассмотрим длину ломаной 
	- $\Delta l_{1} + \Delta l_{2} + \dots + \Delta l_{n} = \sqrt{\Delta l_{1}^{2} + \Delta l_{2}^{2}  + \dots + \Delta l_{n}^{2} }$.
- Пусть кривая задана параметрически: $x = \phi(t), \ y = \psi(t),\alpha \leq t \leq \beta \  \implies \Delta y = \phi'(t)\Delta t, \ \Delta x = \psi'(t)\Delta t$
	- $\Delta l_{1} + \Delta l_{2} + \dots + \Delta l_{n}  = \displaystyle\sum\limits_{i = 1}^{n} \sqrt{\Delta x_{i}^{2} + \Delta y_{i}^{2}} = \displaystyle\sum\limits_{i = 1}^{n} \sqrt{\left(\Delta \phi(t)_{i}\right)^{2} + \left(\Delta \psi(t)_{i}\right)^{2}} = \lim{n}{\inf} \sum\limits_{i = 1}^{n} \sqrt{\left(\phi_{i}'(t)\right)^{2} + \left(\psi_{i}'(t)\right)^{2}} = \displaystyle\int\limits_{a}^{b} \left[\sqrt{\left(\phi'(t)\right)^{2} + \left(\psi'(t)\right)^{2}}\right] dt$
- Если кривая задана в явном виде $y = f(x)$,  $ \implies \ell = \displaystyle\int\limits_{a}^{b} \sqrt{1 + y'(x)^{2}}dx$
- Если кривая задана в полярных координатах: $\phi \in \left[\alpha; \beta\right]$ $x =\rho(\phi)\cos{\phi}, \ y = \rho(\phi)\sin{\phi}$ $ \implies \Delta x^{2} + \Delta y^{2} = \Delta \ell^{2}$
	- $\dfrac{d x}{d \phi} = \dfrac{d \rho}{d \phi}\cos{\phi} - \rho(\phi)\sin{\phi}$
	- $\dfrac{d y}{d \phi} = \dfrac{d \rho}{d \phi}\sin{\phi} + \rho(\phi)\cos{\phi}$
	- $dx = \left(d\rho \cos{\phi} - \rho(\phi)\sin{\phi}\right)d\phi$
	- $dy = \left(d\rho \sin{\phi} + \rho(\phi)\cos{\phi}\right)d\phi$
	- $dx^{2} + dy^{2} = \left(\left(d\rho \cos{\phi} - \rho\sin{\phi}\right)d\phi\right)^{2} + \left(\left(d\rho \sin{\phi} + \cos{\phi}\right)d\phi\right)^{2} = \left(d\rho^{2} + \rho^{2}\right)d\phi^{2}$
	- $\ell = \displaystyle \int\limits_{\alpha}^{\beta} \sqrt{d\rho^{2} + \rho^{2}}d\phi$

### Вычисление объемов и поверхности тел
- Рассмотрим тела, ограниченные такой поверхностью, что любая прямая, параллельная оси $Oz$, один раз входит и один раз выходит в поверхность. Пусть при любом $z$ известна площадь сечения этого тела плоскостью, параллельной плоскости $Oxy$ $\Delta z_{i}$ - расстояние между этими сечениями. Тогда разбиваем тело сечениями и составляем интегральную сумму: $\sigma = \displaystyle\sum\limits_{i=1}^{n} S(z_{i})\Delta z_{i} \implies $  $\lim{n}{\inf} \sigma = V = \displaystyle\int S(z) dz$. 
- Вычисление объема тела вращения
	- Вращаем криволинейною трапецию вокруг оси $X$, это и называется телом вращения. Делаем разбиение отрезка $[a;b]$ точками $x_{1}, x_{2}. \dots, x_{n}$. Составляем интегральную сумму $\sigma = \displaystyle\sum\limits_{i=1}^{n} f(\xi_{i})^{2} \pi\ \Delta x_{i} \implies \lim{n}{\inf} \sigma = V = \pi \displaystyle\int\limits_{a}^{b} f(x)^{2} dx $
- Вычисление поверхности тела вращения
	- $2\pi r \ell \leq S \leq 2\pi R \ell $
	- $\Delta S_{i} = 2\pi \dfrac{f(x_{i + 1}) - f(x_{i})}{2} \Delta l_{i}$
	- $\lim{n}{\inf} \sigma = \lim{n}{\inf} \displaystyle\sum\limits_{i = 1}^{n} \Delta S_{i} \implies 2 \pi \displaystyle\int_{a}^{b} f(x) \sqrt{1 + y'(x)^{2}}dx$

### Несобственные интегралы первого рода 
- Пусть $f(x)$ задана на бесконечном промежутке $\left[a;+ \inf\right]$, где она ограничена и интегрируема на каждом конечном промежутке по Риману. Тогда $\lim{A}{\inf} \displaystyle\int\limits_{a}^{A} f(x) dx$. Если предел существует, то существует $\displaystyle\int\limits_{a}^{\inf} f(x) dx$ .

### Несобственные интегралы второго рода 
- Пусть $f(x)$ задана на $(a;b), x \rightarrow b-0 \implies \ f(x) \rightarrow \pm \inf$
	- $\forall \eps > 0 \ \exists \delta > 0, \ \bigg|\displaystyle\int\limits_{a}^{b - \delta} f(x) dx\bigg| < \eps \implies \exists\lim{\delta}{0} \int\limits_{a}^{b - \delta} dx$. Аналогично определяется интеграл второго рода, если $f(x)$ обращается в $\inf$ вблизи правого конца или в какой - то внутренней точке. $\implies \displaystyle\int\limits_{a}^{b} = \lim{\delta_{1}, \delta_{2}}{0}\left[\displaystyle\int\limits_{a}^{c - \delta_{1}} + \displaystyle\int\limits_{c + \delta_{2}}^{b}\right]$.

***Пример***
- $y = f(x) = e^{-x}$
	- $\lim{A}{+\inf} \int\limits_{0}^{A} = \lim{A}{+\inf}[-e^{x}]\bigg|^{A}_{0} = \lim{\Delta }{+\inf}[-e^{-A} + 1] = 1$
- Аналогично рассматриваются  $\displaystyle\int\limits_{-\inf}^{a} f(x) dx$, $\displaystyle\int\limits_{-\inf}^{+\inf} f(x) dx = \lim{A, B}{\inf} \displaystyle\int\limits_{-A}^{B} f(x) dx$

### Критерий Коши сходимости несобственного интеграла
- $\displaystyle\int\limits_{a}^{+\inf} f(x) dx$ Сходится тогда и только тогда, когда $\forall E > 0 \ \forall \eps > 0  \ \exists E_{1}, E_{2} > E:  \displaystyle\int\limits_{E_{1}}^{E_{2}} f(x) dx < \eps $

### Признак сравнения несобственных интегралов
- Если $f(x)$ на $[a;+\inf)$ удовлетворяет условию $f(x) \leq g(x)$
	- $\displaystyle\int\limits_{a}^{+\inf} f(x) dx$ сходится $ \implies$  $\displaystyle\int\limits_{a}^{+\inf} g(x) dx$ сходится
	- $\displaystyle\int\limits_{a}^{+\inf} f(x) dx$ расходится$\implies \displaystyle\int\limits_{a}^{+\inf} g(x) dx$ расходится 

***Пример***

- $f(x) = \dfrac{1}{x^{n}}, \ \displaystyle\int\limits_{a}^{+\inf} \dfrac{dx}{x^{n}} = \lim{A}{+\inf} \displaystyle\int\limits_{a}^{A} \dfrac{dx}{x^{n}} = \lim{A}{+\inf} \dfrac{x^{-n + 1}}{-n + 1}\bigg|^{A}_{a} $. Сходится при $n > 1$. При $n=1 \implies \displaystyle\int\limits_{a}^{+\inf} \dfrac{dx}{x} = \ln{x}\bigg|^{+\inf}_{a}$. При $n <  1$ расходится.
	- Для несобственного интеграла второго рода ситуация обратная $\displaystyle\int\limits_{a}^{b} f(x) dx = \int\limits_{a}^{0} + \int\limits_{0}^{b}$
	- $\displaystyle\int\limits_{a}^{0} \dfrac{dx}{x^{n}} $. При $n \geq 1$ расходится, при $n < 1$ сходится.

### Признак Дирихле
- $\displaystyle\int\limits_{a}^{+\inf} g(x)f(x)dx $ Сходится, если $g(x)$ монотонно убывает, а $f(x)$ имеет ограниченную первообразную.

## Лекция 15.03.2023
### Числовые ряды 
- Составим бесконечную сумму чисел $a_{1} + a_{2} + \dots + a_{n}$. На основе элементов этой суммы составим частичные суммы: $S_{1} = a_{1}, \ S_{2} = a_{1} + a_{2}, \ S_{3} = a_{1} + a_{2} + a_{3}, \dots , S_{n} = a_{1} + a_{2} + \dots + a_{n}. \ S =  \lim{n}{\inf} S_{n}$. Если этот предел существует, он называется суммой бесконечного ряда.

***Обозначение***
- $\displaystyle\sum_\limits{n=1}^{\inf} a_{n} = S$. Если этот предел существует, то ряд называется сходящимся, иначе расходящимся.

### Критерий Коши сходимости числового ряда
- $\{S_{n}\}$ сходится тогда и только тогда, когда $\forall \eps > 0 \ \exists N_{\eps} \ : \forall n > N_{\eps} \ \forall p \in \NN \implies \left|S_{n + p} - S_{n}\right| < \eps$

***Пример***
- Гармонический ряд: $\displaystyle\sum\limits_{n=1}^{\inf}\dfrac{1}{n}$ (Расходится)

### Признаки сходимости рядов с положительными членами 
- Если имеются два ряда с положительными членами $\rho_{k}, \rho_{k}'$. $\lim{k}{\inf}\dfrac{\rho_{k}}{\rho_{k}'} = C \neq 0 \implies$ оба ряда сходятся и расходятся одновременно.
- $\forall k:$ $\rho_{k} \leq \rho_{k}':$  $\displaystyle\sum\limits_{k=1}^{\inf} \rho_{k}'$ сходится $\implies$ $\displaystyle\sum\limits_{k=1}^{\inf} \rho_{k}$ сходится .  $\displaystyle\sum\limits_{k=1}^{\inf} \rho_{k}$ расходится $\implies$  $\displaystyle\sum\limits_{k=1}^{\inf} \rho_{k}'$ расходится.

### Признак Даламбера 
- $\exists N \in \NN : \forall n > N:$ $\dfrac{p_{n+1}}{p_{n}} = |q| < 1 \implies \displaystyle\sum\limits_{n=1}^{\inf} p_{n}$ сходится. $\dfrac{p_{n+1}}{p_{n}} = |q| > 1 \implies \displaystyle\sum\limits_{n=1}^{\inf} p_{n}$ расходится 
- Доказательство (на основе геометрической прогрессии):
	- $\dfrac{p_{k + 1}}{p_{k}} = |q| < 1$
	- $p_{k + n} = q^{n} p_{k}$
	- Получим последовательность, зависящую от номера $n$ и имеет вид геометрической прогрессии со знаменателем $|q| < 1$. Это сходящаяся последовательность.
- Доказательство (на основе предельной формы):
	- $\lim{n}{\inf} \dfrac{p_{n + 1}}{p_{n}} = q \implies $$\forall \eps > 0 \ \exists N_{\eps} : \forall n > N_{\eps} \implies \bigg|\dfrac{p_{n+ 1}}{p_{n}} - q\bigg| < \eps$.
	- $\lim{n}{\inf}\dfrac{p_{n + 1}}{p_{n}} = q > 1 \implies $ ряд расходится
	- $\bigg|\dfrac{p_{n + 1}}{p_{n}} - q\bigg| < \eps$
	- $q - \eps < \dfrac{p_{n + 1}}{p_{n}} < q + \eps$
	- $q = 1 + \alpha \implies q = 1 + \alpha > q - \eps \implies $ Ряд расходится.

***Пример***
- Рассмотрим ряд $\displaystyle\sum\limits_{n=1}^{\inf} \dfrac{1}{n^{\alpha}}$. Доказана расходимость гармонического ряда, $\sum\limits_{n=1}^{\inf} \dfrac{1}{n^{\alpha}} \left(\alpha = 1\right)$ 
	- $\alpha < 1: \dfrac{1}{n^{\alpha}} >  \dfrac{1}{n}$ (Ряд расходится)

### Радикальный признак Коши сходимости положительных рядов
- Ряд с положительными членами $\displaystyle\sum\limits_{n=1}^{\inf} p_{n}$ сходится $\implies \forall N \in \NN \ \exists n > N:$ $\sqrt[n]{p_{n}}  < 1$. Если $\sqrt[n]{p_{n}} > 1$ ряд расходится.
- Доказательство: 
	- $ \sqrt[n]{p_{n}} \leq q$
	- $p_{n} \leq q^{n}, \ p_{n + 1} \leq q^{n + 1}p_{n}$
- Верна и предельная форма: $\lim{n}{\inf}\sqrt[n]{p_{n}} = q < 1 \implies \displaystyle\sum\limits_{n=1}^{\inf} p_{n}$ Сходится.

### Знакопеременные ряды
- $\forall n$ встречаются как положительные, так и отрицательные члены.

### Знакочередующиеся ряды
- $p_{1} - p_{2} + p_{3} - p_{4} + \dots + \left(-1\right)^{n + 1}p_{n} + \dots = \displaystyle\sum\limits_{n=1}^{\inf}(-1)^{n + 1}p_{n}$, $p_{i} > 0$

### Признак Лейбница сходимости знакочередующегося ряда
- Знакочередующийся ряд, в котором $|p_{n}|$ $\rightarrow 0$.
- Доказательство: 
  - $S_{2n + 1} = S_{2n - 1} - (a_{2n} - a_{2n + 1}) \implies$ Убывает
  - $S_{2n} + (a_{2n - 1} - a_{2n}) = S_{2n + 2} \implies$ Возрастает.
  - $S_{2n} = p_{1} - \left(p_{2} - p_{3}\right) - \left(p_{4} - p_{5}\right) - \dots - \left(p_{2n - 1} - p_{2n}\right) \implies$ $S_{2n} < p_{1}$ 
  - $S_{2n + 1} = \left(p_{1} - p_{2}\right) + \left(p_{3} - p_{4}\right) + \dots + \left(p_{2n} - p_{2n + 1}\right) \implies S_{2n + 1} > 0$
  - $S_{2n + 1} - S_{2n} = a_{2n + 1} \rightarrow 0 \implies \lim{n}{\inf} S_{2n} = \lim{n}{\inf}S_{2n + 1} = 0 \implies$ $S$ сходится.


***Пример*** 
- $\displaystyle\sum\limits_{n=1}^{\inf} \dfrac{(-1)^{n - 1}}{n}$ ряд Лейбница.

### Интегральный признак сходимости рядов с положительными членами
- Рассмотрим $f(x)$,$ \ x \in \left[1; +\inf\right)$, $f(x)$ $\downarrow$ 
- $\displaystyle\sum\limits_{x=1}^{\inf}f(x)$, $\displaystyle\int\limits_{1}^{\inf} f(x) dx$ сходятся и расходятся одновременно.
- Доказательство:
  -  $k \leq x \leq k + 1$
  - $f(k) \geq f(x) \geq f(k + 1)$
  - $\displaystyle\int\limits_{k}^{k + 1} f(k) dx \geq \displaystyle\int\limits_{k}^{k + 1} f(x) dx \geq \displaystyle\int\limits_{k}^{k + 1}f(k + 1) dx$
  - $\displaystyle\sum\limits_{x=1}^{k} f(x) \leq \displaystyle\int\limits_{1}^{k + 1}f(x) dx \leq \displaystyle\sum\limits_{x =1}^{k + 1} f(x) $
  - $k \rightarrow +\inf \implies$ из сходимости и расходимости $\displaystyle\int\limits_{1}^{\inf} f(x) dx$ следует сходимость и расходимость $\displaystyle\sum\limits_{x=1}^{\inf}f(x)$

## Лекция 22.03.2023
### Определение функционального ряда
- Пусть имеется бесконечный набор функций $\{u_{1}(x), u_{2}(x), \dots, u_{n}(x), \dots\}$ заданных на некотором промежутке. Составим формальную сумму бесконечного количества слагаемых: $\displaystyle\sum_{n=1}^{\inf} u_{n}(x)$
- Частичная сумма ряда $S_{n}(x) = \displaystyle\sum_{k=1}^{n} u_{k}(x)$
- Суммой ряда в конкретной точке $x_{0}$ называется $\lim{x}{x_{0}} S_{n}(x)$
- Сходимость для каждой точки $x \in X$ называется поточечной сходимостью

### Равномерная сходимость ряда
- Функциональный ряд сходится равномерно, если: $\forall \eps > 0 \ \exists N(\eps) \in \NN \ \forall n > N(\eps) \ \forall x \in X:|S_{n}(x) - S(x)| < \eps$. 

### Критерий Коши равномерной сходимости функционального ряда
- Функциональный ряд сходится равномерно тогда и только тогда, когда: $\forall \eps > 0 \ \exists N(\eps) \in \NN \ \forall n > N(\eps) \ \forall x \in X: \bigg|S_{n + p}(x) - S_{n}(x)\bigg| < \eps$

### Первая Теорема Вейерштрасса о свойствах сумм равномерно сходящихся рядов
- Если ряд из непрерывных на некотором отрезке функций $u_{n}(x)$ сходится на этом отрезке равномерно, то он сходится непрерывно на  этом отрезке.
  -  $\eps' = \dfrac{\eps}{3} \implies \forall \eps' > 0 \ \exists \delta(\eps) > 0 \ \forall x \in X: \bigg|x - x_{0}\bigg| < \delta  \implies \ \bigg|S_{n}(x) - S_{n}(x_{0})\bigg| < \eps' $
  - $\bigg|S_{n}(x) - S_{n}(x_{0})\bigg| = \bigg|S_{n}(x) - S_{n + p}(x) + S_{n + p}(x) - S_{n + p}(x_{0}) + S_{n + p}(x_{0}) - S_{n}(x_{0})\bigg| \leq \\ \leq \bigg|S_{n}(x) - S_{n + p}(x)\bigg| + \bigg|S_{n+p}(x) - S_{n+p}(x_{0})\bigg| + \bigg|S_{n + p}(x_{0}) - S_{n}(x_{0})\bigg| < \eps$

### Вторая Теорема Вейерштрасса о свойствах сумм равномерно сходящихся рядов
- Ряд из непрерывных функций, сходящийся равномерно можно интегрировать почленно:
  - $\displaystyle\int\limits_{a}^{b} \sum\limits_{n=1}^{n} u_{n}(x)dx = \sum\limits_{n=1}^{n} \displaystyle\int_{a}^{b} u_{n}(x)dx$ 


### Третья Теорема Вейерштрасса о свойствах сумм равномерно сходящихся рядов
- Если ряд из дифференцируемых функций сходится на некотором промежутке, а ряд из производных этих функций сходится на этом промежутке равномерно, то исходный ряд можно дифференцировать почленно:
- $\left(\displaystyle\sum\limits_{n=1}^{n}u_{n}(x)\right)' = \displaystyle\sum\limits_{n=1}^{n}u_{n}'(x)$

### Определение степенного ряда 
- Степенным рядом называется функциональный ряд $\displaystyle\sum\limits_{n=1}^{\inf} C_{n}(x - x_{0})^{n}$ 
### Теорема Абеля
- Если $\displaystyle\sum\limits_{n=1}^{\inf} C_{n} (x - x_{0})^{n}$ сходится в некоторой точке $x'$, то он сходится абсолютно  $\forall x: |x| < |x'|$
  - Пусть ряд сходится при $x = x'$. Тогда это числовой ряд, а его частичными суммами являются числовые последовательности $\implies \exists M: |S_{n}| \leq M$ 
  - Перейдем к ряду с переменными $|x| < |x'|: \bigg|\displaystyle\sum\limits_{n=1}^{\inf} C_{n}(x - x_{0})^{n}\bigg| \leq M$

### Абсолютная сходимость ряда
- Ряд сходится абсолютно, если сходится ряд $\displaystyle\sum\limits^{\inf}_{n=1} \big|u_{k}\big|$

### Степенной ряд Тейлора
- Из Теорем Вейерштрасса следует, что степенной ряд можно дифференцировать почленно и притом неограниченное число раз. Значит, он сходится к некоторой дифференцируемой $n$ раз функции. А значит справедлива формула Тейлора: $f(x) = f(x_{0}) + \dfrac{f'(x_{0})}{1!}(x - x_{0}) + \dots  + R_{n + 1}; \ R_{n + 1} \rightarrow 0 \implies f(x) = \displaystyle\sum\limits^{\inf}_{n=1} \dfrac{f^{(n)}(x_{0})}{n!}(x - x_{0})^{n}$

### Нахождение радиуса сходимости степенного ряда по формуле Даламбера

- $R \ = \ \lim{n}{\inf}\bigg|\dfrac{C_{n}}{C_{n + 1}}\bigg|$

### Нахождение радиуса сходимости степенного ряда по формуле Коши - Адамара

- $R  \ = \ \lim{n}{\inf} \dfrac{1}{\sqrt[n]{\big|C_{n}\big|}}$

 

