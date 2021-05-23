from agro_pro import app
from flask import render_template


@app.route('/msp')
def get_msp():
    return render_template('sub_1/table_msp.html')
