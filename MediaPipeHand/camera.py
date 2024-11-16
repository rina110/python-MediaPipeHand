from operator import truediv

import cv2 #openCV

# while True: #永久ループ
#     ret, video = cap.read()#画像取得
#
#     cv2.imshow('camera' , video)#表示
#
#     key =cv2.waitKey(10) #ESCで終了
#     if key == 27:
#         break
count = 0
# cap.release() #終了
# cv2.destroyAllWindows()

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 0番目のカメラ。DirectShow書かないと動かなかったwindows
        self.cap.set(cv2.CAP_PROP_SETTINGS, 1)  # カメラ設定ウィンドウ表示

        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)

    def read(self):
        ret, video = self.cap.read()  # 画像取得
        return video

    def show(self):
        cv2.imshow('camera', self.read())  # 表示

    def show(self, video):
        cv2.imshow('camera', video)  # 表示

    def close_cheack(self):
        key = cv2.waitKey(10)  # ESCで終了
        if key == 27:
            return True
        return False

    def close(self):
        self.cap.release()  # 終了
        cv2.destroyAllWindows()