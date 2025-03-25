# Problem 1: New Horizons
# Step 1: Copy the following code into your IDE.

# Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. Store the instance in a variable named apollo.

# The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    # def set_catchphrase(self, new_catchphrase):
    #     # Check if the catchphrase is less than 20 characters and contains only letters and spaces
    #     if len(new_catchphrase) < 20 and re.fullmatch(r"[A-Za-z ]+", new_catchphrase):
    #         self.catchphrase = new_catchphrase
    #         print("Catchphrase Updated!")
    #     else:
    #         print("Invalid catchphrase")
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"


apollo = Villager( "Apollo", "Eagle", "pah")
bones = Villager("Bones", "Dog", "yip yip")
# Instantiate your villager here
# Example Usage:

# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 
bones.catchphrase = "ruff it up"

print(bones.greet_player("Samia"))
print(bones.name)
print(bones.species)  
print(bones.catchphrase) 
print(bones.furniture) 
print(bones.greet_player("Sachin"))
# Example Output:

# Apollo
# Eagle
# pah
# []