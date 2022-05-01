# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
import urllib.request
import pyrebase

# thingspeak
date = str(input("enter date : "))
date = date.replace(' ', "%20")
date = date.replace('\n', "%0A")
name = str(input("enter your name : "))
name = name.replace(' ', "%20")
name = name.replace('\n', "%0A")
face = str(input("Enter your Face ID : "))
face = face.replace(' ', "%20")
face = face.replace('\n', "%0A")
mask = str(input("Enter your mask : "))
mask = mask.replace(' ', "%20")
mask = mask.replace('\n', "%0A")
status = str(input("Enter your status : "))
status = status.replace(' ', "%20")
status = status.replace('\n', "%0A")

# msg = str(input('Enter your message : '))
# msg = msg.replace(' ', "%20")
# msg = msg.replace('\n', "%0A")
b = urllib.request.urlopen('https://api.thingspeak.com/update?api_key=RL2RLT93U16LUYS5&field1=0'+date+name+face+mask+status)
print("\nYour message has successfully been sent!")

# firebase data
# cred = credentials.Certificate("D:\encryption image\serviceAccountKey.json")
# firebase_admin.initialize_app(cred, {
# 	'databaseURL': 'https://batch7-project-a09d0-default-rtdb.firebaseio.com/'
# })

# ref = db.reference('/')
# ref.set({
# 	"Attendance":
# 	{
# 		"date": date,
# 		"name": name,
# 		"face_id": face,
# 		"mask": mask,
# 		"status": status
# 	}
# })

firebaseConfig = {
  'apiKey': "AIzaSyBVxy4oK6LzUREKBSgik39cxkxUl_Ea64M",
  'authDomain': "batch7-project-a09d0.firebaseapp.com",
  'databaseURL': "https://batch7-project-a09d0-default-rtdb.firebaseio.com",
  'projectId': "batch7-project-a09d0",
  'storageBucket': "batch7-project-a09d0.appspot.com",
  'messagingSenderId': "976184391607",
  'appId': "1:976184391607:web:d1b45ebef488e440981a32"
}


firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

data = {'date': date, 'name': name, 'face_id': face, 'mask': mask, 'status': status}
db.child('Attendance').push(data)








