import time

def getWorkTime():
    names = {}
    try:
        while True:
            print("press 'Enter' to continue!!")
            input()
            name = input("Enter your name: ")
            if name not in names.keys():
                startTime = time.time()
                names[name] = startTime
                print("begin to work!")     
            else:
                endTime = time.time()
                print("end work time:",round(endTime,2))
                print("work time:",round(endTime-names[name],2))
    except KeyboardInterrupt:
        print("End!!")

# 10秒后启动程序

while True:
    time.sleep(12)
    if time.sleep(12) == True:
        print("Today ends!")
    time.sleep(12)
    print("Today begins!")
    getWorkTime()
