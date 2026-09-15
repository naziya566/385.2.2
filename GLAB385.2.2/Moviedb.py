#print('Hello')
# Movie DB Dictionary Project

# Movie Database
movie_db = {}

# Add a movie
def add_movie():
    # Got data from user and saved into variables
    title = input('Enter the movie title: ')
    year = input('Enter the movie year: ')
    genre = input('Enter the movie genre: ')
    director = input('Enter the movie director: ')
    actors = input('Enter the name of actors(comma separated): ')

    # Used data to create a movie in the database
    movie_db[title] = {
        'year': year,
        'genre': genre,
        'director': director,
        'actors': actors.split(",")
    }

    print(f'🎉 Success: {title} added!' )
#movie database
# Add a movie
# Edit a movie
# Delete a movie
# view a movie
# Search a movie
# save and load a movie
# Error handling 
# data validation a movie
while True:
    print('====Movie Database MGMT System===')
    print('1. Exit') 
    print('2. Add a movie')
    choice=input('What do I want to do?')
    
    if choice == '1':
        print('Goodbye! Come Back Soon!')
        break
    elif choice == '2':
        add_movie()       
    else:
        print('❌ Invalid Option. Please try again.')