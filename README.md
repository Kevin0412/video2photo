# video2photo
Use python to composite star trail picture.
使用python合成星轨图片。
1.py and 2.py are two methods to make star trail video.1 is weighted average of (xn-average(x))^2.2 is maxima.
1.py和2.py是合成星轨视频的两种算法。1是方差加权平均。2是最大值。
2 can show more stars,but the frame quality of the result may not good.1 shows fewer stars,but a better picture quality.
2可以展示更多星星，但画质不一定好。1展示的星星少一点，但画质高。
2 is recommended in sunny nights without any cloud.1 is recommended in nights with a little cloud or nights with lots of stars especially in suburbs.
2建议在无云的晴夜使用。1建议在有少量云的夜晚使用或者类似郊区这种有许多星的。
Stars can be seen in cities.
城市里能看到星星。
analyze.py is a tool to know the brightness of your video,which can help you to decide your range.
analyze.py是一个展示亮度的工具，可帮助你确定范围。
pltshow.py shows a picture in matplotlib.pyplot.
pltshow.py在matplotlib.pyplot中展示图片。
5.py and 6.py are also two methods to do such things.5 is maxima of the difference between three together frames,using the middle frame.6 is weighted average that the square of the difference between three together frames serves as the weight of the middle frame.
5.py和6.py也是合成的两种算法。5是取连续三帧差的最大值，取这三帧中的中间帧。6是加权平均，三帧之间的差的平方作为中间帧的权重。
6 is better than 1 in a bit cloudy situation.While 5 has a special style of image.1 has the best frame quality.2 is best for starry and sunny nights.You can use these four methods to make star trail video.videos recording moving things can also be processed into videos of movement track.Practice is the only criterion for testing truth.
在有少量云的情况下6比1好。5有一种特别的画面风格。1有最好的画质。2对满天星的晴朗夜晚最好。你可以使用这四种算法来合成星轨视频。拍摄运动物体的视频也能被处理成运动轨迹的视频。实践是检验真理的唯一标准。
