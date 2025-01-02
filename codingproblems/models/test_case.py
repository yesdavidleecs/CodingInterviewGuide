from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class TestCase:
    """Represents a single test case for a LeetCode problem"""
    input_data: Any
    expected: Any
    description: str = ""
    timeout_ms: Optional[int] = None
    
    def __str__(self) -> str:
        return (f"TestCase(description='{self.description}', "
                f"input={self.input_data}, expected={self.expected})")
