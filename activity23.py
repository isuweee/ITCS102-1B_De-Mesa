# LIST by De Mesa, Adrian

BFF = ["Jana", "Jhaztine", "Afuang", "Roshly", "JP", "Denver", "Sandra", "Sam"]
#        0       1        2       3      4    5       6      7

print(f'FIRST LIST:\n{BFF}\n{BFF[1]}\n{BFF[3:7]}\n')
#       All      2nd      3rd to 7th 

BFF.append("Perez") # Adding an item ;D
print(f'ADDED PEREZ:\n{BFF}\n')

BFF.insert(2, 'Teki') # Inserting an item in between the other items :D
print(f'INSERT TEKI IN BETWEEN:\n{BFF}\n')

BFF.pop() # Removing the last muehehe ;D
print(f'REMOVE LAST ITEM\n{BFF}\n')
# You can use BFF.remove('name') rin if gusto mo specific

print(f'COUNTING ITEMS:\n{len(BFF)}') # Counting the number of items ;D
# BFF.len() would also work if ayaw mo mag print
