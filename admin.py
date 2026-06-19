print("*-----welcome-----*")
movie_details=[ { "name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },{ "name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action","Adventure", "Drama"] }, { "name": "Back to the Future", "year": 1985, "duration": 114,"genres": ["Adventure", "Comedy", "Sci-Fi"] } ]
choice = 0
print("1. To add a movie enter - a")
print("2. To see the list of the movie enter - l")
print("3. To search a movie in the list enter - s")
print("4. To view the details of movie enter - v")
print("5. To delete enter - d ")
print("6. To quit enter - q")
def input_int(prompt):
     while True:
            value = int(input(prompt))
            if value >= 1:
                return value
            else:
                print("Please enter an integer greater than or equal to 1.")
def input_something(prompt):
     while True:
        value = input(prompt).strip().title()
        if value:
            return value
        else:
            print("Input cannot be empty.")
def add():
    name=input_something("enter the movie name: ").title()
    year = input_int("enter the released year of the movie: ")
    duration = input_int("Enter the duration of the movie: ")
    genres = []
    for i in range(0,10):
        genres_input = input_something("enter one genres: ").title()
        genres_choice = input_something("do you want to enter more genres (yes/no): ").lower()
        if genres_choice is "yes":
            genres.append(genres_input)
            continue
        else:
            break
    movie_details.append({"name":name,"year":year, "duration":duration, "genres":genres } )

def list():
          for i,j in enumerate(movie_details):
            print(f"{i+1}. {j["name"]} - ({j["year"]}) ")
def search():
    movie = input_something("enter the movie name you want to search: ").lower()
    found = False
    for i in range(len(movie_details)):
        if movie in movie_details[i]["name"].lower():
            print("Movie is found. here are the details:")
            list()
            found = True
        elif not movie_details:
            print("No movie saved")
            found = True
    if not found:
         print("ERROR!!!you enter wrong name or the movie is not present!!!")
def view():
    if not movie_details:
        print("No movies saved")
        return
    list()
    index1 = input_int("Enter movie index number: ")
    if 1 <= index1 <= len(movie_details):
        movie = movie_details[index1 - 1]  
        print(f"Name: {movie['name']}")
        print(f"Year: {movie['year']}")
        print(f"Duration: {movie['duration']} minutes")
        print(f"Genres: {', '.join(movie['genres'])}")
    else:
        print("Invalid index number")
while True:
    print("Choose: [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")
    choice = input_something("enter your choice: ").lower()
    # to add the new movie
    if choice == "a":
        add()
    # to print movie name 
    elif choice == "l":
         list()
    # to search the movie
    elif choice == "s":
        search()
    elif choice =="v":
        view()
    elif choice == "d":
        list()
        index = input_int("Enter the index of the movie you want to delete: ")
        movie_details.pop(index - 1)
    elif choice == "q":
        print("good bye!!!!")
        break
    else:
        print("invalid choice")