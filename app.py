from flask import Flask, render_template, url_for
app = Flask(__name__, template_folder='template')

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


if __name__ == "__main__":
    app.run(debug=True)
