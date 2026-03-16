def main_func(originals, backups) -> set[str]:
    return set(map(lambda s: s.upper(), originals + tuple(filter(lambda s: not s.isdigit(), backups))))
    # is_corrupt = lambda s: not s.isdigit()
    # filtered = list(filter(is_corrupt, backups))
    # capitalize = lambda s: s.upper()
    # capitalized = list(map(capitalize, list(originals) + filtered))
    # return set(capitalized)


run_cases = [
    (
        
            ("Mortgage", "Marriage Certificate", "Boot.dev Certificate"),
            ("VEHICLE TITLE", "MORTGAGE"),
        
        {"MORTGAGE", "MARRIAGE CERTIFICATE", "BOOT.DEV CERTIFICATE", "VEHICLE TITLE"},
    ),
    (
        
            ("ANNUITY", "WATER BILL"),
            ("Photo Album", "1235023451345", "Year Book"),
        
        {"ANNUITY", "WATER BILL", "PHOTO ALBUM", "YEAR BOOK"},
    ),
]

submit_cases = run_cases + [
    ((), (), set()),
    (
        
            ("RECEIPT FOR 1st AND LAST RENT", "School Loan"),
            ("SCOOTER REGISTRATION", "314159", "ENGLISH MAJOR DEGREE"),
        
        {
            "RECEIPT FOR 1ST AND LAST RENT",
            "SCHOOL LOAN",
            "SCOOTER REGISTRATION",
            "ENGLISH MAJOR DEGREE",
        },
    ),
]