import requests
import random

def get_random_book():
    # Get total number of books
    base_url = "https://gutendex.com/books"
    response = requests.get(base_url)
    data = response.json()
    print(data['count'])

    # How many book per page
    books_per_page=len(data['results'])
    print(books_per_page)
    
    # Generate random int between 1 and the number of books
    #book_id = random.randint(1, data['count'])
    test_book_id = 26184
    print(test_book_id)

    # Find the random book from json
    for title in data['results']:
        if test_book_id == title['id']:
            for author in title['authors']:
                print (f"The random book of the day is '{title['title']}' written by the {author['name']}")


# === Run the script ===
if __name__ == "__main__":
    get_random_book()

