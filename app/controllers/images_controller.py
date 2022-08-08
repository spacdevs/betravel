import os
from flask import send_from_directory, current_app


class ImagesController:
    def storage(self, name):
        upload_path = os.path.join(os.getcwd(), "uploads")
        return send_from_directory(upload_path, name)
