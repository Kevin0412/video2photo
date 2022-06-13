import cv2
import numpy as np
import os
name='starsky3'#文件名
vc=cv2.VideoCapture(name+'.mp4')
n=1
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
timeF = 1
i = 0
video=cv2.VideoWriter(name+'_5.mp4',cv2.VideoWriter_fourcc('H','2','6','5'),vc.get(5),(frame.shape[1],frame.shape[0]))
while rval:#两帧差最大值
    if (n % timeF == 0 and rval and n>3):#n:需要处理的帧的范围
        i += 1
        if i==1:
            img1=frame.astype(np.float64)[:,:,0]*0.114+frame.astype(np.float64)[:,:,1]*0.587+frame.astype(np.float64)[:,:,2]*0.299
        elif i==2:
            img2=frame.astype(np.float64)[:,:,0]*0.114+frame.astype(np.float64)[:,:,1]*0.587+frame.astype(np.float64)[:,:,2]*0.299
            img=frame
            imgp=(frame[:,:,0]*0).astype(np.float64)
            imgq=img*0
        else:
            img3=frame.astype(np.float64)[:,:,0]*0.114+frame.astype(np.float64)[:,:,1]*0.587+frame.astype(np.float64)[:,:,2]*0.299
            imgo=abs(img2*2-img1-img3)
            mask=(abs(imgo-imgp+2**-1024)/(imgo-imgp+2**-1024)+1)/2
            imgp+=(imgo-imgp)*mask
            imgq[:,:,0]=img[:,:,0]*mask+imgq[:,:,0]*(1-mask)
            imgq[:,:,1]=img[:,:,1]*mask+imgq[:,:,1]*(1-mask)
            imgq[:,:,2]=img[:,:,2]*mask+imgq[:,:,2]*(1-mask)
            img1=img2
            img2=img3
            img=frame
            video.write(imgq)
            cv2.imshow('img',cv2.resize(imgq,(1280,720)))
        print(i)
    rval, frame = vc.read()
    n = n + 1
    cv2.waitKey(1)
cv2.destroyAllWindows()
vc.release()
video.release()
