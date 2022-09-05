from manim import *

class Circulator(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):
        # Display circulator circuit
        circuit_circulator = ImageMobject("circulator.png").scale(0.9).shift(LEFT*10.4+DOWN*12.9)

        # Port 1 Circulator
        port1_num_circ=MathTex("1").set_color(YELLOW)
        port1_num_circ.shift(DOWN * 11.4)
        port1_num_circ.shift(LEFT * 12.75)
        port1_num_circ.scale(1.8)
        # Port 2 Circulator
        port2_num_circ=MathTex("2").set_color(YELLOW)
        port2_num_circ.shift(DOWN * 11.4)
        port2_num_circ.shift(LEFT * 8.1)
        port2_num_circ.scale(1.8)
        # Port 3 Circulator
        port3_num_circ=MathTex("3").set_color(YELLOW)
        port3_num_circ.shift(DOWN * 14.1)
        port3_num_circ.shift(LEFT * 10.02)
        port3_num_circ.scale(1.8)
        # R_load label
        R_load=MathTex("R_{L}").scale(1.3).shift(DOWN * 13.65).shift(LEFT * 9.7)
        R_load[0].set_color(WHITE)

        self.play(
            Write(port1_num_circ)
        )
        self.play(
            Write(port2_num_circ)
        )
        self.play(
            Write(port3_num_circ)
        )

        # Right arrow
        long_right_arrow_wave=Tex('$\Longrightarrow$').scale(5).next_to(ant_symbol).shift(RIGHT*2.6).set_color(WHITE)

        self.play(
            FadeIn(long_right_arrow_wave, shift=RIGHT)
        )

        # n^2 = 9
        nsquared=MathTex("n^2", #0
        "=", #1
        "9", #2
        ).next_to(long_right_arrow_wave).scale(1.6).shift(LEFT*3.25+UP*0.9)

        nsquared[0].set_color(YELLOW)
        nsquared[1].set_color(WHITE)
        nsquared[2].set_color(YELLOW)
        self.play(Write(nsquared))

        # 3-port matrix
        m1_3port = MathTex(r"\mathrm{S}").set_color(YELLOW)
        eq_3port = MathTex("=")
        m2_3port = Matrix([[r"\mathrm{S}_{11}", r"\mathrm{S}_{12}", r"\mathrm{S}_{13}"],
                           [r"\mathrm{S}_{21}", r"\mathrm{S}_{22}", r"\mathrm{S}_{23}"],
                           [r"\mathrm{S}_{31}", r"\mathrm{S}_{32}", r"\mathrm{S}_{33}"]], left_bracket="(", right_bracket=")", element_alignment_corner=DR-DR)
        m1_3port.shift(LEFT*2)
        eq_3port.next_to(m1_3port)
        m2_3port.next_to(eq_3port)
        m2_3port[0][0].set_color(BLUE)
        m2_3port[0][1].set_color(GREEN)
        m2_3port[0][2].set_color(TEAL)
        m2_3port[0][3].set_color(RED)
        m2_3port[0][4].set_color(ORANGE)
        m2_3port[0][5].set_color(GOLD_A)
        m2_3port[0][6].set_color(PURPLE)
        m2_3port[0][7].set_color(MAROON_D)
        m2_3port[0][8].set_color(LIGHT_PINK)

        g_3port = VGroup(m1_3port, m2_3port, eq_3port).next_to(long_right_arrow_wave).scale(2).shift(RIGHT*3.7+UP*0)

        self.play(Write(g_3port))

        self.wait(3)

        def create_csv(s):
            fin = open("manim_gif_data/circulator_data/"+s+".txt", "rt")
            fout = open("manim_gif_data/circulator_data/"+s+".csv", "wt")

            for line in fin:
                fout.write(' '.join(line.split()).replace(' 1', '1').replace(' ', ',')+'\n')

            fin.close()
            fout.close()

        ### Set x-axis limits to 13-18 GHz
        self.play(
            Unwrite(dc_label),
            ReplacementTransform(ax, ax_highfreq)
        )
        #x_axis_config={"numbers_to_include": np.arange(13, 18.001, 1), "label_direction": UP},
        create_csv('s11')
        create_csv('s12')
        create_csv('s13')
        create_csv('s21')
        create_csv('s22')
        create_csv('s23')
        create_csv('s31')
        create_csv('s32')
        create_csv('s33')
        s11_circ = np.loadtxt(open("manim_gif_data/circulator_data/s11.csv", "rb"), delimiter=",", skiprows=2)
        s12_circ = np.loadtxt(open("manim_gif_data/circulator_data/s12.csv", "rb"), delimiter=",", skiprows=2)
        s13_circ = np.loadtxt(open("manim_gif_data/circulator_data/s13.csv", "rb"), delimiter=",", skiprows=2)
        s21_circ = np.loadtxt(open("manim_gif_data/circulator_data/s21.csv", "rb"), delimiter=",", skiprows=2)
        s22_circ = np.loadtxt(open("manim_gif_data/circulator_data/s22.csv", "rb"), delimiter=",", skiprows=2)
        s23_circ = np.loadtxt(open("manim_gif_data/circulator_data/s23.csv", "rb"), delimiter=",", skiprows=2)
        s31_circ = np.loadtxt(open("manim_gif_data/circulator_data/s31.csv", "rb"), delimiter=",", skiprows=2)
        s32_circ = np.loadtxt(open("manim_gif_data/circulator_data/s32.csv", "rb"), delimiter=",", skiprows=2)
        s33_circ = np.loadtxt(open("manim_gif_data/circulator_data/s33.csv", "rb"), delimiter=",", skiprows=2)

        circulator_s11 = ax_highfreq.plot_line_graph(s11_circ[:,0], s11_circ[:,1], add_vertex_dots=False, line_color=BLUE)
        circulator_s12 = ax_highfreq.plot_line_graph(s12_circ[:,0], s12_circ[:,1], add_vertex_dots=False, line_color=TEAL)
        circulator_s13 = ax_highfreq.plot_line_graph(s13_circ[:,0], s13_circ[:,1], add_vertex_dots=False, line_color=GREEN)
        circulator_s21 = ax_highfreq.plot_line_graph(s21_circ[:,0], s21_circ[:,1], add_vertex_dots=False, line_color=PURPLE)
        circulator_s22 = ax_highfreq.plot_line_graph(s22_circ[:,0], s22_circ[:,1], add_vertex_dots=False, line_color=LIGHT_PINK)
        circulator_s23 = ax_highfreq.plot_line_graph(s23_circ[:,0], s23_circ[:,1], add_vertex_dots=False, line_color=MAROON_D)
        circulator_s31 = ax_highfreq.plot_line_graph(s31_circ[:,0], s31_circ[:,1], add_vertex_dots=False, line_color=RED)
        circulator_s32 = ax_highfreq.plot_line_graph(s32_circ[:,0], s32_circ[:,1], add_vertex_dots=False, line_color=GOLD_A)
        circulator_s33 = ax_highfreq.plot_line_graph(s33_circ[:,0], s33_circ[:,1], add_vertex_dots=False, line_color=ORANGE)

        # \left(0.2\log_{1.1}\left(x+0.06\right)\right)-23

        framebox_s11 = SurroundingRectangle(m2_3port[0][0], buff = .2)
        framebox_s12 = SurroundingRectangle(m2_3port[0][1], buff = .2)
        framebox_s13 = SurroundingRectangle(m2_3port[0][2], buff = .2)
        framebox_s21 = SurroundingRectangle(m2_3port[0][3], buff = .2)
        framebox_s22 = SurroundingRectangle(m2_3port[0][4], buff = .2)
        framebox_s23 = SurroundingRectangle(m2_3port[0][5], buff = .2)
        framebox_s31 = SurroundingRectangle(m2_3port[0][6], buff = .2)
        framebox_s32 = SurroundingRectangle(m2_3port[0][7], buff = .2)
        framebox_s33 = SurroundingRectangle(m2_3port[0][8], buff = .2)

        self.play(AnimationGroup(Create(framebox_s11),Write(circulator_s11),run_time=3,lag_ratio=0.5))
        self.wait(3)
        self.play(AnimationGroup(ReplacementTransform(framebox_s11,framebox_s12),Write(circulator_s13),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s12,framebox_s13),Write(circulator_s12),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s13,framebox_s21),Write(circulator_s31),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s21,framebox_s22),Write(circulator_s33),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s22,framebox_s23),Write(circulator_s32),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s23,framebox_s31),Write(circulator_s21),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s31,framebox_s32),Write(circulator_s23),run_time=3,lag_ratio=0.5))
        self.play(AnimationGroup(ReplacementTransform(framebox_s32,framebox_s33),Write(circulator_s22),run_time=3,lag_ratio=0.5))
        
        self.wait(3)

with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": False}):
    scene = Circulator()
    scene.render()