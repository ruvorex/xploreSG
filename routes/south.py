import shelve

from flask import Blueprint, render_template
from flask import flash, render_template, redirect, url_for, request

from classes.Enquiry import Enquiry
from forms import createEnquiryForm

south = Blueprint('south', __name__)


@south.route('/south/LazarusIsland')
def viewLazarusIsland():
    return render_template("south/Lazarus_Island.html")
