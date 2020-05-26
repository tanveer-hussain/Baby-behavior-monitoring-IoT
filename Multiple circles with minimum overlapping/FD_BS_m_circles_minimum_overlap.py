import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np
import imutils
import math
import threading

def main():
    
    
        
    cap = cv2.VideoCapture(vid_path)
    status1, previous_frame = cap.read()
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    copy_frame = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    hsv = np.zeros_like(previous_frame)
    hsv[...,1] = 255
    t = 20
    red = 30
    check_red = 1
    start = 0
    radiuce_up_limit =60
    radiuce_low_limit = 30
    i = 0
    
    while(i < total_frames - 1):
        ret, frame = cap.read()
        i = i + 1
        
    
        frame1 = frame.copy()
        current_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        current_frame = cv2.GaussianBlur(current_frame, (var_blur,var_blur), 0)   
        
    # frame differening
        frame_diff = cv2.absdiff(current_frame,copy_frame)
        
        ret ,binary_image1 = cv2.threshold(frame_diff,3,255,cv2.THRESH_BINARY)
    
        # Background Subtraction
        binary_image3 = fgbg.apply(current_frame)
    
        # combination of two methods
        final_binary = cv2.bitwise_and(binary_image3,binary_image1)
            
        lab_val = 255
        n_labels, img_labeled, lab_stats, _ = \
            cv2.connectedComponentsWithStats(final_binary, connectivity=8, 
                                             ltype=cv2.CV_32S)
        
        if check_red == 1:
            red = red +10
            if red > radiuce_up_limit:
                check_red =0    
        else:
            red = red -10
            if red == radiuce_low_limit:
                check_red =1     
        
        
        
        if  lab_stats[1:, 4].size > 2:
            
            
    #        print(lab_stats[1:,4].size)
            re = lab_stats[1:, 4].argsort()[-2:][::-1] + 1
            
    
            largest_mask = np.zeros(final_binary.shape, dtype=np.uint8)
            largest_mask[img_labeled == re[0]] = lab_val
            cnts1 = cv2.findContours(largest_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts1 = cnts1[0] if imutils.is_cv2() else cnts1[1]
            
           
            largest_mask[img_labeled == re[1]] = lab_val
            cnts2 = cv2.findContours(largest_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts2 = cnts2[0]  if imutils.is_cv2() else cnts2[1]
    
            if len(cnts2) > 1:      
                X1 = cnts2[0][0]
                X2 = cnts2[1][0]
                 
                cX1 = X1[0][0]
                cY1 = X1[0][1]
                cX2 = X2[0][0]
                cY2 = X2[0][1]
                
                # distance between obj1 and obj2
                dist1 = math.sqrt((cX1-cX2)**2 + (cY1-cY2)**2)
                
                
                if dist1 < 90:
                    cX2 = cX1
                    cY2 = cY1
                    radiuce_up_limit =100
                else:
                    radiuce_up_limit =60
                
           
            
            cv2.circle(frame, (cX1, cY1), red, (0, 255, 255), 3)
            cv2.circle(frame, (cX2, cY2), red, (0, 255, 255), 3)
            cv2.putText(frame,'Breathing',(10,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),1,cv2.LINE_AA)
            cv2.imshow('Frame',frame)
        else:
            t = t+1
            if t > 40:
                if  lab_stats[1:, 4].size > 0 and start == 1:
                    
                    t = 0
                cv2.putText(frame,'Not Breathing',(10,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1,cv2.LINE_AA)
                cv2.imshow('Frame',frame)
            else:
                cv2.circle(frame, (cX1, cY1), red, (0, 255, 255), 3)
                cv2.circle(frame, (cX2, cY2), red, (0, 255, 255), 3)
                cv2.putText(frame,'Breathing',(10,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),1,cv2.LINE_AA)
                cv2.imshow('Frame',frame)
            previous_frame = current_frame
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    
Tk().withdraw()
vid_path = askopenfilename(filetypes =(("Video File", "*.mp4"),("Video File","*.avi"),("Video File", "*.flv"),("All Files","*.*")),
                           title = "Choose a video.")

no_of_threads = 1
var_blur = 3
thred = []
jobs = []
for i in range(0, no_of_threads):

 thred = threading.Thread(target=main)
 jobs.append(thred)


for j in jobs:
 j.start()

for j in jobs:
 j.join()   
#    
#    
#    
    
    
    
    
    
    
    
