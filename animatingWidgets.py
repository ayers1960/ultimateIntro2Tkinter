import customtkinter as ctk
from PIL import Image, ImageTk
from os import walk

class AnimatedButton(ctk.CTkButton):

    def __init__(self, parent, lightPath, darkPath, btnCmd):

        #animation logic setup
        self.frames = self.import_folders(lightPath, darkPath)
        self.frame_index = 20
        self.animationLength = len(self.frames)-1
        self.animation_status = ctk.StringVar(value='start')
        self.animation_status.trace('w', self.animate)
        if btnCmd == "infinite":
            command = self.infinite_animate    
        else:            
            command=self.triggerAnimation
        super().__init__(
            master=parent,
            text = 'a animated button', 
            image = self.frames[self.frame_index],
            command = command,
        )
        self.pack(expand=True)

    def infinite_animate(self):
            self.animation_status.set("running")            
            self.frame_index = (self.frame_index + 1) % self.animationLength
            self.configure(image= self.frames[self.frame_index])
            self.after(20, self.infinite_animate)

    def triggerAnimation(self):
        if self.animation_status.get() == 'start':
            self.frame_index = 0
            self.animation_status.set('forward')
        if  self. animation_status.get() == 'end':
            self.fram_index = self.animationLength
            self.animation_status.set('backward')

    def animate(self, *args):
        pauseTime = 75
        if self.animation_status.get() == 'forward':
            self.frame_index += 1
            self.configure(image = self.frames[self.frame_index])
            if self.frame_index < self.animationLength:
                self.after(pauseTime, self.animate)
            else:
                self.animation_status.set('end')
             
        
        if self.animation_status.get() == 'backward':
            self.frame_index -= 1
            self.configure(image = self.frames[self.frame_index])
            if self.frame_index > 0:
                self.after(pauseTime, self.animate)
            else:
                self.animation_status.set('start')
               
        print(self.animation_status.get())
        window.update()
        
    def import_folders(self, lightPath, darkPath):
        imagePaths = []
        for path in (lightPath, darkPath):
            for (folderName, subFolders, imageData) in walk(path):
                sortedData = sorted(
                    imageData, 
                    #key = lambda item: int(item[6:11]),
                    key = lambda item: item
                )
                fullPathData = [path + '/' + item for item in sortedData]
                imagePaths.append(fullPathData)
        imagePaths = zip(*imagePaths)
    
        ctk_images = []
        for imagePath in imagePaths:
            ctk_image = ctk.CTkImage(
                light_image = Image.open(imagePath[0]),
                dark_image = Image.open(imagePath[1]),
            )
            ctk_images.append(ctk_image)
        return ctk_images

#window
window = ctk.CTk()
window.title("Animating Widgets")
window.geometry('300x200')

ctk.set_appearance_mode('dark')
AnimatedButton(window, 'black','yellow', "once")
AnimatedButton(window, 'dark','light', "infinite")

#run
window.mainloop()