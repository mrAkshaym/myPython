acronym = {'LOL':"Laughing out loud", 'IDK' :"I don't know"}

#print(acronym)

#print(acronym['LOL'])

#print(acronym['BFF']) #output KeyError: 'BFF'

#print(acronym.get('BFF')) #output None
#print(acronym.get('BFF', "Not in dictionary")) #output Not in dictionary

#print(acronym.keys()) #output dict_keys(['LOL', 'IDK'])

# Commenting the function body for clarity

#movie = {'Baazigar': '08:00', 'Tom': '13:00', 'Derry Girls': '09:30', 'Breaking bad': '14:00'}
#print(movie)
#print(movie.items())
#print(sorted(movie.items(), key=lambda x: x[0]))
# output : [('Baazigar', '08:00'), ('Breaking bad', '14:00'), ('Derry Girls', '09:30'), ('Tom', '13:00')]

#print(sorted(movie.items(), key=lambda x: x[1]))
#output: [('Baazigar', '08:00'), ('Derry Girls', '09:30'), ('Tom', '13:00'), ('Breaking bad', '14:00')]

#
'''
def movie_schedule():
    movie_dict={}
    addMoreMovies = True
    while addMoreMovies:
        movie = input("Enter movie: ")
        time = input("Enter time: ")
        movie_dict[movie] = time
        addMoreMovies = input("Add more movies? (y/n) ") == "y"

    print("Movies by time:", sorted(movie_dict.items(), key=lambda x: x[1]))
'''

contacts = {
    'Shubham': {'phone': '1234', 'email': 'shubh@example.com'},
    'Rahul': {'phone': '5678', 'email': 'rahul@example.com'},
    'Vikram': {'phone': '9999', 'email': 'vikram@example.com'}
}

for student in contacts:
    #print("emails ",contacts[student].get('email')); #works as expected
    print("emails ",contacts[student]['email']); #works as expected



        
#if __name__ == "__main__":
#   movie_schedule()