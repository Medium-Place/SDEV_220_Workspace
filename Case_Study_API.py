# Attempting to create this but it's bs 
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Create the book data for three books 
books = [
    {
        "book_id": 1,
        "book_name": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Scribner"
    },
    {
        "book_id": 2,
        "book_name": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publisher": "J.B. Lippincott & Co."
    },
    {
        "book_id": 3,
        "book_name": "1984",
        "author": "George Orwell",
        "publisher": "Secker & Warburg"
    }
]

# Route to get all books 
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route to get a specific book by its ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    # Find the book with the given ID
    book = next((book for book in books if book["book_id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Route to add a new book 
@app.route('/books', methods=['POST'])
def add_book():
    # Create a new book with the data 
    book = {
        'id': books[-1]['id'] + 1,
        'book_name': request.json['book_name'],
        'author': request.json['author'],
        'publisher': request.json['publisher']
    }
    books.append(book)
    return jsonify(book)

# Route to update an existing book through its ID
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    # Find the book to update
    book = [book for book in books if book['id'] == id]
    # Update the specified fields in the request
    book[0]['book_name'] = request.json.get('book_name', book[0]['book_name'])
    book[0]['author'] = request.json.get('author', book[0]['author'])
    book[0]['publisher'] = request.json.get('publisher', book[0]['publisher'])
    return jsonify(book[0])

# Route to delete a book by its ID
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    # Find the book to delete
    book = [book for book in books if book['id'] == id]
    books.remove(book[0])
    return jsonify({'result': 'Book deleted'})

# Run the Flask application in debug mode 
if __name__ == '__main__':
    app.run(debug=True)
