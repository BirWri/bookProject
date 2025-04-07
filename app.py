import requests

def get_random_book():
    # Step 1: Get total number of books
    base_url = "https://gutendex.com/books"
    response = requests.get(base_url)
    data = response.json()
    print(data['count'])

# === Run the script ===
if __name__ == "__main__":
    get_random_book()

