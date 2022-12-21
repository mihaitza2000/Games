void GenerateCars(){
     if(i % 5 == 0){
        e = new enemy(enemyImgAngry.width, enemyImgAngry.height,i,'a');
        E[i] = e;
     }
     else{
       if(i == 11 || i == 19){
         e = new enemy(enemyImgPolice.width, enemyImgPolice.height,i,'p');
         E[i] = e;
       }
       else if(i == 14){
         e = new enemy(enemyImgAmbulance.width, enemyImgAmbulance.height,i,'e');
         E[i] = e;
       }
       else{
         randEnemy = floor(random(1,3));
         if(randEnemy == 1){
           e = new enemy(enemyImgRed.width, enemyImgRed.height,i,'r');
           E[i] = e;
         }
         else if(randEnemy == 2){
           e = new enemy(enemyImgYellow.width, enemyImgYellow.height,i,'y');
           E[i] = e;
         }
       }
     }
}
