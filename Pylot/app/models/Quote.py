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
			create_data = {
				'quotes': info['quote'],
				'author': info['author'],
				'user_id': info['user_id']
				}
			self.db.query_db(create_query, create_data)
			return {'status': True}
	def show(self, id):
		show_query = 'SELECT quotes.quotes, quotes.author, quotes.user_id, quotes.id AS quote_id, users.name, users.id FROM quotes JOIN users on quotes.user_id = users.id'
		# show_query = 'SELECT favorites.user_id AS no_show, quotes.id AS quote_id, quotes.quotes, quotes.author, quotes.user_id, users.id, users.name FROM users JOIN quotes ON users.id = quotes.user_id LEFT JOIN favorites ON quotes.user_id = favorites.user_id WHERE favorites.user_id != :id OR favorites.user_id is NULL'
		# show_data = { 'id': id}
		return self.db.query_db(show_query)
	def show_favs(self, id):
		print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
		print id
		query = 'SELECT favorites.user_id AS fav_user_id, quotes.id AS quote_id, quotes.quotes, quotes.author, quotes.user_id, users.id, users.name, favorites.id AS fav_id, favorites.quote_id AS fav_quote_id FROM users JOIN quotes ON users.id = quotes.user_id JOIN favorites ON quotes.id = favorites.quote_id WHERE favorites.user_id = :id'
		data = { 'id': id}
		return self.db.query_db(query, data)
	def add_fav(self, info):
		print 'AAAAAAAAAAAAADDDDDDDDDDDD FFFFFFFFAAAAAVVVVVVV'
		print info
		fav_query = 'INSERT INTO favorites (user_id, quote_id, created_at, updated_at) VALUES (:user_id, :quote_id, now(), now())'
		fav_data = {
			'user_id': info['user_id'], 
			'quote_id': info['quote_id']
			}
		return self.db.query_db(fav_query, fav_data)
	def delete_fav(self, id):
		del_query = 'DELETE FROM favorites WHERE id = :id'
		del_data = { 'id': id}
		return self.db.query_db(del_query, del_data)	
