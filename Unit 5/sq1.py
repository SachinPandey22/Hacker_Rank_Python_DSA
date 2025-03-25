# Problem 1: New Horizons
# Step 1: Copy the following code into your IDE.

# Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. Store the instance in a variable named apollo.

# The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".
class Villager:
    
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    def set_catchphrase(self, new_catchphrase):
        # Check if the catchphrase is less than 20 characters and contains only letters and spaces
        if len(new_catchphrase) < 20 and new_catchphrase.replace(" ", "").isalpha():
            self.catchphrase = new_catchphrase
            print("Catchphrase Updated!")
        else:
            print("Invalid catchphrase")
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    def add_item(self, item_name):
        lst = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in lst:
            self.furniture.append(item_name)
    def print_inventory(self):
        inventory_dic = {}
        if not self.furniture:
            print("Inventory Empty")
            return
        for inv in self.furniture:
            if inv in inventory_dic:
                inventory_dic[inv] += 1
            else:
                inventory_dic[inv] = 1
        inv = ",".join(f"{items}: {Count}" for items, Count in inventory_dic.items())
        print(inv)
def of_personality_type(townies, personality_type):
    for nam in townies:
        result = []
        for town in townies:
            if personality_type == town.personality:
                result.append(town.name)
        return result
            
        
# apollo = Villager( "Apollo", "Eagle", "pah")
# bones = Villager("Bones", "Dog", "yip yip")
# Instantiate your villager here
# Example Usage:

# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 
# bones.catchphrase = "ruff it up"
# alice = Villager("Alice", "Koala", "guvnor")

# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)

# print(bones.greet_player("Samia"))
# print(bones.name)
# print(bones.species)  
# print(bones.catchphrase) 
# print(bones.furniture) 
# print(bones.greet_player("Sachin"))

# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)

# alice = Villager("Alice", "Koala", "guvnor")

# alice.print_inventory()

# alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
# alice.print_inventory()

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))