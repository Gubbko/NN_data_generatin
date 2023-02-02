import Generate_image
from cv2 import VideoCapture, imread, resize, imwrite

Video_Path = "C:\\Users\\Gubbko\\Desktop\\Bosch\\Videos\\" + "21-09-17-12-39-53.mp4"

Path_to_save_images = "C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\images\\new\\"
img_for_training = imread("C:\\Users\\Gubbko\\Desktop\\Bosch\\Lane_2023\\Stop.jpg")

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
        x1, y1 = Generate_image.rand_chords(frame1, sign1)
        x2, y2 = Generate_image.rand_chords(frame2, sign2)
        x3, y3 = Generate_image.rand_chords(frame3, sign3)
        
        
        imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+1),
                Generate_image.add_sign_without_background_to_image(frame1,
                                                                    sign1,
                                                                    x1, y1,
                                                                    lowerbounds_for_chromokey,
                                                                    upperbounds_for_chromokey,
                                                                    place))
        
        imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+2),
                Generate_image.add_sign_without_background_to_image(frame2,
                                                                    sign2,
                                                                    x2 , y2,
                                                                    lowerbounds_for_chromokey,
                                                                    upperbounds_for_chromokey,
                                                                    place))
        
        imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1+3),
                Generate_image.add_sign_without_background_to_image(frame3,
                                                                    sign3,
                                                                    x3, y3,
                                                                    lowerbounds_for_chromokey,
                                                                    upperbounds_for_chromokey,
                                                                    place))
        
        count_1 = count_1 + 3
    count = count + 1
    
