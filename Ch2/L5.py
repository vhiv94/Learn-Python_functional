def main_func(document: str):
    lines = document.split("\n")
    changed_lines = list(map(convert_line, lines))
    return "\n".join(changed_lines)


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line

run_cases = [
    (
        "* Alai\n- Dink Meeker\n",
        "* Alai\n* Dink Meeker\n",
    ),
    (
        "* Ender Wiggin\n- Petra Arkanian\n* Bean\n",
        "* Ender Wiggin\n* Petra Arkanian\n* Bean\n",
    ),
    (
        "- Fly Molo - Dragon Army\n- Carn Carby - Rabbit Army\n* Ambul - Rabbit Army\n",
        "* Fly Molo - Dragon Army\n* Carn Carby - Rabbit Army\n* Ambul - Rabbit Army\n",
    ),
]

submit_cases = run_cases + [
    (
        "- Bonzo Madrid\n- Stilson\n- The Formics\n- Peter Wiggin\n- Valentine Wiggin\n- Colonel Graff\n",
        "* Bonzo Madrid\n* Stilson\n* The Formics\n* Peter Wiggin\n* Valentine Wiggin\n* Colonel Graff\n",
    ),
]