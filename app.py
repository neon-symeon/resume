from flask import Flask, render_template
import oyaml as yaml
import datetime

app = Flask(__name__)
# app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    website_data = yaml.load(open('my_data.yaml'), Loader=yaml.SafeLoader)
    year = datetime.datetime.now().year

    return render_template('index.html', data=website_data, year=year)


@app.route('/testy/')
def testy():
    website_data = yaml.load(open('my_data.yaml'), Loader=yaml.SafeLoader)
    year = datetime.datetime.now().year

    return render_template('idx_testy.html', data=website_data, year=year)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
