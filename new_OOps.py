# multi level inheritence
class phone:
    def call(self):
        print("we can make  call using this")

    def alarm(self):
        print(" we can use alarm using this")

class realme(phone):
    def video_call(self):
        print("it have videocall fecility")

    def music(self):
        print("play music")

a1= phone() #obj of phone
a1.alarm()

realme1=realme()  # obj of realme
realme1.call()
realme1.video_call()

class realme6(realme):
    def camera(self):
        print("realme6 can have higher picture quality")

b1=realme6()
b1.camera()
b1.call()

