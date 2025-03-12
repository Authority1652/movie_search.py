# importing requests after installing it
import requests

def movies(find_movie):

    api_key = "fa2434c1"
    find_movie = input("name_of_movie: ").title()
    base_url = f"http://www.omdbapi.com/?t={find_movie}&apikey={api_key}"


    response = requests.get(base_url)
    # print(response)
    if response.status_code == 200:
        data = response.json()
        # print(data)

        film = {
            "Title": data["Title"],
            "Year": data["Year"],
            "Genre": data["Genre"],
            "Director": data["Director"],
            "Writer": data["Writer"],
            "Actors": data["Actors"],
            "Plot": data["Plot"],
            "Awards": data["Awards"],
            "BoxOffice": data["BoxOffice"]
        }


        if film:
            print(f"The title of the film is: {film['Title']}")
            print(f"The year it was released was: {film['Year']}")
            print(f"The film genre is: {film['Genre']}")
            print(f"The movie director is: {film['Director']}")
            print(f"The Movie writer is: {film['Writer']}")
            print(f"The Movie cast are: {film['Actors']}")
            print(f"The Movie plot: {film['Plot']}")
            print(f"The Won awards are: {film['Awards']}")
            print(f"The BoxOffice Made: {film['BoxOffice']}")
        else:
            print("could  not find movie")



movies("search")
