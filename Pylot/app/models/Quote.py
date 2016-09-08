from system.core.model import Model

class Quote(Model):
	def __init__(self):
		super(Quote, self).__init__()
	def create(self, info):
		errors = []
		if len(info['quote']) < 10:
			errors.append('Quote must be at least 10 characters')
		if len(info['author']) < 2:
			errors.append('Author must be at least 2 characters')
		if errors:
			return {'status': False, 'errors': errors}
		else:
			create_query = 'INSERT INTO quotes (quotes, author, user_id, created_at, updated_at) VALUES (:quotes, :author, :user_id, now(), now())'
			create_data = {'quotes': info['quote'], 'author': info['author'], 'user_id': info['user_id']}
			self.db.query_db(create_query, create_data)
			return {'status': True}