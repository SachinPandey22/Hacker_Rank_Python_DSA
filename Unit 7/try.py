def recursive_crash():
    print("I will run forever")
    recursive_crash() 
    
recursive_crash()