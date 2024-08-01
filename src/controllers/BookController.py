from models.BookModel import BookModel


class BookController:

    def __init__(self):
        self.book_model = BookModel()

    def verify_data(self, book_id, title, author, category_id):
        try:
            book = self.book_model.verify_data(book_id, title, author, category_id)
            if book:
                return {'status_code': 200, 'response': 'Verify data', 'result': book}
            else:
                return {'status_code': 404, 'response': 'Don’t Verify data'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error verifying data: {e}'}

    def create_book(self, book_id, title, author, category_id, stock):
        try:
            self.book_model.create_book(book_id, title, author, category_id, stock)
            return {
                'result': f'{book_id, title, author, category_id, stock}'
            }
        except Exception as e:
            return {
                'status_code': 500,
                'response': f'Error when creating the book: {e}'
            }

