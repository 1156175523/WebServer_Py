import time, uuid

from ormClass import Field, Model, StringField, IntegerField, FloatField, TextField, BooleanField

def next_id():
    return '%015d%s000' %(int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'
    
    id = StringField(name='id', primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(name='email', ddl='varchar(50)')
    passwd = StringField(name='passwd', ddl='varchar(50)')
    admin = BooleanField(name='admin')
    name = StringField(name='name', ddl='varchar(50)')
    image = StringField(name='image', ddl='varchar(500)')
    created_at = FloatField(name='created_at', default=time.time)

class Blog(Model):
    __table__ = 'blogs'
    
    id = StringField(name='id', primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(name='user_id', ddl='varchar(50)')
    user_name = StringField(name='user_name', ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(name='name', ddl='varchar(50)')
    summary = StringField(name='summary', ddl='varchar(200)')
    content = TextField(name='content')
    created_at = FloatField(name='created_at', default = time.time)
    
class Comment(Model):
    __table__ = 'comments'
    
    id = StringField(name='id', primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(name='blog_id', ddl='varchar(50)')
    user_id = StringField(name='user_id', ddl='varchar(50)')
    user_name = StringField(name='user_name', ddl='varchar(50)')
    user_image = StringField(name='user_image', ddl='varchar(500)')
    content = TextField(name='content')
    created_at = FloatField(name='created_at', default = time.time)