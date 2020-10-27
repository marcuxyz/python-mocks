def filter_books_by_pages(books):
    return [book for book in books if book["pages"] > 300]
