void TreeTest(){
    for(i = 0; i < nrTrees;i++){
      int p;
      if(T1[i].getData('x') < -T1[i].getData('w')){
        p = floor(random(1,3));
        t1 = new tree(T2[i].getData('w'), T2[i].getData('h'),i,p,1);
        T1[i] = t1;
      } 
      if(T2[i].getData('x') < -T2[i].getData('w')){
        p = floor(random(1,3));
        t2 = new tree(T2[i].getData('w'), T2[i].getData('h'),i,p,1);
        T2[i] = t2;
      } 
      T1[i].show();
      T2[i].show();
      T1[i].update();
      T2[i].update();
    }
    for(i = 0; i < nrCars/4;i++){
      T[i].show();
      T[i].update();
    }
}
