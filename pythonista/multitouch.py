from scene import *

class MyScene (Scene):
	def setup(self):
		# This will be called before the first frame is drawn.
		pass
	
	def draw(self):
		# This will be called for every frame (typically 60 times per second).
		# it clears the screen
		background(0, 0, 0)
		# Draw a green circle for every finger that touches the screen:
		fill(0, 1, 0)
		for touch in self.touches.values():
			ellipse(touch.location.x - 50, touch.location.y - 50, 100, 100)
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass

	def touch_ended(self, touch):
		pass

run(MyScene())
