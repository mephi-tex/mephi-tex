MathJax.Hub.Config({
    TeX: {
        Macros: {
            braket: ["\\langle #1 \\rangle", 1],
            wrapmat: ["\\begin{#1} #2 \\end{#1}", 2],
            mat: ["\\wrapmat{Vmatrix}{#1}", 1],
            det: ["\\wrapmat{vmatrix}{#1}", 1],
            upline: ["\\overline{#1}", 1],
            dnline: ["\\underline{#1}", 1],
        }
    }
});
