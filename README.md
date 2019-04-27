# Neuro-Evolution
Use of genetic algorithm to achieve stable piloting of a 3 integrator based control model.


The genetic algorithm is a method for solving both constrained and unconstrained optimization problems that is based on natural selection, the process that drives biological evolution. The genetic algorithm repeatedly modifies a population of individual solutions. At each step, the genetic algorithm selects individuals at random from the current population to be parents and uses them to produce the children for the next generation. Over successive generations, the population "evolves" toward an optimal solution. You can apply the genetic algorithm to solve a variety of optimization problems that are not well suited for standard optimization algorithms, including problems in which the objective function is discontinuous, nondifferentiable, stochastic, or highly nonlinear. The genetic algorithm can address problems of mixed integer programming, where some components are restricted to be integer-valued.

Acceleration vehicle control is a mode of control involving acceleration of the only input the pilot can adjust. Such input results in an adjustment of the acceleration of the vehicle. This mode of control is well-know for being very unstable and difficult to control.
The following program achieves a model capable of achieve acceleration control by making use of genetic algorithms. 
The model consits of a neural network with the environment as input (model position, velocity and acceleration) and a desicion as ouput (decrease acceleration, mantain acceleration or increase acceleration). The neural network uses one hidden layer with 8 nodes to account for non-linearities.
