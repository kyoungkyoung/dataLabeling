import cv2
import os

folder_path = "C:/Users/han/Desktop/snack_data_original/5th_mix_data_all_rabeled_resize_x"

width = 640
height = 640

for foodlist in os.listdir(folder_path):
    food_path = os.path.join(folder_path, foodlist)
    img = cv2.imread(food_path)
    resize_img = cv2.resize(img, (width, height), cv2.INTER_AREA)
    cv2.imwrite(food_path, resize_img)
    print(f"{foodlist}가 resize 되었습니다")