
from flask import Flask, jsonify
from flask.scaffold import F
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
import pandas as pd

app = Flask(__name__)
api = Api(app)
CORS(app, support_credentials=True)

class Task(Resource):
    def get(self): # что делать на GET запрос #Этот метод получает список всех тасков
        data = pd.read_csv('data.txt') # читаем файл 
        data = data.to_dict('records') # делаем словарь, здесь эсть разные аргументы типо index или list
        return data # отправляем данные на клиент
    
    def post(self): # Создать новый таск
        parser = reqparse.RequestParser() # парсер реквеста
        parser.add_argument('task') # скармливаем параметр в парсер
        parser.add_argument('date')
        parser.add_argument('reminder')
        args = parser.parse_args() #создаём словарь аргументов реквеста
        if not args['task'] or not args['date'] or not args['reminder']: # если нет одного из параметров
            return {'success': False, 'message': 'Incorect parameters!'} # материмся и посылаем
        rawData = pd.read_csv('data.txt')
        data = rawData.to_dict(orient='list') 
        idArray = data['id'] # получаем массив айди
        lastId = idArray[-1] # получаем последний айди
        newTask = pd.DataFrame(data={ # формируем объект для записи
            'id': lastId+1,
            'task': args['task'],
            'date': args['date'],
            'reminder': args['reminder'] 
        }, index=[lastId])
        rawData = rawData.append(newTask) # вставляем новый таск в массив
        rawData.to_csv('data.txt', index=False)
        return {'success': True}
    pass
    
    def delete(self):
        parser = reqparse.RequestParser()

        parser.add_argument('id')

        args = parser.parse_args()
        if not args['id']:
            return {'success': False, 'message': 'Incorrect parameters!'}
        id = int(args['id'])
        rawData = pd.read_csv('data.txt')
        data = rawData.to_dict('index')
        if len(data)+1 <= id: # если айди нет в массиве 
            return {'success': False, 'message': 'Object with specified id not found!'}
        del data[id-1]
        rawData = pd.DataFrame.from_dict(data, orient='index') # Преобразуем словарь для записи в файл
        rawData.to_csv('data.txt', index=False)
        return {'success': True}

        

    def put(self): # поменяй reminder у таска
        parser = reqparse.RequestParser()

        parser.add_argument('id')
        parser.add_argument('reminder')

        args = parser.parse_args()
        if not args['id'] or not args['reminder']:
            return {'success': False, 'message': 'Incorrect parameters'}

        rawData = pd.read_csv('data.txt')
        data = rawData.to_dict('index')
        id = int(args['id'])
        if len(data)+1 <= id:
            return {'success': False, 'message': 'Object with specified id not found!'}
        data[id-1]['reminder'] = args['reminder']
        rawData = pd.DataFrame.from_dict(data, orient='index')
        rawData.to_csv('data.txt', index=False)
        return {'success': True}
        
api.add_resource(Task, '/')

if __name__ == '__main__':
    app.run(debug=True)  # запусти наше АПИ URL: http://127.0.0.1:5000
