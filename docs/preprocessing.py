from itertools import chain
from pathlib import Path
import time

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


def fix_preambles(md_roots):
    prompt = "fixing preambles..."
    print(prompt, end="\r")

    preamble = get_preamble()
    glob = Path.cwd().glob

    last_size = 0
    for file in chain(*(glob(root + "/**/*.md") for root in md_roots)):
        text = file.read_text("utf-8")

        s, e = get_macros_pos(text)
        macros = text[s: e]

        if macros:
            if macros != preamble:
                print(prompt, "Updating preamble in", file, " "*last_size, end="\r")
            else:
                print(prompt, "Skipping preamble in", file, " "*last_size, end="\r")
            text = text[:s] + preamble + text[e:]
        else:
            print(prompt, "Creating preamble in", file, " "*last_size, end="\r")
            text = START + preamble + END + "\n" + text

        time.sleep(0.075)  # make it visible ;)
        file.write_text(text, "utf-8")
        last_size = len(str(file))

    print(prompt, "done", " "*(last_size+20))


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


def run_all(md_roots):
    fix_preambles(md_roots)
    generate_literature()
