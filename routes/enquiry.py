import shelve

from flask import Blueprint, render_template
from flask import flash, render_template, redirect, url_for, request

from classes.Enquiry import Enquiry
from forms import createEnquiryForm

enquiry = Blueprint('enquiry', __name__)


@enquiry.route('/ContactUs', methods=['GET', 'POST'])
def viewEnquiry():
    form = createEnquiryForm(request.form)

    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        purpose = form.purpose.data
        query = form.query.data
        this_enquiry = Enquiry(name, email, purpose, query)

        with shelve.open('enquiry', writeback='True') as enquiries:
            enquiries[str(this_enquiry.getId())] = this_enquiry

        flash('Thank you for contacting Explore Singapore. We will get back to you shortly.', category='success')
        return redirect(url_for("enquiry.viewEnquiry"))
    else:
        flash('Unable to create form, please retry again!')
    return render_template("enquiry/viewEnquiry.html", form=form)
