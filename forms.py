from flask_wtf import FlaskForm
from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, EmailField, SubmitField, validators


class createEnquiryForm(Form):
    name = StringField('Name', [validators.length(3, 128, message='Name must be between 3 to 128 characters'),
                                validators.DataRequired(message='Name is required')])
    email = EmailField('Email', [validators.Email(granular_message=True),
                                 validators.DataRequired(message='Email is required')])
    purpose = SelectField('Purpose', [validators.DataRequired('Purpose is required')],
                          choices=[("", 'Select a Purpose'), ('General Questions', 'General Questions'),
                                   ('Feedback / Feature Request', 'Feedback / Feature Request')], default=""
                          )
    query = TextAreaField('Enquiry',
                          [validators.length(3, 1000, message='Enquiry must be between 3 to 1000 characters'),
                           validators.DataRequired('Enquiry is required')])
    submit = SubmitField('Submit')
