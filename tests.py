import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def run_examples():
    """Run the manual examples and print formatted output."""

    test_cases = [
      ### get_files_info
        #(".", "current directory"),
        #("pkg", "'pkg' directory"),
        #("/bin", "'/bin' directory"),
        #("../", "'../' directory"),

      ### get_file_content
        #("lorem.txt", "'lorem.txt' file"),

        #("main.py", "'main.py' file"),
        #("pkg/calculator.py", "'pkg/calculator.py' file"),
        #("/bin/cat", "'/bin/cat' file"),
        #("pkg/does_not_exist.py", "'pkg/does_not_exist.py' file")

      ### write_file
        #("lorem.txt", "'lorem.txt' file", "wait, this isn't lorem ipsum"),
        #("pkg/morelorem.txt", "'pkg/morelorem.txt' file", "lorem ipsum dolor sit amet"),
        #("/tmp/temp.txt", "'/tmp/temp.txt' file", "this should not be allowed")

      ### run_python_file
        ("main.py", "'main.py' file", []),
        ("main.py", "'main.py' file", ["3 + 5"]),
        ("tests.py", "'tests.py' file", []),
        ("../main.py", "'../main.py' file", []),
        ("nonexistent.py", "'nonexistent.py' file", [])
    ]

    for directory, label, args in test_cases:
        print(f"run_python_file(\"calculator\", \"{directory}\"):", args)
        print(f"Result for {label}:")
        result = run_python_file("calculator", directory, args)
        print(result)
        print()


if __name__ == "__main__":
    run_examples()