float xi,yi,wi,hi,xj,yj,wj,hj;
boolean slide,keepSlide;
float band,band1,band2;
void EnemyTest(){
  boolean up, down;
  for(i = 0; i< nrCars;i++){
      if(E[i].getData('x') < -E[i].getData('w')){
        GenerateCars();
      }
      xi = E[i].getData('x');
      yi = E[i].getData('y');
      wi = E[i].getData('w');
      hi = E[i].getData('h');
      band = E[i].getBand(i);
      keepSlide = true;
      for(int j = 0 ; j!=i && j < nrCars && keepSlide;j++){
        slide = false;
        up = true;
        down = true;
        xj = E[j].getData('x');
        yj = E[j].getData('y');
        wj = E[j].getData('w');
        hj = E[j].getData('h');
        slideNow();
        if(slide){
          band1 = E[j].getBand(j)-1/3.0;
          band2 = E[j].getBand(j)+2/3.0;
           if(band != -1.0 && up){
             if(band!=band1){
               E[i].changeposYE(band-1/3.0);
               down = false;
               keepSlide = false;
             }
             else{
               band = band1;
               keepSlide = true;
             }   
           }
           else{
             down = true;
             up = false;
             keepSlide = false;
           }
           if(band != 2/3.0 && down){
             if(band!=band2){
               E[i].changeposYE(band+1/3.0);
               up = false;
               keepSlide = false;
             }
             else{
               band = band2;
               keepSlide = true;
             }
           }
           else{
             down = false;
             up = true;
             keepSlide = false;
           }
        }
      }
      E[i].show();
      E[i].update();
  }
}
void slideNow(){
  if(((xi > xj && xi < xj + wj) && (yi > yj && yi < yj + hj))||
     ((xi + wi > xj && xi + wi < xj + wj) && (yi > yj && yi < yj + hj))||
     ((xi > xj && xi < xj + wj) && (yi + hi > yj && yi + hi < yj + hj))||
     ((xi + wi > xj && xi + wi < xj + wj) && (yi + hi > yj && yi + hi < yj + hj))){
        slide = true; 
     } 
  if(((xj > xi && xj < xi + wi) && (yj > yi && yj < yi + hi))||
     ((xj + wj > xi && xj + wj < xi + wi) && (yj > yi && yj < yi + hi))||
     ((xj > xi && xj < xi + wi) && (yj + hj > yi && yj + hj < yi + hi))||
     ((xj + wj > xi && xj + wj < xi + wi) && (yj + hj > yi && yj + hj < yi + hi))){
       slide = true; 
     }
}
