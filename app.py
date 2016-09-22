import tkinter as tk
from tkinter import ttk
from tkinter import BOTH, END, LEFT, YES, ACTIVE

from bs4 import BeautifulSoup
import requests

import time
import re
import os

#Change download directory to desktop
os.chdir(os.path.join(os.getenv('userprofile'),'Desktop'))
def popupmsg(msg):
	popup = tk.Tk()
	popup.wm_title('ERROR')
	label = ttk.Label(popup, text=msg, font=('Times New Roman', 12))
	label.grid(row=0)
	button = ttk.Button(popup, text='Okay', command=popup.destroy)
	button.grid(row=1)
	popup.mainloop()

class App(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		tk.Tk.wm_title(self, 'Program')
		container = tk.Frame(self)
		container.grid(sticky='nsew')

		self.frames = {}
		for F in (Tutorial, Home):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='nsew')
		self.show_frame(Tutorial)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class Tutorial(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label1 = tk.Label(self, text='Page One', font=('Times New Roman', 12))
		label1.pack(pady=10, padx=10)
		label2 = tk.Label(self, text='''Search a song with the search bar then
click the search button. Click on an
album and click the select button. You
can then do whatever you want. The files
are downloaded to your desktop.''')
		label2.pack(pady=10, padx=10)
		button1 = tk.Button(self, text='Okay',\
							command=lambda: controller.show_frame(Home))
		button1.pack()

class Home(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='Home', font=('Times New Roman', 12))
		label.grid(column=2, sticky='n')

		button1 = ttk.Button(self, text='Back to instructions',\
								command=lambda:controller.show_frame(Tutorial))
		button2 = ttk.Button(self, text='Search',\
								command=lambda:self.search_bar())
		button3 = ttk.Button(self, text ='Select', command=lambda:self.album())
		button4 = ttk.Button(self, text='Download',\
								command=lambda:self.download())
		button5 = ttk.Button(self, text='Add to queue',\
								command=lambda:self.add_queue())
		button6 = ttk.Button(self, text='Check queue',\
								command=lambda:self.check_queue())
		button7 = ttk.Button(self, text='Download Album',\
								command=lambda:self.download_album())
		button8 = ttk.Button(self, text='Download queue',\
								command=lambda:self.download_queue())
		button9 = ttk.Button(self, text='Clear queue',\
								command=lambda:self.clear_queue())
		button10 = ttk.Button(self, text='Check size',\
								command=lambda:self.size())
		button1.grid(row=0, column=0, sticky='nw')
		button2.grid(row=1, column=11, sticky='e')
		button3.grid(row=1, column=12, sticky='e')
		button4.grid(row=1, column=14, sticky='e')
		button5.grid(row=2, column=11, sticky='e')
		button6.grid(row=2, column=12, sticky='e')
		button7.grid(row=1, column=15, sticky='e')
		button8.grid(row=2, column=13, sticky='e')
		button9.grid(row=2, column=14, sticky='e')
		button10.grid(row=1, column=13, sticky='e')

		self.entry = ttk.Entry(self)
		self.entry.grid(row=1, sticky='e')

		self.listbox = tk.Listbox(self)
		self.listbox.grid(row=3, columnspan=2, sticky='e')
		self.listbox2 = tk.Listbox(self)
		self.listbox2.grid(row =3, column=3, sticky='e')

		#self.flag is used to stop the user from downloading an unselected song
		self.flag = 0
		self.soupFlag = False
		self.soup1 = 0
		self.soup2 = 0
		self.queue = []

		#Gives searchName a default char so the program won't
		#repetedly get data from the website
		if len(self.entry.get()) == 0:
			self.searchName = ' '

	def search_bar(self):
		temp = self.searchName[0]
		self.searchName = self.entry.get()

		if len(self.searchName) != 0:
			lst = ['http://downloads.khinsider.com/game-soundtracks/browse/A',\
					'http://downloads.khinsider.com/game-soundtracks/browse/B',\
					'http://downloads.khinsider.com/game-soundtracks/browse/C',\
					'http://downloads.khinsider.com/game-soundtracks/browse/D',\
					'http://downloads.khinsider.com/game-soundtracks/browse/E',\
					'http://downloads.khinsider.com/game-soundtracks/browse/F',\
					'http://downloads.khinsider.com/game-soundtracks/browse/G',\
					'http://downloads.khinsider.com/game-soundtracks/browse/H',\
					'http://downloads.khinsider.com/game-soundtracks/browse/I',\
					'http://downloads.khinsider.com/game-soundtracks/browse/J',\
					'http://downloads.khinsider.com/game-soundtracks/browse/K',\
					'http://downloads.khinsider.com/game-soundtracks/browse/L',\
					'http://downloads.khinsider.com/game-soundtracks/browse/M',\
					'http://downloads.khinsider.com/game-soundtracks/browse/N',\
					'http://downloads.khinsider.com/game-soundtracks/browse/O',\
					'http://downloads.khinsider.com/game-soundtracks/browse/P',\
					'http://downloads.khinsider.com/game-soundtracks/browse/Q',\
					'http://downloads.khinsider.com/game-soundtracks/browse/R',\
					'http://downloads.khinsider.com/game-soundtracks/browse/S',\
					'http://downloads.khinsider.com/game-soundtracks/browse/T',\
					'http://downloads.khinsider.com/game-soundtracks/browse/U',\
					'http://downloads.khinsider.com/game-soundtracks/browse/V',\
					'http://downloads.khinsider.com/game-soundtracks/browse/W',\
					'http://downloads.khinsider.com/game-soundtracks/browse/X',\
					'http://downloads.khinsider.com/game-soundtracks/browse/Y',\
					'http://downloads.khinsider.com/game-soundtracks/browse/Z']

			if self.searchName[0] != temp:
				for i in range(0,26):
					if ord(self.searchName[0]) == ord(chr(97 + i)) or\
							ord(self.searchName[0]) == ord(chr(65 + i)):
						request = requests.get(lst[i])
						self.soupFlag = False
						break

			if self.soupFlag == False:
				soup = BeautifulSoup(request.text)
				self.soup1 = soup
				self.soupFlag = True

			results = []
			for item in self.soup1.find_all(href = re.compile('album/')):
				results.append(item.text)

			displayResults = []
			for j in range(0, len(results)):
				if results[j].lower().startswith(self.searchName.lower()):
					displayResults.append(results[j])

			self.listbox.delete(0, END) #Clears the listbox
			for k in displayResults:
				self.listbox.insert(END, k)

			self.listbox.grid(row=3, column=0)

		else:
			self.listbox.delete(0, END)
			self.searchName = ' '
			self.soupFlag = False

	def album(self):
		songName = []

		if self.listbox.get(ACTIVE) != self.flag:
			self.flag = self.listbox.get(ACTIVE)
			url = self.soup1.find('a', text=self.listbox.get(ACTIVE))['href']
			request = requests.get(url)
			soup = BeautifulSoup(request.text)
			self.soup2 = soup

		for item in self.soup2.find_all('a', text='Download'):
			songName.append(item.previous_element.previous_element.previous_element)

		self.listbox.delete(0, END)
		for i in songName:
			self.listbox.insert(END, i)

	def size(self):
		if self.soup2 != 0:
			size = self.soup2.find('a', text='Download').\
					next_element.next_element.next_element.text
			popupmsg('Size: ' + size)

		else:
			popupmsg('Select a song first')

	def download(self):
		if self.soup2 != 0:
			url = self.soup2.find('a', text=self.listbox.get(ACTIVE))['href']
			request = requests.get(url)
			soup = BeautifulSoup(request.text)
			url = soup.find('audio')['src']
			request = requests.get(url)
			filename = url.split('/')[-1]

			with open(filename, 'wb') as f:
				f.write(request.content)

			self.listbox2.delete(0, END)
			self.listbox2.insert(END, filename + ' downloaded')
			time.sleep(2)

		else:
			popupmsg('Select a song first')

	def add_queue(self):
		if self.soup2 != 0:
			url = self.soup2.find('a', text=self.listbox.get(ACTIVE))['href']
			request = requests.get(url)
			soup = BeautifulSoup(request.text)
			url = soup.find('audio')['src']
			self.queue.append(url)

		else:
			popupmsg('Select a song first')

	def check_queue(self):
		tempList = []

		if self.queue != []:
			for song in self.queue:
				tempList.append(song.split('/')[-1])

			popupmsg(tempList)

		else:
			popupmsg('The queue is empty')

	def download_album(self):
		if self.soup2 != 0:
			self.clear_queue()

			for item in self.soup2.find_all('a', text='Download'):
				self.queue.append(item['href'])

			self.listbox2.delete(0, END)

			for url in self.queue:
				request = requests.get(url)
				soup = BeautifulSoup(request.text)
				url = soup.find('audio')['src']
				request = requests.get(url)
				filename = url.split('/')[-1]

				with open(filename, 'wb') as f:
					f.write(request.content)

				self.listbox2.insert(END, filename + ' downloaded')
				self.listbox2.update()
				time.sleep(5)

			self.clear_queue()

		else:
			popupmsg('Select a song first')

	def download_queue(self):
		if self.soup2 != 0:
			if self.queue != []:
				self.listbox2.delete(0, END)
				for url in self.queue:
					request = requests.get(url)
					filename = url.split('/')[-1]

					with open(filename, 'wb') as f:
						f.write(request.content)

					self.listbox2.insert(END, filename + ' downloaded')
					self.listbox2.update()
					time.sleep(5)

				self.clear_queue()

			else:
				popupmsg('There is nothing in queue')
		else:
			popupmsg('Select a song first')

	def clear_queue(self):
		self.queue[:] = []

app = App()
app.mainloop()