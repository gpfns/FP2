from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796io1234567f'

from agro_pro import req_controller
from agro_pro import req_controller2
from agro_pro import api_controller