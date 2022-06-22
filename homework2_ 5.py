rating = [9, 8, 6, 4, 2, 2, 1]

while True:
    el_of_rating = input('Enter any element of my rating (it must be any natural number)\n')
    if el_of_rating.isdigit():
        rating.append(int(el_of_rating))
        rating.sort(reverse=True)
        print(rating)
    elif el_of_rating == 'q':
        break