import processing.sound.*;
SoundFile horn, brake, siren;
int sec, nrCars =21,nrTrees = 100;
//image variables
PImage carImg, enemyImgRed, enemyImgYellow, enemyImgAngry, 
        enemyImgPolice,enemyImgAmbulance, treeImg, helycopter;
//declare ojects
car c;
enemy e;
tree  t1,t2,t;
//declare arrays
enemy[] E = new enemy[nrCars];
tree[] T1 = new tree[nrTrees], T2 = new tree[nrTrees],T = new tree[nrTrees/4];
hely h;
//boolean variables
boolean over = false, pause = false, start = true, moveHel = false, changed = false, waitHorn = false, waitBreak = false;
//size half road
float wRoad = 120, hornAmpl = 0.5, breakAmpl = 0.1, randEnemy; 
int timeStart, timeFinish = 0, i, soundBreakFinish, soundHornFinish;
//set up
void setup(){
  fullScreen(); 
  //size(1000,1000);
  horn = new SoundFile(this,"Sounds/horn.mp3");
  brake = new SoundFile(this,"Sounds/brake.mp3");
  siren = new SoundFile(this,"Sounds/siren.mp3");
  //load image objects
  carImg = loadImage("Images/carImg.png");
  enemyImgRed = loadImage("Images/enemyImgRed.png");
  enemyImgYellow = loadImage("Images/enemyImgYellow.png");
  enemyImgAngry = loadImage("Images/enemyImgAngry.png");
  enemyImgPolice = loadImage("Images/enemyImgPolice.png");
  enemyImgAmbulance = loadImage("Images/enemyImgAmbulance.png");
  helycopter = loadImage("Images/helycopter.png");
  treeImg = loadImage("Images/treeImg.png");
  //initialize objects
  for(i = 0; i< nrCars;i++){
    GenerateCars();
  }
  c = new car(100,height/2,carImg.width,carImg.height,2.0,0.05);
  for(i =0 ;i < nrTrees; i++){
    t1 = new tree(treeImg.width, treeImg.height,i,i,1);
    T1[i] = t1;
    t2 = new tree(treeImg.width, treeImg.height,i,i,1);
    T2[i] = t2;
  }
  for(i =0 ;i < nrTrees/4; i++){
    t = new tree(treeImg.width, treeImg.height,i,i,0);
    T[i] = t;
  }
}
void draw(){
  //test game over
  if(over || pause){
    if(over){
      timeFinish = millis()/1000;
      background(0);
      textAlign(CENTER);
      textSize(40);
      fill(250,30,50);
      text("Game Over",width/2,height/2);
      textSize(20);
      textAlign(CENTER);
      text(timeStart,width/2,height/2+60);
      //if mouse pressed restart game
      if(mousePressed){
        over = false;
        setup();
      }
    }
    if(key == 'k'){
      pause = false;
      timeFinish = millis()/1000 - timeStart;
    }
    start = true;
  }
  else{
    frameRate(1000);
    timeStart = millis()/1000 - timeFinish;
    background(30,240,50);
    fill(0);
    textSize(100);
    text(timeStart,100,100);
    //draw road
    strokeWeight(0);
    fill(230);
    rect(0,height/2 + wRoad,width,-2*wRoad);
    for(i = 0; i < 7; i++){
      fill(0);
      strokeWeight(1);
      line(0,height/2 - wRoad + i*40,width,height/2 - wRoad + i*40);
    }
    if(keyPressed){
      if(!waitHorn){
        soundHornFinish = millis();
        if(key == 'h'){
          horn.amp(hornAmpl);
          horn.play();
          if(soundHornFinish - timeStart > 2){
            waitHorn = true;
          }
        }
      }
      if(!waitBreak){
        soundBreakFinish = millis();
        if(key == 'a'){
          brake.play();
          brake.amp(breakAmpl);
          if(soundBreakFinish - timeStart > 2){
            waitBreak = true;
          }
        }
      }
    }
    if(!keyPressed){
      waitHorn = false;
      waitBreak = false;
    }
    //draw car
    c.show();
    //control car
    c.move();
    //keep car on road
    c.stayIn();
    //enemy test
    EnemyTest();
    //test if end game
    OverTest();
    //test for tree
    TreeTest();
    if(key == 'p'){
      pause = true;
    }
    if(timeStart % 10 == 0 && timeStart > 0){
      h = new hely(helycopter.width, helycopter.height);
      moveHel = true;
    }
    if(moveHel){
       h.show();
       h.update();
       h.checkOut();
    }
  }
}
