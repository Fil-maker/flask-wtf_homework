from flask import Flask
from flask import render_template, url_for

from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars.sqlite")
    app.run()


@app.route('/')
def journal():
    session = db_session.create_session()
    name, team_leader, duration, team_id, finished = [], [], [], [], []
    for job in session.query(Jobs).all():
        leader = session.query(User).filter(User.id == job.team_leader).first()

        name.append(job.job)
        team_leader.append(leader.name + ' ' + leader.surname)
        duration.append(job.work_size)
        team_id.append(job.collaborators)
        finished.append(job.is_finished)
    return render_template('journal.html', count=len(name), link=url_for('static', filename='css/style.css'), name=name,
                           team_leader=team_leader, duration=duration, team_id=team_id, finished=finished)


if __name__ == '__main__':
    main()
