from routes.data import to_do_list

from flask import Flask

app = Flask(__name__)
app.register_blueprint(to_do_list)

app.run(host='0.0.0.0', port='3001', debug=True)