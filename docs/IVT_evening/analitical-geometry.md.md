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

$\usepackage[left=10mm,right=10mm,$
$    top=10mm,bottom=20mm,bindingoffset=0cm]{geometry}$

$%%% Работа с русским языком$
$\usepackage{cmap}                   % поиск в PDF$
$\usepackage{mathtext}               % русские буквы в фомулах$
$\usepackage{indentfirst}            % Отступ первого параграфа$
$\usepackage[T2A]{fontenc}           % кодировка$
$\usepackage[utf8]{inputenc}         % кодировка исходного текста$
$\usepackage[english,russian]{babel} % локализация и переносы$

$%% Кастомизация списокв$
$\usepackage[inline]{enumitem}$

$%%% Дополнительная работа с математикой$
$\usepackage{amsmath,amsfonts,amssymb,amsthm,mathtools} % AMS$
$\usepackage{icomma} % "Умная" запятая: $0,2$ --- число, $0, 2$ --- перечисление$

$%% Номера формул$
$\mathtoolsset{showonlyrefs=true} % Показывать номера только у тех формул, на которые есть \eqref{} в тексте.$

$%% Шрифты$
$\usepackage{euscript} % Шрифт Евклид$
$\usepackage{mathrsfs} % Красивый матшрифт$
$\usepackage[bbgreekl]{mathbbol}$

$%% Табличика там где хочецца$
$\usepackage{float}$

$%% Графички функций$
$\usepackage{pgfplots}$
$\usepackage{tikz}$
$\pgfplotsset{every axis/.style={scale only axis}}$

$%% wrapfigure$
$\usepackage{wrapfig}$


$%% Эпиграф$
$\usepackage{epigraph}$

$\usepackage{fixltx2e}$

$\usepackage{graphicx}$
$\graphicspath{{img/}}$

$\usepackage{blkarray}$

$\usepackage{scalerel}$

$\renewcommand{\kbldelim}{(}$
$\renewcommand{\kbrdelim}{)}$


$%% фигуры$
$\usepackage{import}$
$\usepackage{xifthen}$
$\usepackage{pdfpages}$
$\usepackage{transparent}$


$%% Оглавление с ссылками и ссылки на разные вещи$
$\usepackage[unicode=true, colorlinks=true, linkcolor=blue, urlcolor=blue]{hyperref}$
$\usepackage{nameref}$

$%% Ссылки на пункты description$
$\makeatletter$
$\let\orgdescriptionlabel\descriptionlabel$
$\renewcommand*{\descriptionlabel}[1]{%$
$  \let\orglabel\label$
$  \let\label\@gobble$
$  \phantomsection$
$  \protected@edef\@currentlabel{#1\unskip}%$
$  \let\label\orglabel$
$  \orgdescriptionlabel{#1}%$
$}$
$\makeatother$

$%% Свои команды$
$\DeclareMathOperator{\rk}{\mathop{\mathrm{rk}}}$
$\DeclareMathOperator{\tr}{\mathop{\mathrm{tr}}}$
$\DeclareMathOperator{\pr}{\mathop{\mathrm{pr}}}$
$\DeclareMathOperator{\ort}{\mathop{\mathrm{ort}}}$
$\DeclareMathOperator{\vol}{\mathop{\mathrm{vol}}}$
$\DeclareMathOperator{\Vol}{\mathop{\mathrm{Vol}}}$
$\let\Im\undefined$
$\DeclareMathOperator{\Im}{\mathop{\mathrm{Im}}}$
$\DeclareMathOperator{\sgn}{\mathop{\mathrm{sgn}}}$
$\let\hom\undefined$
$\DeclareMathOperator{\hom}{\mathop{\mathrm{Hom}}}$
$\let\L\undefined$
$\DeclareMathOperator{\L}{\mathop{\mathrm{L}}}$
$\DeclareMathOperator{\diag}{\mathop{\mathrm{diag}}}$
$\DeclareMathOperator{\spec}{\mathop{\mathrm{Spec}}}$
$\DeclareMathOperator{\vht}{\mathop{\mathrm{ht}}}$
$\DeclareMathOperator{\id}{\mathop{\mathrm{Id}}}$

$%% Черный квадрат в доказательствах$
$\renewcommand\qedsymbol{$\blacksquare$}$

$%% Красивые <= и >=$
$\renewcommand{\geq}{\geqslant}$
$\renewcommand{\leq}{\leqslant}$

$%% Более привычные греческие буквы$
$\renewcommand{\phi}{\varphi}$
$\renewcommand{\epsilon}{\varepsilon}$

$%% Перенос знаков в формулах (по Львовскому)$
$\newcommand*{\hm}[1]{#1\nobreak\discretionary{}$
${\hbox{$\mathsurround=0pt #1$}}{}}$

$\newcommand\iso{\xrightarrow{$
$    \,\smash{\raisebox{-0.65ex}{\ensuremath{\scriptstyle\sim}}}\,}}$

$\newcommand{\RomanNumeralCaps}[1]$
$    {\MakeUppercase{\romannumeral #1}}$

$\newenvironment{amatrix}[2]{%$
$    \left(\begin{array}{@{}*{#1}{c}|*{#2}{c}@{}}$
$}{%$
$    \end{array}\right)$
$}$

$%% Сокращения для обозначения множеств$
$\newcommand{\NN}{\mathbb{N}}$
$\newcommand{\ZZ}{\mathbb{Z}}$
$\newcommand{\RR}{\mathbb{R}}$
$\newcommand{\CC}{\mathbb{C}}$
$\newcommand{\FF}{\mathbb{F}}$
$\newcommand{\QQ}{\mathbb{Q}}$
$\newcommand{\EE}{\mathbb{E}}$

$%% Соси жопу, mathbbol, хочу mathbb от amsmath   $
$\DeclareSymbolFontAlphabet{\mathbbold}{bbold}$
$\DeclareSymbolFontAlphabet{\mathbb}{AMSb}$

$%% Жоские буквы для базисов$
$\newcommand\E{\mathbbold{e}}$
$\newcommand\F{\mathbbold{f}}$
$\let\G\undefined$
$\newcommand\G{\mathbbold{g}}$


$%% Изоморфизм$
$\newcommand*\MapsTo{%$
$  \xrightarrow[]{\raisebox{-0.25 em}{\smash{\ensuremath{\sim}}}}%$
$}$

$% Символ делимости (три вертикальные точки)$
$\DeclareRobustCommand{\divby}{%$
$  \mathrel{\text{\vbox{\baselineskip.65ex\lineskiplimit0pt\hbox{.}\hbox{.}\hbox{.}}}}%$
$}$

$\makeatletter$
$\newcommand*\bigcdot{\mathpalette\bigcdot@{.5}}$
$\newcommand*\bigcdot@[2]{\mathbin{\vcenter{\hbox{\scalebox{#2}{$\m@th#1\bullet$}}}}}$
$\makeatother$

$\makeatletter$
$\newcommand{\customlabel}[2]{%$
$   \protected@write \@auxout {}{\string \newlabel {#1}{{#2}{\thepage}{#2}{#1}{}} }%$
$   \hypertarget{#1}{#2}$
$}$
$\makeatother$

$%% Команда для ||w||$
$\DeclarePairedDelimiter\norm{\lVert}{\rVert}%$

$\makeatletter$
$\let\oldnorm\norm$
$\def\norm{\@ifstar{\oldnorm}{\oldnorm*}}$
$\makeatother$

$% Syntax: \colorboxed[<color model>]{<color specification>}{<math formula>}$
$\newcommand*{\colorboxed}{}$
$\def\colorboxed#1#{%$
$  \colorboxedAux{#1}%$
$}$
$\newcommand*{\colorboxedAux}[3]{%$
$  % #1: optional argument for color model$
$  % #2: color specification$
$  % #3: formula$
$  \begingroup$
$    \colorlet{cb@saved}{.}%$
$    \color#1{#2}%$
$    \boxed{%$
$      \color{cb@saved}%$
$      #3%$
$    }%$
$  \endgroup$
$}$
<!-- Macros: end -->

```{contents} Аналитическая геометрия
---
depth: 3
```

# Аналитическая геометрия

Преподаватель - Михайлов Владислав Дмитриевич

## Лекция 02.09.2022



### Векторы
$$\textit{Вектор - это направленный отрезок.}$$ 

Длина вектора $|\vec{AB}|$

Краткая запись  $|\vec{a}|$

**Факт**
Векторы коллинеарны, если они лежат на параллельных прямых или на одной прямой

**Факт**
Два вектора называются равными, если равны их длины (модули) и они коллинеарны и соноправлены

**Факт**

Если два вектора коллинеарны, то они отличаются на константу.


**Свойства**

*Сложение*

 - По правилу треугольника

 - По правилу паралелограмма

*Сложение*
- $$ \vec{a} + \vec{b} = \vec{b} + \vec{a}$$
- $$ \vec{a} + (\vec{b} + \vec{c}) = (\vec{a} + \vec{b}) + \vec{c} $$

- $$\exists \vec{0} : \vec{a} + \vec{0} = \vec{a}$$

- $$\forall \vec{v} \in \mathbb {R}^n : \exists \vec{v}^{-1} : \vec{v} + \vec{v}^{-1} = \vec{0} $$


Вектором $\lambda \vec{a}$ называется вектор, такой что : $|\lambda\vec{a}| = |\lambda||\vec{a}|$



Вектор $\lambda \vec{a}$ коллинеарен вектору $\vec{a}$ и сонаправлен, если $\lambda \geq 0$


**Свойства**
*Умножение векторов на константу*


- $$ \lambda (\vec{a} + \vec{b}) = \lambda\vec{b} + \lambda\vec{a}$$

- $$ (\lambda + \mu)\vec{a} = \lambda\vec{a} + \mu\vec{b}4$$

- $$\lambda(\mu\vec{a}) = (\lambda\mu)\vec{a}$$

### Линейная зависимость системы векторов


$\vec{v} = \alpha_{1} \vec{a}_{1} + \alpha_{2} \vec{a}_{2} + ... + \alpha_{n} \vec{a}_{n}$ - линейная комбинация

Система линейно зависима, если для линейной комбинации существует $\alpha \in {\alpha_{1}, \alpha_{2}, ... , \alpha_{n}}$ такой, что $\alpha \neq 0$


Доказательство : пусть $\alpha_{i} \neq 0$ и линейная комбинация равна нулю.


- $\alpha_{1} \vec{a}_{1} + \alpha_{2} \vec{a}_{2} + ... + \alpha_{i - 1} \vec{a}_{i - 1} + \alpha_{i} \vec{a}_{i} + ... + \alpha_{n} \vec{a}_{n} = 0$

- $\alpha_{i} \vec{a}_{i} = - \alpha_{1} \vec{a}_{1} - \alpha_{2} \vec{a}_{2} ... - \alpha_{i - 1} \vec{a}_{i - 1} ... - \alpha_{n} \vec{a}_{n}$

- т.к. $\alpha_{i} \neq 0$, то можно разделить обе части на $\alpha_{i}$

- Получим: $\vec{a}_{i} = -\dfrac{\alpha_{1}}{\alpha_{i}}\vec{a}_{1} - -\dfrac{\alpha_{2}}{\alpha_{i}}\vec{a}_{2} - ... - -\dfrac{\alpha_{i - 1}}{\alpha_{i}}\vec{a}_{i - 1} ... -\dfrac{\alpha_{n}}{\alpha_{i}}\vec{a}_{n}$

- Назовем коэффициенты при $\vec{a}_{i}$ --- $\lambda_{i}$, тогда $\vec{a}_{i} = \lambda_{1} \vec{a}_{1} + \lambda_{2} \vec{a}_{2} + ... + \lambda_{i - 1} \vec{a}_{i - 1} + ... + \lambda_{n} \vec{a}_{n}$

- Получим представление $\vec{a}_{i}$ в виде остальных векторов


### Достаточное условие линейной зависимости
**Теорема**
Если в системе векторов присутсвует нулевой вектор, то система линейно зависима.


**Факт**
Если часть векторов системы линейно зависима, то и остальные векторы линейно зависимы


**Факт**
Если система векторов не является линейно зависимой, то она линейно независима.

**Теорема**
Система линейно независима, если единственная ее линейная комбинация равна нулю.



**Следствие**


- Два вектора линейно зависимы тогда и только тогда, когда они колинеарны

- Если $\vec{a} = \lambda\vec{b}$, то векторы коллинеарны, это и есть линейная зависимость.

- $3$ вектора линейно зависимы тогда и только тогда, когда они компланарны (лежат в одной или параллельных плоскостях)

**Упражнение**

Пусть $\vec{a}, \vec{b}, \vec{c} $ - линейно зависимы. Доказать компланароность $\{\vec{a}, \vec{b}, \vec{c}\}$. Доказательство : По определению линейной зависимости $\vec{a} = \lambda \vec{b} + \gamma\vec{c}$, тогда $\vec{a}$ лежит в одной плоскости, по правилу паралелограмма. Обратно : Пусть $\vec{a}, \vec{b}, \vec{c} $ - компланарны. Доказать их линейную зависимость. Доказательство : так как векторы лежат в одной плоскости, можно представить один вектор из системы в виде суммы двух других.


**Утверждение**

Любые 4 вектора линейно зависимы в трехмерном пространстве.

Доказательство : Пусть даны произвольные 4 вектора $\vec{a}, \vec{b}, \vec{c}, \vec{d}$. Приведем к одному началу эти векторы. На любой тройке этих векторов образуем куб $ABCDA'B'C'D'$. В нем

- $\vec{AC} = \vec{AB} + \vec{BC}$
- $\vec{AC'} = \vec{AC} + \vec{AA'}$
- $\vec{AC'} = \vec{AB} + \vec{BC} + \vec{AA'}$ . Где $\vec{AB} = \alpha\vec{a}, {BC} = \beta \vec{b}, \vec{AA'} = \gamma \vec{c}$.

Получим $\vec{AC'} = D$. Вывод : $D = \alpha\vec{a} + \beta \vec{b} + \gamma \vec{b}$. Следовательно $\{\vec{D}, \vec{a}, \vec{b}, \vec{c}\}$ - линейно зависима.

**Определение**

Базисом в трехмерном пространстве называется система из трех линейно независимых (неколлинеарных) векторов. Любой вектор соответсвующего пространства может быть разложен и при том единственным образом. Коэффициенты этого разложения называются координатами вектора в этом базисе

**Упражнение**

Дано $\{\vec{a}, \vec{b}, \vec{c}\}$ - Базис. Тогда $v \in \mathbb {R}^3 : v = \alpha\vec{a} + \beta\vec{b} + \gamma\vec{c}.$ $(\alpha, \beta, \gamma)$ - коэффициенты вектора $v$ в базисе $\{\vec{a}, \vec{b}, \vec{c}\}$

**Определение**

Ортонормированный базис - базис из попарно перпендикулярных (ортогональных) векторов длины 1. Такие векторы принято называть $\vec{i}, \vec{j}, \vec{k}$.

**Следствие**

$\vec{a} = X\vec{i} + Y\vec{j} + Z\vec{k}$,\\ $X, Y, Z $ - проекции.

$X^2 + Y^2 + Z^2 = |\vec{a}|^2 \\ $

$\cos{\alpha}^2 + \cos{\beta}^2 + \cos{\gamma}^2 = 1$