import cv2
import numpy as np
import os
name='starsky3'
vc = cv2.VideoCapture(name+'.mp4')  # 读入视频文件，命名cv
n = 1  # 计数
if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
    rval = False
timeF = 1  # 视频帧计数间隔频率
i = 0
imgo=frame.astype(np.float)[:,:,0]*0
imgp=frame.astype(np.float)[:,:,0]*0
while rval:  # 循环读取视频帧
    if (n % timeF == 0 and rval and n>4):  # 每隔timeF帧进行存储操作
        i += 1
        imgo+=frame.astype(np.float)[:,:,0]*0.114+frame.astype(np.float)[:,:,1]*0.587+frame.astype(np.float)[:,:,2]*0.299
        imgp+=(frame.astype(np.float)[:,:,0]*0.114+frame.astype(np.float)[:,:,1]*0.587+frame.astype(np.float)[:,:,2]*0.299)**2
        print(i)
    rval, frame = vc.read()
    n = n + 1
    cv2.waitKey(1)
vc.release()
imgo=imgo/i
imgp=(imgp/i-imgo**2)*i
vc = cv2.VideoCapture(name+'.mp4')  # 读入视频文件，命名cv
n = 1  # 计数
if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
    rval = False
timeF = 1  # 视频帧计数间隔频率
i = 0
while rval:  # 循环读取视频帧
    if (n % timeF == 0 and rval and n>4):  # 每隔timeF帧进行存储操作
        i += 1
        if i==1:
            img=(frame*0).astype(np.float)
        frame1=frame.astype(np.float)[:,:,0]*0.114+frame.astype(np.float)[:,:,1]*0.587+frame.astype(np.float)[:,:,2]*0.299
        img[:,:,0]+=frame[:,:,0].astype(np.float)*((frame1-imgo)**2+2**-52)
        img[:,:,1]+=frame[:,:,1].astype(np.float)*((frame1-imgo)**2+2**-52)
        img[:,:,2]+=frame[:,:,2].astype(np.float)*((frame1-imgo)**2+2**-52)
        print(i)
    rval, frame = vc.read()
    n = n + 1
    cv2.waitKey(1)
vc.release()
img[:,:,0]=(img[:,:,0]/(imgp+2**-52*i)+0.5)
img[:,:,1]=(img[:,:,1]/(imgp+2**-52*i)+0.5)
img[:,:,2]=(img[:,:,2]/(imgp+2**-52*i)+0.5)
cv2.imwrite(name+'_6.png',img)