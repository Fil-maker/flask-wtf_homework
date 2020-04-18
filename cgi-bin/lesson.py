from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    user_id = StringField('id Астронавта', validators=[DataRequired()])
    user_pass = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('id капитана', validators=[DataRequired()])
    captain_pas = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Авторизация', link=url_for('static', filename='css/mars_style.css'))


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(1)
    return render_template('double_login.html', title='Авторизация', form=form,
                           link=url_for('static', filename='css/mars_style.css'))


@app.route('/distribution')
def distribution():
    passengers = ['Me', 'My Friend', 'My-strAnGE-friend']
    return render_template('distribution.html', size=len(passengers), passengers=passengers, title="Размещение",
                           link=url_for('static', filename='css/mars_style.css'))


@app.route('/table/<string:gen>/<int:age>')
def table(gen, age):
    if gen == 'female':
        if age >= 21:
            r, g, b = 128, 64, 64
        else:
            r, g, b = 128, 100, 100
    if gen == 'male':
        if age >= 21:
            r, g, b = 64, 64, 128
        else:
            r, g, b = 100, 100, 128
    if age >= 21:
        return render_template('table.html', r=r, g=g, b=b, ref=url_for('static', filename='img/old.jpg'))
    return render_template('table.html', r=r, g=g, b=b, ref=url_for('static', filename='img/yong.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
