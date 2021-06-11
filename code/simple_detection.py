import cv2
import numpy as np

stamp_source = cv2.imread('stamps/sources/stamp_source.png')
stamp_target = cv2.imread('stamps/targets/stamp_target_01.png')

result = cv2.matchTemplate(stamp_source, stamp_target, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


if max_val >= 0.8:
    found_img_w = stamp_target.shape[1]
    found_img_h = stamp_target.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + found_img_w, top_left[1] + found_img_h)

    cv2.rectangle(stamp_source, top_left, bottom_right, color=(0,255,0), thickness=2, lineType=cv2.LINE_4)
    cv2.imshow('Result', stamp_source)

    cv2.waitKey()
else:
    print('Target Not Found')
