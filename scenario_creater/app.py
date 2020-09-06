from flask import Flask
from scenario_creater.generator.person.west import get_properties as get_west_prop
from scenario_creater.generator.person.east import get_properties as get_east_prop
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/person/<type>')
def get_person(type):
    result = {}

    if 'west' == type:
        result = get_west_prop()
    elif 'east' == type:
        result = get_east_prop()

    return json.dumps(result, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    app.run()
