/*
void Looping(){
  std::vector<int> n = {1,2,3,4};
  int sum = 0;
  //loop
  int i = 0;
  while ( i < n.size()){
    sum += n[i];
    i += 1;
  }
  std::cout << "The total is " << sum << std::endl;

}
*/
/*
void Looping(){
  std::vector<int> n = {2,3,4,5};
        
  for (int i : n){
  std:cout<< i<< std::endl;}
    
}
*/

void Looping(){
  std::vector<int> n = {1,2,3,4,5,6,7,8};
  int sum_even=0;
  int sum_odd=0;
  int count_even=0;
  int count_odd=0;
    for (int i : n){
      if (i % 2 == 0){
	sum_even +=i;
	count_even +=1;}
      else{
	sum_odd +=i;
        count_odd +=1;}} 


       std::cout<<"the total number of even: "<<sum_even<<std::endl;
       std::cout<<"how many even numbers: "<<count_even<<std::endl;
       std::cout<<"the total number of odd : "<<sum_odd<<std::endl;
       std::cout<<"how many odd numbers: "<<count_odd<<std::endl;
    }

