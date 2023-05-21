from vncdotool import api

# 创建 VNC 会话
vnc = api.connect('10.151.116.71:1')

#vnc.mouseMove(315, 300)
#print(vnc.x)
#vnc.mousePress(1)
#vnc.mouseMove(270, 885)
#print(vnc.x)
#vnc.mousePress(1)

vnc.keyPress('1')
vnc.captureScreen('screen.png')
print('screen ok')

