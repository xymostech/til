import users
import db
import posts

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)

@app.route('/')
def main():
    if not is_logged_in():
        return redirect(url_for('login'))

    the_posts = posts.get_posts(get_logged_in_user())
    date_posts = posts.group_posts_by_date(the_posts)

    context = {
        'dates': sorted(date_posts.keys(), reverse=True),
        'date_posts': date_posts,
        'empty': len(the_posts) == 0
    }

    return render_template("main.html", **context)

def is_logged_in():
    return 'userid' in session

def do_login(username):
    session['userid'] = users.get_userid(username)

def do_logout():
    session.pop('userid')

def get_logged_in_user():
    return session['userid']

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if users.check_login(request.form['username'], request.form['password']):
            do_login(request.form['username'])
            return redirect(url_for('main'))
        else:
            return render_template("login.html",
                                   login_error="Invalid username or password")
    else:
        return render_template("login.html")

@app.route('/register', methods=['POST'])
def register():
    if users.add_user(request.form['username'], request.form['password']):
        return redirect(url_for('login'))
    else:
        return render_template("login.html",
                               register_error="Couldn't register that username")

@app.route('/post', methods=['POST'])
def post():
    if not is_logged_in():
        return redirect(url_for('login'))

    post = request.form['post']
    posts.add_post(post, get_logged_in_user())

    return redirect(url_for('main'))

@app.route('/logout')
def logout():
    do_logout()
    return redirect(url_for('main'))

app.teardown_appcontext(db.cleanup_db)

app.secret_key = "boo"

if __name__ == "__main__":
    app.run(host="::", port=8739, debug=True)
