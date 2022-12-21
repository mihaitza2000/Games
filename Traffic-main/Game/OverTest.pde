void OverTest(){
    float xcar = c.getData('x');
    float ycar = c.getData('y');
    float wcar = c.getData('w');
    float hcar = c.getData('h');
    for(i = 0; i < nrCars; i++){
      float xenemy = E[i].getData('x');
      float yenemy = E[i].getData('y');
      float wenemy = E[i].getData('w');
      float henemy = E[i].getData('h');
      float d = 2;
      if((xcar > xenemy+d && xcar < xenemy + wenemy-d  && ycar > yenemy+d && ycar < yenemy + henemy-d)||
        (xcar + wcar > xenemy+d && xcar + wcar < xenemy + wenemy-d && ycar > yenemy+d && ycar < yenemy + henemy-d)||
        (xcar > xenemy+d && xcar < xenemy + wenemy-d && ycar + hcar > yenemy+d  && ycar + hcar < yenemy + henemy-d)||
        (xcar +wcar > xenemy+d && xcar + wcar < xenemy + wenemy-d && ycar + hcar > yenemy+d && ycar + hcar < yenemy + henemy-d)){
           over = true; 
        }
     if((xenemy > xcar+d && xenemy < xcar + wcar-d  && yenemy > ycar+d && yenemy < ycar + hcar-d)||
        (xenemy + wenemy > xcar+d && xenemy + wenemy < xcar-d + wcar && yenemy > ycar+d && yenemy < ycar + hcar-d)||
        (xenemy > xcar+d && xenemy < xcar + wcar-d && yenemy + henemy > ycar+d  && yenemy + henemy < ycar + hcar-d)||
        (xenemy +wenemy > xcar+d && xenemy + wenemy < xcar + wcar-d && yenemy + henemy > ycar+d && yenemy + henemy < ycar + hcar-d)){
           over = true; 
        }
    }
}
