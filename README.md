# pytest-shabang

Example on how to run non python code as pytest tests

A friend from Intel asked a question

He want a test runner which run executables and fail based on return codes only,

He also mentioned pytest is problematic for him, since it's importing all the python files

## Setup

```bash
virtualenv .venv
source .venv/*/activate
pip install pytest
```

## Running tests

```bash
> pytest -q
.FFF..                                                      [100%]
============================ FAILURES =============================
_________________ file: tests/test_failed_bash.sh _________________
execution failed with
   returncode: 127
---------------------- Captured stderr call -----------------------
/home/fruch/Projects/pytest-shabang/tests/test_failed_bash.sh: line 3: also: command not found
_________________ file: tests/test_failed_perl.pl _________________
execution failed with
   returncode: 255
---------------------- Captured stderr call -----------------------
syntax error at /home/fruch/Projects/pytest-shabang/tests/test_failed_perl.pl line 3, near "to write"
Execution of /home/fruch/Projects/pytest-shabang/tests/test_failed_perl.pl aborted due to compilation errors.
________________ file: tests/test_failed_python.py ________________
execution failed with
   returncode: 1
---------------------- Captured stderr call -----------------------
Traceback (most recent call last):
  File "/home/fruch/Projects/pytest-shabang/tests/test_failed_python.py", line 4, in <module>
    import somthing
ModuleNotFoundError: No module named 'somthing'
3 failed, 3 passed in 0.05 seconds
```

## Adding new tests

lets say we want to add a test written in  `Ruby`

1. Drop a file that starts with `test_` into tests direcotry

1. Make sure file is executable like that:

    ```bash
    chmod +x tests/test_whatever.rb
    ```

1. Make sure the shabang ontop of the file is vaild

    ```ruby
    #!/usr/local/bin/ruby -w
    ```

1. one last importent bit, make sure not to remove this line from the pytest.ini, this the line that make sure python files aren't imported at test collection phase

    ```ini
    [pytest]
    python_files = !*.py
    ```
