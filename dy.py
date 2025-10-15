from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return f"User: {username}"

@app.route('/post/<int:post_id>')
def show_order(order_id):
    return f"Order ID: {order_id}"

if __name__ == '__main__':
    app.run(debug=True)