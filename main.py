from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # app.run()
    user1 = User()
    user1.name = "Ridley"
    user1.surname = "Scott"
    user1.age = 21
    user1.position = "captain"
    user1.speciality = "research engineer"
    user1.address = "module_1"
    user1.email = "scott_chief@mars.org"

    user2 = User()
    user2.name = "Matvey"
    user2.surname = "Zhikharev"
    user2.age = 15
    user2.position = "captain"
    user2.speciality = "data scientist"
    user2.address = "module_8"
    user2.email = "maestro@mars.org"

    user3 = User()
    user3.name = "Jack"
    user3.surname = "Marso"
    user3.age = 41
    user3.position = "first_pilot"
    user3.speciality = "research engineer"
    user3.address = "module_1"
    user3.email = "scott_chef@mars.org"

    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = "2, 3"
    job.is_finished = False

    db_sess = db_session.create_session()
    # db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()