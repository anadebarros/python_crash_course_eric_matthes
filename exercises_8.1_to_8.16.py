# 8.1
def display_message():
    print("I'm learning python")


display_message()

# 8.2


def favorite_book(book):
    print(f"One of my favorite books is {book.title()}")


favorite_book("perfume")

# 8.3


def make_shirt(size, message):
    print(f"This shirt is size {size} and has '{message}' printed on it.")


make_shirt("M", "yo yo yo what??")
make_shirt(size="M", message="what's up")

# 8.4


def make_shirt(size="L", message="I love python"):
    print(f"This shirt is size {size} and has '{message}' printed on it.")


make_shirt()
make_shirt("M")
make_shirt(message="whatevs")

# 8.5


def describe_city(city, country="Portugal"):
    print(f"{city.title()} is in {country}")


describe_city("lisbon")
describe_city("porto")
describe_city("tokyo")

# 8.6


def city_country(city, country):
    city_country = city.title() + ", " + country.title()
    return city_country


print(city_country("santiago", "chile"))
print(city_country("lisboa", "portugal"))

# 8.7


def make_album(artist, title):
    album = {'artist': artist, 'album_title': title}
    return album


print(make_album("prince", "purple rain"))


def make_album(artist, title, tracks=""):
    album = {'artist': artist, 'album_title': title}
    if tracks:
        album['tracks'] = tracks
    return album


print(make_album("alanis", "jagged little pill", 10))

# 8.8
while True:
    print("Please enter information about your favorite album.")
    print("(Press 'q' to quit at any time.)")
    album_artist = input("Please enter an artist's name: ")
    if album_artist == "q".lower():
        break
    album_title = input("Please enter the album title: ")
    if album_title == "q".lower():
        break
    album_tracks = input("Please enter the number of tracks: ")
    if album_tracks == "q".lower():
        break
    print(make_album(album_artist, album_title, album_tracks))
