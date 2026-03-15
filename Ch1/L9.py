def main_func(line):
    return f"{line.strip().rstrip().upper().replace('.', '')}..."
    # stripped = line.strip().rstrip()
    # capitalized = stripped.upper()
    # no_dot = capitalized.replace('.', '')
    # return f"{no_dot}..."

run_cases = [
    (
        "You can't spell America without Erica",
        "YOU CAN'T SPELL AMERICA WITHOUT ERICA...",
    ),
    ("Friends don't lie.", "FRIENDS DON'T LIE..."),
    (" She's our friend and she's crazy!", "SHE'S OUR FRIEND AND SHE'S CRAZY!..."),
]

submit_cases = run_cases + [
    (" You're gonna slay 'em dead, Nance. ", "YOU'RE GONNA SLAY 'EM DEAD, NANCE..."),
]