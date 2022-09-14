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

## Overview

Example to demonstrate PDF.js library usage with a viewer optimized for mobile usage.

## Getting started

Build PDF.js using `gulp dist-install` and run `gulp server` to start a web server.
You can then work with the mobile viewer at
http://localhost:8888/examples/mobile-viewer/viewer.html.

Refer to `viewer.js` for the source code of the mobile viewer.
