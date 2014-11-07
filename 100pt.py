#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=500,height=500, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4


class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "green")
		self.up.grid(row=0,column=1)
					
		# "Bind" an action to the first button
                self.button1 = Button(self.myContainer1)
		self.button1.configure(text="left", background= "green")
		self.button1.grid(row=1,column=0)												
		self.up.bind("<Button-1>", self.moveUp)
		self.button1.bind("<Button-1>", self.button1Click)
		self.button2 = Button(self.myContainer1)
	        self.button2.configure(text="down", background= "green")
	        self.button2.grid(row=2,column=1)
	        self.button2.bind("<Button-1>", self.button2Click)
       	        self.button4 = Button(self.myContainer1)
	        self.button4.configure(text="right", background= "green")
	        self.button4.grid(row=1,column=2)
	        self.button4.bind("<Button-1>", self.button4Click)
      	        self.button5 = Button(self.myContainer1)
	        self.button5.configure(text="          ", background= "green")
	        self.button5.grid(row=1,column=1)
                
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()
		

    
         
        # Animate function that will bounce target left and right, and trigger the collision detection  
	def animate(self):
	    global target
	    global direction
	    tx1,ty1,tx2,ty2 = drawpad.coords(target)
	    
	    # Insert the code here to make the target move, bouncing on the edges    
	        
	    if tx2 > drawpad.winfo_width(): 
                direction = - 10
            elif tx1 < 0:
                direction = 10
    #Move our oval object by the value of direction
            drawpad.move(target,direction,0)
# Wait for 1 millisecond, then recursively call our animate function
               
            
            
            #  This will trigger our collision detect function
            didWeHit = self.collisionDetect()
            if didWeHit == False:
                drawpad.after(5, self.animate) 

                
            # Use the value of didWeHit to create an if statement
            # that determines whether to run drawpad.after(1,self.animate) or not
            
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
		global drawpad
                global player
                # Get the co-ordinates of our player AND our target
                # using x1,y1,x2,y2 = drawpad.coords(object)\
                x1,y1,x2,y2 = drawpad.coords(player)
                tx1,ty1,tx2,ty2 = drawpad.coords(target) 
                if (tx1 <= x1 and tx2 >= x2) and (ty1 <= y1 and ty2 >= y2):
                    drawpad.itemconfig(target, fill="pink")
                    return True
                else:
                    return False
        def button4Click(self, event):   
	   global oval
	   global player
	   x1,y1,x2,y2 = drawpad.coords(player)
           global player
           x1, y1, x2, y2 = drawpad.coords(player)
           if (x1 > 0 and x2 < 500):
               drawpad.move(player, 20, 0)
           else:
               print ""

		
	def button1Click(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
                if (x1 > 0 and x2 < 500):
                    drawpad.move(player, -20, 0)
                else:
                    return
                
        def button2Click(self, event):
            global oval
	    global player
	    drawpad.move(player,0,20)
	    	
	def moveUp(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
                drawpad.move(player,0,-10)


                # Do your if statement - remember to return True if successful!    
myapp = MyApp(root)

root.mainloop()