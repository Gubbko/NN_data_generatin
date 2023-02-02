# sourcery skip: hoist-statement-from-loop, merge-nested-ifs
from cv2 import VideoCapture, imread, resize, imwrite, rectangle
import random
# https://docs.opencv.org/3.4/d9/d61/tutorial_py_morphological_ops.html

Video_Path = [
    "C:\\Users\\Gubbko\\Desktop\\Bosch\\Videos\\" + "21-09-17-12-39-53.mp4",
    "C:\\Users\\Gubbko\\Desktop\\Bosch\\Videos\\" + "21-09-17-12-42-08.mp4",
    "C:\\Users\\Gubbko\\Desktop\\Bosch\\Videos\\" + "21-09-17-12-47-28.mp4",
    "C:\\Users\\Gubbko\\Desktop\\Bosch\\Videos\\" + "21-09-17-12-49-42.mp4",
    "C:\\Users\\Gubbko\\Desktop\\Bosch\\Videos\\" + "21-09-17-13-00-00.mp4",
    ]

#Video_Path = "C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\Video.mp4"
# C:\Users\Gubbko\Desktop\Bosch\Lane_2023\images
Path_to_save_images = "C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\images\\new\\"
img_for_training = [
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Circle_1.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Circle_2.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Circle_3.jpg"),
    
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\CrossWalk_1.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\CrossWalk_2.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\CrossWalk_3.jpg"),
    
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Forward_1.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Forward_2.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Forward_3.jpg"),
    
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Highway_1.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Highway_2.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Highway_3.jpg"),
    
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\MainRoad_1.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\MainRoad_2.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\MainRoad_3.jpg"),
    
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\NoHighway_1.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\NoHighway_2.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\NoHighway_3.jpg"),
    
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\NoWay_1.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\NoWay_2.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\NoWay_3.jpg"),
    
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Parking_1.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Parking_2.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Parking_3.jpg"),
    
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Stop_1.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Stop_2.jpg"),
    imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\all_signs\\Stop_3.jpg")
    ]

# If number equal 5 program will skip 4 frames and save 5 one
every_frame = 3

# here you can cut collor of background
upperbounds_for_chromokey = [220, 220, 220]
lowerbounds_for_chromokey = [0, 0, 0]

# coordinates to put image for training
place = [100, 100]

# new size of image for training
img_size = (120, 120)

sign_size1 = (120, 120)
sign_size2 = (100, 100)
sign_size3 = (80, 80)

####################################################################################################
# Next part you don't need to change
def rand_chords(img, sign):
    
    base_x = len(img)
    subs_x = len(sign)
    base_y = len(img[0])
    subs_y = len(sign[0])
    
    #print(f"base = {base_x}:{base_y} -------------- subs = {subs_x}:{subs_y}")

    max_x = base_x - subs_x
    max_y = base_y - subs_y

    #print(f"base_x={base_x},sub={subs_x}, max={max_x}")
    #print(f"base_x={base_y},sub={subs_y}, max={max_y}")

    new_x_chord = random.randint(0, max_x)
    new_y_chord = random.randint(0, max_y)

    #print(new_x_chord)
    #print(max_x)
    return new_x_chord, new_y_chord
    
def add_sign_without_background_to_image(frame_to, sign, x, y):
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

cap1 = VideoCapture(Video_Path[0])
count = 0
count_1 = 2598

sign1 = resize(img_for_training[2], sign_size1)
sign2 = resize(img_for_training[2], sign_size2)
sign3 = resize(img_for_training[2], sign_size3)

while 1:
    try:
        frame1 = cap1.read()[1]
        frame2 = cap1.read()[1]
        frame3 = cap1.read()[1]
        
        if count % every_frame == 0:
            
        
            x1, y1 = rand_chords(frame1, sign1)
            x2, y2 = rand_chords(frame2, sign2)
            x3, y3 = rand_chords(frame3, sign3)
            
            
            #frame_to_write = add_sign_without_background(frame, sign1, 0, 0)
            imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+1), add_sign_without_background_to_image(frame1, sign1, x1, y1))
            #print(f"index = {count_1+1}: and x value = {x1}")
            #imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+1), frame_to_write)
            
            #frame_to_write2 = add_sign_without_background(frame, sign2, -70 , -60)
            imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+2), add_sign_without_background_to_image(frame2, sign2, x2 , y2))
            #imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+2), frame_to_write2)
            
            #frame_to_write3 = add_sign_without_background(frame, sign3, -80, 110)
            imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+3), add_sign_without_background_to_image(frame3, sign3, x3, y3))
            #imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+3), frame_to_write3)
            count_1 = count_1 + 3
        count = count + 1
    except KeyboardInterrupt:
        print("Interupt")
        break
    
