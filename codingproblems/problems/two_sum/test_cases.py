from typing import List
from codingproblems.models.test_case import TestCase


def get_test_cases() -> List[TestCase]:
    return [
        TestCase(
            input_data=([2, 7, 11, 15], 9),
            expected=[0, 1],
            description="Basic case with solution at beginning"
        ),
        TestCase(
            input_data=([3, 2, 4], 6),
            expected=[1, 2],
            description="Solution in middle of array"
        ),
        TestCase(
            input_data=([3, 3], 6),
            expected=[0, 1],
            description="Same numbers"
        ),
        TestCase(
            input_data=([1, 2, 3, 4], 8),
            expected=[],
            description="No solution exists"
        )
    ]