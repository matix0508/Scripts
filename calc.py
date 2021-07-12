from math import sqrt, log, pi
from typing import List, Union
import matplotlib.pyplot as plt
import numpy as np

class Quadratic:
    def __init__(self, a: float, b: float, c: float, show: bool = True) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.p = self.get_p()
        self.delta = self.get_delta()
        self.solutions = []
        self.solve()
        self.show_info()

    def value(self, x: float) -> float:
        return self.a * x ** 2 + self.b * x + self.c

    def get_p(self) -> float:
        return -self.b / (2 * self.a)
        

    def get_delta(self) -> float:
        output = self.b ** 2 - 4 * self.a * self.c
        return output

    def two_solutions(self) -> List[float]:
        x1 = -self.b + sqrt(self.delta)
        x1 /= 2 * self.a
        x2 = -self.b - sqrt(self.delta)
        x2 /= 2 * self.a
        output = [x1, x2]
        output.sort()
        return output

    def one_solution(self) -> float:
        return -self.b / (2 * self.a)

    def solve(self) -> None:
        if self.delta > 0:
            self.solutions = self.two_solutions()
        if self.delta == 0:
            self.solutions = self.one_solution()

    def __str__(self) -> str:
        if self.a == 1:
            output = "x^2"
        else:
            output = f"{self.a}x^2"
        if self.b > 0:
            if self.b == 1:
                output = f"{output} + x"
            else:
                output = f"{output} + {self.b}x"
        elif self.b < 0:
            if self.b == 1:
                output = f"{output} - x"
            else:
                output = f"{output} - {abs(self.b)}x"
        if self.c > 0:
            output = f"{output} + {self.c}"
        elif self.c < 0:
            output = f"{output} - {abs(self.c)}"
        return output

    
        

    def show_info(self) -> None:
        print("\t" + str(self))
        print(f"\tdelta: {self.delta}")
        if self.solutions:
            print(f"\tSolutions: {self.solutions}")
        else:
            print("\tNo real solutions")

    def show_graph(self) -> None:
        if len(self.solutions) == 2:
            x = np.linspace(self.solutions[0] - 10, self.solutions[1] + 10, 100)
        else:
            x = np.linspace(self.p - 10, self.p + 10, 100)
        y = np.array([self.value(item) for item in x])
        plt.plot(x, y)
        plt.hlines(0, -100, 100, colors='black', linestyles='dashed')
        plt.vlines(0, -100, 100, colors='black', linestyles='dashed')
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)
        plt.show()
        
