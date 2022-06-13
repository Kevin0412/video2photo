import cv2
import numpy as np
import os
name='starsky5'#文件名
vc = cv2.VideoCapture(name+'.mp4')
n = 1
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
timeF = 1
i = 0
imgo=frame.astype(np.float)[:,:,0]*0
imgp=frame.astype(np.float)[:,:,0]*0
while rval:#求平均
    if (n % timeF == 0 and rval and n in range(9,551)):#n:需要处理的帧的范围
        i += 1
        imgo+=frame.astype(np.float)[:,:,0]*0.114+frame.astype(np.float64)[:,:,1]*0.587+frame.astype(np.float64)[:,:,2]*0.299
        print(i)
    rval, frame = vc.read()
    n = n + 1
    cv2.waitKey(1)
vc.release()
imgo=imgo/i
vc = cv2.VideoCapture(name+'.mp4')
video=cv2.VideoWriter(name+'_1.mp4',cv2.VideoWriter_fourcc('I','4','2','0'),vc.get(5),(imgo.shape[1],imgo.shape[0]))
n = 1
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
timeF = 1
i = 0
while rval:#由该像素点与平均的亮度差的平方为权重加权平均
    if (n % timeF == 0 and rval and n>8):#n:需要处理的帧的范围
        i += 1
        if i==1:
            img=(frame*0).astype(np.float64)
        frame1=frame.astype(np.float64)[:,:,0]*0.114+frame.astype(np.float64)[:,:,1]*0.587+frame.astype(np.float64)[:,:,2]*0.299
        imgp+=(frame1-imgo)**2+2**-1024
        img[:,:,0]+=frame[:,:,0].astype(np.float64)*((frame1-imgo)**2+2**-1024)
        img[:,:,1]+=frame[:,:,1].astype(np.float64)*((frame1-imgo)**2+2**-1024)
        img[:,:,2]+=frame[:,:,2].astype(np.float64)*((frame1-imgo)**2+2**-1024)
        img1=frame*0
        img1[:,:,0]=(img[:,:,0]/imgp+0.5)
        img1[:,:,1]=(img[:,:,1]/imgp+0.5)
        img1[:,:,2]=(img[:,:,2]/imgp+0.5)
        video.write(img1.astype(np.uint8))
        cv2.imshow('img1',cv2.resize(img1.astype(np.uint8),(1280,720)))
        cv2.waitKey(1)
        print(i)
    rval, frame = vc.read()
    n = n + 1
    cv2.waitKey(1)
cv2.destroyAllWindows()
vc.release()
video.release()
