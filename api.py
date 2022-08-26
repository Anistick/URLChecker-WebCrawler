# Developer API
import requests
def CheckURL(URL):
  def iv():
    return False
  def v():
    return True
    r = None
    try:
      r = requests.get(URL)
      if r.status_code == 200:
        v()
      else:
        iv()
    except:
      iv()

def CheckURLs_Legacy(URLTable,IsTuple):
  if not IsTuple:
    ValidTable = []
    for URL in URLTable:
      def iv():
        URL = False
        ValidTable.append(URL)
      def v():
        URL = True
        ValidTable.append(URL)
      r = None
      try:
        r = requests.get(URL)
        if r.status_code == 200:
          v()
        else:
          iv()
      except:
        iv()

    return ValidTable

  if IsTuple:
    global ValidTuple
    ValidTuple = ()
    for URL in URLTable:
      def iv():
        global ValidTuple
        ValidTuple += (False,)
      def v():
        global ValidTuple
        ValidTuple += (True,)
      r = None
      try:
        r = requests.get(URL)
        if r.status_code == 200:
          v()
        else:
          iv()
      except:
        iv()
    
    return ValidTuple

def TupleIs(obj):
  if type(obj) == tuple:
    return True
  else:
    return False

def CheckURLs(URLTable):
  if not TupleIs(URLTable):
    ValidTable = []
    for URL in URLTable:
      def iv():
        URL = False
        ValidTable.append(URL)
      def v():
        URL = True
        ValidTable.append(URL)
      r = None
      try:
        r = requests.get(URL)
        if r.status_code == 200:
          v()
        else:
          iv()
      except:
        iv()

    return ValidTable

  if TupleIs(URLTable):
    global ValidTuple
    ValidTuple = ()
    for URL in URLTable:
      def iv():
        global ValidTuple
        ValidTuple += (False,)
      def v():
        global ValidTuple
        ValidTuple += (True,)
      r = None
      try:
        r = requests.get(URL)
        if r.status_code == 200:
          v()
        else:
          iv()
      except:
        iv()
    
    return ValidTuple
