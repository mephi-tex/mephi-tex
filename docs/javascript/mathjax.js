// window.MathJax = {
//   tex: {
//     inlineMath: [["\\(", "\\)"]],
//     displayMath: [["\\[", "\\]"]],
//     processEscapes: true,
//     processEnvironments: true
//   },
//   options: {
//     ignoreHtmlClass: ".*|",
//     processHtmlClass: "arithmatex"
//   }
// };

window.MathJax = {
  tex: {
    inlineMath: [ ["\\(","\\)"] ],
    displayMath: [ ["\\[","\\]"] ],
    processEscapes: true,
    processEnvironments: true,
    Macros: {
      // braket: "{\\bf R}",
      // bold: ["{\\bf #1}",1]
      braket: ["\\langle #1 \\rangle", 1],
      wrapmat: ["\\begin{#1} #2 \\end{#1}", 2],
      mat: ["\\wrapmat{Vmatrix}{#1}", 1],
      det: ["\\wrapmat{vmatrix}{#1}", 1],
      upline: ["\\overline{#1}", 1],
      dnline: ["\\underline{#1}", 1],
    }
    // preamble: [
    //   "\\newcommand{\\braket}[1]{ \\langle #1 \\rangle }",
    //   "\\newcommand{\\wrapmat}[2]{ \\begin{#1} #2 \\end{#1} }",
    //   "\\newcommand{\\mat}[1]{\\wrapmat{Vmatrix}{#1}}",
    //   "\\newcommand{\\det}[1]{\\wrapmat{vmatrix}{#1}}",
    //   "\\newcommand{\\upline}[1]{\\overline{#1}}",
    //   "\\newcommand{\\dnline}[1]{\\underline{#1}}"
    // ]
  },
  options: {
    ignoreHtmlClass: ".*",
    processHtmlClass: "arithmatex"
  }
};

// const DEFAULT_PREAMBLE_PATH = "preamble.sty";
// let preamble = await this.app.vault.adapter.read(DEFAULT_PREAMBLE_PATH);

// if (MathJax.tex2chtml == undefined) {
//   MathJax.startup.ready = () => {
//     MathJax.startup.defaultReady();
//     MathJax.tex2chtml(preamble);
//   };
// } else {
//   MathJax.tex2chtml(preamble);
// }

// window.MathJax = {
//   options: {
//     ignoreHtmlClass: 'tex2jax_ignore',
//     processHtmlClass: 'tex2jax_process',
//     renderActions: {
//       find: [10, function (doc) {
//         for (const node of document.querySelectorAll('script[type^="math/tex"]')) {
//           const display = !!node.type.match(/; *mode=display/);
//           const math = new doc.options.MathItem(node.textContent, doc.inputJax[0], display);
//           const text = document.createTextNode('');
//           const sibling = node.previousElementSibling;
//           node.parentNode.replaceChild(text, node);
//           math.start = {node: text, delim: '', n: 0};
//           math.end = {node: text, delim: '', n: 0};
//           doc.math.push(math);
//           if (sibling && sibling.matches('.MathJax_Preview')) {
//             sibling.parentNode.removeChild(sibling);
//           }
//         }
//       }, '']
//     }
//   }
// };

document$.subscribe(() => {
  MathJax.typesetPromise()
})
