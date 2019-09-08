# Abstract
Neuroevolution techniques have been successfully applied in many reinforcement learning tasks. This
study aims at determining whether a neuroevolution method can be used to determine a stable tripleintegrator artificial vehicle controller system with the presence of a disturbing force. Control vehicles
involving more than one integration layer are known for being very unstable and difficult to control in
the presence of disturbance. Therefore a need to generate an artificial controller is originated. This study
contains a description of the experiment conducted, followed by an explanation of how genetic algorithms
and artificial neural networks are implemented to construct neuroevolution methods. Subsequently, the
product of the experiment is discussed by analyzing the results and different experiments are executed
using various parameters to analyze the effectiveness of crossover and mutation.


# Introduction 
Optimizing neural networks with genetic algorithms has proven to be a compelling approach to many control
tasks such as computer game playing or robot control, as described in [3]. In such scenarios, a policy needs to
be learned to determine which actions are taken by the controller. The need to use neuroevolution originates
in the nature of the given scenario. The aim of this study is to achieve stability. However, stability cannot
be instantly accomplished by a single action, but it rather depends on a sequence of actions. Meaning that
a single action cannot be evaluated to be good or bad, but rather a combination of actions. These scenarios
are possible to solve using reinforcement learning, a technique that consists of evaluating the effectiveness
of a sequence of actions instead of singular action and awarding the solutions having greater effectiveness.
Neuroevolution then becomes a very suitable approach to achieve the aim of this study, as it is very efficient
and promising method to deal with reinforcement learning scenarios.
At this point a question can arise to determine whether a neuroevolution method can be used to achieve
a stable triple-integrator vehicle control system with the presence of a disturbing force. To answer this, a
study is performed employing a neuroevolution method to the scenario imposed.
By conducting an experiment where a population of artificial vehicle controllers are evolved using neuroevolution, an analysis of the results will be drawn and it be demonstrated that neuroevolution produces
promising results, by successfully achieving a population with most of the vehicles being stable after 50
generations. Moreover, the effects crossover and mutation rate will be tested to analyze their influence on
the evolution process to draw conclusions for obtaining faster and more stable results.

# Experiment Description 
The experiment consists of using neuroevolution (see section 4) to evolve a population composed of vehicle
controllers. The control system of the vehicles is determined by an artificial neural network, which takes
position p, velocity v and acceleration a as inputs, and outputs a predicted jerk input change j. The jerk
input results in a change in acceleration da, at which is appended a disturbance acceleration signal at each
time step to hinder the process of the jerk prediction. The following block of code pictures the vehicle control.
time ← 0<br/>
acc ← 0<br/>
vel ← 0<br/>
pos ← 0<br/>
while time < simulation time do<br/>
     	jerk ← Predict(pos, vel, acc)<br/>
	acc ← acc + jerk<br/>
  acc ← acc + random uniform(−max disturbance, max disturbance)<br/>
  vel ← vel + acc<br/>
  pos ← pos + vel<br/>
  time ← time + 1<br/>
end while<br/>
