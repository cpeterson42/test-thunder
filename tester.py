import os
import sys
import random
import importlib
import json
# from firebase_interface import update_firebase_with_result


# Usage: python3 tester.py test_name
# Add test: python3 tester.py add_test test_4
class Tester:
    def __init__(self, tests_dir="tests", expected_results_file="expected_results.json"):
        self.tests_dir = tests_dir
        self.test_files = [f for f in os.listdir(
            tests_dir) if f.endswith('.py')]

        with open(expected_results_file, 'r') as file:
            self.expected_results = json.load(file)

    def run(self, test_name):
        chosen_test = f"{test_name}.py"
        if chosen_test not in self.test_files:
            print(f"Error: Test {chosen_test} not found!")
            return

        module = importlib.import_module(
            f'{self.tests_dir}.{chosen_test[:-3]}')
        result = str(module.test_function())
        expected_result = self.expected_results.get(chosen_test[:-3])
        success = (result == expected_result)
        print(f"Success?: {success}")

        # update_firebase_with_result(success)

    def add_test(self, test_name):
        chosen_test = f"{test_name}.py"
        if chosen_test not in self.test_files:
            print("Error: Test not found!")
            return

        module = importlib.import_module(
            f'{self.tests_dir}.{chosen_test[:-3]}')
        result = module.test_function()

        self.expected_results[test_name] = str(result)
        with open("expected_results.json", 'w') as file:
            json.dump(self.expected_results, file, indent=4)


if __name__ == "__main__":
    tester = Tester()

    if len(sys.argv) > 2 and sys.argv[1] == "add_test":
        test_name = sys.argv[2]
        tester.add_test(test_name)
    else:
        test_name = sys.argv[1] if len(sys.argv) > 1 else None
        tester.run(test_name)
