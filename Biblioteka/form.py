from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired




class StorageForm(FlaskForm):
    book = StringField("book", validators=[DataRequired()])
    author = StringField("author",validators=[DataRequired()])
    year = StringField("year",validators=[DataRequired()])
    pages = IntegerField("pages", validators=[DataRequired()])
    read = StringField("read", validators=[DataRequired()])