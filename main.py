import Generate_image
from cv2 import imread, imwrite

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

every_frame = 3

# here you can cut collor of background
upperbounds_for_chromokey = [220, 220, 220]
lowerbounds_for_chromokey = [0, 0, 0]
bounds = [upperbounds_for_chromokey, lowerbounds_for_chromokey]

cap0 = Generate_image.images_by_video(Video_Path[0], every_frame)
cap1 = Generate_image.images_by_video(Video_Path[1], every_frame)
cap2 = Generate_image.images_by_video(Video_Path[2], every_frame)
cap3 = Generate_image.images_by_video(Video_Path[3], every_frame)
cap4 = Generate_image.images_by_video(Video_Path[4], every_frame)

count = 0
count_1 = 0

def prosidure(cap, frame, sign_to):
    global count_1
    sign = cap.resize_training_image(sign_to, 60, 120)
    x, y = cap.rand_chords(frame, sign)
    imwrite(Path_to_save_images + "/%#05d.jpg" % (count_1), cap.add_sign_without_background_to_image(frame, sign, x, y, bounds))
    count_1 += 1
    progress_bar(count, 20000)

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = ' ' * int(percent / 2) + '-' * (50 - int(percent / 2))
    print(f"\r|{bar}| {percent:.3f}%", end="\r")

while 1:
    try:
        if count % every_frame == 0:
            
            frame0 = cap0.get_frame()
            frame1 = cap1.get_frame()
            frame2 = cap2.get_frame()
            frame3 = cap3.get_frame()
            frame4 = cap4.get_frame()
            
            prosidure(cap0, frame0, img_for_training[0])
            prosidure(cap1, frame1, img_for_training[0])
            prosidure(cap2, frame2, img_for_training[0])
            prosidure(cap3, frame3, img_for_training[0])
            prosidure(cap4, frame4, img_for_training[0])
            
            frame0 = cap0.get_frame()
            frame1 = cap1.get_frame()
            frame2 = cap2.get_frame()
            frame3 = cap3.get_frame()
            frame4 = cap4.get_frame()
            
            prosidure(cap0, frame0, img_for_training[1])
            prosidure(cap1, frame1, img_for_training[1])
            prosidure(cap2, frame2, img_for_training[1])
            prosidure(cap3, frame3, img_for_training[1])
            prosidure(cap4, frame4, img_for_training[1])
            
            frame0 = cap0.get_frame()
            frame1 = cap1.get_frame()
            frame2 = cap2.get_frame()
            frame3 = cap3.get_frame()
            frame4 = cap4.get_frame()
            
            prosidure(cap0, frame0, img_for_training[2])
            prosidure(cap1, frame1, img_for_training[2])
            prosidure(cap2, frame2, img_for_training[2])
            prosidure(cap3, frame3, img_for_training[2])
            prosidure(cap4, frame4, img_for_training[2])
        count = count + 1
    except KeyboardInterrupt:
        print("Interupt")
        break