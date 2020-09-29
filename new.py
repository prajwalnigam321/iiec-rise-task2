#! /usr/bin/python3

print("Content-type:text/html")
print()

import pyttsx3
import os
import subprocess 
import cgi
pyttsx3.speak("welcome")

cmd=cgi.FieldStorage()
value=cmd.getvalue("cmd")


choice=value
which True:
  if('date' in choice .lower())or('what is today' in choice.lower()):
   ret=subprocess.getoutput('date')
   print(ret)
   print(f"todays date is :{ret}")
  elif('firefox' in choice.lower())or("web browser" in choice.lower()):
   ret=subprocess.getoutput("firfox")
   print("we have started firefox")
  elif('calendar' in choice.lower())or ('cal' in choice.lower()):
   ret=subprocess.getoutput("cal")
   print(f"This month calendar:{ret}")
  elif("gedit" in choice.lower()) or("text editor" in choice.lower())or("notepad" in choice.lower()):
   print("the text editor was opened..")
   ret=subprocess.getoutput("sudo gedit")
   print(ret)
  else: 
   print("we can't understand ")











