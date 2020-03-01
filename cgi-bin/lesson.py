from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def login():
    return render_template('base.html', title='Авторизация')


@app.route('/training/<profession>')
def training(profession):
    img1 = '''{}'''.format(url_for('static', filename='img/ship_cs.png'))
    img2 = '''{}'''.format(url_for('static', filename='img/ship_et.png'))
    if 'инженер ' in profession or 'строитель' in profession:
        return render_template('login.html', training_station='Инженерные тренажеры', idm=img2)
    return render_template('login.html', training_station='Научные симуляторы', idm=img1)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
