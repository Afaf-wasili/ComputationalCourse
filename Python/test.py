# Open the file for reading
infile = open('oceans.txt', 'r')

# Move the file pointer to the specific position (binary index)
infile.seek(10)  # Move to the 11th character (index 10), for example

# Read until the next space to get the whole word
data = infile.read().split()[0]  # Split by spaces and take the first word
print(data)

# Close the file
infile.close()
