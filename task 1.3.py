#Atomic Codebreaker
encoded_lists = [[1,2,3,4,6],
                 [5,7,8,9,15],
                 [12,14,16,18],
                 [10,11,12,13,16,17,18,20]
                 ]
#code for explode_chains
for encoded_list in encoded_lists:
    exploded_list = []
    i = 0
result = explode_chains(encoded_lists)
print(result)
