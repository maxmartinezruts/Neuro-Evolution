// Daniel Shiffman
// Neuro-Evolution Flappy Bird with TensorFlow.js
// http://thecodingtrain.com
// https://youtu.be/cdUNkwXx-I4

const TOTAL = 100;
let birds = [];
let savedBirds = [];
let counter = 0;
let slider;




function keyPressed() {
  console.log(key)
  if (key == 'S') {
    console.log('S printed')
    let bird = birds[0];
    saveJSON(bird.brain, 'bird.json');
  }
  if (key == 'ArrowLeft') {
    left()
  }
  if (key == 'ArrowRight') {
    right()
  }
}

function left(){
  this.acceleration -= 0.1
}
function right(){
  this.acceleration += 0.1
}

function setup() {
  createCanvas(640, 480);
  tf.setBackend('cpu');
  slider = createSlider(1, 10, 1);
  for (let i = 0; i < TOTAL; i++) {
    birds[i] = new Bird();
  }
  this.acceleration = 0
  this.acceleration += ((Math.random()*2)-1)/3;

this.velocity = 0
this.position = width/2
console.log(this.position)
}

function draw() {
  this.acceleration += ((Math.random()*2)-1)/20;
  this.velocity += this.acceleration
  this.position += this.velocity
  for (let n = 0; n < slider.value(); n++) {
    
    counter++;


     
    for (let j = birds.length - 1; j >= 0; j--) {
      if (birds[j].position.x <0 || birds[j].position.x > width  || birds[j].position.y <0 || birds[j].position.y >height){
        savedBirds.push(birds.splice(j, 1)[0]);

      }
    
  }

    

    for (let i = birds.length - 1; i >= 0; i--) {
      if (birds[i].offScreen()) {
        savedBirds.push(birds.splice(i, 1)[0]);
      }
    }

    for (let bird of birds) {
      bird.think();
      bird.update();
    }

    if (birds.length === 0) {
      counter = 0;
      this.acceleration = 0
      this.acceleration += ((Math.random()*2)-1)/3;

this.velocity = 0
this.position = width/2
      nextGeneration();
    }
    if (counter > 800){
      for (let j = birds.length - 1; j >= 0; j--) {
          savedBirds.push(birds.splice(j, 1)[0]);      
      }
      counter = 0;
      this.acceleration = 0
      this.acceleration += ((Math.random()*2)-1)/3;

this.velocity = 0
this.position = width/2
      nextGeneration();
    }
  }

  // All the drawing stuff
  background(0);
  stroke(255);
  fill(255, 50);
  ellipse(this.position, height/2, 50, 50);
  for (let bird of birds) {
    bird.show();
  }


}

// function keyPressed() {
//   if (key == ' ') {
//     bird.up();
//     //console.log("SPACE");
//   }
// }