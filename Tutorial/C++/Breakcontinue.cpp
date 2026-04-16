/*
Break = Exit the loop
Continue = Skip this turn only
for, if conditional statement, etc 
 */




/*
void Breakcontinue(){
  for (int i = 4; i < 8; ++i){
    if ( i== 7){
      break;
    }
  std::cout<<"result_i: "<<i<<std::endl;
  }
}
*/


/*
void Breakcontinue(){
  for (int i = 4; i < 8; ++i){
    if ( i== 4){
      continue;
    }
     std::cout<<"result_i: "<<i<<std::endl;
  }
}
*/



void Breakcontinue(){
  for (int i = 0; i < 10; ++i){
    if ( i % 2 == 1){
      continue;
    }
  std::cout<<"result_i: "<<i<<std::endl;
  }
}
