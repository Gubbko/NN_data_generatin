import Generate_image
from tqdm import trange
import colorama
from cv2 import imread, imwrite

debug = True

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

every_frame = 1

# here you can cut collor of background
upperbounds_for_chromokey = [220, 220, 220]
lowerbounds_for_chromokey = [0, 0, 0]
bounds = [upperbounds_for_chromokey, lowerbounds_for_chromokey]

cap0 = Generate_image.images_by_video(Video_Path[0], every_frame)

video_lenght0 = cap0.get_video_lenght()


count = 0
count_of_images = 0

def prosidure(cap, frame, sign_to):
    global count_of_images
    sign = cap.resize_training_image(sign_to, 60, 120)
    x, y = cap.rand_chords(frame, sign)
    imwrite(Path_to_save_images + "/%#05d.jpg" % (count_of_images), cap.add_sign_without_background_to_image(frame, sign, x, y, bounds))
    count_of_images += 1


try:
    print(f"{colorama.Fore.YELLOW}\r")
    
    for _ in trange(video_lenght0 - 1, desc='Video proccesed', unit=' frames', disable = not debug):
        if count % every_frame == 0:

            frame0 = cap0.get_frame()
            prosidure(cap0, frame0, img_for_training[0])

            frame0 = cap0.get_frame()
            prosidure(cap0, frame0, img_for_training[1])

            frame0 = cap0.get_frame()
            prosidure(cap0, frame0, img_for_training[2])

        count = count + 1

    print(f"{colorama.Fore.GREEN}\r")
    print(f'Program has generated {count_of_images} images')
    print(f"{colorama.Fore.WHITE}\r")
except KeyboardInterrupt:
    print(f"{colorama.Fore.RED}\r")
    print("Program was stoped by interupt")
    print(f'Program has generated {count_of_images} images')
    print(f"{colorama.Fore.RESET}\r")
