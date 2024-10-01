# List of strings
data = ["apple", "banana", "cherry"]

# Function to save data to a file
def save_to_file(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

# Save data to fruits.txt
save_to_file(data, "fruits.txt")
print("Data has been saved to fruits.txt.")
