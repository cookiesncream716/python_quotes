from system.core.controller import *

class Quotes(Controller):
	def __init__(self, action):
		super(Quotes, self).__init__(action)
		self.load_model('Quote')
	def create(self, id):
		quote = {
			'quote': request.form['quote'],
			'author': request.form['author'],
			'user_id': id
		}
		# print 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
		# print quote
		quote_status = self.models['Quote'].create(quote)
		# print quote_status
		if quote_status['status'] == True:
			return redirect('/users/show')
		else:
			for error in quote_status['errors']:
				flash(error)
				return redirect('/users/show')