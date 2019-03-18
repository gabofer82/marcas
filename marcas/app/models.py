import os
from datetime import datetime, time

from pony import orm

from marcas.settings import PATHS, DEV_MODE


class DataBase:
    db = orm.Database()

    @classmethod
    def create_it(cls):
        create = not os.path.isfile(os.path.join(PATHS.get('ROOT_DIR',
                                                       'database.sqlite')))
        # if file exists its created
        cls.db.bind(provider='sqlite', filename='database.sqlite',
                    create_db=create)
        # if file is created, then tables will be created
        cls.db.generate_mapping(create_tables=create)

    @classmethod
    def config_db(cls):
        cls.create_database()
        cls.config_orm()

    @staticmethod
    def config_orm():
        orm.set_sql_debug(DEV_MODE)


class Person(DataBase.db.Entity):
    first_name = orm.Required(str)
    last_name = orm.Required(str)
    id_card = orm.Required(str)
    positions = orm.Set('Position')
    records = orm.Set('Record')
    schedules = orm.Set('Schedule')
    timestamp = orm.Required(datetime, default=datetime.now)
    # pic


class Schedule(DataBase.db.Entity):
    id = orm.Required(int, auto=True)
    day = orm.Required(str)
    ingress = orm.Required(time)
    exit = orm.Required(time)
    person = orm.Required(Person)
    timestamp = orm.Required(datetime, default=datetime.now)
    orm.PrimaryKey(id, day, ingress, exit)


class Record(DataBase.db.Entity):
    timestamp = orm.Required(datetime, default=datetime.now)
    action = orm.Required(str)
    person = orm.Required(Person)


class Position(DataBase.db.Entity):
    name = orm.Required(str)
    person = orm.Required(Person)
    timestamp = orm.Required(datetime, default=datetime.now)
