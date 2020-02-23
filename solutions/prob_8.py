'''Project Euler - Problem 8
   Largest product in a series

   The four adjacent digits in the 1000-digit number (resources/problem_8.txt)
   that have the greatest product are 9 × 9 × 8 × 9 = 5832.

   Find the thirteen adjacent digits in the 1000-digit number that have the 
   greatest product. What is the value of this product?
'''
import pathlib


adjacent_len = 13


def get_number_string():
    # Get the file path that contains the number
    file_path = pathlib.Path.cwd().joinpath(pathlib.Path('resources/problem_8.txt'))
    with open(file_path, 'r') as f:
        rows = f.readlines()
    
    number_string = ''
    # Merge rows into a single string
    for row in rows:
        number_string += row[:-1] if row[-1] == '\n' else row
    
    return number_string


def solve():
    max_product = 0
    cur_product = 0
    max_index = adjacent_len

    # Get the 1000 digit string
    number_string = get_number_string()
    str_len = len(number_string)

    for beg_index in range(0, str_len - adjacent_len):
        # If the 0 was found within the last adjacent_len digits, there is no need to continue
        max_index = beg_index + adjacent_len

        if '0' in number_string[beg_index : max_index]:
            # if 0, will need to skip and recalculate the base current product
            beg_index +=1
            cur_product = 0
            continue

        elif cur_product == 0: # need to recalculate
            cur_product = 1
            for i in range(beg_index, max_index):
                cur_product *= int(number_string[i])

        else:
            # Rather than recalculating the entire product by iterating through each number
            # divide by what would be the first number and then multiply by the last
            divider = int(number_string[beg_index - 1])
            cur_product /= divider
            cur_product *= int(number_string[max_index - 1])
            
        # Set the max
        max_product = max(cur_product, max_product)
        
        # Shift to the next 13 numbers
        beg_index += 1
        
    return max_product