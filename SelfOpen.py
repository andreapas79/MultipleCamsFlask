import webbrowser

import socket
def open_Ip():
    try:
        print('ok')
        hname = socket.gethostname()
        hip = socket.gethostbyname(hname)
    except:
        print("Unable to get Hostname and IP")
    finally:
        webbrowser.open_new_tab('http://{}:3000'.format(hip))