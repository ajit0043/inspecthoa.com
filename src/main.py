from flask import Flask
from flask import jsonify
from views.user import user_views
from views.hoas import hoas_views

app = Flask(__name__)
app.debug = True


app.register_blueprint(user_views)
app.register_blueprint(hoas_views)

if __name__ == '__main__':
    app.run(debug=True)

