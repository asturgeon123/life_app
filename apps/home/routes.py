# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

from flask_login import current_user

from apps import db
from apps.authentication import blueprint
from apps.authentication.models import Users, Companys

from apps.home.forms import UserProfileForm,FlightLogForm,CompanyForm

@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')


@blueprint.route('/user.html', methods=['GET','POST'])
@login_required
def update():
    profile_form = UserProfileForm(request.form,obj=current_user)

    if request.method == "GET":
        return render_template('home/user.html',form=profile_form)

    if request.method == "POST":
        print("POST",request.form)

        #Update User
        current_user.update(request.form)
        print(current_user)  # {}
        db.session.commit()

        return render_template('home/user.html',form=profile_form)



@blueprint.route('/log_flight.html', methods=['GET','POST'])
@login_required
def log_flight():
    profile_form = FlightLogForm(request.form)

    if request.method == "GET":
        return render_template('home/log_flight.html',form=profile_form)

    if request.method == "POST":
        print("POST",request.form)

        #Update User
        current_user.update(request.form)
        print(current_user)  # {}
        db.session.commit()

        return render_template('home/log_flight.html',form=profile_form)


@blueprint.route('/add_company.html', methods=['GET','POST'])
@login_required
def select_company():
    profile_form = CompanyForm(request.form)

    #Get all company names
    company_names = Companys.query.all()
    print(company_names)

    if request.method == "GET":
        return render_template('home/add_company.html',form=profile_form)

    if request.method == "POST":
        print("POST",request.form)

        company_name = request.form['company_name']
        if 'register' in request.form:
            print("Registering company")
            # Check if name already exists
            company = Companys.query.filter_by(company_name=company_name).first()
            if company:
                print("Company already exists")
                return render_template('/index.html',
                                    msg='Name already registered',
                                    success=False,
                                    form=profile_form)

            # else we can create the user
            company = Companys(**request.form)
            db.session.add(company)
            db.session.commit()
            return render_template('home/add_company.html',form=profile_form)

        if 'update' in request.form:
            #Update User
            #current_user.update(request.form)
            #db.session.commit()
            print(current_user)

            return render_template('home/add_company.html',form=profile_form)


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except Exception as e:
        print(e)
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
