from HVAC_Model import forest, forestAux

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

import json
from flask import Flask, request, jsonify

app = Flask(__name__)

Text = 0
SetPoint = 0
People = 0
Tint = 0
Month = 0
Day = 0
Hour = 0
Interval = 1

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
        resultados = forest.predict([solution.variables + [Text, SetPoint, People, Tint, Month, Day, Hour, Interval]])
        
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

        new_solution.variables[0] = round(random.random()*(-100),2)
        new_solution.variables[1] = round(random.random()*(-100),2)
        new_solution.variables[2] = round(random.random()*(-100),2)
        new_solution.variables[3] = round(random.random()*(-100),2)
            
        return new_solution

    def get_name(self) -> str:
        return 'Optimización'

@app.route('/optimizar', methods=['POST'])
def mopso():
    data = request.get_json()

    global Text
    global SetPoint
    global People
    global Tint
    global Month
    global Day
    global Hour
    global Interval

    Text = data['Text']
    SetPoint = data['SetPoint']
    People = data['People']
    Tint = data['Tint']
    Month = data['Month']
    Day = data['Day']
    Hour = data['Hour']
    Interval = data['Interval']

    problem = Optimizacion()
    mutation_probability = 1.0 / problem.number_of_variables
    max_evaluations = 1000
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

    salida = {'cap': solutions[0].variables, 'obj': solutions[0].objectives}

    print(forestAux.predict([solutions[0].variables + [Text, People, Tint]]))

    return json.dumps(salida)