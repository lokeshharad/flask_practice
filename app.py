from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
        'author': 'Lokesh Harad',
        'title': 'Blog-Post-1',
        'content': 'First Post Content',
        'date_posted': 'Feb. 02, 2021'
    }, 
    {
        'author': 'User 2',
        'title': 'Blog-Post-2',
        'content': 'Second Post Content',
        'date_posted': 'Jan. 02, 2021'
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)