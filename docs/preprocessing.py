from pathlib import Path

MACROS = "<!-- Macros: {} -->\n"
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
    return "\n".join([f"${line}$" if line else "" for line in text[s: e].split("\n")])


def fix_preambles():
    preamble = get_preamble()

    for file in Path.cwd().glob("./!(literature)/**/*.md"):
        text = file.read_text("utf-8")

        s, e = get_macros_pos(text)
        macros = text[s: e]

        if macros:
            text = text[:s] + preamble + text[e:]
        else:
            text = START + preamble + END + "\n" + text

        file.write_text(text, "utf-8")


LITERATURE = """# {name}

Веб-просмотр:

<a href="https://github.com/0dminnimda/mephi-docs/blob/main/docs/_static/literature/{name}.pdf">Здесь</a> можно найти запасной веб-просмотр, на случай, если этот не работает <br>
Также можно <a href="../_static/literature/{name}.pdf">скачать PDF</a>

<object data="../_static/literature/{name}.pdf" type="application/pdf" width="960vw%" height="720vw%">
    <iframe src="../_static/literature/{name}.pdf" width="960vw%" height="720vw%" style="border: none;">
        У-упс, этот браузер не поддерживает встроенные PDF 😅
    </iframe>
</object>
"""


def generate_literature():
    gen_path = Path("literature")

    for file in Path.cwd().glob("./_static/literature/*.pdf"):
        gen_file = gen_path / file.with_suffix(".md").name
        gen_file.write_text(LITERATURE.format(name=file.stem), "utf-8")


def run_all():
    fix_preambles()
    generate_literature()
