from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'index page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'login page'


@app.route('/user/<username>')
def show_user_profile(username):  # 将参数username传入
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post_profile(post_id):
    return 'Post %d' % post_id


@app.route('/test/<path:test_path>')
def show_test_path(test_path):
    return 'Path is %s' % test_path


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('show_user_profile', username=123215))
    # print(url_for('user'))


if __name__ == '__main__':
    app.run(debug=True)
