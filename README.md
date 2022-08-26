# WebCrawler
## Check out the valid URLs.

### You are free to fork this Repl, as it is now a template.
# Introduction
To use WebCrawler, basically press the Run button with an arrow next to it.
```
Input URL, type "STOP" without the quotes to stop: 
```
Make sure to type a URL, so here's an example:
```
Input URL, type "STOP" without the quotes to stop: https://example.com
```
Now just press the Enter key or Return or whatever you use to send the input to the program.
Type STOP in the next input when you're done.
It will check if `https://example.com` is a valid URL!
```
https://example.com is a valid URL!
```
As you can see, it succeded because https://example.com is an accessible website!
# Developer API
To use the developer API, just use our api.py file and import it anywhere!
## Introduction
### CheckURL
###### function CheckURL(URL)
CheckURL is a function that lets you check 1 URL.
Example usage is shown below.
```py
from api import CheckURL
google = CheckURL("https://www.google.com")
```
To check if it is valid or invalid, a key note is
```py
if google == True:
  print("Then it's valid!")
elif google == False: # Otherwise:
  print("It's invalid!")
```
### CheckURLs
###### function CheckURLs(URLTable)
CheckURLs is a function that lets you check lots of URLs. Lists and Tuples only.
Example usage is shown below.
List:
```py
from api import CheckURLs
google = CheckURLs(["https://www.google.com","https://www.anistick.com"])
print(google)
```
Tuple:
```py
from api import CheckURLs
google = CheckURLs(("https://www.google.com","https://www.anistick.com",))
print(google)
```
### CheckURLs_Legacy
###### function CheckURLs_Legacy(URLTable,IsTuple)
CheckURLs_Legacy is a function that lets you check lots of URLs. Lists and Tuples only.
Example usage is shown below.
List:
```py
from api import CheckURLs_Legacy
# False because it is not a tuple
google = CheckURLs(["https://www.google.com","https://www.anistick.com"],false)
print(google)
```
Tuple:
```py
from api import CheckURLs_Legacy
# True because it is a tuple
google = CheckURLs(("https://www.google.com","https://www.anistick.com",),true)
print(google)
```