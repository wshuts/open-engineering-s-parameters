from manim import *

class TextOverlay(Scene):
    def construct(self):
        title_properties = Text("Interpreting Standing Waves", color=YELLOW)
        title_properties.scale(0.7)
        title_properties.to_edge(UP).shift(LEFT*3.2+UP*0.1).shift(LEFT*0.5)

        underline_properties = Line(LEFT, RIGHT, color=YELLOW)
        underline_properties.set_width(1.1*title_properties.get_width())
        underline_properties.next_to(title_properties, DOWN)
        underline_properties.shift(UP * 0.1)

        self.play(Write(title_properties), GrowFromCenter(underline_properties))
        self.wait(3)

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = TextOverlay()
    scene.render()
