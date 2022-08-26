import requests
import replit as rep
EOF = "STOP"
URLTable = []
def itr():
  for URL in URLTable:
    def iv():
      print(f"{URL} is an invalid URL!")
    def v():
      print(f"{URL} is a valid URL!")
    r = None
    try:
      r = requests.get(URL)
      if r.status_code == 200:
        v()
      else:
        iv()
    except:
      iv()

def inp():
  lne = input(f"Input URL, type \"{EOF}\" without the quotes to stop: ")
  if (lne != EOF):
    URLTable.append(lne)
    inp()
  else:
    rep.clear()
    itr()
inp()