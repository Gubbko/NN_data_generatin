# sourcery skip: hoist-statement-from-loop, merge-nested-ifs
from cv2 import VideoCapture, imread, resize, imwrite
# https://docs.opencv.org/3.4/d9/d61/tutorial_py_morphological_ops.html

Video_Path = "C:\\Users\\Gubbko\\Desktop\\Bosch\\Videos\\" + "21-09-17-12-39-53.mp4"

#Video_Path = "C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\Video.mp4"
Path_to_save_images = "C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\images\\"
img_for_training = imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\Stop.jpg")

# If number equal 5 program will skip 4 frames and save 5 one
every_frame = 20

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

def add_sign_without_background_to_image(frame_to, sign, x = 0, y = 0):
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

cap1 = VideoCapture(Video_Path)
count = 0
count_1 = 0
while 1:
    frame1 = cap1.read()[1]
    frame2 = cap1.read()[1]
    frame3 = cap1.read()[1]
    sign1 = resize(img_for_training, sign_size1)
    sign2 = resize(img_for_training, sign_size2)
    sign3 = resize(img_for_training, sign_size3)

    if count % every_frame == 0:
        #frame_to_write = add_sign_without_background(frame, sign1, 0, 0)
        imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+1), add_sign_without_background_to_image(frame1, sign1, 0, 0))
        #imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+1), frame_to_write)
        
        #frame_to_write2 = add_sign_without_background(frame, sign2, -70 , -60)
        imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+2), add_sign_without_background_to_image(frame2, sign2, -70 , -60))
        #imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+2), frame_to_write2)
        
        #frame_to_write3 = add_sign_without_background(frame, sign3, -80, 110)
        imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+3), add_sign_without_background_to_image(frame3, sign3, -80, 110))
        #imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+3), frame_to_write3)
        count_1 = count_1 + 3
    count = count + 1
    
