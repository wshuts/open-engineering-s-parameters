from manim import *

class VmaxVmin(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 1, 0.25],
            y_range=[-2, 2, 0.5],
            x_length=10,
            y_length=5,
            tips=False,
        )
        ax.shift(DOWN*0+LEFT*0.4)

        point_v_max = ax.c2p(1.145, 1.7)
        point_v_min = ax.c2p(1.145, 0.305)

        V_max_line = ax.get_horizontal_line(point_v_max, line_func=DashedLine, stroke_width=4).set_color(YELLOW_E)
        V_min_line = ax.get_horizontal_line(point_v_min, line_func=DashedLine, stroke_width=4).set_color(YELLOW_E)

        V_max_label = MathTex(r'|',r'V_\mathrm{max}',r'|').next_to(V_max_line, direction=UP).shift(RIGHT*5.26+DOWN*0.12).scale(1).set_color(WHITE).shift(LEFT*0.2)
        V_max_label.set_color_by_tex_to_color_map({
        r'V_\mathrm{max}': YELLOW_D,
        }) 
        V_min_label = MathTex(r'|',r'V_\mathrm{min}',r'|').next_to(V_min_line, direction=UP).shift(RIGHT*5.26+DOWN*0.12).scale(1).set_color(WHITE).shift(LEFT*0.2)
        V_min_label.set_color_by_tex_to_color_map({
        r'V_\mathrm{min}': YELLOW_D,
        }) 
        vswr_V_eq_long = MathTex(r'\mathrm{Voltage \ Standing \ Wave \ Ratio}',r'=',r'{{|',r'V_\mathrm{max}',r'|}','\over',r'{|',r'V_\mathrm{min}',r'|}}').scale(1).shift(LEFT*0+DOWN*3.12).set_color(WHITE)
        vswr_V_eq_long.set_color_by_tex_to_color_map({
        r'V_\mathrm{max}': YELLOW_D,
        r'V_\mathrm{min}': YELLOW_D,
        r'\mathrm{Voltage \ Standing \ Wave \ Ratio}': TEAL,
        }) 
        vswr_V_eq = MathTex(r'\mathrm{VSWR}',r'=',r'{{|',r'V_\mathrm{max}',r'|}','\over',r'{|',r'V_\mathrm{min}',r'|}}').scale(1).shift(LEFT*0+DOWN*3.12).set_color(WHITE)
        vswr_V_eq.set_color_by_tex_to_color_map({
        r'V_\mathrm{max}': YELLOW_D,
        r'V_\mathrm{min}': YELLOW_D,
        r'VSWR': TEAL,
        }) 
        self.play(Write(V_min_label))
        self.wait(3)
        self.play(Write(V_max_label))
        self.wait(3)
        self.play(Write(vswr_V_eq_long))
        self.wait(3)
        self.play(ReplacementTransform(vswr_V_eq_long, vswr_V_eq))

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = VmaxVmin()
    scene.render()
