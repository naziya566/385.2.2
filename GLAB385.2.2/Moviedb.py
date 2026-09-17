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
        # 9/16/2026 wednesday
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

# Edit a movie

# Delete a movie

# View all movies
def show_all():
    print('⭐️ All movies in Database ⭐️')
    print('===============')
    for movie in movie_db:
        print(f"Movie: {movie}")
        for key, value in movie_db[movie].items():
            print(f"{key}: {value}")
        print('===============')

# Search Movies

# Save and load movie from a file

# Error handling

# Data validation

# We have to find a way, to repeatly ask the user what action they want to take
while True:
    print('==== 🎬 Movie Database MGMT System 🎬 ====')
    print('1. Exit')
    print('2. Add Movie')
    print('3. Show All Movies')

    choice = input('What do you want to do? ')

    if choice == '1':
        print('👋 Goodbye. Comeback soon!')
        break
    elif choice == '2':
        add_movie()
    elif choice == '3':
        show_all()
    else:
        print('❌ Invalid Option. Please try again.')
     # Second code with editional features
     # We have to find a way, to repeatly ask the user what action they want to take
while True:
    print('==== 🎬 Movie Database MGMT System 🎬 ====')
    print('1. Exit')
    print('2. Add Movie')
    print('3. Show All Movies')
    print('4. Edit Existing Movie')
    print('5. Delete a Movie')
    print('6. Search for a Movie')
    print('7. Save data to a file')
    print('8. Load data from a file')

    choice = input('What do you want to do? ')

    if choice == '1':
        print('👋 Goodbye. Comeback soon!')
        break
    elif choice == '2':
        add_movie()
    elif choice == '3':
        show_all()
    elif choice == '4':
        print('Edit Movie')
    elif choice == '5':
        print('Deleting a movie')
    elif choice == '6':
        print('Searching for movie')
    elif choice == '7':
        print('Saving data to file')
    elif choice == '8':
        print('Loading data from file')
    else:
        print('❌ Invalid Option. Please try again.')

    # practice 9/16/2026 wednesday
    # Edit a movie

def delete_movie():
    # Ask user what movie to delete
    title = input('Enter the movie title you want to delete: ')

    try:
        # find movie to delete
        if title not in movie_db:
            raise KeyError(f'{title} not found in database.')

        # Confirm deletion
        confirm = input(f'Are you sure you want to delete {title}? (y/n): ')
        if confirm.lower() == 'y':
            del movie_db[title]
            print(f'✅ {title} has been deleted.')
        else:
            print('❌ Deletion cancelled.')
    except Exception as e:
        print(f'❌ Error: {e}')
        if title not in movie_db:
            # if cant find movie keyerror
            raise KeyError(f'{title} not found in database.')

        # Show current info
        print(f'Current information for {title}')
        print(movie_db[title])

        # Collect updated info from user
        year = input('Enter the movie year (or press Enter to keep current value(s)): ')
        genre = input('Enter the movie genre (or press Enter to keep current value(s)): ')
        director = input('Enter the movie director (or press Enter to keep current value(s)): ')
        actors = input('Enter the name of actors(comma separated) (or press Enter to keep current value(s)): ')

        # Update with new information
        # Can other datatype than booleans evaluate to true or false
        if year:
            movie_db[title]['year'] = year
        if genre:
            movie_db[title]['genre'] = genre
        if director:
            movie_db[title]['director'] = director
        if actors:
            movie_db[title]['actors'] = actors.split(",")

        print(f'✅ {title} has been updated.')
    except Exception as e:
        print(f'❌ Error: {e}')