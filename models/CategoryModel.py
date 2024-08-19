from config.Connection import Connection


class CategoryModel:

    def __init__(self):
        self.db = Connection()

    def verify_category(self, category_id, category_name):
        query = "SELECT * FROM categories WHERE category_id = %s AND category_name = %s"
        params = (category_id, category_name)
        try:
            return self.db.execute_query(query, params)
        except Exception as e:
            return f'Error verifying category: {e}'

    def create_category(self, category_id, category_name):
        query = "INSERT INTO categories(category_id, category_name) VALUES(%s, %s)"
        params = (category_id, category_name)
        try:
            return self.db.update_query(query, params)
        except Exception as e:
            return f'Error when creating the category: {e}'