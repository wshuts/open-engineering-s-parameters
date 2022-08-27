from manim import *

class Vmin(Scene):
    def construct(self):
        axes = Axes(x_range=[0,2*PI], y_range=[-2.5,2.5])

        V_min_point = axes.coords_to_point(2*PI,0.3)
        V_min_line = axes.get_horizontal_line(V_min_point, line_func=DashedLine, stroke_width=4).set_color(YELLOW_E)

        self.play(Create(axes), Create(V_min_line))
        self.wait(3)

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Vmin()
    scene.render()
