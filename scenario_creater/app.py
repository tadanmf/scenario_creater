from flask import Flask, Response
from scenario_creater.generator import background,  event, scene
from scenario_creater.generator.person import east, west
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/person/<type>')
def get_person(type):
    result = {}

    if 'west' == type:
        result = west.get_properties()
    elif 'east' == type:
        result = east.get_properties()

    return json.dumps(result, ensure_ascii=False, indent=2)


@app.route('/scenario')
def get_scenario():
    response = {'title': '시나리오 크리에이터',
                'contents': {
                    'background': background.select(),
                    'scene': scene.select(),
                    'event': event.select(),
                }}
    return Response(json.dumps(response, ensure_ascii=False, indent=2),
                    content_type="application/json; charset=utf-8"), 200


if __name__ == '__main__':
    app.run()
