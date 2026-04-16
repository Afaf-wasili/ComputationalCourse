#include"Class.h"

// main function
void Class(){

  Rectangle rec(3.5,6.3); //rec: pointer
  std::cout<< "area:" << rec.get_area() <<std::endl;
  std::cout<<"perimeter:" << rec.get_perimeter() <<std::endl;
 }
