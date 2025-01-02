from abc import ABC, abstractmethod
from typing import List, Callable
from ..models.test_case import TestCase

class Problem(ABC):
    @abstractmethod
    def solution_function(self) -> Callable:
        """Return the function that solves the problem"""
        raise NotImplementedError("Each problem must implement its solution")

    @abstractmethod
    def get_test_cases(self) -> List[TestCase]:
        """Return a list of test cases for the problem"""
        raise NotImplementedError("Each problem must provide test cases")

    @property
    def name(self) -> str:
        return self.__class__.__name__