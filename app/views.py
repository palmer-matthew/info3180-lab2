"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile')
def profile():
    info = {
        'name': 'Matthew Palmer',
        'locate': 'Kingston, Ja',
        'tag': '@m-apalm',
        'bio': 'This is a simple paragraph about me. I am a second year Computing student majoring in Computer Science. \
        I am interesed in alot of things as my interests invlove music, coding , reading and gaining knowledge plus more. \
        I do not know which area of Computing I would like to focus in so for now I am just trying to get experience in various \
        aspects of Computing such as Web Development.',
        'lst': { 'Posts': 7, 'Following': 100, 'Followers': 250 },
    }
    return render_template(
        'profile.html', 
        name = info['name'],
        location = info['locate'],
        tag = info['tag'],
        bio = info['bio'],
        lst = info['lst'],
        date = "Placeholder"
    )


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
