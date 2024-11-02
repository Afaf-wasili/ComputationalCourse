class Rectangle{

private:
  double length  ;
  double width ;

public:
  Rectangle(double x, double y) : length(x), width(y) {}
  
  double get_area(){
    return length * width;
  }
  double get_perimeter(){
    return  get_area()* 2;  //2 * (length * width);
  }

  
}; 
 
int Class(){ // Class word is your choose
   Rectangle rec(23,24);

   std::cout<< "result= "<< rec.get_area() <<std::endl;
   std::cout<< "result= "<< rec.get_perimeter() <<std::endl;
   return 0;
    }
  

