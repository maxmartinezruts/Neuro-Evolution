// Daniel Shiffman
// Neuro-Evolution Flappy Bird with TensorFlow.js
// http://thecodingtrain.com
// https://youtu.be/cdUNkwXx-I4

class Bird {
    constructor(brain) {
        this.y = height / 2;
        this.x = width /2;
        this.position = createVector(this.x, this.y)
        this.acceleration = createVector(0,0);

        this.velocity = createVector(0,0);
        this.acceleration.add(p5.Vector.random2D().div(3));

        this.score = 0;
        this.fitness = 0;
        if (brain) {
            this.brain = brain.copy();
        } else {
            this.brain = new NeuralNetwork(3,6, 3);
        }
    }
  
    dispose() {
        this.brain.dispose();
    }
  
    show() {
        stroke(255);
        fill(255, 50);
        ellipse(this.position.x, this.position.y, 32, 32);
    }
  
    left(){
        this.acceleration.add(createVector(-0.1,0))
    }
    right(){
        this.acceleration.add(createVector(0.1,0))
    }
   
   
    mutate() {
        this.brain.mutate(0.1);
    }
  
    think() {
       
    
        let inputs = [];
        inputs[0] = this.position.x;
        inputs[1] = this.velocity.x;
        inputs[2] = this.acceleration.x;
        let output = this.brain.predict(inputs);
        // console.log(output[0], output[1], output[2])
        //if (output[0] > output[1] && this.velocity >= 0) {
            
        if (output[0] > output[1] && output[0] > output[2]){
            // console.log('output 0 is greater')
            this.left()
        }
        if (output[2] > output[1] && output[2] > output[0]){
            // console.log('output 2 is greater')
            this.right()
        }
    }
  
    offScreen() {
      return this.y > height || this.y < 0;
    }
  
    update() {
      this.score++;
        this.acceleration.add(p5.Vector.random2D().div(20))
        this.acceleration.y =0
       this.velocity.add(this.acceleration)
      
      //this.velocity *= 0.9;
      this.position.add(this.velocity)
    }
  }
