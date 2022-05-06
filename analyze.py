import cv2
import numpy as np
import os
def time_add(time,seconds):
    if seconds in range(-86400,86401):
        time[5]+=seconds
        time[4]+=round(time[5]/60-0.5+2**-53)
        time[3]+=round(time[4]/60-0.5+2**-53)
        time[2]+=round(time[3]/24-0.5+2**-53)
        time[5]=time[5]%60
        time[4]=time[4]%60
        time[3]=time[3]%24
        if time[2] in range(1,28):
            pass
        else:
            if time[2]==29:
                if time[1]==2 and time[0]%4!=0:
                    time[2]=1
                    time[1]=3
            elif time[2]==30:
                if time[1]==2 and time[0]%4==0:
                    time[2]=1
                    time[1]=3
            elif time[2]==31:
                if time[1] in [4,6,9,11]:
                    time[2]=1
                    time[1]+=1
            elif time[2]==32:
                if time[1] in [1,3,5,7,8,10]:
                    time[2]=1
                    time[1]+=1
                else:
                    time[2]=1
                    time[1]=1
                    time[0]+=1
            elif time[2]==0:
                if time[1] in [2,4,6,8,9,11]:
                    time[2]=31
                    time[1]-=1
                elif time[1] in [5,7,10,12]:
                    time[2]=30
                    time[1]-=1
                elif time[1]==3:
                    if time[0]%4==0:
                        time[2]=29
                    else:
                        time[2]=28
                    time[1]-=1
                elif time[1]==1:
                    time[2]=31
                    time[1]=12
                    time[0]-=1
    else:
        if seconds>0:
            for n in range(round(seconds/86400-0.5+2**-53)):
                time_add(time,86400)
            time_add(time,seconds%86400)
        else:
            for n in range(-round(seconds/86400-0.5+2**-53)):
                time_add(time,-86400)
            time_add(time,seconds%86400)
name='starsky5'#文件名
time=[2022,5,5,4,35,30]#拍摄结束时间
time_add(time,-17985)#拍摄时长（秒）
vc = cv2.VideoCapture(name+'.mp4')
n = 1
if vc.isOpened():
    rval,frame=vc.read()
else:
    rval=False
timeF=1
i = 0
with open(name+'.csv','w+') as F:
    F.write('time,B,G,R,brightness,H,S,V\n')
    while rval:
        if (n % timeF == 0 and rval):
            frame=cv2.resize(frame,(1,1))
            hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            F.write(str(time[0])+'/'+str(time[1])+'/'+str(time[2])+' '+str(time[3])+':'+str(time[4])+':'+str(time[5])+','+\
                str(frame[0][0][0])+','+str(frame[0][0][1])+','+str(frame[0][0][2])+','+\
                    str(0.114*frame[0][0][0]+0.587*frame[0][0][1]+0.299*frame[0][0][2])+','+\
                        str(hsv[0][0][0])+','+str(hsv[0][0][1])+','+str(hsv[0][0][2])+'\n')
            time_add(time,30)#拍摄间隔（秒）
            i += 1
        rval, frame = vc.read()
        n = n + 1
        cv2.waitKey(1)
vc.release()