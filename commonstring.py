
strs = ['flower', 'flow', 'flight']

# Initialize the prefix to the first string
pref = strs[0]

# Get the length of the prefix
preflen = len(pref)

# Iterate through the remaining strings
for s in strs[1:]:
    # Adjust the prefix length until it matches the start of the current string
    while pref != s[0:preflen]:
        preflen -= 1
        pref = pref[0:preflen]
   
# Print the final prefix
print(pref)
