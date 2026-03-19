from enum import Enum

CSVExportStatus = Enum("CSVExportStatus", "PENDING PROCESSING SUCCESS FAILURE")

def get_csv_status(status: CSVExportStatus, data: list[list[str | int]]) -> tuple[str, list[list[str]]]:
    match status:
        case CSVExportStatus.PENDING:
            return "Pending...", list(map(lambda line: list(map(lambda val: str(val), line)), data))
        case CSVExportStatus.PROCESSING:
            pass
        case CSVExportStatus.SUCCESS:
            pass
        case CSVExportStatus.FAILURE:
            pass
            return "Unkown error, retrying...", data
        case _:
            raise Exception("unkown export status")


run_cases = [
    (
        CSVExportStatus.PENDING,
        [
            ["Customer ID", "Billed", "Paid"],
            [1, 100, 100],
            [2, 400, 99],
            [3, 50, 25],
        ],
        (
            "Pending...",
            [
                ["Customer ID", "Billed", "Paid"],
                ["1", "100", "100"],
                ["2", "400", "99"],
                ["3", "50", "25"],
            ],
        ),
    ),
    (
        CSVExportStatus.PROCESSING,
        [
            ["Customer ID", "Billed", "Paid"],
            ["1", "100", "100"],
            ["2", "400", "99"],
            ["3", "50", "25"],
        ],
        (
            "Processing...",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
    (
        CSVExportStatus.SUCCESS,
        "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        (
            "Success!",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
    (
        CSVExportStatus.FAILURE,
        [
            ["Customer ID", "Billed", "Paid"],
            [1, 100, 100],
            [2, 400, 99],
            [3, 50, 25],
        ],
        (
            "Unknown error, retrying...",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
]

submit_cases = run_cases + [
    (
        CSVExportStatus.PENDING,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", 100],
            ["Moist Turtle", "Good", 200],
            ["Burning Lizard", "Very Good", 1000],
            ["Mossy Frog", "Poor", 10],
        ],
        (
            "Pending...",
            [
                ["Card Name", "Condition", "Value"],
                ["Sparky Mouse", "Fair", "100"],
                ["Moist Turtle", "Good", "200"],
                ["Burning Lizard", "Very Good", "1000"],
                ["Mossy Frog", "Poor", "10"],
            ],
        ),
    ),
    (
        CSVExportStatus.PROCESSING,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", "100"],
            ["Moist Turtle", "Good", "200"],
            ["Burning Lizard", "Very Good", "1000"],
            ["Mossy Frog", "Poor", "10"],
        ],
        (
            "Processing...",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
    ),
    (
        CSVExportStatus.SUCCESS,
        "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        (
            "Success!",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
    ),
    (
        CSVExportStatus.FAILURE,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", 100],
            ["Moist Turtle", "Good", 200],
            ["Burning Lizard", "Very Good", 1000],
            ["Mossy Frog", "Poor", 10],
        ],
        (
            "Unknown error, retrying...",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
    ),
    (1, None, ("Exception Raised:", "unknown export status")),
]


def test(status, data, expected_output):
    print("---------------------------------")
    print(f"Checking: {status}")
    print("Expected:")
    print(f"{expected_output[0]}")
    print(f"{expected_output[1]}")
    try:
        result = get_csv_status(status, data)
    except Exception as e:
        result = expected_output[0], str(e)
    print("Actual:")
    print(f"{result[0]}")
    print(f"{result[1]}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False