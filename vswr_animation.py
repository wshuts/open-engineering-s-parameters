from manim import *

class vswr_animation(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):
        ax = Axes(
            x_range=[0, 1, 0.25],
            y_range=[-2, 2, 0.5],
            x_length=10,
            y_length=5,
            tips=False,
        )
        ax.shift(DOWN*0+LEFT*0.4)

        title_properties = Text("Interpreting Standing Waves", color=YELLOW)
        title_properties.scale(0.7)
        title_properties.to_edge(UP).shift(LEFT*3.2+UP*0.1).shift(LEFT*0.5)

        underline_properties = Line(LEFT, RIGHT, color=YELLOW)
        underline_properties.set_width(1.1*title_properties.get_width())
        underline_properties.next_to(title_properties, DOWN)
        underline_properties.shift(UP * 0.1)
        self.play(Write(title_properties), GrowFromCenter(underline_properties))
        self.wait(3)
        self.play(Write(ax),run_time=2)
        self.wait(3)
        phi = 0
        b_inc = ax.plot(lambda x: np.sin(15*x+phi)).set_color(BLACK)
        b_ref = ax.plot(lambda x: -0.7*np.sin(15*x+20)).set_color(BLACK)
        b_sum = ax.plot(lambda x: np.sin(15*x+phi)-0.7*np.sin(15*x+20)).set_color(BLACK)
        point_v_max = ax.c2p(1.145, 1.7)
        point_v_min = ax.c2p(1.145, 0.305)
        for phi in range(0, 200*8):
            a_inc = b_inc
            b_inc = ax.plot(lambda x: np.sin((15*x)-((phi/10)+(1/10)))).set_color(BLUE)
            self.remove(a_inc)
            self.add(b_inc)
            if phi >= 20*8:
                a_ref = b_ref
                b_ref = ax.plot(lambda x: -0.7*np.sin((15*x)+(((phi)/10)+(1/10)))).set_color(RED)
                self.remove(a_ref)
                self.add(b_ref)
            if phi >= 40*8:
                a_sum = b_sum
                b_sum = ax.plot(lambda x: np.sin((15*x)-((phi/10)+(1/10)))-0.7*np.sin((15*x)+(((phi)/10)+(1/10)))).set_color(GREEN)
                self.remove(a_sum)
                self.add(b_sum)
            if phi == 90*8:
                V_max_line = ax.get_horizontal_line(point_v_max, line_func=DashedLine, stroke_width=4).set_color(YELLOW_E)
                self.add(V_max_line)
            if phi == 70*8:
                V_min_line = ax.get_horizontal_line(point_v_min, line_func=DashedLine, stroke_width=4).set_color(YELLOW_E)
                self.add(V_min_line)
            if phi == 110*8:
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

            self.wait(0.08)
        self.wait(3)
