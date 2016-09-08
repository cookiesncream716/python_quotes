from system.core.model import Model
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    def create(self, info):
        # print "MMMMOOOODDDDEEELLLL"
        # print info['name']
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        if not info['name']:
            errors.append('Name cannot be blank')
        elif len(info['name']) < 2:
            errors.append('Name must be at least 2 characters long')
        if not info['alias']:
            errors.append('Alias cannot be blank')
        elif len(info['alias']) < 2:
            errors.append('Alias must be at least 2 characters long')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append("Email format must be valid")
        if len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['confirm_password']:
            errors.append('Password and Password Confirmation must match')
            
        if errors:
            # print '+++++++++++++++++'
            # print errors
            return {'status': False, 'errors': errors}
        else:
            password = info['password']
            hashed_password = self.bcrypt.generate_password_hash(password)
            create_query = 'INSERT INTO users (name, alias, email, password, birthday, created_at, updated_at) VALUES (:name, :alias, :email, :password, :birthday, now(), now())'
            create_data = {'name': info['name'], 'alias': info['alias'], 'email': info['email'], 'password': hashed_password, 'birthday': info['birthday']}
            # print '****************************'
            # print create_data
            self.db.query_db(create_query, create_data)
            # print "SSSSSSSAAAAAAAVVVVVVEEEEEEDDDDDD"
            user_query = 'SELECT * FROM users ORDER BY id DESC LIMIT 1'
            user = self.db.query_db(user_query)
            # print user[0]
            return {'status': True, 'user': user[0]}
    def login(self, data):
        password = data['password']
        login_query = 'SELECT * FROM users WHERE email= :email LIMIT 1'
        login_data = {'email': data['email']}
        user = self.db.query_db(login_query, login_data)
        # print '##############################################'
        # print user
        if user:
            if self.bcrypt.check_password_hash(user[0]['password'], password):
                return user[0]
        return False 
