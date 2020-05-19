from HVAC_Model import forest

from jmetal.algorithm.multiobjective.omopso import OMOPSO
from jmetal.operator import UniformMutation
from jmetal.operator.mutation import NonUniformMutation
from jmetal.util.archive import CrowdingDistanceArchive
from jmetal.util.termination_criterion import StoppingByEvaluations
 
from jmetal.core.problem import FloatProblem
from jmetal.core.solution import FloatSolution

from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from jmetal.operator import BitFlipMutation, SPXCrossover

from time import time
import random

class Optimizacion(FloatProblem):
    def __init__(self):
        super(Optimizacion, self).__init__()

        self.number_of_objectives = 4
        self.number_of_variables = 4
        self.number_of_constraints = 0

        self.obj_directions = [self.MAXIMIZE, self.MINIMIZE, self.MINIMIZE, self.MAXIMIZE]
        self.obj_labels = ['Comfort', 'Energy', 'Cost', 'COP']

        self.lower_bound = self.number_of_variables * [0.0]
        self.upper_bound = self.number_of_variables * [1.0]
        
    def evaluate(self, solution: FloatSolution) -> FloatSolution:
        resultados = forest.predict([solution.variables + [10, 23.5, 1700, 23, 9, 11, 18, 1]])
        
        solution.objectives[0] = resultados[0][0]
        solution.objectives[1] = resultados[0][1]
        solution.objectives[2] = resultados[0][2]
        solution.objectives[3] = resultados[0][3]

        return solution

    def create_solution(self) -> FloatSolution:
        new_solution = FloatSolution(lower_bound=self.lower_bound, 
                                    upper_bound=self.upper_bound, 
                                    number_of_objectives= self.number_of_objectives,
                                    number_of_constraints= self.number_of_constraints)

        if 10 < 23.5:
            new_solution.variables[0] = 0
            new_solution.variables[1] = 0
            new_solution.variables[2] = round(random.random()*(-100),2)
            new_solution.variables[3] = round(random.random()*(-100),2)
        else:
            new_solution.variables[0] = round(random.random()*(-100),2)
            new_solution.variables[1] = round(random.random()*(-100),2)
            new_solution.variables[2] = 0
            new_solution.variables[3] = 0

        return new_solution

    def get_name(self) -> str:
        return 'Optimización'

if __name__ == '__main__':
    problem = Optimizacion()
    mutation_probability = 1.0 / problem.number_of_variables
    max_evaluations = 250
    swarm_size = 100

    algorithm = OMOPSO(
        problem=problem,
        swarm_size=swarm_size,
        epsilon=0.001,
        uniform_mutation=UniformMutation(probability=mutation_probability, perturbation=0.5),
        non_uniform_mutation=NonUniformMutation(mutation_probability, perturbation=0.5,
                                                max_iterations=int(max_evaluations / swarm_size)),
        leaders=CrowdingDistanceArchive(100),
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations)
    )

    algorithm.run()
    solutions = algorithm.get_result()
    print(str(solutions[0]))