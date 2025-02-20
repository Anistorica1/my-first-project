import pyautogui as pa
import time
## 鼠标移动  --> 最小写0，最大写分辨率-1
pa.moveTo(100, 100)
## 鼠标移动时间
pa.moveTo(100, 100,duration=1)  #  鼠标要用一秒的时间到达这个位置
## 鼠标偏移 -->偏  ,且当前鼠标位置不能是(0,0)
pa.move(100, 100,duration=1)
## 获取屏幕分辨率
x,y = pa.size()
print(x,y)
## 获取当前鼠标位置
x,y = pa.position()
print(x,y)
## 实时获取鼠标位置
# x,y = pa.position()
# while True:
#     x1,y1 = pa.position()
#     if x1 != x or y1 != y:  # 这个有点东西，鼠标不动的时候就不会输出坐标了
#         x = x1
#         y = y1
#         print(x,y)  # 这里是死循环

## 鼠标点击（默认左键单击）
pa.moveTo(100,100)
time.sleep(1)  # 最好弄一个延迟，不然会报错
pa.click(clicks = 1,interval = 2,button = 'right',duration = 1)   # click 方法，前面两个参数传坐标，
# 第三个传点几下,第四个表间隔，点击的间隔,第五个是选择左右中,duration功能同上
## 鼠标按住
pa.mouseDown()
time.sleep(3)
## 鼠标抬起
pa.mouseUp()
## 鼠标滑轮，正数向上滑动，负数向下滑动
pa.click()
time.sleep(1)
pa.scroll(1000)  # 这个滑轮你要注意有没有选中窗口

## 键盘输入
pa.click()
time.sleep(1)
pa.write('123',interval = 1)  # interval 可传入打每个字的间隔
## 按键输入
pa.click()
time.sleep(1)
pa.press('f5',presses= 2)  # presses 是按多少次
## 组合按键
pa.hotkey('ctrl','v')  # 组合按键就是这么输入的
## 按键按住，抬起
pa.keyDown('shift')
pa.keyUp('shift')
## 屏幕截图
pa.screenshot('screenshot.png',region=(1,1,100,100))  # 可写绝对路径，也可以写相对路径，相对路径保存在project的目录下
# 这里的region指的是截取范围
## 消息框
pa.alert('alert','title')  # 第一个传内容，第二个是标题，第三个是确定按钮的内容
# 这个有暂停的效果

##

