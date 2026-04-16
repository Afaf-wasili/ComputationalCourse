/*
for looping: read data from 0, ....
While looping: read the total of data
*/


/*
void Looping(){
  for(int i = 0; i < 11; i+=1){   //start, end, steps
    std::cout<< "i=" << i <<std::endl;
  }
}
*/


/*

void Looping(){
  std::vector<int> n = {0,1,2,3,4,5,6,7,8,9,10};

  for (int i: n){

 std::cout<< "i=" << i <<std::endl;
}}

*/


void Looping(){
    int sum_even = 0;
    int sum_odd = 0;
    int count_even = 0;
    int count_odd =0 ;
  for(int i =0; i<11; i+=1){
    if(i % 2 == 0){
      sum_even +=i;
      count_even +=1;}

    else if (i % 2 ==1){
      sum_odd +=i;
      count_odd +=1;
    }

  }
      std::cout<<" sum_even ="<<  sum_even<<std::endl;
      std::cout<< "count_even ="<< count_even<<std::endl;
      std::cout<< "sum_odd = "<<sum_odd<<std::endl; 
      std::cout<< "count_even =" <<count_even<<std::endl;
}


/*
void Looping(){ //while: count of data only
  std::vector<int> n = {2,3,4,5,6,7,8};
  int count;
  int i =0;
  while(i < n.size()){
    count += n[i];
      i += 1;
  }
  std::cout<<"i="<<i<<std::endl;
}
*/
