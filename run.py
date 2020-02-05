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

if __name__ == '__main__':
    try:
        # Check to make sure an argument has been passed
        if len(argv) < 2:
            raise exceptions.MissingInputError()

        # The argument passed should be the solution name
        solution_name = argv[1]

        # Get the solution module and execute solve function
        solution_mod = import_module(f'solutions.{solution_name}')
        solution_mod.solve()
    except (exceptions.MissingInputError) as e:
        print(e.message)
    except Exception as e:
        print(e)
