from manim import *

ONE_MINUTE =60

class VswrAnimation(Scene):
    def construct(self):
        self.wait(ONE_MINUTE)

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = VswrAnimation()
    scene.render()