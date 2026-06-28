from flask import Flask, render_template, request, render_template_string
import sqlite3
from urllib.parse import unquote
app = Flask(__name__)

# Sample user data    

cat_profiles = [
    {'id': 1, 'cat_name': 'Fluffy', 'cat_image': 'fluffy.jpg'},
    {'id': 2, 'cat_name': 'Whiskers', 'cat_image': 'whiskers.jpg'},
    {'id': 3, 'cat_name': 'Mittens', 'cat_image': 'mittens.jpg'},
    {'id': 4, 'cat_name': 'Shadow', 'cat_image': 'shadow.jpg'},
    {'id': 5, 'cat_name': 'Oreo', 'cat_image': 'oreo.jpg'},
    {'id': 6, 'cat_name': 'Socks', 'cat_image': 'socks.jpg'},
    {'id': 7, 'cat_name': 'Ginger', 'cat_image': 'ginger.jpg'},
    {'id': 8, 'cat_name': 'Snowball', 'cat_image': 'snowball.jpg'},
    {'id': 9, 'cat_name': 'Simba', 'cat_image': 'simba.jpg'},
    {'id': 10, 'cat_name': 'Luna', 'cat_image': 'luna.jpg'},
]

@app.route('/')
def user_list():
    return render_template('user_list.html', cat_profiles=cat_profiles[:-1], chal_name="WAF",chal_p=' BlackList : ["{{}}", \'"\', "flag", "id", "system","import"]')

@app.route('/user/<userid>')
def user_profile(userid):

    cat_profile = next((cat for cat in cat_profiles if cat['id'] == int(userid)), None)
    if cat_profile:
        return render_template('user_profile.html', cat_name=cat_profile['cat_name'], cat_image=cat_profile['cat_image'])

BLACKLIST = ["{{}}", '"', "flag", "id", "system","import"]

def is_input_valid(user_input):
    for term in BLACKLIST:
        if term in user_input:
            return False
    return True

@app.errorhandler(404) 
def page_not_found(error): 
    url = unquote(request.url)
    if not is_input_valid(url):
        return render_template_string("<h1>H4cker!!!</h1>")
    return render_template_string("<h2>User %s not found</h2><br/>"%url), 404

@app.errorhandler(500) 
def page_err_found(error): 
    url = unquote(request.url) 
    if not is_input_valid(url):
        return render_template_string("<h1>H4cker!!!</h1>")
    return render_template_string("<h2>User %s not found</h2><br/>"%url), 500

if __name__ == '__main__':
    app.run()