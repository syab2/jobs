from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    team_leader_id = StringField("Team Leader Id")
    work_size = StringField('Work Size')
    collaborators = StringField('Collaborators')
    is_finished = BooleanField('Is Job finished?')
    submit = SubmitField('Submit')
