# Testing

This project utilizes the [pytest](https://pytest.org/) as the testing framework.

Tests are organized into test suites to group related test cases together. Each Django app typically has its own test suite. You can find test suites in the `tests` directory of each app.

Within each test suite, individual test cases are written to verify specific functionality or behavior of the code. These test cases are located in Python files within the test suite directory.

To run the tests for the project, run either

```bash
pytest
```

or

```bash
invoke test
```
