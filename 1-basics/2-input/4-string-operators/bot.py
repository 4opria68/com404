# Read bot data
print("Please enter number of lives")
lives = int(input())

print("Please enter energy level")
energy = int(input())

print("Please enter shield level")
shield = int(input()) 

# Display bot data
print("Lives:", "♥" * lives)
print("Energy:", "♦" * energy)
print("Shield:", "♦" * shield)

# Ask user for eye character 
print("Please enter an eye character:")
eye = input() 

# Ask user for the length of the glasses
print("Please enter the length of the glasses:")
length = int(input())

# Display an ascii glasses
print()

print("#########" + (" " * length)  + "#########")
print("#   " + eye + "   #" + ("#" * length) + "#   " + eye + "   #")
print("#########" + (" " * length) + "#########")

print()