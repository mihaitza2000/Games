class hely{
  private
    float wHelycopter;
    float hHelycopter;
    float posXEl;
    float posYEl;
    float velE = 2;
  public
    hely(float w,float h){
      this.wHelycopter = w;
      this.hHelycopter = h;
      this.posXEl = width + w;
      this.posYEl = h;
    }
    void show(){
      image(helycopter,this.posXEl,this.posYEl,wHelycopter,hHelycopter);
    }
    void update(){
      this.posXEl -= 4*this.velE;
      this.posYEl += this.velE/10;
    }
    void checkOut(){
      if(this.posXEl < -wHelycopter){
        moveHel = true;
      }
    }
}
