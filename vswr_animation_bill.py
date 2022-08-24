from manim import *

ONE_MINUTE =60

class VswrAnimation(Scene):
    def construct(self):
        axes = Axes(x_range=[0,2*PI], y_range=[-1,1])
        sine_wave = axes.plot(lambda t: 1*np.sin(2*t))
        self.add(axes, sine_wave)
        #self.wait(ONE_MINUTE)

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = VswrAnimation()
    scene.render()