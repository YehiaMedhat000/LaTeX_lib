from math import gcd, lcm
from random import randint
   
# Needs more generalization
def generator(temp, sol_temp,
              out_file='gen_out', sol_file='gen_sol',
              n=100, lower=1, upper=500):
    
    '''
    Make exercies using LaTeX with specific template
    ...

    Args
    ----
        temp: str
            The question template
        sol_temp: str
            The solution template 
        n: int
            The number of templates generated
        out_file: str
            The file name in which the questions templates are passed
        sol_file: str
            The file name in which the answers templates are passed
        lower: int
            The lower bound for the `randint()` function
        upper: int
            The upper bound for the `randint()` function
    '''

    # Opening the files
    with open(out_file, 'w') as f1, open(sol_file, 'w') as f2:
        # Looping to fill the templates
        for i in range(n):
            a = randint(lower, upper)
            b = randint(lower, upper)
            c = randint(lower, upper)
            d = randint(lower, upper)
            if a/b <= c/d:
                continue

            # Least common multiplier for the two denomenators
            denom = lcm(b, d)

            # Calculations for the final simplifications
            result_numerator = (denom / b) * a  - (denom / d) * c
            # The whole part beside the fraction
            integer = result_numerator // denom
            # The remainder value of result_numerator
            rem = result_numerator % denom
            # The greatest common factor of rem and denom
            g_common_factor = gcd(int(rem), int(denom))

            f1.write(temp.format(a))

            if integer:
                f2.write(sol_temp.format(int(integer), int(rem / g_common_factor), int(denom / g_common_factor)))               
            else:
                f2.write(sol_temp.format(' ', int(rem / g_common_factor), int(denom / g_common_factor)))