from flask import Flask, render_template
from routes.enquiry import enquiry
from routes.south import south

app = Flask(__name__)
app.secret_key = 'RTYUjnbgf59ij34rhgieudfk'

app.register_blueprint(enquiry)
app.register_blueprint(south)


@app.route('/')
def home():
    return render_template('home.html')




if __name__ == '__main__':
    app.run(debug=True)
