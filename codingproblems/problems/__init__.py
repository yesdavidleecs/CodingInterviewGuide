"""
Problems package initialization.
This can be empty or can provide registration of available problems.
"""
from typing import Dict, Type
from codingproblems.core.problem import Problem

#Optional: Registry of available problems
PROBLEM_REGISTRY: Dict[str, Type[Problem]] = {}

def register_problem(problem_class: Type[Problem]) -> None:
    """Register a problem class in the registry."""
    PROBLEM_REGISTRY[problem_class.__name__] = problem_class

def get_problem(name: str) -> Type[Problem]:
    """Get a problem class from the registry."""
    return PROBLEM_REGISTRY.get(name)

__all__ = ['register_problem', 'get_problem', 'PROBLEM_REGISTRY']