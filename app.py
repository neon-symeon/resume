import oyaml as yaml
from flask import Flask
from flask import render_template
import datetime

app = Flask(__name__)
# app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    website_data = yaml.load(open('my_data.yaml'), Loader=yaml.SafeLoader)
    year = datetime.datetime.now().year

    return render_template('index.html', data=website_data, year=year)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
