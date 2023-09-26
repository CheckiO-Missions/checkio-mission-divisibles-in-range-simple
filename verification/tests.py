"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {"input": [10, 2], "answer": 5},
        {"input": [10, 3], "answer": 3},
        {"input": [10, 5], "answer": 2},
        {"input": [15, 4], "answer": 3},
        {"input": [20, 6], "answer": 3},
        {"input": [100, 10], "answer": 10},
        {"input": [200, 25], "answer": 8},
        {"input": [50, 7], "answer": 7},
        {"input": [60, 8], "answer": 7},
        {"input": [70, 9], "answer": 7}
    ],
    "Extra": [
        {"input": [int(1e9), 2], "answer": 5e8},
        {"input": [int(1e9), int(1e9)], "answer": 1}
    ]
}
