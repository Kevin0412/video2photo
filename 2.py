import cv2
import numpy as np
import os
name='starsky4'#文件名
vc=cv2.VideoCapture(name+'.mp4')
n=1
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
timeF = 1
i = 0
video=cv2.VideoWriter(name+'_2.mp4',cv2.VideoWriter_fourcc('I','4','2','0'),vc.get(5),(frame.shape[1],frame.shape[0]))
while rval:#亮度最大值
    if (n % timeF == 0 and rval and n>0):#n:需要处理的帧的范围
        i += 1
        if i==1:
            imgq=frame*0
        frame1=frame.astype(np.float64)[:,:,0]*0.114+frame.astype(np.float64)[:,:,1]*0.587+frame.astype(np.float64)[:,:,2]*0.299
        imgq1=imgq.astype(np.float64)[:,:,0]*0.114+imgq.astype(np.float64)[:,:,1]*0.587+imgq.astype(np.float64)[:,:,2]*0.299
        imgq[:,:,0]+=((frame[:,:,0].astype(np.float64)-imgq[:,:,0].astype(np.float64))*(((frame1.astype(np.float64)-imgq1.astype(np.float64)+2**-1024)/abs(frame1.astype(np.float64)-imgq1.astype(np.float64)+2**-1024)+1)/2)).astype(np.uint8)
        imgq[:,:,1]+=((frame[:,:,1].astype(np.float64)-imgq[:,:,1].astype(np.float64))*(((frame1.astype(np.float64)-imgq1.astype(np.float64)+2**-1024)/abs(frame1.astype(np.float64)-imgq1.astype(np.float64)+2**-1024)+1)/2)).astype(np.uint8)
        imgq[:,:,2]+=((frame[:,:,2].astype(np.float64)-imgq[:,:,2].astype(np.float64))*(((frame1.astype(np.float64)-imgq1.astype(np.float64)+2**-1024)/abs(frame1.astype(np.float64)-imgq1.astype(np.float64)+2**-1024)+1)/2)).astype(np.uint8)
        video.write(imgq)
        print(i)
        cv2.imshow('img',cv2.resize(imgq,(1280,720)))
    rval, frame = vc.read()
    n = n + 1
    cv2.waitKey(1)
cv2.destroyAllWindows()
vc.release()
video.release()
