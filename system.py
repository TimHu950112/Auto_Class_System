from datetime import datetime
import webbrowser
from subprocess import call

url = {
    "國文": "https://meet.google.com/_meet/ndn-hkpt-ano",
    "數學": "https://meet.google.com/_meet/che-wwot-gmq",
    "英文": "https://meet.google.com/_meet/rss-qpob-dfm",
    "化學": "https://cgsh208.neocities.org/error.html",
    "探究": "https://meet.google.com/kzw-mmkr-hcu",
    "力學": "https://meet.google.com/gse-bypj-kid",
    "公民": "https://meet.google.com/dhz-tgrf-bsc",
    "歷史": "https://meet.google.com/keg-jozc-jod",
    "音樂": "https://meet.google.com/okr-gipi-ung",
    "家政": "https://meet.google.com/cmj-vxxt-xow",
    "國防": "https://meet.google.com/khk-twen-fsh",
    "測試":"https://meet.google.com/khk-twen-fsh"
}

today = datetime.today().weekday()
timetable = {
    0: {"英文": ["8:00", "10:00"], "數學": ["10:00", "11:00"], "國文": ["11:00", "12:00"], "化學": ["13:00", "14:00"], "公民": ["14:00", "16:10"], "小璧": ["16:15", "17:10"]},
    1: {"數學": ["8:00", "10:00"], "探究": ["10:00", "12:00"], "音樂": ["13:00", "14:00"], "體育": ["14:00", "15:00"], "國防": ["15:00", "16:10"]},
    2: {"數學": ["8:00", "9:00"], "英文": ["9:00", "10:00"], "家政": ["10:00", "12:00"], "歷史": ["13:00", "14:00"], "國文": ["14:00", "16:10"]},
    3: {"力學": ["8:00", "9:00"], "英文": ["9:00", "10:00"], "選修": ["11:00", "12:00"], "彈性": ["13:00", "16:10"]},
    4: {"化學": ["8:00", "9:00"], "體育": ["9:00", "10:00"], "英文": ["10:00", "11:00"], "歷史": ["11:00", "12:00"], "國文": ["13:00", "14:00"], "力學": ["14:00", "15:00"], "社團": ["15:00", "16:10"]},
    5:{"測試":["20:00","21:00"],},
    6:{"測試":["20:00","21:00"]}
}

def show_notification(message):
    cmd = 'display notification \"' + message + '\" with title \"自動上線系統\"'
    call(["osascript", "-e", cmd])

def main():
    if today not in timetable:
        show_notification("找不到對應課程或不是上課時間")
        return
    
    current_time = datetime.now().strftime("%H:%M")
    for subject, times in timetable[today].items():
        start_time = times[0]
        end_time = times[1]
        if start_time <= current_time < end_time:
            show_notification("這節是" + subject + "課")
            webbrowser.open(url[subject])
            break
    else:
        show_notification("找不到對應課程或不是上課時間")

if __name__ == "__main__":
    main()