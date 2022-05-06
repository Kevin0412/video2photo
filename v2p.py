import cv2
import numpy as np
import os
name='starsky4'#文件名
vc = cv2.VideoCapture(name+'.mp4')  # 读入视频文件，命名cv
n = 1  # 计数
if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
    rval = False
timeF = 1  # 视频帧计数间隔频率
i = 0
while rval:  # 循环读取视频帧
    if (n % timeF == 0 and rval and n in range(1,557)):  #n:帧范围
        i += 1
        if i==1:
            imgo=frame.astype(np.int32)
            imgp=frame.astype(np.int32)**2
            imgq=frame*0
            imgr=frame*0+255
        else:
            imgo+=frame
            imgp+=frame.astype(np.int32)**2
        frame1=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        imgq1=cv2.cvtColor(imgq,cv2.COLOR_BGR2GRAY)
        imgq[:,:,0]+=((frame[:,:,0].astype(np.float16)-imgq[:,:,0].astype(np.float16))*(((frame1.astype(np.float16)-imgq1.astype(np.float16)+0.5)/abs(frame1.astype(np.float16)-imgq1.astype(np.float16)+0.5)+1)/2)).astype(np.uint8)
        imgq[:,:,1]+=((frame[:,:,1].astype(np.float16)-imgq[:,:,1].astype(np.float16))*(((frame1.astype(np.float16)-imgq1.astype(np.float16)+0.5)/abs(frame1.astype(np.float16)-imgq1.astype(np.float16)+0.5)+1)/2)).astype(np.uint8)
        imgq[:,:,2]+=((frame[:,:,2].astype(np.float16)-imgq[:,:,2].astype(np.float16))*(((frame1.astype(np.float16)-imgq1.astype(np.float16)+0.5)/abs(frame1.astype(np.float16)-imgq1.astype(np.float16)+0.5)+1)/2)).astype(np.uint8)
        imgr1=cv2.cvtColor(imgr,cv2.COLOR_BGR2GRAY)
        imgr[:,:,0]-=((imgr[:,:,0].astype(np.float16)-frame[:,:,0].astype(np.float16))*((1-(frame1.astype(np.float16)-imgr1.astype(np.float16)-0.5)/abs(frame1.astype(np.float16)-imgr1.astype(np.float16)-0.5))/2)).astype(np.uint8)
        imgr[:,:,1]-=((imgr[:,:,1].astype(np.float16)-frame[:,:,1].astype(np.float16))*((1-(frame1.astype(np.float16)-imgr1.astype(np.float16)-0.5)/abs(frame1.astype(np.float16)-imgr1.astype(np.float16)-0.5))/2)).astype(np.uint8)
        imgr[:,:,2]-=((imgr[:,:,2].astype(np.float16)-frame[:,:,2].astype(np.float16))*((1-(frame1.astype(np.float16)-imgr1.astype(np.float16)-0.5)/abs(frame1.astype(np.float16)-imgr1.astype(np.float16)-0.5))/2)).astype(np.uint8)
        print(i)
    rval, frame = vc.read()
    n = n + 1
    cv2.waitKey(1)
vc.release()
img2=(imgo.astype(np.float)/i+0.5).astype(np.uint8)
img3=((imgp.astype(np.float)/i-(imgo.astype(np.float)/i)**2)**0.5*2+0.5).astype(np.uint8)
cv2.imwrite(name+'_2.png',img3)
cv2.imwrite(name+'_1.png',img2)
cv2.imwrite(name+'_3.png',imgq)
cv2.imwrite(name+'_4.png',imgr)
cv2.destroyAllWindows()
img1=cv2.imread(name+'_1.png')
img2=cv2.imread(name+'_3.png')
img3=cv2.imread(name+'_4.png')
imgg1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY).astype(np.float64)
imgg2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY).astype(np.float64)
imgg3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY).astype(np.float64)
img1[:,:,0]=img2[:,:,0]*(imgg2-imgg1+2**-52)/(imgg2-imgg3+2**-51)+img3[:,:,0]*(imgg1-imgg3+2**-52)/(imgg2-imgg3+2**-51)
img1[:,:,1]=img2[:,:,1]*(imgg2-imgg1+2**-52)/(imgg2-imgg3+2**-51)+img3[:,:,1]*(imgg1-imgg3+2**-52)/(imgg2-imgg3+2**-51)
img1[:,:,2]=img2[:,:,2]*(imgg2-imgg1+2**-52)/(imgg2-imgg3+2**-51)+img3[:,:,2]*(imgg1-imgg3+2**-52)/(imgg2-imgg3+2**-51)
cv2.imwrite(name+'_5.png',img1)