import datetime

## https://github.com/sinarezaei/pykson
from pykson import JsonObject, IntegerField, StringField, ObjectListField, Pykson, DateTimeField


class Course(JsonObject):
    name = StringField()
    teacher = StringField()


class Score(JsonObject):
    score = IntegerField()
    course = Course()


class Student(JsonObject):
    first_name = StringField()
    last_name = StringField()
    age = IntegerField()
    scores = ObjectListField(Score)
    md = DateTimeField('%Y-%m-%d')

    def __init__(self, first_name, last_name, age, md, scores, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.md = md
        self.scores = scores


json_text = '{"first_name":"John", "last_name":"Smith", "age": 25, ' \
            '"scores": [ {"course": {"name": "Algebra", "teacher" :"Mr. Schmidt"}, "score": 100},' \
            ' {"course": {"name": "Statistics", "teacher": "Mrs. Lee"}, "score": 90} ]}'
student = Pykson().from_json(json_text, Student)
student.md = datetime.datetime.now()
print(type(student))
s = Pykson().to_json(student)
print(s)

s = Student("John", "Smith", 25, datetime.datetime.now(), 90, [])
print(Pykson().to_json(s))
