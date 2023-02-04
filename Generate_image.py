# sourcery skip: hoist-statement-from-loop, merge-nested-ifs
from cv2 import VideoCapture, resize, CAP_PROP_FRAME_COUNT
import random
# https://docs.opencv.org/3.4/d9/d61/tutorial_py_morphological_ops.html

class images_by_video():
    def __init__(self, video, frames_iter = 10):
        self.cap = VideoCapture(video)
        self.frames_iter = frames_iter

    def get_frame(self):
        return self.cap.read()[1]
    
    def get_video_lenght(self):
        return int(self.cap.get(CAP_PROP_FRAME_COUNT))
    
    def rand_chords(self, img, sign):
        base_x = len(img)
        subs_x = len(sign)
        base_y = len(img[0])
        subs_y = len(sign[0])
        #print(f"base = {base_x}:{base_y} -------------- subs = {subs_x}:{subs_y}")
        max_x = base_x - subs_x
        max_y = base_y - subs_y
        new_x_chord = random.randint(0, max_x)
        new_y_chord = random.randint(0, max_y)
        return new_x_chord, new_y_chord
    
    def add_sign_without_background_to_image(self, frame_to, sign, x, y, bounds):
        lowerbounds_for_chromokey = bounds[1]
        upperbounds_for_chromokey = bounds[0]
        for i in range(len(sign)):
            for j in range(len(sign[i])):
                if (
                    lowerbounds_for_chromokey[0]
                    < sign[i][j][0]
                    < upperbounds_for_chromokey[0]
                    and lowerbounds_for_chromokey[1]
                    < sign[i][j][1]
                    < upperbounds_for_chromokey[1]
                    and lowerbounds_for_chromokey[2]
                    < sign[i][j][2]
                    < upperbounds_for_chromokey[2]
                ):
                    frame_to[i+x][j+y] = sign[i][j]
        #rectangle(frame_to,(y,x),(y+len(sign[0]),x+len(sign)),(0,255,0),2)
        return frame_to
    
    def resize_training_image(self, sign, min = 60, max = 120):
        size = random.randint(min, max)
        sign = resize(sign, [size, size])
        return sign

if __name__ == "__main__":
    print("main")
