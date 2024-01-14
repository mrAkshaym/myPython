
def age_in_decades():
    age = int(input("Add your age in years \n"))
    decades = age//10
    years = age %10
    print("you are", decades, "decades old and", years, "years old")


if __name__ == "__main__":
    age_in_decades()
    