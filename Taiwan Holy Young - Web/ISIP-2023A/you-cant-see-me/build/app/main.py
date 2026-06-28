from flask import Flask, render_template,redirect
import sqlite3

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
    {'id': 10233, 'cat_name': 'Not Real Flag', 'cat_image': 'abc.jpg'},
    {'id': 38401, 'cat_name': 'Edward FLAG{You_saw!!!}', 'cat_image': 'edward.jpg'}
]

@app.route('/')
def user_list():
    return render_template('user_list.html', cat_profiles=cat_profiles[:-2])

@app.route('/user/<userid>')
def user_profile(userid):
    cat_profile = next((cat for cat in cat_profiles if cat['id'] == int(userid)), None)
    if userid == "9" and cat_profile:
        return render_template('user_pro.html', cat_name=cat_profile['cat_name'], cat_image=cat_profile['cat_image'] ,next_id=10233)
    elif userid == "10233" and cat_profile:
        return render_template('user_pro.html', cat_name=cat_profile['cat_name'], cat_image=cat_profile['cat_image'] ,next_id=38401)
    elif userid == "38401" and cat_profile:
        return render_template('user_pro.html', cat_name=cat_profile['cat_name'], cat_image=cat_profile['cat_image'] ,next_id=5)
    elif cat_profile:
        return render_template('user_profile.html', cat_name=cat_profile['cat_name'], cat_image=cat_profile['cat_image'])
    else:
        return "User not found"

if __name__ == '__main__':
    app.run()