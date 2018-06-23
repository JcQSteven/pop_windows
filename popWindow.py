import win32api,win32con,win32gui
import threading
import time 
import random
import winsound
def alert(num):
    win32api.MessageBox(0, "test", str(num),win32con.MB_OK)

def play_music():
    winsound.Beep(2000,50)
def setWallPaper(pic):
    # open register
    regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # refresh screen
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,pic, win32con.SPIF_SENDWININICHANGE)
def foo(hwnd,mouse):
  if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
 


if __name__ == "__main__":

    win32gui.EnumWindows(foo, 0)

    pic='C:\Users\king_\Desktop\1.jpeg'


    num_1=20   #totle windows number
    num_2=20
    num_3=20
    num_4=16
    decrise=30
    count_w=0
    count_h=0
    thread_list=[]
    hwnd_list=[]
    width=win32api.GetSystemMetrics(0)
    height=win32api.GetSystemMetrics(1)
    size_w=200
    size_h=100
    
    #left
    for i in range(num_1):#open windows
        i=threading.Thread(target=alert,args=(i,))
        i.start()
    for i in range(num_1):#change position
        #print(i)
        time.sleep(0.1)
        w=win32gui.FindWindow(None,str(i))
        win32gui.SetWindowPos(w, win32con.HWND_TOPMOST, count_w,count_w,size_w,size_h, win32con.SWP_SHOWWINDOW)
        count_w=count_w+decrise
        play_music()
    for i in range(num_1):#close windows
        w=win32gui.FindWindow(None,str(i))
        win32gui.SendMessage(w, win32con.WM_CLOSE)

    #random
    for i in range(num_2):#open windows
        i=threading.Thread(target=alert,args=(i,))
        i.start()
    tmp=count_w
    for i in range(num_2):#change position
        #print(i)
        time.sleep(0.1)
        w=win32gui.FindWindow(None,str(i))
        win32gui.SetWindowPos(w, win32con.HWND_TOPMOST, count_w,random.randint(tmp-200,tmp+200),size_w,size_h, win32con.SWP_SHOWWINDOW)
        count_w=count_w+decrise
        play_music()
    for i in range(num_2):#close windows
        w=win32gui.FindWindow(None,str(i))
        win32gui.SendMessage(w, win32con.WM_CLOSE)
    
    #right
    for i in range(num_3):#open windows
        i=threading.Thread(target=alert,args=(i,))
        i.start()
    for i in range(num_3):#change position
        time.sleep(0.1)
        w=win32gui.FindWindow(None,str(i))
        if i%2==0:
            win32gui.SetWindowPos(w, win32con.HWND_TOPMOST, width-size_w,count_h,int(size_w/2),int(size_h/2), win32con.SWP_SHOWWINDOW)
        else:
            win32gui.SetWindowPos(w, win32con.HWND_TOPMOST, width-size_w,count_h,size_w,size_h, win32con.SWP_SHOWWINDOW)
        play_music()
        width=width-decrise
        count_h=count_h+decrise
    for i in range(num_3):#close windows
        w=win32gui.FindWindow(None,str(i))
        win32gui.SendMessage(w, win32con.WM_CLOSE)

    
    #center
    count_w=0
    count_h=0
    for i in range(num_4):#open windows
        i=threading.Thread(target=alert,args=(i,))
        i.start()
    for i in range(num_4):#change position
        time.sleep(0.1)
        w=win32gui.FindWindow(None,str(i))
        # for i in range(4):
        print(count_w)
        # print(count_h)
        win32gui.SetWindowPos(w, win32con.HWND_TOPMOST,count_w,count_h,int(width/4),int(height/4), win32con.SWP_SHOWWINDOW)
        play_music()
        count_w=int(width/4 * (i%4))
        count_h=int(height/4 * (i/4))

    for i in range(num_4):#close windows
        w=win32gui.FindWindow(None,str(i))
        win32gui.SendMessage(w, win32con.WM_CLOSE)



