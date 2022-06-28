from flask import Flask

from app.config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)

from app import routes