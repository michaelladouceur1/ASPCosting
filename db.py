from mongoengine import *

connect('mongoengine_test', host='mongodb://localhost/database_name')

class Post(Document):
	title = StringField(required=True, max_length=200)
	content = StringField(required=True)
	author = StringField(required=True, max_length=50)

post_1 = Post(
	title='Sample Post',
	content='Some engaging content',
	author='Scott'
)

post_1.save()
