import argparse
from codingproblems import TestRunner
from codingproblems.problems import register_problem, get_problem, PROBLEM_REGISTRY
from codingproblems.problems.two_sum import TwoSum

def main():
    print("registering problems...")
    register_problem(TwoSum)

    parser = argparse.ArgumentParser(description='Run LeetCode problem tests')
    parser.add_argument('problem', nargs='?', help='Problem name to run')
    parser.add_argument('--list', action='store_true', help='List all available problems')
    args = parser.parse_args()

    if args.list:
        print("\nAvailable problems:")
        for name in sorted(PROBLEM_REGISTRY.keys()):
            print(f"- {name}")
        return

    if not args.problem:
        print("Please specify a problem name or use --list to see available problems")
        return

    problem_class = get_problem(args.problem)
    if not problem_class:
        print(f"Problem '{args.problem}' not found")
        return

    runner = TestRunner()
    problem = problem_class()
    runner.run_tests(problem)

if __name__ == "__main__":
    main()