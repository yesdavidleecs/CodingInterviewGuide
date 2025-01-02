from codingproblems import Problem, TestRunner
from codingproblems.models.test_case import TestCase
from typing import List, Callable

class TwoSum(Problem):
    def solution_function(self) -> Callable:
        def two_sum(nums: List[int], target: int) -> List[int]:
            seen = {}
            for i, num in enumerate(nums):
                complement = target - num
                if complement in seen:
                    return [seen[complement], i]
                seen[num] = i
            return []
        return two_sum

    def get_test_cases(self) -> List[TestCase]:
        return [
            TestCase(
                input_data=([2, 7, 11, 15], 9),
                expected=[0, 1],
                description="Basic case"
            ),
            TestCase(
                input_data=([3, 3], 6),
                expected=[0, 1],
                description="Same numbers"
            )
        ]