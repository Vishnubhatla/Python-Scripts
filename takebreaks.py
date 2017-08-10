import time
import webbrowser
i=1
print("Breaks started from: "+time.ctime())
while(i<=3) :
    time.sleep(5)
    webbrowser.open("https://github.com/bmorelli25/Become-A-Full-Stack-Web-Developer")
    i=i+1

print("breaks done")
