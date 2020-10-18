from datetime import datetime
import requests

    
def send_by_firebase(data, token):
    data = {
        "to": token,
        "notification": {
            "title": "Mensaje BBVA BioLock",
            "body": data['message']
            },
        "data": {
            "message": data['message'], 
            "other_user": data['other_user'],
            "my_user": data['my_user'], 
            "date": (datetime.now()).strftime("%Y/%m/%d - %H:%M"), 
            "read": "0"
            }
        }   

    #this key was copy firebase authorization
    head = {"Authorization": "key=AAAACQ-uo0M:APA91bF57o72gtxLfMRYYw1y75mduHPLJDe-F4bAGEbAyUIqneuozxMPmGh4UTMyi8xfyid5VrMh-LieMZRYQIDszVqU-7Q25hdX6QoypxsBTuZEWBbWPy0s2D5ZyPZ5cA5H-uqGjcoF"}
    test = requests.post('https://fcm.googleapis.com/fcm/send', json = data, headers = head)