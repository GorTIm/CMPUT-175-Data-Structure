import pygame,sys,time
from pygame.locals import*

# User-defined classes
class Dot:
   dotColor=pygame.Color('blue')
   dotRadius=15
   def _init_(self,color,center,radius):
      self.color=color
      self.center=center
      self.radius=radius
      
   def drawDot(self,surface):
   #This function calls the pygame.draw.circle function to draw the circle
      #color is the pygame.Color object
      #center is a list object containing the x and y int coords of the center
      #radius is an int object
      #surface is pygame.Surface object where the circle will be drawn
      pygame.draw.circle(surface, dotColor, self.center, dotRadius, 0)  

#Main program
pygame.init()
surfaceSize = (500, 400) # example window size
windowTitle = 'Bypass' # example title
frameDelay = 0.01 # smaller is faster game

# Create the window
surface = pygame.display.set_mode(surfaceSize, 0, 0)
pygame.display.set_caption(windowTitle)


# create and initialize object
dot1Center=[50,70]
dot1=Dot(dot1Center)

# Refresh the display
pygame.display.update()
#Call drawDot
dot1.drawDot(surface)

mousePosition=pygame.mouse.get_pos()




while True:
# Handle events
  for event in pygame.event.get():
#event is a variable referring to pygame.event.Event object 
    if event.type == QUIT:
#type is an attribute of the event object
      pygame.quit()
      sys.exit()

# Refresh the display
pygame.display.update()

# Set the frame speed by pausing between frames
time.sleep(frameDelay)     
            