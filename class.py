#導入函式庫
from email.headerregistry import DateHeader
import sys
from time import monotonic
import webbrowser
import datetime
from subprocess import call

#設定連結、課表
url = {"國文":"https://meet.google.com/_meet/ndn-hkpt-ano","數學":"https://meet.google.com/_meet/che-wwot-gmq","英文":"https://meet.google.com/_meet/rss-qpob-dfm",
"化學":"https://cgsh208.neocities.org/error.html","探究":"https://meet.google.com/kzw-mmkr-hcu","力學":"https://meet.google.com/gse-bypj-kid","公民":"https://meet.google.com/dhz-tgrf-bsc ",
"歷史":"https://meet.google.com/keg-jozc-jod","音樂":"ttps://meet.google.com/okr-gipi-ung","家政":"https://meet.google.com/cmj-vxxt-xow","國防":"https://meet.google.com/khk-twen-fsh"}
Mon={"英文":["8:00","10:00"],"數學":["10:00","11:00"],"國文":["11:00","12:00"],"化學":["13:00","14:00"],"公民":["14:00","16:10"],"小璧":["16:15","17:10"]}
Tue={"數學":["8:00","10:00"],"探究":["10:00","12:00"],"音樂":["13:00","14:00"],"體育":["14:00","15:00"],"國防":["15:00","16:10"]}
Wed={"數學":["8:00","9:00"],"英文":["9:00","10:00"],"家政":["10:00","12:00"],"歷史":["13:00","14:00"],"國文":["14:00","16:10"]}
Thu={"力學":["8:00","9:00"],"英文":["9:00","10:00"],"選修":["11:00","12:00"],"彈性":["13:00","16:10"]}
Fri={"化學":["8:00","9:00"],"體育":["9:00","10:00"],"英文":["10:00","11:00"],"歷史":["11:00","12:00"],"國文":["13:00","14:00"],"力學":["14:00","15:00"],"社團":["15:00","16:10"]}
time=[Mon,Tue,Wed,Thu,Fri]

#定義錯誤訊息
def error():
    print("找不到對應課程或不是上課時間")
    cmd = 'display notification \"' + \
    "❌找不到對應課程或不是上課時間❌" + '\" with title \"自動上線系統\"'
    call(["osascript", "-e", cmd])

#取得時間
datetime.datetime.today()
weekday=datetime.datetime.today().weekday()
sys.path.append("libs") 

#dict to list
list_value=list(time[weekday].values())
list_key=list(time[weekday])

n=0 #set index
while True:
    try:
        d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + str(list_value[n][0]), '%Y-%m-%d%H:%M') #取得課程開始時間
        d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + str(list_value[n][1]), '%Y-%m-%d%H:%M') #取得課程結束時間
        n_time = datetime.datetime.now() #取得當前時間
        if n_time > d_time and n_time < d_time1:
            break
        n+=1
    except:
        error()
        break
#通知
try:
    print(list_key[n]+"課") #顯示課程名稱
    #傳送通知
    cmd = 'display notification \"' + \
        "這節是"+str(list_key[n])+"課" + '\" with title \"自動上線系統\"'
    call(["osascript", "-e", cmd])  
    webbrowser.open(url[list_key[n]]) #打開該課程網頁
except:
    pass



