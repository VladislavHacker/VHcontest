from app import db
import json


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    patronymic = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(200), unique=False, nullable=False)
    password = db.Column(db.String(300), unique=False, nullable=False)
    salt = db.Column(db.String(10), unique=False, nullable=False)

    def get_dict(self):
        res = {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'patronymic': self.patronymic,
            'email': self.email,
            'password': self.password,
            'salt': self.salt
        }
        return res

    def get_public(self):
        res = {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'patronymic': self.patronymic,
            'email': self.email
        }
        return json.dumps(res)

    def __repr__(self):
        return json.dumps(self.get_dict())

    def __str__(self):
        return json.dumps(self.get_dict())


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(300), unique=False)
    condition = db.Column(db.Text, unique=False)
    input_example = db.Column(db.Text, unique=False)
    output_example = db.Column(db.Text, unique=False)
    input_description = db.Column(db.Text, unique=False)
    output_description = db.Column(db.Text, unique=False)
    time_limit = db.Column(db.Integer, unique=False)
    memory_limit = db.Column(db.Integer, unique=False)
    process_limit = db.Column(db.Integer, unique=False)
    test_generator = db.Column(db.Text, unique=False)
    test_generator_language = db.Column(db.String(20), unique=False)
    checker = db.Column(db.Text, unique=False)
    checker_language = db.Column(db.String(20), unique=False)
    author_solution = db.Column(db.Text, unique=False)
    author_solution_language = db.Column(db.String(20), unique=False)

    def get_dict(self):
        res = {
            'id': self.id,
            'name': self.name,
            'condition': self.condition,
            'input_example': self.input_example,
            'output_example': self.output_example,
            'input_description': self.input_description,
            'output_description': self.output_description,
            'time_limit': self.time_limit,
            'memory_limit': self.memory_limit
        }
        return res

    def __repr__(self):
        return json.dumps(self.get_dict())

    def __str__(self):
        return json.dumps(self.get_dict())


class Test(db.Model):
    __tablename__ = 'tests'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, unique=False, nullable=False)
    input = db.Column(db.Text, unique=False)
    output = db.Column(db.Text, unique=False)

    def __repr__(self):
        pass


class TestResult(db.Model):
    __tablename__ = 'tests_result'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sending_id = db.Column(db.Integer, unique=False)
    test_id = db.Column(db.Integer, unique=False)
    time = db.Column(db.Integer, unique=False)
    memory = db.Column(db.Integer, unique=False)
    result = db.Column(db.String(20), unique=False)

    def get_dict(self):
        res = {
            'id': self.id,
            'sending_id': self.sending_id,
            'test_id': self.test_id,
            'time': self.time,
            'memory': self.memory,
            'result': self.result
        }
        return res

    def __repr__(self):
        return json.dumps(self.get_dict())

    def __str__(self):
        return json.dumps(self.get_dict())


class Sending(db.Model):
    __tablename__ = 'sendings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Integer, unique=False)
    user_id = db.Column(db.Integer, unique=False)
    task_id = db.Column(db.Integer, unique=False)
    code = db.Column(db.Text, unique=False)
    language = db.Column(db.String(100), unique=False)
    result = db.Column(db.String(20), unique=False)
    time = db.Column(db.Integer, unique=False)
    memory = db.Column(db.Integer, unique=False)

    def __repr__(self):
        res = {
            'id': self.id,
            'task_id': self.task_id,
            'user_id': self.user_id,
            'language': self.language,
            'result': self.result,
            'time': self.time,
            'memory': self.memory
        }
        return json.dumps(res)

    def __str__(self):
        res = {
            'id': self.id,
            'task_id': self.task_id,
            'user_id': self.user_id,
            'language': self.language,
            'result': self.result,
            'time': self.time,
            'memory': self.memory
        }
        return json.dumps(res)


class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, unique=False)
    token = db.Column(db.String(400), unique=False)
    refresh_token = db.Column(db.String(400), unique=False)

    def get_dict(self):
        res = {
            'id': self.id,
            'user': self.user,
            'token': self.token,
            'refresh_token': self.refresh_token
        }
        return res

    def __repr__(self):
        return json.dumps(self.get_dict())

    def __str__(self):
        return json.dumps(self.get_dict())
