from manim import *

class SceneEfieldThru(MovingCameraScene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage[european,straightvoltages,straightlabels]{circuitikz}")

        circ="""\\begin{circuitikz}[american, line width=1pt]
                    \\draw[ultra thin](-4,0) to [R] (0,0) to [cute inductor] (3.5,-0) to[vC] (4.5,-0) to[diode] (10,-0);
                    \\draw[short, *-] (5.5,-0) to (5.49,0.01) to (5.51,-0.01) to (5.51,0.01) to (5.51,-0.01) to (5.49,-0.01) to (5.5,0.0) to [short, *-] (5.5,-2.5) to (5.49,-2.49) to (5.51,-2.51) to (5.51,-2.49) to (5.51,-2.51) to (5.49,-2.51) to (5.5,-2.5) ;
                    \\draw[ultra thin](0,0) to [capacitor,l^] (0,-1) to (0,-0.8) node[ground]{};;
                    \\draw[ultra thin](-4,-2.5) to [diode] (-2,-2.5) to [cute inductor] (1,-2.5) to[C] (3.5,-2.5) to[vC] (10,-2.5);
                    \\draw[ultra thin, short, *-] (5.5,-2.5) to [short, *-] (5.5,-2.5) to [short, -] (5.5,-2.5);
                    \\draw[ultra thin](4,-2.5) to [R] (4,-4.2) to (4,-4) node[ground]{};;
                    \\end{circuitikz}"""
        circuit1=Tex(circ,tex_template=myTemplate,stroke_width=2,fill_opacity=0).scale(0.5) #.shift(LEFT*-8.84)

        circuit_group1=VGroup(*[circuit1.copy() for s in range(30)]).set_x(0).arrange_in_grid(rows=6, buff=(0, 0.8)).scale(0.6).rotate(PI/22).set_color(DARK_GRAY)

        rectangle_efield = Rectangle(height=6.1, width=12, stroke_width=3, color=YELLOW_D, fill_color=BLACK, fill_opacity=0).shift(DOWN*0.25)
        rectangle_title = MathTex(r'\mathop{\mbox{$E$$-$$\mathrm{Field \ Simulation \ | \ Phase}$:\ }}',r'\phi ',r'=', color=YELLOW_D).scale(1.2)
        rectangle_title.set_color_by_tex_to_color_map({
        r'\phi': BLUE,
        r'=': BLUE
        })

        rectangle_title.shift(UP*3.35).shift(LEFT*0.7)
        rectangle_subtitle = MathTex(r'\mathop{\mbox{\textbf{E$/$M Solver:} Finite Integration Technique (FIT)}}', color=RED_B).scale(0.8)
        rectangle_subtitle.shift(DOWN*3.68)

        # 0-360 deg loop tracker (counter)
        start = 0
        x_var = Variable(start, '', num_decimal_places=0).shift(UP*3.35+RIGHT*3.1).scale(1.2)
        x_var.set_color(BLUE)
        Deg = Tex("°").scale(1.2)
        Deg.set_color(BLUE)
        Deg.add_updater(lambda x: x.next_to(x_var,RIGHT,buff=0.05).shift(UP*0.1))

        #self.add(x_var)
        #self.add(Deg)

        self.wait(3)
        self.play(
            Write(circuit_group1)
        )
        self.wait(3)
        self.play(
            Create(rectangle_efield),
            Write(rectangle_title),
        )
        self.wait(3)
        self.play(
            rectangle_efield.animate.set_opacity(1),
            Write(x_var),
            Write(Deg)
        )
        self.wait(3)
        self.play(Write(rectangle_subtitle))
        self.wait(3)
        for i in range(1, 7):
            x_var.tracker.set_value(0)
            self.play(x_var.tracker.animate.set_value(360), run_time=2, rate_func=linear)

        self.wait(3)


with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": True}):
    scene = SceneEfieldThru()
    scene.render()