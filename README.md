# Cookbook Programming Style

## Due Date

Tuesday, April 26th, 2022 at 2:50 pm

## Introduction

In this practical assignment, you will practice writing programs in the Cookbook programming style by converting a program written in the Monolithic programming style to a program that uses the Cookbook programming style.
Through this exercise, you will put into practice the following learning objective(s):

- The constraints associated with the Cookbook programming style and how to implement it in Python
- The complexity associated with the Monolithic and Cookbook programming styles
- Whether the Monolithic and Cookbook programming styles support unit testing

## Instructions

Please perform each of the following steps in order.

### Install Dependencies

Install the dependencies listed in `pyproject.toml` by running `poetry install`.

### Run and Analyze the Monolithic Term Context Program

Run the Monolithic term context program by running `poetry run python term_context_monolithic.py pride_and_prejudice.txt good`. You should see the following output.

```console
Input file: pride_and_prejudice.txt
Term: good

- of a _good_ fortune, must 
- in a _good_ word for 
- while. How _good_ it was 
- such a _good_ joke, too, 
- therefore, in _good_ spirits to 
- had a _good_ deal of 
- such perfect _good_ breeding!" He 
- world are _good_ and agreeable 
- With your_ _good_ sense, to 
- take the _good_ of everybody's
```

In `writing/reflection.md`, describe the high-level behavior of the Monolithic term context program. Then, read through the Monolithic program, making sure that you understand how the program produces its high-level behavior.

### Convert the Monolithic Program to a Cookbook Program

Take the following steps to convert the Monolithic term context program to a Cookbook term context program.

First, define the following procedures (i.e. functions) using the `def` keyword in the `term_context_cookbook.py` file. Also, add the docstring for each of these procedures as listed below.

- `read_file`
  - Docstring: `"""Read in the data from the input file as characters."""`
- `group_char_data_into_words`
  - Docstring: `"""Group characters into words."""`
- `gather_contexts_from_words`
  - Docstring: `"""Gather contexts for first ten occurrences of term."""`
- `print_contexts`
  - Docstring: `"""Print input and contexts."""`

Then, using the docstrings as a guide, go through the Monolithic program and copy each portion of code into the appropriate procedure in the Cookbook program. For example, the code in the Monolithic program that reads in the data from the input file as characters should be copied into the `read_file` procedure defined in the Cookbook program.

Next, determine which variables should be declared as global variables in the Cookbook program and declare them under the `# Declare global variables` comment in the Cookbook program. To determine which variables should be global, in the Cookbook program, look at which variables are shared between procedures. These variables that are shared between procedures may be undefined before you declare them as global variables, which should also serve as a hint.

Next, use `global` statements in any procedure that uses a global variable. For example, if a procedure uses a global variable called `input_file`, then you should have the statement `global input_file` in that procedure.

Lastly, call each procedure in the correct order under the `# Call procedures` comment in the Cookbook program.

After you have finished the conversion, make sure the Cookbook program has the same high-level behavior as the Monolithic program by running `poetry run python term_context_monolithic.py pride_and_prejudice.txt good` and `poetry run python term_context_cookbook.py pride_and_prejudice.txt good` in succession and verifying that their outputs are identical.

To further verify the correct behavior of the Cookbook program, execute the test suite by running `poetry run pytest`. Make sure to revise your Cookbook program until all tests pass.

### Bonus

For one bonus point, refactor the `group_char_data_into_words` procedure using methods of the `list` and `str` data types so that the procedure contains only three lines or less.

### Reflect on Your Work

Answer all questions in `writing/reflection.md`.

### Run GatorGrader

To check your approximate progress on this assignment, [run GatorGrader](https://proactiveprogrammers.com/proactive-skills/technical-skills/using-gatorgrader/).

## Assessment Strategy

This assignment will be assessed based on the following components:

- **Percentage of Passing GatorGrader Checks**: If source code is required, you should repeatedly update the implementation of your source code until it passes all of the GatorGrader checks by, for instance, producing the correct output. If technical writing is required, you should repeatedly revise your technical writing until it also passes all of GatorGrader's checks about, for instance, the length of its content.
- **Percentage of Passing GitHub Actions Checks**: You will receive checkmarks for any additional checks on source code and/or technical writing, other than the "Run GatorGrader" check, that are encoded in GitHub Actions. You will receive a checkmark for each passing GitHub Actions check. As with the previous grading component, you are encouraged to repeatedly amend your source code and/or technical writing until all of your GitHub Actions checks pass.
  - Please note that the "Check Spelling" GitHub Actions check may flag proper nouns or other real words if the dictionary it uses does not contain them. If your "Check Spelling" GitHub Actions check is failing due to a correctly spelled word being incorrectly flagged as "unknown" by CSpell, you will need to add the word to the list of words in `.github/cspell.json`.
- **Mastery of Software Engineering Concepts and Skills**: You will receive a checkmark for demonstrating mastery of each of the following concepts and skills of software engineering exercised in this assignment that is not checked by GatorGrader. If you receive checkmarks for all of the following concepts and skills and have all GatorGrader checks pass, you will know that you have mastered all of the learning objectives of this assignment. For this assignment, you must:
  - Make small, focused commits
  - Write commit messages that abide by [the seven rules of a great Git commit](https://cbea.ms/git-commit)
  - Correctly describe the high-level behavior the term context program
  - Correctly provide code examples for the constraints associated with the Cookbook programming style
  - Correctly explain which programming style is associated with more complexity
  - Correctly explain which programming style is easier to unit test
