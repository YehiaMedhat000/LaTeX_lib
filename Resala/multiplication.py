''' This is a script for generating a problem set in LaTeX for multiplication '''
import random as rand


if __name__ == "__main__":
    with open("problems.txt", 'w') as p:
        rand.seed(42)
        for n in range(1000):
            a = rand.randint(10, 999)
            b = rand.randint(10, 999)
            p.write(f"\\item $\\begin{{array}}{{r}} {a} \\\\ \\times \\quad {b} \\\\ \\hline \\end{{array}}$\n")
