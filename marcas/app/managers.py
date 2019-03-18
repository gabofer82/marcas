from pony import orm
from .models import Person, Schedule, Record, Position


class Persons:
    def get(self):
        with orm.db_session:
            Person.select(lambda p: None)
            orm.select(p for p in Person).order_by(Person.last_name)

    def create(self, first_name, last_name, id_card):
        with orm.db_session:
            return Person(first_name=first_name, last_name=last_name,
                          id_card=id_card)


class Schedules:
    def get(self):
        with orm.db_session:
            return Schedule.select(lambda s: None)


class Records:
    def get(self):
        with orm.db_session:
            return Record.select(lambda r: None)


class Positions:
    def get(self):
        with orm.db_session:
            return Position.select(lambda p: None)

    def create(self, name, person_id):
        with orm.db_session:
            return Position(name=name,
                            person=person_id)
