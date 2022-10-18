from itertools import chain
from pathlib import Path


# if you need to change them, import it and do whatever you like with it
MD_ROOTS = ["IVT", "IVT_evening"]


def get_mds():
    roots = (Path(__file__).parent / root for root in MD_ROOTS)
    return chain(*(root.glob("**/*.md") for root in roots))


def print_over(previous_size, *args):
    output = " ".join((str(arg) for arg in args))
    print(output + " " * (previous_size - len(output)), end="\r")
    return len(output)


MACROS = "<!-- Macros: {} -->"
START = MACROS.format("start")
END = MACROS.format("end")


def get_macros_pos(string):
    s = string.find(START)
    e = string.find(END, s)

    if s != -1 and e != -1:
        return s + len(START), e
    return 0, 0


def get_preamble():
    text = Path("./preamble.sty").read_text("utf-8")
    s, e = get_macros_pos(text)
    lines = (
        f"${line}$"
        for line in text[s:e].split("\n")
        if line and not line.startswith("%")
    )
    return "\n" + "\n".join(lines) + "\n"


def fix_preambles():
    prompt = "fixing preambles..."
    size = print_over(0, prompt)

    preamble = get_preamble()
    for file in get_mds():
        text = file.read_text("utf-8")

        s, e = get_macros_pos(text)
        macros = text[s:e]

        if macros:
            if macros != preamble:
                size = print_over(size, prompt, "Updating preamble in", file)
            else:
                size = print_over(size, prompt, "Skipping preamble in", file)
            text = text[:s] + preamble + text[e:]
        else:
            size = print_over(size, prompt, "Creating preamble in", file)
            text = START + preamble + END + "\n" + text

        file.write_text(text, "utf-8")

    print_over(size, prompt, "done")
    print()


def fix_line_endings():
    IGNORE_START = "<!-- start-ignore: fix_line_endings -->"
    IGNORE_END = "<!-- end-ignore: fix_line_endings -->"

    prompt = "fixing line endings..."
    size = print_over(0, prompt)

    for file in get_mds():
        size = print_over(size, prompt, file)
        text = file.read_text("utf-8")

        result = ""
        ignores = False
        for line in text.split("\n"):
            if line == IGNORE_START:
                ignores = True
            elif line == IGNORE_END:
                ignores = False
            elif not ignores and line:
                if not line.endswith("  "):
                    line += "  "
            result += line + "\n"
        result = result[:-1]

        file.write_text(result, "utf-8")

    print_over(size, prompt, "done")
    print()


USUAL_MAP = {
    "<=": r"\leq ",
    ">=": r"\geq ",
    "-->": chr(0),
    "<->": r"\leftrightarrow ",
    "->": r"\rightarrow ",
    "<-": r"\leftarrow ",
    "<=>": r"\ident ",
    chr(0): "-->",
}


def fix_usual_repr():
    prompt = "fixing usual representations..."
    size = print_over(0, prompt)

    for file in get_mds():
        size = print_over(size, prompt, file)
        text = file.read_text("utf-8")

        for pattern, repl in USUAL_MAP.items():
            if pattern.startswith("\\"):  # latex command
                text = text.replace(pattern + " ", repl)
            text = text.replace(pattern, repl)

        file.write_text(text, "utf-8")

    print_over(size, prompt, "done")
    print()


def remove_private_parts():
    REMOVE_START = "<!-- start-private -->"
    REMOVE_END = "<!-- end-private -->"

    prompt = "removing private parts..."
    size = print_over(0, prompt)

    for file in get_mds():
        size = print_over(size, prompt, file)
        text = file.read_text("utf-8")

        result = ""
        removes = False
        for line in text.split("\n"):
            if line == REMOVE_START:
                removes = True
            elif line == REMOVE_END:
                removes = False

            if not removes:
                result += line + "\n"
        result = result[:-1]

        file.write_text(result, "utf-8")

    print_over(size, prompt, "done")
    print()


LITERATURE = """# {name}

Веб-просмотр:

<a href="https://github.com/0dminnimda/mephi-docs/blob/main/docs/_static/literature/{name}.pdf">Здесь</a> можно найти запасной веб-просмотр, на случай, если этот не работает <br>
Также можно <a href="../_static/literature/{name}.pdf">скачать PDF</a>

object
<object data="../_static/literature/{name}.pdf" type="application/pdf" style="width:150%; height:1000px;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</object>

iframe
<iframe src="../_static/literature/{name}.pdf" style="width:150%; height:1000px; border: none;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</iframe>

gh object
<object data="https://github.com/0dminnimda/mephi-docs/blob/main/docs/_static/literature/{name}.pdf" type="application/pdf" style="width:150%; height:1000px;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</object>

gh iframe
<iframe src="https://github.com/0dminnimda/mephi-docs/blob/main/docs/_static/literature/{name}.pdf" style="width:150%; height:1000px; border: none;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</iframe>

rtd object
<object data="https://mephi-tex.rtfd.io/ru/latest/_static/literature/{name}.pdf" type="application/pdf" style="width:150%; height:1000px;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</object>

rtd iframe
<iframe src="https://mephi-tex.rtfd.io/ru/latest/_static/literature/{name}.pdf" style="width:150%; height:1000px; border: none;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</iframe>

google object
<object data="http://docs.google.com/gview?url=https://github.com/mephi-tex/mephi-tex/blob/main/docs/_static/literature/{name}.pdf?raw=true&embedded=true" type="application/pdf" style="width:150%; height:1000px;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</object>

google iframe
<iframe src="http://docs.google.com/gview?url=https://github.com/mephi-tex/mephi-tex/blob/main/docs/_static/literature/{name}.pdf?raw=true&embedded=true" style="width:150%; height:1000px;" frameborder="0">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</iframe>

google rtd object
<object data="http://docs.google.com/gview?url=https://mephi-tex.rtfd.io/ru/latest/_static/literature/{name}.pdf&embedded=true" type="application/pdf" style="width:150%; height:1000px;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</object>

google rtd iframe
<iframe src="http://docs.google.com/gview?url=https://mephi-tex.rtfd.io/ru/latest/_static/literature/{name}.pdf&embedded=true" style="width:150%; height:1000px;" frameborder="0">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</iframe>

pdfobject
<div id="example1" style="width:150%; height:1000px;" frameborder="0">hello?</div>
<script src="../_static/javascript/pdfobject.js"></script>
<script>PDFObject.embed("../_static/literature/{name}.pdf", "#example1", {{
   fallbackLink: 'У-упс, этот браузер не поддерживает встроенные PDF 😅'
}});</script>

.
<iframe src="http://docs.google.com/gview?url=https://mephi-tex.rtfd.io/ru/latest/_static/literature/{name}.pdf" style="width:150%; height:1000px;" frameborder="0">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</iframe>
"""
"""
https://github.com/afragen/embed-pdf-viewer
    <iframe src="../_static/literature/{name}.pdf" style="width:150%; height:1000px; border: none;">
        У-упс, этот браузер не поддерживает встроенные PDF 😅
    </iframe>
    <object data="../_static/literature/{name}.pdf" type="application/pdf" style="width:150%; height:1000px;">
        У-упс, этот браузер не поддерживает встроенные PDF 😅
    </object>

<iframe src="http://docs.google.com/gview?url=https://mephi-tex.rtfd.io/ru/latest/_static/literature/{name}.pdf&embedded=true" style="width:100%; height:1000px;" frameborder="0"></iframe>
"""


def generate_literature():
    gen_path = Path("literature")

    for file in Path(__file__).parent.glob("./_static/literature/*.pdf"):
        gen_file = gen_path / file.with_suffix(".md").name
        gen_file.write_text(LITERATURE.format(name=file.stem), "utf-8")


def fix_mermaid_code():
    """
    Files need to be kept in that way so Obsidian will also render them properly
    """

    for file in Path(__file__).parent.glob("**/*.md"):
        text = file.read_text("utf-8")
        file.write_text(text.replace("```mermaid", "```{mermaid}"), "utf-8")


def preprocess_locally():
    # fix_line_endings()
    fix_preambles()
    fix_usual_repr()
    # generate_literature()


def preprocess_for_server():
    remove_private_parts()
    fix_line_endings()
    fix_mermaid_code()


if __name__ == "__main__":
    preprocess_locally()
