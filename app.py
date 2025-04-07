import requests
import random

def get_random_book():
    # Get total number of books
    base_url = "https://gutendex.com/books"
    response = requests.get(base_url)
    data = response.json()
    print(data['count'])
    
    # Generate random int between 1 and the number of books
    book_id = random.randint(1, data['count'])
    print(book_id)

# === Run the script ===
if __name__ == "__main__":
    get_random_book()

