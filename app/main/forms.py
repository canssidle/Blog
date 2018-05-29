from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write something interesting about yourself', validators=[Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField("Share",validators=[Required()])
    body = TextAreaField("Share your story", validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    name = StringField(" Name")
    comment_body = StringField("Comment",validators=[Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    name = StringField("" Name")
    email = StringField("Email")
    submit= SubmitField('Subscribe')