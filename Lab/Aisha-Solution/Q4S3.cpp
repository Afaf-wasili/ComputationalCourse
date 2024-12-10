
void Q4S3(){
  //Question 1: define the varaible i to be integer
  int i = 0;
  
    for (i = 2; i < 8; ++i){
  // Question 2:  Modify this function to stop the loop entirely when `i` equals 6. 
      if (i == 6){
            continue;
        }

        // Question 3: Print values of `i`:
      std::cout<<i<<std::endl ;
        
    }
}

/*
// Question 3: Replace `continue` with `break`. How does this change the behavior of the loop?the loop while stop at number 6 ans not continue 
void Q4S3(){
int i = 0;

    for (i = 2; i < 8; ++i){
  // Question 2:  Modify this function to stop the loop entirely when `i` equals 6.
      if (i == 6){
            break;
        }

        // Question 3: Print values of `i`:
      std::cout<<i<<std::endl ;

    }

}
*/
