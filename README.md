# Project Euler 100 Challenge

Personal repository for the Project Euler 100 challenge in 2020.
Solutions provided in Python 3.7.6 environment.

## Running the solutions

The project uses the memory_profiler module to help measure the
efficiency of the solutions. To execute a solution for one of the
problems included in this project run:

    `python3 run.py prob_1`

In the command above `prob_1` could be replaced with a reference to
any one of the solutions in the solutions directory.

## Unit Tests

A unit test is created for each solution provided in the `tests`
directory. The tests for the solutions are in individual files named
`test_prob_*.py`. The tests run the solution and check that the return
value aligns with the expected answer for the problem.

In addition, a unit test is provided for the utility functions in
`test_utils.py`.

To run the unit tests, use the following command:

    `python3 -m unittest discover -s tests`
