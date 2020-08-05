from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    lang = SelectField(
        'Language', 
        choices=[
            ('py', 'Python'), 
            ('js', 'JavaScript'),
            ('rb', 'Ruby'),
            ('cpp', 'C++')
        ]
    )
    src = TextAreaField(
        'Source code', 
        validators=[DataRequired()],
        render_kw={'rows':30, 'cols':88}
    )
    submit = SubmitField('Run >>')