# # import pytesseract
# # from pytesseract import Output
# # import cv2
# # img = cv2.imread('/home/ave0235/Desktop/pradeep/micr/micr_api/deep_learning_samples/10_jpg/img_1.jpg')

# # d = pytesseract.image_to_data(img, lang='mcr', output_type=Output.DICT)
# # print(d)
# # n_boxes = len(d['level'])
# # for i in range(n_boxes):
# #     (x, y, w, h, c) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i], d['conf'][i])
# #     print(x,y,w,h,c)
# #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# # cv2.imshow('img', img)
# # cv2.waitKey(0)

import cv2
import numpy as np
import os
import pytesseract
from PIL import Image
from io import BytesIO



roi_per_img = {"/deep_learning_samples/10_jpg/img_1.jpg": (940, 1040),
               "/deep_learning_samples/10_jpg/img_2.jpg": (940, 1040),
               "/deep_learning_samples/10_jpg/img_3.jpg": (940, 1040),
               "/deep_learning_samples/10_jpg/img_4.jpg": (940, 1040),
               "/deep_learning_samples/10_jpg/img_5.jpg": (940, 1040),
               "/deep_learning_samples/10_jpg/img_6.jpg": (940, 1040),
               "/deep_learning_samples/10_jpg/img_7.jpg": (940, 1040),
               "/deep_learning_samples/10_jpg/img_8.jpg": (940, 1040),
               "/deep_learning_samples/10_jpg/img_9.jpg": (940, 1040),
               "/deep_learning_samples/10_jpg/img_10.jpg": (940, 1040)
               }


def get_roi(image_path):
    img = cv2.imread(image_path)
    y = 610
    x = 0
    h = 80
    w = 820

    cropped_image = image[y:y+h, x:x+w]

    gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    # cropped_image = gray_image[268:276,31:396]
    return gray_image
    x1, x2 = roi_per_img[image_path]
    return img[x1:x2, :]




img_dir = "/home/ave0235/Desktop/pradeep/micr/deep_learning_samples/10_jpg/"


for idx in range(18, 19):
    img_path = os.path.join(img_dir, "img_{}.jpg".format(idx))
    # print(img_path)
    # img_path = "/content/drive/My Drive/datasets/bank_cheques/IDRBT Cheque Image Dataset/300/Cheque 083654.tif"
    image = cv2.imread(img_path)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    roi = get_roi(img_path)
    print(roi)
    cv2.imshow("image",roi)
    cv2.waitKey(0) 
    american_cheque_data = pytesseract.image_to_string(roi, lang='mcr')
    print(american_cheque_data)
    # american_cheque_data = american_cheque_data.strip()
    # micr_data = american_cheque_data.splitlines()[-1]
    # micr_data = micr_data.split()
    # routing_number = micr_data[0]
    # routing_number = routing_number.strip('c')
    # account_number = micr_data[1]
    # account_number = account_number.strip('a')
    # cheque_number = micr_data[2]
    # cheque_number = cheque_number[:-1]
    # # print(routing_number, account_number, cheque_number)


# import cv2
# image  = cv2.imread("/home/ave0235/Desktop/pradeep/micr/deep_learning_samples/10_jpg/img_13.png")
# cv2.imshow("ROI", image)
# y = 275
# x = 35
# h = 250
# w = 400

# crop = image[y:y+h, x:x+w]
# cv2.imshow("Image", crop)
# cv2.waitKey(0)







