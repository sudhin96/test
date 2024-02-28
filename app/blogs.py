from .connect_to_db import ConnectDB


# This class is used to perform all the blogs operations
class Blogs(object):

    def __init__(self):
        self.desc = "All Blogs Operations"
        self.collection_name = "blogs"

    # This function is used to create a blog
    def create_blog(self, data):
        """
        This function is used to create a blog
        :param blog_data:
        :return:
        """
        try:
            # create a dictionary of the blog data
            blog_dict = {
                            "title": data.get('title', ""),
                            "description": data.get('description', "")
                        }

            # connect to the database and insert the blog_dict
            ConnectDB().connect_db()[self.collection_name].insert_one(blog_dict)

            # return a success message
            return {"status": "success", "message": "Blog created successfully"}
        except Exception as e:
            # return a failure message
            return {"status": "failure", "message": str(e)}

    # This function is used to get all the blogs
    def get_all_blogs(self):
        """
        This function is used to get all the blogs
        :return:
        """
        try:
            # connect to the database and get all the blogs
            blogs = ConnectDB().connect_db()[self.collection_name].find({},{"_id":0})

            # return the blogs
            return {"status": "success", "blogs": list(blogs)}
        except Exception as e:
            # return a failure message
            return {"status": "failure", "message": str(e)}