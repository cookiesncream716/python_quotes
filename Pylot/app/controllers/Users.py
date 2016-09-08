
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
    def index(self):
        # name = self.models['User'].test()
        # print'1111111111111111111111111111'
        # print name[0]['name']
        return self.load_view('index.html')
    def create(self):
        # print '************************************'
        new_info = {
            'name': request.form['name'],
            'alias': request.form['alias'],
            'email': request.form['new_email'],
            'password': request.form['new_password'],
            'confirm_password': request.form['confirm_password'],
            'birthday': request.form['birthday']
        }
        # print '99999999999999999999999999999999999'
        # print new_info
        create_status = self.models['User'].create(new_info)
        # print 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS'
        # print create_status
        if create_status['status'] == True:
            session['name'] = create_status['user']['name']
            session['id'] = create_status['user']['id']
            return redirect('/users/show')
        else:
            for error in create_status['errors']:
                flash(error)
            return redirect('/')    
    def login(self):
        data = {
            'email': request.form['email'],
            'password': request.form['password']
        }
        login_status = self.models['User'].login(data)
        # print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
        # print login_status
        if login_status == False:
            # print 'FFFFFFFAAAAAAAAALLLLLLLSSSSSSSEEEEEEE'
            flash('Error loggin in')
            return redirect('/')
        else:
            session['name'] = login_status['name']
            session['id'] = login_status['id']
            return redirect('/users/show')
    def show(self):
        return self.load_view('quotes.html', name = session['name'], id = session['id'])
    def logout(self):
        session.clear
        return redirect('/')