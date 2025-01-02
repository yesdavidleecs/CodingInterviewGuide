# test_framework/core/test_runner.py
from typing import List, Any, Optional, Callable
import time
import traceback
from dataclasses import dataclass
from ..models.test_case import TestCase
from ..core.problem import Problem
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init()

@dataclass
class TestResult:
    """Stores the result of a single test case execution"""
    passed: bool
    test_case: TestCase
    actual_output: Any
    execution_time: float
    error: Optional[str] = None
    stack_trace: Optional[str] = None

class TestRunner:
    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        
    def format_value(self, value: Any) -> str:
        """Format a value for display in test results"""
        if isinstance(value, list):
            return f"[{', '.join(map(str, value))}]"
        if isinstance(value, dict):
            return f"{{{', '.join(f'{k}: {v}' for k, v in value.items())}}}"
        return str(value)

    def run_single_test(self, 
                       solution_func: Callable, 
                       test_case: TestCase) -> TestResult:
        """Execute a single test case and return the result"""
        start_time = time.time()
        try:
            # Handle different input types (single argument vs multiple arguments)
            if isinstance(test_case.input_data, tuple):
                actual_output = solution_func(*test_case.input_data)
            else:
                actual_output = solution_func(test_case.input_data)

            execution_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            
            # Check if output matches expected
            passed = actual_output == test_case.expected
            
            return TestResult(
                passed=passed,
                test_case=test_case,
                actual_output=actual_output,
                execution_time=execution_time
            )

        except Exception as e:
            execution_time = (time.time() - start_time) * 1000
            return TestResult(
                passed=False,
                test_case=test_case,
                actual_output=None,
                execution_time=execution_time,
                error=str(e),
                stack_trace=traceback.format_exc()
            )

    def print_test_result(self, result: TestResult, test_number: int) -> None:
        """Print the result of a single test case"""
        if result.passed:
            status = f"{Fore.GREEN}PASSED{Style.RESET_ALL}"
        elif result.error:
            status = f"{Fore.RED}ERROR{Style.RESET_ALL}"
        else:
            status = f"{Fore.RED}FAILED{Style.RESET_ALL}"

        print(f"\nTest {test_number}: {status}")
        
        if self.verbose or not result.passed:
            print(f"Description: {result.test_case.description}")
            print(f"Input: {self.format_value(result.test_case.input_data)}")
            print(f"Expected: {self.format_value(result.test_case.expected)}")
            
            if result.error:
                print(f"Error: {result.error}")
                if self.verbose:
                    print("Stack trace:")
                    print(result.stack_trace)
            else:
                print(f"Actual: {self.format_value(result.actual_output)}")
            
            print(f"Execution time: {result.execution_time:.2f}ms")
            
            if result.test_case.timeout_ms and result.execution_time > result.test_case.timeout_ms:
                print(f"{Fore.YELLOW}Warning: Test exceeded timeout of {result.test_case.timeout_ms}ms{Style.RESET_ALL}")

    def run_tests(self, problem: Problem) -> bool:
        """Run all test cases for a given problem and return whether all tests passed"""
        print(f"\nRunning tests for {problem.name}:")
        print("=" * 50)
        
        solution_func = problem.solution_function()
        test_cases = problem.get_test_cases()
        
        if not test_cases:
            print(f"{Fore.YELLOW}Warning: No test cases provided{Style.RESET_ALL}")
            return True
        
        results: List[TestResult] = []
        for test_case in test_cases:
            result = self.run_single_test(solution_func, test_case)
            results.append(result)
        
        # Print individual test results
        for i, result in enumerate(results, 1):
            self.print_test_result(result, i)
        
        # Print summary
        passed_count = sum(1 for r in results if r.passed)
        total_time = sum(r.execution_time for r in results)
        avg_time = total_time / len(results)
        
        print("\nTest Summary:")
        print("=" * 50)
        print(f"Total Tests: {len(results)}")
        print(f"Passed: {passed_count}")
        print(f"Failed: {len(results) - passed_count}")
        print(f"Average Time: {avg_time:.2f}ms")
        print(f"Total Time: {total_time:.2f}ms")
        
        if passed_count == len(results):
            print(f"\n{Fore.GREEN}All tests passed!{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}Some tests failed.{Style.RESET_ALL}")
        
        return passed_count == len(results)

# Example usage:
if __name__ == "__main__":
    # Example problem for testing
    class ExampleProblem(Problem):
        def solution_function(self) -> Callable:
            def add_numbers(a: int, b: int) -> int:
                return a + b
            return add_numbers

        def get_test_cases(self) -> List[TestCase]:
            return [
                TestCase(
                    input_data=(1, 2),
                    expected=3,
                    description="Simple addition"
                ),
                TestCase(
                    input_data=(0, 0),
                    expected=0,
                    description="Add zeros"
                ),
                TestCase(
                    input_data=(-1, 1),
                    expected=0,
                    description="Add negative number"
                )
            ]

    # Run tests
    runner = TestRunner()
    problem = ExampleProblem()
    runner.run_tests(problem)