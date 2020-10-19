from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__, template_folder='template')

app.config['SECRET_KEY'] = '1640a0dc17d31a9d49a2581a452f98ef'

posts = [
    {
        'name': 'Shivam Choudhary',
        'date': '18th oct 2020',
        'content': 'Flask Content',
        'title': 'Blog-1'
    },
    {
        'name': 'Flask',
        'date': '20th oct 2020',
        'content': 'Flask blog content',
        'title': 'Blog-2'
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About Page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'a@b.com' and form.password.data == '1111':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(
                'Login in unsuccessfull. Please Check your email and password', 'danger')
    return render_template('login.html', title='login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
