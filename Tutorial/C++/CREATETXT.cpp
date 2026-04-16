/*

//create txt file:

void  CREATETXT(){
  ofstream file("particles.txt");

  string particles[3] = {"electron","proton", "neutron"};

  for (int i = 0; i < 3; i++){
    file<< particles[i]<<endl;
  }

  file.close();

   std::cout<<"particles are written to file"<<std::endl;
    
}
*/


//read txt file

void CREATETXT(){
  ifstream file("particles.txt");
  string line;

   for (int i = 0; i < 3; i++){
     getline(file,line);
     std::cout <<line<<std::endl;
   }
   
 file.close();
}
