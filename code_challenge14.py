# Anime List Maker By De Mesa, Adrian ^^

list = []

while True:
    anime = input("Enter Anime Title (Type 'exit' to stop): ")
    if anime.lower()== 'exit':
        break
    list.append(anime)

num = len(list)
print("Your list contains:")
for i in range(1,num+1,1):
    print(f'{i}. {list[i-1]}')
