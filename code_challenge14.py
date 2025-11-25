# Anime List Maker By De Mesa, Adrian ^^

lists = []

print("===ANIME LIST MAKER===")
while True:
    anime = input("Enter Anime Title (Type 'exit' to stop): ")
    if anime.lower() == 'exit':
        print("========END==========")
        break
    lists.append(anime)

num = len(lists)

print("Your Anime List Contains:")
for i in range(1, num + 1, 1):
    print(f'- {lists[i-1]}')

print("Quite a taste you have there mate ;)")
