"""
Fixes all of the files before they can be rendered
They need to be kept in that way so Obsidian will also render them properly
"""

from pathlib import Path

for file in Path.cwd().glob("docs/**/*.md"):
    text = file.read_text("utf-8")
    file.write_text(text.replace("```mermaid", "```{mermaid}"), "utf-8")
