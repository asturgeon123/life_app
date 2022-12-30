# -*- encoding: utf-8 -*-


from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import Length
from wtforms.widgets import TextArea

from wtforms import DateField

class UserProfileForm(FlaskForm):
    first_name = StringField(u'First Name',
                             id='first_name',)

    last_name  = StringField(u'Last Name',
                             id='last_name',)

    address    = StringField(u'Address',id='address')
    city       = StringField(u'City',id='city')
    state      = StringField(u'State',id='state')
    zip_code   = StringField(u'Zip Code',id='zip_code')
    country    = StringField(u'Country',id='country')

    phone_number = StringField(u'Phone',id='phone_number',validators=[Length(min=7, max=11, message='Not a valid phone number')])
    about_me = StringField(u'About Me',id='about_me', widget=TextArea())


class FlightLogForm(FlaskForm):
    student_name = StringField(u'Student Name',id='student_name')

    #ground_start = DateTimeField(u'Ground Start',id='ground_start',widget=DateField())
    #ground_end = DateTimeField(u'Ground End',id='ground_end',widget=DateField())

    ground_total = DecimalField(u'Ground Instruction',id='ground_total')
    
    aircraft_tailnumber = StringField(u'Aircraft Tailnumber',id='aircraft_tailnumber',validators=[Length(min=4, max=6, message='Not a valid phone number')])
    hobbs_start = DecimalField(u'Hobbs Start',id='hobbs_start')
    hobbs_end = DecimalField(u'Hobbs End',id='hobbs_end')
    hobbs_total = DecimalField(u'Hobbs Total',id='hobbs_total')

    remarks = StringField(u'Remarks',id='remarks', widget=TextArea())

class CompanyForm(FlaskForm):
    company_name = StringField(u'Company Name',id='company_name')
    company_address = StringField(u'Company Address',id='company_address')
    company_city = StringField(u'Company City',id='company_city')
    company_state = StringField(u'Company State',id='company_state')
    company_zip_code = StringField(u'Company Zip Code',id='company_zip_code')
    company_country = StringField(u'Company Country',id='company_country')
    company_phone_number = StringField(u'Company Phone Number',id='company_phone_number')
    company_email = StringField(u'Company Email',id='company_email')

    instruction_pay_rate = DecimalField(u'Instruction Pay Rate',id='instruction_pay_rate')