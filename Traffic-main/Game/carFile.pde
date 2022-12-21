class car{
  private
    //car members
    float posXC;
    float posYC;
    float velC;
    float hCar;
    float wCar;
    float accC;
   
  public
    //construnctor car
    car(float x,float y,float w, float h,float v, float a){
      this.posXC = x;
      this.posYC = y;
      this.velC = v;
      this.hCar = h;
      this.wCar = w;
      this.accC = a;
    }
    //show car
    void show(){
      image(carImg,this.posXC,this.posYC,carImg.width,carImg.height);
    }
    //control car to move
    void move(){
      if(keyPressed){
        if(key == 's'){
          this.posYC += velC/2.0;
          this.posXC += 0.5;
        }
        if(key == 'w'){
          this.posYC -= velC/2.0;
          this.posXC += 0.5 ;
        }
        if(key == 'd'){
          this.velC += this.accC;
          this.posXC += this.velC;
        }
        if(key == 'a'){
          this.posXC -= this.velC/2.0;
        }
      }
      else{
        velC = 4;
      }
    }
    //bounders for car
    void stayIn(){
      this.posYC = constrain(this.posYC, height/2 - wRoad ,height/2 + wRoad - hCar);
      this.posXC = constrain(this.posXC, 0, width - wCar);
    }
    //get data about car
    float getData(char data){
      if(data == 'x'){
        return this.posXC;
      }
      else if(data == 'y'){
        return this.posYC;
      }
      else if(data == 'w'){
        return this.wCar;
      }
      else if(data == 'h'){
        return this.hCar;
      }
      else if(data == 'v'){
        return this.velC;
      }
      else{
        return 0;
      }
    }
    void stop(){
      this.velC = 0;
    }
    void start(){
      this.velC = 4;
    }
}
