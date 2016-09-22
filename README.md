# Khinsider-Download-GUI
Downloads music from Khinsider.

# Instructions
Type in the name of an album from Khinsider.com and click the search button. A list of albums will popup. Select an album and click the select button. You have to select a song first before you can download the song, download the album or use any of the queue options.


# Goals From Finishing This Project
- Learn some basics of object oriented programming [x]
- Learn how to create a gui/executable file [x]

# What I Learned
I learned about methods and instance variables and how they interact with each other and other classes.
Oop is a pain in the butt. You can easily lose track of variables inside classes, especially if a class is inheriting another class. You have to be focused to keep track of all the variables you are currently working with.
Making an executable file is easier than I expected. I thought creating an executable file takes many lines of codes. All you need is to download a third party module to compile a script into an executable file.
I learned web scraping as a bonus from this project. I did not know what web scraping is until I started this project.

# Things I Can Improve On/ Do In The Future
Do not use tkinter. Tkinter have poor documentation and bad tutorials. Tkinter have many limitations that prevents you from making an aesthetically pleasing GUI.
I could make my classes smaller. I wasn’t sure whether to put functions inside classes as methods or to put them outside.
Use better variable names. I think some of my variable names are confusing, but I don’t know what to name them.
Document my code better.

# Thought Process Throughout The Project
Initially I was unsure what to code. I eventually decided to work on an executable file that allows you to download music from a website.
I did a lot of research before starting on this project. I learned that you needed to program a GUI before making it into an executable file. I decided to use tkinter instead of pyqt, as others claim that it is easier to use.
I started to look at the official tkinter document and it was horrible. The official document was designed for coders with prior knowledge of tkinter. Then, I spent days finding other websites for tkinter and tutorials for beginners for tkinter. After a couple of days I couldn’t find any good documents or tutorials for tkinter and I was losing hope. Miraculously, I came across the channel sentdex on youtube that have a tutorial on tkinter (https://www.youtube.com/playlist?list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk) and a decent tkinter document (http://effbot.org/tkinterbook/).
I started to work on program immediately. However, soon after a few line of codes, a syntax error kept causing my code to crash. I was unable to find the source of the error for a day or two.
After the I fixed the error, I started to work on simple GUI objects. And immediately I got a huge problem. I did not know how to get data from websites. I did a quick search on google about pulling data from websites and I learned about web scraping.
Coding this project went smooth after that. The only thing that annoyed me was the limitations of tkinter. I wanted to make my GUI look nice, but I couldn’t. Because of tkinter.
Once I finished coding my program, it was time for me to make it into an executable file. I downloaded the cx_Freeze module to compile my script. I kept getting errors from cx_Freeze and I couldn’t find the error. My exe file closes immediately, every time when I open it. I searched everywhere online, and every forum says cx_Freeze is compatible with Python 3.5 and they don’t know why there is any problems with it. After 5 hours of trying to fix my problem, I downloaded pyinstaller to compile my script, as it is compatible with Python 3.5. It worked. Then I uploaded this to GitHub and put all of this nonsense behind me.


# Time It Took To Complete This Project
Between a week to two weeks.
