print("*-----welcome-----*")
print("Choose: [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")
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
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
            else:
                print("Please enter an integer greater than or equal to 1.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def input_something(prompt):
     while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty.")

while choice != "q":
    choice = input_something("enter your choice: ").lower()
    # to add the new movie
    if choice == "a":
        new_movie_detail={ "name": "", "year": 0, "duration": 0, "genres":""  }
        new_movie_detail["name"] = input_something("enter the movie name: ")
        new_movie_detail["year"] = input_int("enter the released year of the movie: ")
        new_movie_detail["duration"] = input_int("Enter the duration of the movie: ")
        genres = input_something("enter the genres os the movie: ")
        genres = [genre.strip() for genre in genres_input.split(",") if genre.strip()]

        while len(genres) == 0:
            genres_input = input_something(
                "Enter at least one genre: "
            )
            genres = [genre.strip() for genre in genres_input.split(",") if genre.strip()]
        new_movie_detail["genres"]= genres


        movie_details.append(new_movie_detail)
    # to print movie name 
    elif choice == "l":
        for i in range(len(movie_details)):
            movie_name = movie_details[i]["name"]
            print(f"{i+1}. {movie_name}")
    # to search the movie
    elif choice == "s":
        movie = input_something("enter the movie name you want to search: ")
        for i in range(len(movie_details)):
            if movie == movie_details[i]["name"]:
                print("Movie is found. here are the details:")
                print(movie_details[i])
            else:
                print("ERROR!!!you enter wrong name or the movie is not present!!!")
    
    elif choice =="v":
        movie = input_something("enter the movie name you want to search: ")
        for i in range(len(movie_details)):
            if movie == movie_details[i]["name"]:
                print("here are the details: ")
                print(movie_details[i])
            else:
                print("ERROR!!!you enter wrong name or the movie is not present!!!")
    elif choice == "d":
        movie_details.pop()