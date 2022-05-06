# video2photo
Use python to composite star trail picture.
使用python合成星轨图片。
1.py and 2.py are two methods to make star trail video.1 is weighted average of (xn-average(x))^2.2 is maxima.
1.py和2.py是合成星轨视频的两种算法。1是方差加权平均。2是最大值。
2 can show more stars,but the picture quality of the result may not good.1 shows fewer stars,but a better picture quality.
2可以展示更多星星，但画质不一定好。1展示的星星少一点，但画质高。
2 is recommended in sunny nights without any cloud.1 is recommended in nights with a little cloud or nights with lots of stars especially in suburbs.
2建议在无云的晴夜使用。1建议在有少量云的夜晚使用或者类似郊区这种有许多星的。
Stars can be seen in cities.
城市里能看到星星。
analyze.py is a tool to know the brightness of your video,which can help you to decide your range.
analyze.py是一个展示亮度的工具，可帮助你确定范围。
pltshow.py shows a picture in matplotlib.pyplot.
pltshow.py在matplotlib.pyplot中展示图片。
