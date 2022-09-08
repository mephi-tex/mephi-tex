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
