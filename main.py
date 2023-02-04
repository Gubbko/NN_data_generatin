import Generate_image
from tqdm import tqdm, trange
from cv2 import imread, imwrite, CAP_PROP_FRAME_COUNT, VideoCapture

Video_Path = [
    "C:\\Users\\Gubbko\\Desktop\\Bosch\\Videos\\" + "21-09-17-12-39-53.mp4",
    "C:\\Users\\Gubbko\\Desktop\\Bosch\\Videos\\" + "21-09-17-12-42-08.mp4",
    "C:\\Users\\Gubbko\\Desktop\\Bosch\\Videos\\" + "21-09-17-12-47-28.mp4",
    "C:\\Users\\Gubbko\\Desktop\\Bosch\\Videos\\" + "21-09-17-12-49-42.mp4",
    "C:\\Users\\Gubbko\\Desktop\\Bosch\\Videos\\" + "21-09-17-13-00-00.mp4",
    ]

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

every_frame = 8

# here you can cut collor of background
upperbounds_for_chromokey = [220, 220, 220]
lowerbounds_for_chromokey = [0, 0, 0]
bounds = [upperbounds_for_chromokey, lowerbounds_for_chromokey]

cap0 = Generate_image.images_by_video(Video_Path[0], every_frame)

video_lenght0 = cap0.get_video_lenght()


count = 0
count_1 = 0

def prosidure(cap, frame, sign_to):
    global count_1
    sign = cap.resize_training_image(sign_to, 60, 120)
    x, y = cap.rand_chords(frame, sign)
    imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1), cap.add_sign_without_background_to_image(frame, sign, x, y, bounds))
    count_1 += 1

try:
    for _ in trange(video_lenght0 - 1):
        if count % every_frame == 0:
            
            frame0 = cap0.get_frame()
            prosidure(cap0, frame0, img_for_training[0])
            
            frame0 = cap0.get_frame()
            prosidure(cap0, frame0, img_for_training[1])
            
            frame0 = cap0.get_frame()
            prosidure(cap0, frame0, img_for_training[2])
            
        count = count + 1
except KeyboardInterrupt:
    print("Interupt")
