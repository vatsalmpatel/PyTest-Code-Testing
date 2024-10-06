# YAML Configuration Testing with Pytest

This repository contains a test suite for validating complex YAML configuration files used in a web application. The test suite is implemented using `pytest` and tests various aspects of the configuration, including server settings, database connections, microservices, logging, authentication, and more.

## Note

- The sample YAML files were generated using ChatGPT
- **This project follows TDD (Test-Driven Development) Paradigm of Software Engineering, which means that we write tests first, and then write small, inceremental pieces of code (in this case YAML config files) that will pass these tests, leading to robust tested code (in our case YAML configuration files), which is ready at all times to be deployed into production. We have to make sure that the tests are written first, and then your code, not the other way round. Th ewhole point of TDD is to write tests first, and then code, which ensures that your code is robust and free of any bugs.**

## Project Structure

**`
.github/
`**
Contains the CI (Continuous Integration) workflow file that will run pytest on every push or pull request to the master/main branch

**`
code/
`**
The folder contains all the code that is being tested. There are currently two python files, one is the **math_utils.py** which has a simple add function that adds two numbers that returns the result. The other file is **config_loader.py** file, which is used to load the **YAML** files in the **config/** directory. Subsquently, there are tests writte for these YAML files.


**`
config/
`**
This directrory contains the sample YAML files, that will be used to write tests on, and validate the configurations in the YAML file with the help of **pytest**.

**`
test/
`**
This folder contains all the test for the code files in **code/** directory. **test_math_utils_1.py** and **test_math_utils_2.py** contains tests for the **math_utils.py** file in the **code/** directory. The **test_config_sample_1.py** file has tests for the **sample1.yaml** file and **test_config_sample_2.py** file has tests for the **sample2.yaml** file.

## Installing Requirements:

As this is mainly used for writing tests in `pytest`, you will need to first install pytest, which can be done with the help of:

```python
pip install pytest
```

And then you will need to install `pyyaml`, which will be used to read YAML files, in the code:

```python
pip install pyyaml
```

or alternatively, you can use the **requirements.txt** file in the project directory, to install all the necessary packages:

```python
pip install -r requirements.txt
```

## Running the code:

- To run the code, which is mainly running the **tests**, which are mainly written in pytest, you need to run this command in the root directory of the project, and pytest will pick up all the tests from anywhere in the entire direcotry:

    ```Python
    pytest
    ```

- After you run this, you will see this, which means all the tests have successfully run, and there are no failing tests:

    ![test-success-image](/static/test-success.png)

- If one of the tests fail, you will see an error and a message, pointing on what failed:

    ![test-fail-image](/static/test-fail.png)

## Integration with GitHub Action:

- With the help of GitHub Actions, whenever there is a push to the master/main branch or a pull request is sent to the master/main branch, tests are run first with pytest, which ensures that no bugs are introduced to your production code. These tests are run automatically on every pull/push to the master/main branch.

## Future Improvements/Changes:

- Lock users from pushing directly pushing to the master branch by enabling ruleset on this repo
- Add another rule that will ensure that merging to master/main branch only happens if all the tests pass, if not, prevent merge into the master/main branch