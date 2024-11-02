
/*
void Methods(){
  std::vector<std::string> t = {"d", "c", "e" };
  std::vector<std::string> y {"m", "n"};
  t.push_back(y[1]); //adding a new element to the y
   for(const auto& e : t){
   std:cout<< e <<std::endl;
   }

}

*/

/*
void Methods(){ //using continue to remove 
  std::vector<std::string> t = {"a", "b", "c"};
  
    for(const auto& e : t){
  if( e  == "b"){ //how to remove an element from the array
    continue;
  }
   std:cout<< e <<std::endl;
    }
}
                          
*/


void Methods(){//using erase

  std::vector<std::string> t = {"a", "b", "c"}; 
  //t.erase(std::remove(t.begin(), t.end(), "b"));  //how to remove an element from the array  
  std::remove(t.begin(), t.end(), "b"); //how to remove an element from the array  
   for(const auto& e : t){

    	std:cout<< e <<std::endl;
     }
}

