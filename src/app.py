from flask import Flask
from src.routes import *

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='development'
)

app.add_url_rule(routes['index_route'], view_func=routes['indexcontroller'])

app.add_url_rule(routes['create_route'], view_func=routes['createcontroller'])

app.add_url_rule(routes['delete_route'], view_func=routes['deletecontroller'])

app.add_url_rule(routes['update_route'], view_func=routes['updatecontroller'])

