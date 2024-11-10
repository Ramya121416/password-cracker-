#step-1 :
      # **md-5 algo**
import hashlib
inputstring = "ramya"

output = hashlib.md5(inputstring.encode())

print("Hash of the input string:")
print(output.hexdigest())
#output : 69f8ccc05b12ef0f8c94d2d0087124bd (hashcode)
#_____________________________________________________________________________________________________________________________________________________________________

#step-2:
  #crack an MD5 password by brute force
  # we should know the size of password which we given
  # as a brute force approach it takes longer time  to iterate all the possible casses to match the given input.
import hashlib
import itertools

# Step 1: Define the character set and target hash
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
target_hashes = ["69f8ccc05b12ef0f8c94d2d0087124bd"]

# Step 2: Iterate through all combinations of 5-character passwords(as ramya is 5 letters)
for combination in itertools.product(characters, repeat=5):
    # Step 3: Join the tuple into a string
    password = ''.join(combination)
    
    # Step 4: Hash the password using MD5
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    
    # Step 5: Check if the generated hash matches any target hash
    if hashed_password in target_hashes:
        print(f"Password found: {password} -> {hashed_password}")
        break

        
