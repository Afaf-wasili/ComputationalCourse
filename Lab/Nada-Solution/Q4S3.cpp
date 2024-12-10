void Q4S3(){
  //Question 1: define the varaible i to be integer
  
  // for (int i = 2; i < 8; ++i){
  for (int i = 2; i < 8; ++i){
  // Question 2:  Modify this function to stop the loop entirely when `i` equals 6. 
      if ( i % 2 == 0){
            continue;
        }

        // Question 3: Print values of `i`: 
      std::cout<< i << std::endl;
    }

}
/*
  // Question 3: Replace `continue` with `break`. How does this change the behavior of the loop? 
for (int i = 2; i < 8; ++i){
   if ( i % 2 == 1){                                                         
            break;                                                           
        }
   std::cout<< i << std::endl;
 }}
*/
