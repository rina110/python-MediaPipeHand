from MediaPipeHand import camera
from MediaPipeHand import hands

camera = camera.Camera()
hands = hands.Hands()

while True:  # 永久ループ
    frame = camera.read()
    frame_draw_hands = hands.show_hands_point(frame)
    camera.show(frame_draw_hands)
    if camera.close_cheack():
        break

camera.close()