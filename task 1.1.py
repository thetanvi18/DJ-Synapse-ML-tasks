#Ref: w3schools, stackoverflow

#Task 1.1: Superhero Sorting Challenge

jumbled_superheroes = ['DocToR_sTRAngE', 'sPidERmaN', 'MoON_KnigHT', 'caPTAIN_aMERIca', 'hULK']

# Create empty lists to store indices and decoded names
indices = []
decoded_names = []

# Use a list comprehension to convert the names to lowercase
decoded_names = [x.lower().replace('_', ' ') for x in jumbled_superheroes]
decoded_names = [x.title() for x in decoded_names]
print(decoded_names)
# print the indices list
for x in decoded_names:
    indices.append(decoded_names.index(x))
print(indices)

decoded_names.sort(key=lambda x: len(x))

print("Phase 5 kickoff list:")

