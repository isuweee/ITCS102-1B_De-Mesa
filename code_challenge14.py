# Anime List Maker By De Mesa, Adrian ^^

list = []

print("====ANIME LIST MAKER====")
while True:
    anime = input("Enter Anime Title (Type 'exit' to stop): ")
    if anime.lower()== 'exit':
        print("===========END===========")
        break
    list.append(anime)

num = len(list)
print("Your Anime List Contains:")
for i in range(1,num+1,1):
    print(f'- {list[i-1]}')
print("Quite a taste you have there mate ;)")
