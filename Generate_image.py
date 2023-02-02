#from cv2 import VideoCapture, imread, resize, imwrite
import random

def rand_chords(img, sign):
    
    base_x = len(img)
    subs_x = len(sign)
    base_y = len(img[0])
    subs_y = len(sign[0])

    max_x = base_x // 2 - subs_x // 4
    max_y = base_y // 2 - subs_y // 2
    
    new_x_chord = random.randint(0, max_x)
    new_y_chord = random.randint(subs_y // 2,max_y)

    return -new_x_chord, -new_y_chord
    
def add_sign_without_background_to_image(frame_to, sign, x = 0, y = 0, lowerbounds_for_chromokey=None, upperbounds_for_chromokey=None, place = 100):
    if lowerbounds_for_chromokey is None:
        lowerbounds_for_chromokey = [0, 0, 0]
    if upperbounds_for_chromokey is None:
        upperbounds_for_chromokey = [220, 220, 220]
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
                frame_to[i+place[0] + x][j+place[1] + y] = sign[i][j]
    return frame_to


#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
class image_processing():
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def __init__(self,
                 upperbounds_for_chromokey=None,
                 lowerbounds_for_chromokey=None,
                 every_frame = None
                 ):
        
        if upperbounds_for_chromokey    is None: upperbounds_for_chromokey  = [220, 220, 220]
        if lowerbounds_for_chromokey    is None: lowerbounds_for_chromokey  = [0, 0, 0]
        if every_frame                  is None: every_frame                = (120, 120)
            
        self.upperbounds_for_chromokey = upperbounds_for_chromokey
        self.lowerbounds_for_chromokey = lowerbounds_for_chromokey
        self.every_frame = every_frame
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def get_random_coordinate_to_put_image(self, img, sign):
        #print(len(img))
        #print(type(len(img)))
        base_x = len(img)
        #subs_x = len(sign)
        #base_y = len(img[0])
        #subs_y = len(sign[0])
        
        #max_x = base_x // 2 - subs_x // 4
        #max_y = base_y // 2 - subs_y // 2
        
        #new_x_chord = random.randint(0, max_x)
        #new_y_chord = random.randint(subs_y // 2,max_y)
        
        #return -new_x_chord, -new_y_chord
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def add_sign_without_background_to_image(self, frame_to, sign, x = 0, y = 0, place = 100):
        for i in range(len(sign)):
            for j in range(len(sign[i])):
                if (
                    self.lowerbounds_for_chromokey[0]
                    < sign[i][j][0]
                    < self.upperbounds_for_chromokey[0]
                    and self.lowerbounds_for_chromokey[1]
                    < sign[i][j][1]
                    < self.upperbounds_for_chromokey[1]
                    and self.lowerbounds_for_chromokey[2]
                    < sign[i][j][2]
                    < self.upperbounds_for_chromokey[2]
                ):
                    frame_to[i+place[0] + x][j+place[1] + y] = sign[i][j]
        return frame_to
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    print("Can not be used separatly")
