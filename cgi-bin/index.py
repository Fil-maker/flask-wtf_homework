from flask import Flask, url_for, request

app = Flask(__name__)
i = 0


@app.route('/')
def start():
    return "Миссия Колонизация Марса"


@app.route('/promotion')
def promote():
    return '''<h1>Человечество вырастает из детства.</h1>

<h1>Человечеству мала одна планета.</h1>

<h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>

<h1>И начнем с Марса!</h1>

<h1>Присоединяйся!</h1>'''


@app.route('/index')
def index():
    return '''И на Марсе будут яблони цвести!'''


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static',
                                       filename='img/mars.jpeg')}" alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая красная планета</p1>
                  </body>
                </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
<link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static',
                                       filename='img/mars.jpeg')}" alt="здесь должна была быть картинка, но не нашлась">
                    
                    <div class="alert alert-secondary" role="alert">Человечество вырастает из детства.</div>
                    <div class="alert alert-success" role="alert" >Человечеству мала одна планета.</div>
                    <div class="alert alert-dark" role="alert" >Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div class="alert alert-warning" role="alert" >И начнем с марса</div>
                    <div class="alert alert-danger" role="alert" >Присоединяйся!</div>
                  </body>
                </html>'''


@app.route('/astronaut_selection')
def astronaut_selection():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static',
                                                                                  filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 class="greetings_1">Анкета претендента</h1>
                            <h2 class="greetings_2">На участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="name" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Введите Фамилию">
                                    <input type="name" class="form-control" id="surname" placeholder="Введите имя" name="password">
                                    <div class="form-group">
                                        <input type="name" class="form-control" id="email" placeholder="Введите адрес почты" name="password">
                                        <label for="classSelect" >В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>7</option>
                                          <option>8</option>
                                          <option>9</option>
                                          <option>10</option>
                                          <option>11</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
