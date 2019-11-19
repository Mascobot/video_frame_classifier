import os
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
from tkinter import filedialog

classes = []

class App:
	def __init__(self, window, window_title):
		self.window = window
		self.window.title(window_title)
		self.filename = None
			
		self.canvas = tkinter.Canvas(window, width = 640, height = 360)
		self.canvas.pack()

		#Button to upload video:
		self.btn_snapshot=tkinter.Button(window, text="Upload video", width=10, command=self.upload_video)
		#self.btn_snapshot.place(relx=.5, rely=.8, anchor="c")
		self.btn_snapshot.pack(pady=4, anchor=tkinter.S, expand=False)		
		self.sign = tkinter.Label(window, text="by @Mascobot")
		self.sign.pack(pady=4, anchor=tkinter.SW, expand=False)	

		self.window.mainloop()
				
	def upload_video(self):
		if self.filename is None:
			self.filename = filedialog.askopenfilename()
			self.video = MyVideoCapture(self.filename)
			self.scale = tkinter.Scale(label='Start frame number:', orient='horizontal',length=700, resolution = 1, from_=0, to=len(self.video.frame_list), command=self.send_slider_one_number)
			self.scale2 = tkinter.Scale(label='End frame number:', orient='horizontal',length=700, resolution = 1, from_=0, to=len(self.video.frame_list), command=self.send_slider_two_number)
			self.scale.set(1)
			self.scale2.set(len(self.video.frame_list))

			self.scale.pack()
			self.scale2.pack()

			self.btn_create=tkinter.Button(text="Create new Class button", width=20, command=self.new_button, bg="blue")
			self.btn_create.pack(pady=4, anchor=tkinter.SW, expand=False)

			self.LabelEntry = tkinter.Label(text='Type new Class name:')
			self.Class_name = tkinter.Entry()
			self.LabelEntry.pack(anchor=tkinter.SW)
			self.Class_name.pack(anchor=tkinter.SW)

			self.output_txt = tkinter.Text(width=100, height=3)
			self.output_txt.insert('1.0',"Create max 6 classes. " + self.video.video_specs + ". -Images will be saved in their original resolution.-")
			self.output_txt.pack(anchor=tkinter.SW)

			directory = 'Class_Images'
			if not os.path.exists(directory):
				os.makedirs(directory)
		else:
			self.output_txt.delete('1.0', tkinter.END)
			self.output_txt.insert('1.0',"Video already loaded")		
	

	def send_slider_one_number(self, value):
		self.value = int(value)
		self.update_display(self.value)

	def send_slider_two_number(self, value2):
		self.value2 = int(value2)
		self.update_display(self.value2)

	def new_button(self):
		if (self.Class_name.get().strip() == ""):
			self.output_txt.delete('1.0', tkinter.END)
			self.output_txt.insert('1.0',"Please type Class name")
			
		elif (self.Class_name.get().strip() in classes):
			self.output_txt.delete('1.0', tkinter.END)
			self.output_txt.insert('1.0',"Class already exists")
			
		elif (len(classes) > 5):
			self.output_txt.delete('1.0', tkinter.END)
			self.output_txt.insert('1.0',"There are already 6 classes!")
			

		else:
			classes.append(self.Class_name.get().strip())
			if len(classes) == 1:
				self.b_one(classes[-1])
				self.output_txt.delete('1.0', tkinter.END)
				self.output_txt.insert('1.0',"Button " + "'" + str(classes[-1]) + "'" +" created." )
			elif len(classes) == 2:
				self.b_two(classes[-1])
				self.output_txt.delete('1.0', tkinter.END)
				self.output_txt.insert('1.0',"Button " + "'" + str(classes[-1]) + "'" +" created." )
			elif len(classes) == 3:
				self.b_three(classes[-1])
				self.output_txt.delete('1.0', tkinter.END)
				self.output_txt.insert('1.0',"Button " + "'" + str(classes[-1]) + "'" +" created." )
			elif len(classes) == 4:
				self.b_four(classes[-1])
				self.output_txt.delete('1.0', tkinter.END)
				self.output_txt.insert('1.0',"Button " + "'" + str(classes[-1]) + "'" +" created." )
			elif len(classes) == 5:
				self.b_five(classes[-1])
				self.output_txt.delete('1.0', tkinter.END)
				self.output_txt.insert('1.0',"Button " + "'" + str(classes[-1]) + "'" +" created." )
			elif len(classes) == 6:
				self.b_six(classes[-1])	
				self.output_txt.delete('1.0', tkinter.END)
				self.output_txt.insert('1.0',"Button " + "'" + str(classes[-1]) + "'" +" created." )		
			else:
				pass
	

	def b_one(self, button_name):
		button_text = "Save " + "'" + str(button_name) + "'" + " class images"
		self.b_one = tkinter.Button(text=button_text, width=25, command= lambda: self.save_fram(button_name), bg="blue")
		self.b_one.pack(expand=True, pady=2)#anchor=tkinter.W
		

	def b_two(self, button_name):
		button_text = "Save " + "'" + str(button_name) + "'" + " class images"
		self.b_two = tkinter.Button(text=button_text, width=25, command= lambda: self.save_fram(button_name), bg="blue")
		self.b_two.pack(expand=True, pady=2)
				

	def b_three(self, button_name):
		button_text = "Save " + "'" + str(button_name) + "'" + " class images"
		self.b_three = tkinter.Button(text=button_text, width=25, command= lambda: self.save_fram(button_name), bg="blue")
		self.b_three.pack(expand=True, pady=2)		

	def b_four(self, button_name):
		button_text = "Save " + "'" + str(button_name) + "'" + " class images"
		self.b_four = tkinter.Button(text=button_text, width=25, command= lambda: self.save_fram(button_name), bg="blue")
		self.b_four.pack(expand=True, pady=2)	

	def b_five(self, button_name):
		button_text = "Save " + "'" + str(button_name) + "'" + " class images"
		self.b_five = tkinter.Button(text=button_text, width=25, command= lambda: self.save_fram(button_name), bg="blue")
		self.b_five.pack(expand=True, pady=2)	

	def b_six(self, button_name):
		button_text = "Save " + "'" + str(button_name) + "'" + " class images"
		self.b_six = tkinter.Button(text=button_text, width=25, command= lambda: self.save_fram(button_name), bg="blue")
		self.b_six.pack(expand=True, pady=2)	

	def save_fram(self, bname):
		#self.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
		#self.directory = str(filedialog.askdirectory())
		self.bname = bname
		#entryString = str(self.Class_name.get())
		for i in range(int(self.value), int(self.value2)+1):
			self.video.save_frames(self.bname, i)
		self.output_txt.delete('1.0', tkinter.END)
		text = "'" + str(self.bname) + "'" + "images from frame: " + str(int(self.value)) + " to frame: " + str(int(self.value2)) + " were saved in 'Class_Image' folder"
		self.output_txt.insert('1.0',text)	


	def update_display(self, frame_number=0):
		# Get frame from the video 
		ret, frame = self.video.get_frame(frame_number)

		if ret:
			self.img = PIL.Image.fromarray(frame)
			self.img = self.img.resize([640,360])
			self.photo = PIL.ImageTk.PhotoImage(image = self.img)
			self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)


class MyVideoCapture:
	def __init__(self, video_source):
		# Open the video source
		self.cap = cv2.VideoCapture(video_source)
		self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
		self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
		self.fps = self.cap.get(cv2.CAP_PROP_FPS)
		self.video_specs = str("Video uploaded width: " + str(self.width) + ", height: " + str(self.height) + "; frames per second: " + str(self.fps))
		self.totalFrames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
		self.frame_list = list(range(int(self.totalFrames)))
		
		if not self.cap.isOpened():
			raise ValueError("Unable to open video source", video_source)

	def get_frame(self, frame_number):
		if self.cap.isOpened():
			self.cap.set(cv2.CAP_PROP_POS_FRAMES,frame_number)
			ret, frame = self.cap.read()
			if ret:				
				return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
			else:
				return (ret, None)
		else:
			return (ret, None)

	def save_frames(self,label, frame_number):	
		if not os.path.exists('Class_Images'):
				os.makedirs('Class_Images')
		if (self.cap.isOpened()):
			self.cap.set(cv2.CAP_PROP_POS_FRAMES,frame_number)
			ret, frame = self.cap.read()
			if ret:
				cv2.imwrite(os.path.join('Class_Images', str(label)+'_'+str(frame_number)) + '.jpg',frame)
			else:
				print ("rest was not active")	
			
	def __del__(self):
		if self.cap.isOpened():
			self.cap.release()
 

App(tkinter.Tk(), "Video Annotator | Mascobot")