movie = "John Wick"

# index
# print(movie[0])
# print(movie[-1])

# only peak
# print(movie[8] + movie[9] + movie[10] + movie[11])

# slice operator(:)
# end index not includes
# print(movie[-4:])
# print(movie[5:9])
# print(movie[5:])

# print(movie[2:9])
# print(movie[2:9:1])
# print(movie[-4:-1:1])

fav_hero = "The Hulk"

# hero = fav_hero.replace("H", "h")

# print(fav_hero.replace("H", "h"))
# print(fav_hero)
# print(fav_hero.replace("H", "h"))
print(fav_hero[:4] + "h" + fav_hero[5:])
print("💕" * 20)

catchphrase = "I am Groot"

print(catchphrase.swapcase())

message = "     with great power comes great responsibility   "
# msg = message.strip()
print(message.strip())

coded_message = "******SO*S*****"
print(coded_message.strip("*"))

quote = "Dreams are not things that you see in your sleep, Dreams are things that keep you awake"
print(quote.replace("Dreams", "🛌💭", 1))

print(quote.find("you"))
