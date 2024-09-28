# Function to read data from a file
def read_from_file():
    with open("fruits.txt", 'r') as file:
        return [line.strip() for line in file]

# Read and print fruits from the file
for fruit in read_from_file():
    print(fruit)
