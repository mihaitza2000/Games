class tree{
  private
  //members of a tree
    float posXT;
    float posYT;
    float wTree;
    float hTree;
    float velT = 1;
  public
  //tree constructor
    tree(float w,float h,float prob,float x, int out){
      if(out == 1){
        //60*x=2*x+30   60*x+30=(2*x+1)*30
         this.posXT = random(width + 60*x,width + 60*x+30);
      }
      else{
         this.posXT = random(w,width - w);
      }
      //probability of tree to appear left or right side of the road
      if(prob % 2 == 0){
        this.posYT = random(hTree,height/2.0 - 2*wRoad - hTree);
      }
      else{
        this.posYT = random(height/2.0+wRoad+hTree,height-wRoad-hTree);
      }
      this.wTree = w;
      this.hTree = h;
    }
    //show tree
    void show(){
      image(treeImg,posXT,posYT,treeImg.width,treeImg.height);
    }
    //update tree possition by a vellocity
    void update(){
      this.posXT -= this.velT;
    }
    //get data from tree
    float getData(char data){
      if(data == 'x'){
        return this.posXT;
      }
      else if(data == 'y'){
          return this.posYT;
      }
      else if(data == 'w'){
      return this.wTree;
      }
      else if(data == 'h'){
        return this.hTree;
      }
      else if(data == 'v'){
        return this.velT;
      }
      else{
        return 0;
      }
    }
    //equal trees possision with another tree
    void equal(tree t){
      this.posXT = t.getData('x');
      this.posYT = t.getData('y');
    }
    void stop(){
      this.velT = 0;
    }
    void start(){
      this.velT = 4;
    }
}
