import requests
import random

def get_random_book():
    # Get total number of books
    base_url = "https://gutendex.com/books"
    response = requests.get(base_url)
    data = response.json()
    total_number_of_books = data['count']

    # How many book per page
    books_per_page=len(data['results'])

    # Number of pages
    number_of_pages=int(data['count']/books_per_page)
    
    # Generate random int between 1 and the number of pages
    page_number = random.randint(1, number_of_pages)
    #print(page_number)


    # Get data for the page
    page_response = requests.get(f"{base_url}?page={page_number}")
    page_data = page_response.json()
    books = page_data["results"]
    
    # Select a random book from the random page
    random_book = random.choice(books)
    title = random_book['title']
    for author in random_book['authors']:
        print (f"The random book of the day is '{title}' written by {author['name']} ")
    

# === Run the script ===
if __name__ == "__main__":
    get_random_book()

