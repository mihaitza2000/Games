class enemy{
  private
    //enemy members
    float wEnemy;
    float hEnemy;
    float posXE;
    float posYE;
    float velE = 4;
    char col;
  public
    // enemy constructor
    enemy(float w,float h,int i, char c){
      this.wEnemy = w;
      this.hEnemy = h;
      this.col = c;
      //set position of enemy randomly on road
      int x;
      float factor = 0;
      x = floor(random(1,7));
      switch(x){
        case 1: {
          factor =  2/3.0;
          break;
        }
        case 2: {
          factor =  1/3.0;
          break;
        }
        case 3: {
          factor =  0;
          break;
        }
        case 4: {
          factor =  -1/3.0;
          break;
        }
        case 5: {
          factor =  -2/3.0;
          break;
        }
        case 6: {
          factor =  -1.0;
          break;
        }
        default:{
          break;
        }
      }
      this.posYE = height/2 + factor*wRoad;
      this.posXE = random(width + 2*i*81,width+(2*i+1)*81);
    }
    //changed possision's enemy
    void update(){
      if(this.col == 'e'){
        this.posXE -= 2*this.velE;
      }
      else if(this.col == 'p'){
        this.posXE -= 1.8*this.velE;
      }
      else if(this.col == 'a'){
        this.posXE -= 1.6*this.velE;
      }
      else if(this.col == 'y'){
        this.posXE -= 1.4*this.velE;
      }
      else{
        this.posXE -= 1.2*this.velE; 
      }
    }
    //show enemy
    void show(){
      if(this.col == 'r'){
        image(enemyImgRed,posXE,posYE+((1/3.0)*wRoad-enemyImgRed.height)/2,enemyImgRed.width, enemyImgRed.height);
      }
      else if(this.col == 'y'){
        image(enemyImgYellow,posXE,posYE+((1/3.0)*wRoad-enemyImgYellow.height)/2,enemyImgYellow.width, enemyImgYellow.height);
      }
      else if(this.col == 'a'){
        image(enemyImgAngry,posXE,posYE+((1/3.0)*wRoad-enemyImgAngry.height)/2,enemyImgAngry.width, enemyImgAngry.height);
      }
      else if(this.col == 'p'){
        image(enemyImgPolice,posXE,posYE+((1/3.0)*wRoad-enemyImgPolice.height)/2,enemyImgPolice.width, enemyImgPolice.height);
      }
      else if(this.col == 'e'){
        image(enemyImgAmbulance,posXE,posYE+((1/3.0)*wRoad-enemyImgAmbulance.height)/2,enemyImgAmbulance.width, enemyImgAmbulance.height);
      }
    }
    //get data from enemy
    float getData(char data){
      if(data == 'x'){
        return this.posXE;
      }
      else if(data == 'y'){
          return this.posYE;
      }
      else if(data == 'w'){
      return this.wEnemy;
      }
      else if(data == 'h'){
        return this.hEnemy;
      }
      else if(data == 'v'){
        return this.velE;
      }
      else if(data == 'c'){
        return this.col;
      }
      else{
        return 0;
      }
    }
    float getBand(int i){
        return (E[i].getData('y') - height/2)/wRoad;
    }
    //change possition of an enemy with other enemy's possition
    void equal(enemy e){
      this.posXE = e.getData('x');
      this.posYE = e.getData('y');
    }
    void stop(){
      this.velE = 0;
    }
    void start(){
      this.velE = 2;
    }
    void changeposYE(float newBand){
      this.posYE = height/2 + newBand*wRoad;
    }
}
