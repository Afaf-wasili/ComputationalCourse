
/*
void Functions(){
  double principle= 1200;
  double rate= 8;
  double time=1;   
  double si;
  
 si = (principle * rate * time) / 100;
  std::cout<< "result si= " << si <<std::endl;
}
*/



void Function(double principle, double rate, double time){
 double  si = (principle * rate * time) / 100;
  std::cout<< "result si= " << si <<std::endl;
}

int Functions(){
  Function(1200,8,1);
   return 0;
    }



/*
double Function(double principle, double rate, double time){

  return (principle * rate * time) / 100; 
  //  std::cout<< " result of si = " << si <<std::endl;
}

int Functions(){
   Function(1200, 8, 1);
   double result = Function(1200, 8, 1);   
   std::cout << " result = " << result <<std::endl;  
   return 0;
}

*/
