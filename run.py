'''run.py
   Used to execute the problem solutions.

   Attributes:
       solution_file_name -- name for the solution to be executed

    Example execution command from the root dir of the project:
        `python3 run.py prob_1`
'''
from importlib import import_module
from utils import exceptions
from sys import argv
import time
from memory_profiler import profile
import traceback


@profile
def solution_execution(function):
    start = time.time()
    result = function()
    end = time.time()
    print('Solution result: ', result)
    print('total running time: ', end - start)


if __name__ == '__main__':
    try:
        # Check to make sure an argument has been passed
        if len(argv) < 2:
            raise exceptions.MissingInputError()

        # The argument passed should be the solution name
        solution_name = argv[1]

        # Get the solution module and execute solve function
        solution_mod = import_module(f'solutions.{solution_name}')
        solution_execution(solution_mod.solve)

    except (exceptions.MissingInputError) as e:
        print(e.message)
    except Exception as e:
        print('err: ', e)
        traceback.print_exc()
