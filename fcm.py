import requests
import json

serverToken = 'AAAAv3RiIFQ:APA91bE0i2Atdh45zJr-lJ97x4ZmKA5On-j0LL8VelDLKS62ER0LhFWq4dGtI4FoZM1E0JpyUfV-jcE3Xnko_J54bHsnhweZk5dnw4w7o-mCs7wO7AHBfbhE9Ohkvu3JM9Ac6suIrPj_'
deviceToken = 'dPrjm875Q_SQXvRnAxl3bZ:APA91bFFBNKg0huZ_kaesJhKF100lYnnLX_xn3KhsDYkYFnxaNickgEfdEsM3sm2GhhLFyqiZsKDBryeGedFSC-Umrctcaz0z7Bjzz1sgJX04TegNa_7ANkfEmrES1BCbQD-OZ8KmdEN'

headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
      }

def sendAlert(alertid):
    body = {
              'notification': {'title': '* Notfallsanitäterin Daisy *',
                                'body': '** Notfall! ** ID: ' + alertid + ' **'
                                },
              'to':
                  deviceToken,
              'priority': 'high',
            #   'data': dataPayLoad,
            }
    response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
    print(response.status_code)

    print(response.json())

sendAlert("000")
