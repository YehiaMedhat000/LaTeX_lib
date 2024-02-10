from random import randint, random, shuffle, choice
from os import remove
from math import gcd, lcm

class Question():
    
    # Initialize the main attributes
    def __init__(self, n, out_file, sol_file) -> None:

        self.n = n
        self.out_file = out_file
        self.sol_file = sol_file


l_lims = [(-10, 10), (-15, 20), (0, 20), (0, 100), (50, 150)]
l_lims_add = [(0, 10), (10, 50), (0, 30), (30, 100), (50, 250)]

""" templates = {'col_sum': '''\\item \\begin{{tabular}}{{ll}}\\\\
                        \\ & {b} \\\         
                        + & {a} \\\ 
                        \\hline \\\\
                        \\end{{tabular}}
                        ''',
             'col_sub': '''\\item \\begin{{tabular}}{{ll}}\\\\
                        \\ & {b} \\\         
                        - & {a} \\\ 
                        \\hline \\\\
                        \\end{{tabular}}
                        ''',
             'inv_muliplier': '\\frac{b}{a}\n'}"""


def generator(n=100, rational=False, lower=-100, upper=100):
    for j in range(n):
        l = []
        if rational:
            for i in range(10):
                a = randint(lower, upper) + random()
                l.append(a)
        else:
            for i in range(10):
                a = randint(lower, upper)
                l.append(a)
        yield l 


def eq1_add_pos(range=100, out_file='gen_output'):
    with open(out_file, 'w') as f1:
        for i in range(range):
            for j in l_lims_add:
                a = randint(j[0], j[1])
                b = randint(j[0], j[1])
                if a > b:
                    continue
                elif a < 10:
                    continue
                elif b - a <= 10:
                    continue
                f1.write(f'$x + {a} = {b}$ \\\ \n')


def col_sum(n=100, out_file='gen_output', sol_file='gen_sol'):
    ''' 
        Generate column summation problems within specific limits in LaTeX format

        Args:
        range (int): the number of problems to yield, Default=100
        out_file (str): the output file in which the problems will be written, Default= 'gen_output'

        Returns: None

        '''
    with open(out_file, 'w') as f1, open(sol_file, 'w') as f2:
        for i in range(n):
            a = randint(0, 100)
            b = randint(100, 200)
            if b-a < 10:
                continue
            elif b-a in range(0, 201, 10):
                continue
            f1.write(f'''\\item \\begin{{tabular}}{{ll}}\\\\
                        \\ & {b} \\\         
                        - & {a} \\\ 
                        \\hline \\\\
                        \\end{{tabular}}
                        ''')
            f2.write(f'\\item {b-a}\n')


def sort_ex(n=100,
            upper=100,
            lower=-100,
            rational=False,
            out_file='gen_out',
            sol_file='gen_sol'):
    '''
        Generate sorting exercises for rational or non-rational numbers for LaTeX templates
    '''
    # Open the text manager for the main files
    with open(out_file, 'w') as f1, open(sol_file, 'w') as f2:
        for j in range(n):
            l = []
            if rational:
                for i in range(10):
                    a = randint(lower, upper) + random()
                    l.append(a)
            else:
                for i in range(10):
                    a = randint(lower, upper)
                    l.append(a)

            f1.write(f'\\item[{j+1})] {l}\n')
            f2.write(f'\\item[{j+1})] {sorted(l)}\n')
    # Open text managers for editing on the main files to remove the square brackets
    for f in [out_file, sol_file]:
        with open(f, 'r') as f1, open(f+'_edited', 'w') as f2:
            for l in f1:
                l = l.split(' ', 1)
                l = l[0] + ' ' + l[1][1:len(l[1])-2]
                f2.write(l+'\n')

    # Remove unecessary files
    remove(out_file)
    remove(sol_file)

def inv_mulitplier(n=100,
                    upper=100,
                    lower=-100,
                    out_file='gen_out',
                    sol_file='gen_sol'):
    with open(out_file, 'w') as f1, open(sol_file, 'w') as f2:
        for j in range(n):
            a = randint(lower, upper)
            b = randint(lower, upper)
            f1.write(f'\\item[{j+1})] $\\frac{{{b}}}{{{a}}}$\n')
            f2.write(f'\\item[{j+1})] $\\frac{{{a}}}{{{b}}}$\n')

def podmas(n=100,
            upper=100,
            lower=-100,
            out_file='gen_out',
            sol_file='gen_sol'):

    # Create a list of the operations
    podmas = ['\\div','+','-','\\times']
    dict_podmas = {'\\div':'/','+':'+','-':'-','\\times':'*'}
    # Get into the flow
    # 1. Open the files with the context manager
    with open(out_file, 'w') as f1, open(sol_file, 'w') as f2:
        # 2. Iterate for n times
        for j in range(n):
            a = [randint(lower,upper) for i in range(4)]
            shuffle(podmas)
            f1.write(f'\\item[{j+1})] ${a[0]}{podmas[0]}{a[1]}{podmas[1]}{a[2]}{podmas[2]}{a[3]}$\n')
            f2.write(f'\\item[{j+1})]' + exec(f'{a[0]}{dict_podmas[podmas[0]]}{a[1]}{dict_podmas[podmas[1]]}{a[2]}{dict_podmas[podmas[2]]}{a[3]}\n'))



def rational_sum(n=20,upper=100,lower=-100,out_file='gen_out',sol_file='gen_sol'):
    with open(out_file,'w') as f1, open(sol_file,'w') as f2:
        for i in range(n):
            a = [randint(lower,upper) for _ in range(3)]
            b = [randint(0,upper) for _ in range(3)]

            f1.write(f'\\item[{i+1}.)] \\frac{{{a[0]}}}{{{b[0]}}} + \\frac{{{a[1]}}}{{{b[1]}}} + \\frac{{{a[2]}}}{{{b[2]}}}\n')
            f2.write(f'\\item[{i+1}.)] \\frac{{{a[0]*b[1]*b[2] + a[1]*b[0]*b[2] + a[2]*b[0]*b[1]}}}{{{b[0]*b[1]*b[2]}}}\n')
    
    with open(out_file,'a') as f1, open(sol_file,'a') as f2:
        for i in range(n):
            a = [randint(lower,upper) for _ in range(3)]
            b = [randint(0,upper) for _ in range(3)]

            f1.write(f'\\item[{i+1}.)] \\frac{{{a[0]}}}{{{b[0]}}} + {a[1]}% + {b[1]}% + \\frac{{{a[2]}}}{{{b[2]}}}\n')
            f2.write(f'\\item[{i+1}.)] \\frac{{{a[0]*b[2] + a[2]*b[0] + (a[1]+b[1])*(b[0]*b[2])}}}{{{b[0]*b[2]*100}}}\n')

    with open(out_file,'a') as f1, open(sol_file,'a') as f2:
        for i in range(n):
            a = [randint(lower,upper) for _ in range(3)]
            b = [randint(0,upper) for _ in range(3)]

            f1.write(f'\\item[{i+1}.)] \\frac{{{a[0]}}}{{{b[0]}}} + 0.{a[1]} + 0.{b[1]} + \\frac{{{a[2]}}}{{{b[2]}}}\n')
            f2.write(f'\\item[{i+1}.)] \\frac{{{a[0]*b[2] + a[2]*b[0] + (a[1]+b[1])*(b[0]*b[2])}}}{{{b[0]*b[2]*100}}}\n')

    with open(out_file,'a') as f1, open(sol_file,'a') as f2:
        for i in range(n):
            a = [randint(lower,upper) for _ in range(3)]
            b = [randint(0,upper) for _ in range(3)]

            f1.write(f'\\item[{i+1}.)] \\frac{{{a[0]}}}{{{b[0]}}} + {a[1]} + {b[1]} + \\frac{{{a[2]}}}{{{b[2]}}}\n')
            f2.write(f'\\item[{i+1}.)] \\frac{{{a[0]*b[2] + a[2]*b[0] + (a[1]+b[1])*(b[0]*b[2])}}}{{{b[0]*b[2]}}}\n')


def convert_to_frac(n=20, out_file='gen_out', sol_file='gen_sol',lower=-100, upper=100):

    # Place holders for the template
    a = b = i = c = 0
    
    # Question template
    temp1 = "\\item[{}.)] ${} \\frac{{{}}}{{{}}} =$\n"
    temp2 = "\\item[{}.)] ${} =$\n"
    temp3 = "\\item[{}.)] ${}\\%=$\n"
    temp4 = "\\item[{}.)] $|{}\\%|=$\n"

    # Solution template
    sol_temp = "\\item[{}.)] $\\frac{{{}}}{{{}}}$\n"

    # Context manager to open files and write into them
    with open(out_file, 'w') as f1, open(sol_file, 'w') as f2:

        for i in range(n // 2):

            a = randint(lower,upper)
                
            # Write the template into the files
            f1.write(temp3.format(i+1, a))
            f2.write(sol_temp.format(i+1, a, 100))

        for i in range(n // 2):
            
            a = randint(lower, upper)
            
            # Write the template into files
            f1.write(temp4.format(i+1, a))
            f2.write(sol_temp.format(i+1, abs(a), 100))

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
            numbers = [randint(lower, upper) for _ in range(7)]

            f1.write(temp.format(*numbers))
            f2.write(sol_temp.format(*sorted(numbers)))
 




temp = '\\item ${}, {}, {}, {}, {}, {}, {}$\n'
sol = '\\item ${}, {}, {}, {}, {}, {}, {}$\n'
generator(temp=temp, sol_temp=sol, lower=-100, upper=100, n=25)