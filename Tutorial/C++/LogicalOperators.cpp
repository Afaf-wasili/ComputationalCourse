/*
void LogicalOperators(){

  int num = 8;
  int numb = num % 2;
  if (num >0 && numb == 0){
    std::cout<< "The number is positive and even "<< num <<std::endl; 
  } else {
    std::cout<< "The number is positive and odd "<< num <<std::endl;
  }

}
*/

void LogicalOperators(){
  int num = 17;
  if( num % 2 == 0 or  num % 2 == 1){
    std::cout<<"the number is odd" <<std::endl;
  }else{std::cout<<"otherwise" <<std::endl;} 
      

}
