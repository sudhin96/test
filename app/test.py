from flask import Flask, jsonify, request
from .blogs import Blogs
from app import app

# app = Flask(__name__)

data = [{"name": "Poorna", "location": "Bangalore"},
        {"name": "Raj", "location": "Mysore"},
        {"name": "Kumar", "location": "Chennai"}]


@app.route('/hello')  # decorator
def hello_world():
    # view function
    return 'Hello, World!'


@app.route('/createBlog', methods=['POST'])
def create_blog():
    """
    This function is used to create a blog
    :return:
    """
    try:
        # get the blog data from the request
        blog_data = request.get_json()

        # create a blog
        blog = Blogs().create_blog(blog_data)

        # return the blog
        return jsonify(blog)
    except Exception as e:
        # return a failure message
        return jsonify({"status": "failure", "message": str(e)})


@app.route('/getAllBlogs', methods=['GET'])
def get_all_blogs():
    """
    This function is used to get all the blogs
    :return:
    """
    try:
        # get all the blogs
        blogs = Blogs().get_all_blogs()

        # return the blogs
        return jsonify(blogs)
    except Exception as e:
        # return a failure message
        return jsonify({"status": "failure", "message": str(e)})
