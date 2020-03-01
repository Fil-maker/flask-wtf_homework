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


@app.route('/list_prof/<type_>')
def list_prof(type_):
    work_list = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терроформированию',
                 'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман',
                 'пилот дронов']
    if type_ == 'ol':
        return render_template('index.html', req=2, work_list=work_list)
    return render_template('index.html', req=1, work_list=work_list)


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    data = {
        'surname': "Зубарев",
        'name': "Филипп",
        'education': "Низинькое)",
        'profession': "Програмер",
        'sex': "male",
        'motivation': "Мечтал мечтать",
        'ready': True,
    }
    send_vals = list(map(lambda x: x, data.values()))
    return render_template('auto_answer.html', link=url_for('static', filename='css/mars_style.css'), values=send_vals,
                           size=len(data.keys()))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
