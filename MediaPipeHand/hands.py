import cv2
import mediapipe as mp

class Hands:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(
            static_image_mode=True,
            max_num_hands=2,                # 最大検出数
            min_detection_confidence=0.5,   # 検出信頼度
            min_tracking_confidence = 0.7)  # 追跡信頼度

        self.landmark_list = ['WRIST', 'THUMP_CMC', 'THUMB_MCP', 'THUMB_IP', 'THUMB_TIP', 'INDEX_FINGER_MCP', 'INDEX_FINGER_PIP', 'INDEX_FINGER_DIP', 'INDEX_FINGER_TIP', 'MIDDLE_FINGER_MCP', 'MIDDLE_FINGER_PIP', 'MIDDLE_FINGER_DIP', 'MIDDLE_FINGER_TIP', 'RING_FINGER_MCP', 'RING_FINGER_PIP', 'RING_FINGER_DIP', 'RING_FINGER_TIP', 'PINKY_MCP', 'PINKY_PIP', 'PINKY_DIP', 'PINKY_TIP']

    def show_hands_point(self, frame):
        frame = cv2.flip(frame, 1) #画像を左右反転
        frame_h, img_w, _ = frame.shape #サイズ取得
        results = self.hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) # 検出

        if results.multi_hand_landmarks:
            #検出した数分繰り返し
            for h_id, hand_landmarks in enumerate(results.multi_hand_landmarks):
                for landmark in self.landmark_list:
                    # print(landmark)
                    # print(hand_landmarks.landmark[index])

                    mp.solutions.drawing_utils.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp.solutions.hands.HAND_CONNECTIONS,
                        mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
                        mp.solutions.drawing_styles.get_default_hand_connections_style()
                    )
        return frame