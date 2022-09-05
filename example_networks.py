import math
from manim import *

class ExampleNetworks(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):
        ax = Axes(
            x_range=[-0.06, 5.001, 1],
            y_range=[-30.01, 0.5, 5],
            x_length=11,
            y_length=5.7,
            x_axis_config={"numbers_to_include": np.arange(0, 5.001, 1), "label_direction": UP},
            y_axis_config={"numbers_to_include": np.arange(-30.01, 0.5, 5)},
            tips=False,
        )
        ax_highfreq = Axes(
            x_range=[13, 18.001, 1],
            y_range=[-30.01, 0.5, 5],
            x_length=10.9,
            y_length=5.7,
            x_axis_config={"numbers_to_include": np.arange(13, 18.001, 1), "label_direction": UP},
            y_axis_config={"numbers_to_include": np.arange(-30.01, 0.5, 5)},
            tips=False,
        )
        ax_highfreq.shift(DOWN*5.9+RIGHT*2.45).scale(1.25)
        ax_amp = Axes(
            x_range=[13, 18.001, 1],
            y_range=[-40.01, 20.5, 10],
            x_length=10.9,
            y_length=6.7,
            x_axis_config={"numbers_to_include": np.arange(13, 18.001, 1), "label_direction": UP},
            y_axis_config={"numbers_to_include": np.arange(-40.01, 20.5, 10)},
            tips=False,
        )
        ax_amp.shift(DOWN*5.9+RIGHT*2.45).scale(1.25)
        self.play(
            self.camera.frame.animate.set_width(26).move_to(2.2*LEFT+8*DOWN)
        )
        # Title
        title_properties = Text("Example Networks", color=YELLOW)
        title_properties.scale(1.2)
        title_properties.to_edge(UP).shift(LEFT*11+DOWN*5)

        # Title underline
        underline_properties = Line(LEFT, RIGHT, color=YELLOW)
        underline_properties.width=1.1*title_properties.width
        underline_properties.next_to(title_properties, DOWN)
        underline_properties.shift(UP * 0.1)

        self.play(FadeIn(title_properties, shift=LEFT), GrowFromCenter(underline_properties))
        self.wait(3)

        x = Tex("Antennas", "Dummy Loads", "Filters", "Attenuators", "Circulators", "Isolators", "Amplifiers") #, height=5, width=5, dot_scale_factor=3.5)
        for network in x:
            dot = MathTex("\\cdot").scale(3)
            dot.next_to(network[0], LEFT*0.4, buff=0.4)
            network.add_to_back(dot)
        x.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        #x.set_color_by_tex("Antennas", WHITE)

        x.scale(1.45)
        x.shift(LEFT*11.4+DOWN*6.1)
        x.set_opacity(0.5)
        self.play(Write(x))
        self.play(x.submobjects[0].animate.set_opacity(1))

        # PLOT
        ax.shift(DOWN*5.9+RIGHT*2.3).scale(1.25)

        curve1 = ax.plot(lambda x: 27*(-2.71828183** (-((x-2)**2)/(2*(0.2**2))) ) - 0.1, x_range=[0, 5], color=BLUE)

        line1 = ax.get_vertical_line(
            ax.i2gp(2, curve1), line_func=DashedLine, stroke_width=8, color=BLUE_E
        )
        dc_label = MathTex("\mathrm{DC}").next_to(ax).scale(0.9).shift(LEFT*14.29, UP*3.68).set_color(WHITE)
        frequency_label = MathTex("\mathrm{Frequency \ (GHz)}").next_to(ax).scale(1.1).shift(LEFT*9, UP*4.4).set_color(WHITE)
        magnitude_label = MathTex("\mathrm{Magnitude \ (dB)}").next_to(ax).scale(1.1).shift(LEFT*17.2+DOWN*0.3).set_color(WHITE).rotate(PI/2)

        self.play(
            Write(ax),
            Write(dc_label),
            Write(frequency_label),
            Write(magnitude_label),
            run_time=4, lag_ratio=0.2
        )

        ### Antennas
        ant_symbol = ImageMobject("antenna.png").shift(DOWN*12.5+LEFT*10.5).scale(0.7)

        # Port 1 ANT
        port1_num_ant=MathTex("1").set_color(YELLOW)
        port1_num_ant.shift(DOWN * 13.7)
        port1_num_ant.shift(LEFT * 9.8)
        port1_num_ant.scale(1.8)

        self.play(FadeIn(ant_symbol, shift=UP))
        self.play(Write(port1_num_ant))

        # Right arrow
        long_right_arrow_wave=Tex('$\Longrightarrow$').scale(5).next_to(ant_symbol).shift(RIGHT*3).set_color(WHITE)

        self.play(
            FadeIn(long_right_arrow_wave, shift=RIGHT)
        )

        # n^2 = 1
        nsquared=MathTex("n^2", #0
        "=", #1
        "1", #2
        ).next_to(long_right_arrow_wave).scale(1.6).shift(LEFT*3.25+UP*0.9)

        nsquared[0].set_color(YELLOW)
        nsquared[1].set_color(WHITE)
        nsquared[2].set_color(YELLOW)
        self.play(Write(nsquared))

        # 1-port matrix
        matrix_1=MathTex("\mathrm{S}", #0
        "=", #1
        r"\big(", #2
        "\mathrm{S}_{11}", #3
        r"\big)" #4
        ).next_to(long_right_arrow_wave).scale(2.2).shift(RIGHT*4+UP*0)

        matrix_1[0].set_color(YELLOW)
        matrix_1[1].set_color(WHITE)
        matrix_1[2].set_color(WHITE)
        matrix_1[3].set_color(BLUE)
        matrix_1[4].set_color(WHITE)
        self.play(Write(matrix_1))
        self.wait(3)

        # s11 magnitude
        s11_mag=MathTex("|", #0
        "\mathrm{S}_{11}", #1
        "(", #2
        "f", #3
        ")", #4
        "|" #5
        ).next_to(long_right_arrow_wave).scale(2.2).shift(RIGHT*4+UP*0)

        s11_mag[0].set_color(WHITE)
        s11_mag[1].set_color(BLUE)
        s11_mag[2].set_color(WHITE)
        s11_mag[3].set_color(MAROON)
        s11_mag[4].set_color(WHITE)
        s11_mag[5].set_color(WHITE)
        self.play(ReplacementTransform(matrix_1, s11_mag))


        self.play(Write(curve1), run_time=3)
        
        self.wait(3)
        self.play(Write(line1), run_time=1)


        
        # Delete plot antenna curve
        self.wait(3)

        ### Dummy Loads
        self.play(
        FadeOut(ant_symbol, shift=DOWN),
        FadeOut(port1_num_ant, shift=DOWN),
        Uncreate(line1), Uncreate(curve1), run_time=3, lag_ratio=0.2)
        self.play(
            x.submobjects[0].animate.set_opacity(0.5),
            x.submobjects[1].animate.set_opacity(1)
        )

        # Display circuit
        circuit_dummy = ImageMobject("dummy_load.png").scale(0.65).shift(LEFT*10.5+DOWN*12.6)

        self.play(FadeIn(circuit_dummy, shift=RIGHT), run_time=1)

        # Show source framebox
        framebox_source = DashedVMobject(Rectangle(height=4.4, width=3.5).set_color(YELLOW).next_to(circuit_dummy).shift(LEFT*6.7), num_dashes=30, dashed_ratio=0.6)
        self.play(Write(framebox_source), run_time=1.5)
        # Source label
        label_source = Text("Source").set_color(YELLOW).scale(0.9).shift(DOWN*0.2)
        label_source.next_to(framebox_source, direction=UP)
        self.play(Write(label_source))
        self.wait(3)

        # Show load framebox
        framebox_load = DashedVMobject(Rectangle(height=4.4, width=2.7).set_color(YELLOW).next_to(circuit_dummy).shift(LEFT*2.7), num_dashes=27, dashed_ratio=0.6)
        # Load label
        label_load = Text("Load").set_color(YELLOW).scale(0.9).shift(DOWN*0.2)
        label_load.next_to(framebox_load, direction=UP)
        self.play(ReplacementTransform(framebox_source, framebox_load),
        ReplacementTransform(label_source, label_load),
        run_time=1.5)
        self.wait(3)

        # Hide framebox & label
        self.play(Uncreate(framebox_load), Unwrite(label_load))
        self.wait(3)

        # R_source label
        R_source=MathTex("R_{S}").next_to(label_source).scale(1.3).shift(DOWN*0.35+LEFT*4.24)
        R_source[0].set_color(WHITE)

        # R_load label
        R_load=MathTex("R_{L}").next_to(label_load).scale(1.3).shift(DOWN*2.05+RIGHT*0.35)
        R_load[0].set_color(WHITE)

        self.play(Write(R_source))
        self.wait(3)
        self.play(Write(R_load))
        self.wait(3)

        # R_source 50ohm label
        R_source_50=MathTex("50 \ \Omega").next_to(label_source).scale(1.3).shift(DOWN*0.35+LEFT*4.4)
        R_source_50[0].set_color(WHITE)

        # R_load 50ohm label
        R_load_50=MathTex("50 \ \Omega").next_to(label_load).scale(1.3).shift(DOWN*2.05+RIGHT*0.45)
        R_load_50[0].set_color(WHITE)

        self.play(ReplacementTransform(R_source, R_source_50), ReplacementTransform(R_load, R_load_50))

        # Display dummy load curve
        curve_load = ax.plot(lambda x: -30, x_range=[0, 5], color=BLUE)

        line1 = ax.get_vertical_line(
            ax.i2gp(2, curve1), line_func=DashedLine, stroke_width=8, color=YELLOW_E
        )

        self.play(Write(curve_load), run_time=3)
        self.wait(3)
        #self.play(Uncreate(curve_load), run_time=3)
        self.wait(3)

        # Hide dummy load section
        self.play(
        FadeOut(circuit_dummy, shift=DOWN),
        FadeOut(R_source_50, shift=DOWN),
        FadeOut(R_load_50, shift=DOWN),
        Uncreate(curve_load),
        FadeOut(long_right_arrow_wave, shift=RIGHT),
        Unwrite(s11_mag),
        Unwrite(nsquared), run_time=2)
        self.wait(3)
        self.play(
            x.submobjects[1].animate.set_opacity(0.5),
            x.submobjects[2].animate.set_opacity(1)
        )





        ### Filters
        ##### equation (desmos): f\left(x\right)=\frac{1}{\sqrt{1+\left(x-1.4\right)^{\left(2\cdot2\right)}}}

        # Display lowpass circuit
        circuit_lowpass = ImageMobject("lowpass.png").scale(1).shift(LEFT*9.7+DOWN*12.6)

        self.play(FadeIn(circuit_lowpass, shift=RIGHT), run_time=1)

        # Show LC framebox
        framebox_LC = DashedVMobject(Rectangle(height=4.4, width=3.8).set_color(YELLOW).next_to(circuit_lowpass).shift(LEFT*9), num_dashes=30, dashed_ratio=0.6)
        self.play(Write(framebox_LC), run_time=1.5)

        # Source label
        label_LC = Text("LC Filter").set_color(YELLOW).scale(0.9).shift(DOWN*0.2)
        label_LC.next_to(framebox_LC, direction=UP)
        self.play(Write(label_LC))
        self.wait(3)

        # Hide framebox & label
        self.play(Uncreate(framebox_LC), Unwrite(label_LC))
        self.wait(3)

        # R_source label
        R_source=MathTex("R_{S}").next_to(label_source).scale(1.3).shift(DOWN*0.35+LEFT*5.2)
        R_source[0].set_color(WHITE)

        # R_load label
        R_load=MathTex("R_{L}").next_to(label_load).scale(1.3).shift(DOWN*2.5+RIGHT*2.5)
        R_load[0].set_color(WHITE)

        self.play(Write(R_source), Write(R_load))
        self.wait(3)

        # R_source 50ohm label
        R_source_50=MathTex("50 \ \Omega").next_to(label_source).scale(1.3).shift(DOWN*0.32+LEFT*5.3)
        R_source_50[0].set_color(WHITE)

        # R_load 50ohm label
        R_load_50=MathTex("50 \ \Omega").move_to(R_load).scale(1.3).shift(UP*0.1+RIGHT*0.5)
        R_load_50[0].set_color(WHITE)

        self.play(ReplacementTransform(R_source, R_source_50), ReplacementTransform(R_load, R_load_50))
        self.wait(3)

        # L_1 label
        L_1=MathTex("L_{1}").next_to(R_source_50).scale(1.3).shift(RIGHT*1.55)
        L_1[0].set_color(WHITE)

        # C_1 label
        C_1=MathTex("C_{1}").next_to(R_load_50).scale(1.3).shift(LEFT*4)
        C_1[0].set_color(WHITE)
        self.play(Write(L_1))
        self.play(Write(C_1))

        self.wait(3)

        # # Right arrow
        # long_right_arrow_wave=Tex('$\Longrightarrow$').scale(5).next_to(ant_symbol).shift(RIGHT*5.9).set_color(WHITE)

        # self.play(
        #     FadeIn(long_right_arrow_wave, shift=RIGHT)
        # )

        # # n^2 = 4
        # nsquared=MathTex("n^2", #0
        # "=", #1
        # "4", #2
        # ).next_to(long_right_arrow_wave).scale(1.6).shift(LEFT*3.25+UP*0.9)

        # nsquared[0].set_color(YELLOW)
        # nsquared[1].set_color(WHITE)
        # nsquared[2].set_color(YELLOW)
        # self.play(Write(nsquared))

        # # 2-port matrix
        # m1_2port = MathTex(r"\mathrm{S}").set_color(YELLOW)
        # eq_2port = MathTex("=")
        # m2_2port = Matrix([[r"\mathrm{S}_{11}", r"\mathrm{S}_{12}"],
        #                    [r"\mathrm{S}_{21}", r"\mathrm{S}_{22}"]], left_bracket="(", right_bracket=")", element_alignment_corner=DR-DR)
        # m1_2port.shift(LEFT*2)
        # eq_2port.next_to(m1_2port)
        # m2_2port.next_to(eq_2port)
        # m2_2port[0][0].set_color(BLUE)
        # m2_2port[0][1].set_color(GREEN)
        # m2_2port[0][2].set_color(RED)
        # m2_2port[0][3].set_color(PURPLE)
        
        # g_2port = VGroup(m1_2port, m2_2port, eq_2port).next_to(long_right_arrow_wave).scale(2).shift(RIGHT*2.5+UP*0)

        # self.play(Write(g_2port))
        # self.wait(3)

        # # Framebox S21

        # framebox_s21 = SurroundingRectangle(m2_2port[0][2], buff = .2)
        # self.play(Create(framebox_s21))
        # self.wait(3)

        # # Display S21 curve
        # lowpass_s21 = ax.plot(lambda x: 10*np.log10(float(1)/float(math.sqrt(1+((x-2.186)**(2*2))))), x_range=[2.186, 5], color=RED)
        # lowpass_s21_flat = ax.plot(lambda x: 0, x_range=[0, 2.186], color=RED)

        # line1 = ax.get_vertical_line(
        #     ax.i2gp(3.5, lowpass_s21), line_func=DashedLine, stroke_width=8, color=ORANGE
        # )

        # cutoff_label=MathTex("-3 \mathrm{ \ dB}").next_to(R_source_50).scale(1.1).shift(RIGHT*15.8+UP*6.5)
        
        # self.play(
        #     AnimationGroup(
        #         Write(lowpass_s21_flat),
        #         Write(lowpass_s21),
        #         run_time=3,
        #         lag_ratio=0.5
        #         )
        # )
        # self.wait(3)
        # self.play(Write(line1),Write(cutoff_label))

        # self.wait(3)

        # framebox_s12 = SurroundingRectangle(m2_2port[0][1], buff = .2)

        # # Display S12 curve
        # lowpass_s12 = ax.plot(lambda x: 10*np.log10(float(1)/float(math.sqrt(1+((x-2.186)**(2*2))))), x_range=[2.186, 5], color=GREEN)
        # lowpass_s12_flat = ax.plot(lambda x: 0, x_range=[0, 2.186], color=GREEN)

        # self.play(
        #     AnimationGroup(
        #         ReplacementTransform(framebox_s21, framebox_s12),
        #         Write(lowpass_s12_flat),
        #         Write(lowpass_s12),
        #         run_time=3,
        #         lag_ratio=0.5
        #         ),
        #     #AnimationGroup(
        #     #    Uncreate(lowpass_s21),
        #     #    Uncreate(lowpass_s21_flat),
        #     #    run_time=3,
        #     #    lag_ratio=0.5
        #     #)
        # )
        
        # self.wait(3)

        # # Hide S21 and S12 curves

        # self.play(
        # #    AnimationGroup(
        # #        Uncreate(lowpass_s12),
        # #        Uncreate(lowpass_s12_flat),
        # #        run_time=3,
        # #        lag_ratio=0.5
        # #    ),
        #     Uncreate(line1),
        #     FadeOut(cutoff_label)
        # )
        
        # self.wait(3)

        # # Display s11 curve
        # lowpass_s11 = ax.plot(lambda x: 10*np.log10(1-10**((10*np.log10(float(1)/float(math.sqrt(1+((x-2.186)**(2*2))))))/10)), x_range=[2.3976, 5], color=BLUE)
        # lowpass_s11_flat = ax.plot(lambda x: -30, x_range=[0, 2.3976], color=BLUE)

        # framebox_s11 = SurroundingRectangle(m2_2port[0][0], buff = .2)
        # self.play(
        #     ReplacementTransform(framebox_s12, framebox_s11),
        #     AnimationGroup(
        #         Write(lowpass_s11_flat),
        #         Write(lowpass_s11),
        #         run_time=3,
        #         lag_ratio=0.5
        #         )
        # )

        # self.wait(3)

        # framebox_s22 = SurroundingRectangle(m2_2port[0][3], buff = .2)

        # # Display S22 curve
        # lowpass_s22 = ax.plot(lambda x: 10*np.log10(1-10**((10*np.log10(float(1)/float(math.sqrt(1+((x-2.186)**(2*2))))))/10)), x_range=[2.3976, 5], color=PURPLE)
        # lowpass_s22_flat = ax.plot(lambda x: -30, x_range=[0, 2.3976], color=PURPLE)

        # self.play(
        #     AnimationGroup(
        #         ReplacementTransform(framebox_s11, framebox_s22),
        #         Write(lowpass_s22_flat),
        #         Write(lowpass_s22),
        #         run_time=3,
        #         lag_ratio=0.5
        #         )
        # )

        # self.wait(3)

        # # Hide curves section
        # self.play(
        #     Uncreate(framebox_s22),
        #     AnimationGroup(
        #         Uncreate(lowpass_s11),
        #         Uncreate(lowpass_s22),
        #         Uncreate(lowpass_s21),
        #         Uncreate(lowpass_s12)
        #     ),
        #     run_time=1.5,
        #     lag_ratio=0.5
        # )
        # self.play(
        #     AnimationGroup(
        #         Uncreate(lowpass_s11_flat),
        #         Uncreate(lowpass_s22_flat),
        #         Uncreate(lowpass_s21_flat),
        #         Uncreate(lowpass_s12_flat)
        #     ),
        #     run_time=1.5,
        #     lag_ratio=0.5
        # )


        # #FadeOutAndShift(circuit_lowpass, direction=DOWN),
        # #FadeOutAndShift(R_source_50, direction=DOWN),
        # #FadeOutAndShift(R_load_50, direction=DOWN),
        
        # #FadeOutAndShift(long_right_arrow_wave, direction=RIGHT),
        # #Uncreate(s11_mag),
        # #Uncreate(nsquared)
        # #run_time=2)
        # self.wait(3)






        # ### Attenuator

        # self.play(
        #     x.submobjects[2].animate.set_opacity(0.5),
        #     x.submobjects[3].animate.set_opacity(1)
        # )

        # # Display attenuator circuit
        # circuit_attenuator = ImageMobject("/Users/Coto/Documents/edu/attenuator.png").scale(0.65).shift(LEFT*9.7+DOWN*12.6)

        # self.play(
        #     FadeOut(L_1),
        #     FadeOut(C_1),
        #     ReplacementTransform(circuit_lowpass, circuit_attenuator)
        # )

        # # Show attenuator framebox
        # framebox_attenuator = DashedVMobject(Rectangle(height=4.4, width=3.8).set_color(YELLOW).next_to(circuit_lowpass).shift(LEFT*6.4), num_dashes=30, positive_space_ratio=0.6)
        # self.play(Write(framebox_attenuator), run_time=1.5)

        # # Pi-pad attenuator label
        # label_attenuator = Tex(r"$\Pi$-Pad Attenuator").set_color(YELLOW).scale(1).shift(DOWN*0.2)
        # label_attenuator.next_to(framebox_attenuator, direction=UP)
        # self.play(Write(label_attenuator))
        # self.wait(3)

        # # Hide framebox & label
        # self.play(Unwrite(framebox_attenuator), Unwrite(label_attenuator))
        # self.wait(3)

        # # R_1 label
        # R_1=MathTex("R_{1}").next_to(R_load_50).scale(1.3).shift(LEFT*6.6)
        # R_1[0].set_color(WHITE)
        # self.play(Write(R_1))

        # # R_2 label
        # R_2=MathTex("R_{2}").next_to(R_load_50).scale(1.3).shift(LEFT*6).shift(UP*1.8)
        # R_2[0].set_color(WHITE)
        # self.play(Write(R_2))

        # # R_3 label
        # R_3=MathTex("R_{3}").next_to(R_load_50).scale(1.3).shift(LEFT*3.92)
        # R_3[0].set_color(WHITE)
        # self.play(Write(R_3))

        # # Framebox S21

        # framebox_s21 = SurroundingRectangle(m2_2port[0][2], buff = .2)
        # self.play(Create(framebox_s21))
        # self.wait(3)

        # # Display S21 curve
        # attenuator_s21 = ax.plot(lambda x: - (-0.3)/( 0.4 ** (  (0.5*x - ((x)**(x-(9*(x**2)))))   )  ) - 1.8*x - 14.675 - 0.445, x_range=[0, 5], color=RED)
        # line1 = ax.get_vertical_line(
        #     ax.i2gp(4, attenuator_s21), line_func=DashedLine, stroke_width=8, color=ORANGE
        # )
        # cutoff_label=MathTex("-20 \mathrm{ \ dB}").next_to(R_source_50).scale(1.1).shift(RIGHT*16.9+UP*2.6)
        
        # self.play(
        #     AnimationGroup(
        #         #Write(attenuator_s21_flat),
        #         Write(attenuator_s21),
        #         run_time=3,
        #         lag_ratio=0.5
        #         )
        # )

        # self.play(Write(line1),Write(cutoff_label))

        # attenuator_s12 = ax.plot(lambda x: - (-0.3)/( 0.4 ** (  (0.5*x - ((x)**(x-(9*(x**2)))))   )  ) - 1.8*x - 14.675 - 0.445, x_range=[0, 5], color=GREEN)

        # framebox_s12 = SurroundingRectangle(m2_2port[0][1], buff = .2)

        # self.play(
        #     AnimationGroup(
        #         ReplacementTransform(framebox_s21, framebox_s12),
        #         #Write(attenuator_s21_flat),
        #         Write(attenuator_s12),
        #         run_time=3,
        #         lag_ratio=0.5
        #         )
        # )

        # self.wait(3)
        # self.play(
        #     Uncreate(line1),
        #     FadeOut(cutoff_label)
        # )

        # attenuator_s11 = ax.plot(lambda x: (0.2*(np.log(x+0.06)/np.log(1.1))) - 23, x_range=[0, 5], color=BLUE)
        # # \left(0.2\log_{1.1}\left(x+0.06\right)\right)-23
        
        # framebox_s11 = SurroundingRectangle(m2_2port[0][0], buff = .2)

        # self.play(
        #     AnimationGroup(
        #         ReplacementTransform(framebox_s12, framebox_s11),
        #         #Write(attenuator_s21_flat),
        #         Write(attenuator_s11),
        #         run_time=3,
        #         lag_ratio=0.5
        #         )
        # )

        # self.wait(3)

        # attenuator_s22 = ax.plot(lambda x: (0.2*(np.log(x+0.06)/np.log(1.1))) - 23, x_range=[0, 5], color=PURPLE)
        
        # framebox_s22 = SurroundingRectangle(m2_2port[0][3], buff = .2)

        # self.play(
        #     AnimationGroup(
        #         ReplacementTransform(framebox_s11, framebox_s22),
        #         Write(attenuator_s22),
        #         run_time=3,
        #         lag_ratio=0.5
        #         )
        # )

        # self.wait(3)





        # ### Circulator

        # self.play(
        #     x.submobjects[3].animate.set_opacity(0.5),
        #     x.submobjects[4].animate.set_opacity(1)
        # )

        # # Display circulator circuit
        # circuit_circulator = ImageMobject("/Users/Coto/Documents/edu/circulator.png").scale(0.9).shift(LEFT*10.4+DOWN*12.9)

        # self.play(
        #     Uncreate(attenuator_s11),
        #     Uncreate(attenuator_s12),
        #     Uncreate(attenuator_s21),
        #     Uncreate(attenuator_s22),
        #     Uncreate(framebox_s22),
        #     FadeOut(R_1),
        #     FadeOut(R_2),
        #     FadeOut(R_3),
        #     FadeOut(R_source_50),
        #     FadeOut(R_load_50),
        #     Unwrite(g_2port),
        #     Unwrite(nsquared),
        #     FadeOut(long_right_arrow_wave, shift=RIGHT),
        #     FadeOut(circuit_attenuator, shift=DOWN),
        #     FadeIn(circuit_circulator, shift=RIGHT)
        # )

        # # Port 1 Circulator
        # port1_num_circ=MathTex("1").set_color(YELLOW)
        # port1_num_circ.shift(DOWN * 11.4)
        # port1_num_circ.shift(LEFT * 12.75)
        # port1_num_circ.scale(1.8)
        # # Port 2 Circulator
        # port2_num_circ=MathTex("2").set_color(YELLOW)
        # port2_num_circ.shift(DOWN * 11.4)
        # port2_num_circ.shift(LEFT * 8.1)
        # port2_num_circ.scale(1.8)
        # # Port 3 Circulator
        # port3_num_circ=MathTex("3").set_color(YELLOW)
        # port3_num_circ.shift(DOWN * 14.1)
        # port3_num_circ.shift(LEFT * 10.02)
        # port3_num_circ.scale(1.8)
        # # R_load label
        # R_load=MathTex("R_{L}").scale(1.3).shift(DOWN * 13.65).shift(LEFT * 9.7)
        # R_load[0].set_color(WHITE)

        # self.play(
        #     Write(port1_num_circ)
        # )
        # self.play(
        #     Write(port2_num_circ)
        # )
        # self.play(
        #     Write(port3_num_circ)
        # )

        # # Right arrow
        # long_right_arrow_wave=Tex('$\Longrightarrow$').scale(5).next_to(ant_symbol).shift(RIGHT*2.6).set_color(WHITE)

        # self.play(
        #     FadeIn(long_right_arrow_wave, shift=RIGHT)
        # )

        # # n^2 = 9
        # nsquared=MathTex("n^2", #0
        # "=", #1
        # "9", #2
        # ).next_to(long_right_arrow_wave).scale(1.6).shift(LEFT*3.25+UP*0.9)

        # nsquared[0].set_color(YELLOW)
        # nsquared[1].set_color(WHITE)
        # nsquared[2].set_color(YELLOW)
        # self.play(Write(nsquared))

        # # 3-port matrix
        # m1_3port = MathTex(r"\mathrm{S}").set_color(YELLOW)
        # eq_3port = MathTex("=")
        # m2_3port = Matrix([[r"\mathrm{S}_{11}", r"\mathrm{S}_{12}", r"\mathrm{S}_{13}"],
        #                    [r"\mathrm{S}_{21}", r"\mathrm{S}_{22}", r"\mathrm{S}_{23}"],
        #                    [r"\mathrm{S}_{31}", r"\mathrm{S}_{32}", r"\mathrm{S}_{33}"]], left_bracket="(", right_bracket=")", element_alignment_corner=DR-DR)
        # m1_2port.shift(LEFT*2)
        # eq_3port.next_to(m1_3port)
        # m2_3port.next_to(eq_3port)
        # m2_3port[0][0].set_color(BLUE)
        # m2_3port[0][1].set_color(GREEN)
        # m2_3port[0][2].set_color(TEAL)
        # m2_3port[0][3].set_color(RED)
        # m2_3port[0][4].set_color(ORANGE)
        # m2_3port[0][5].set_color(GOLD_A)
        # m2_3port[0][6].set_color(PURPLE)
        # m2_3port[0][7].set_color(MAROON_D)
        # m2_3port[0][8].set_color(LIGHT_PINK)

        # g_3port = VGroup(m1_3port, m2_3port, eq_3port).next_to(long_right_arrow_wave).scale(2).shift(RIGHT*3.7+UP*0)

        # self.play(Write(g_3port))

        # self.wait(3)

        # def create_csv(s):
        #     fin = open("manim_gif_data/circulator_data/"+s+".txt", "rt")
        #     fout = open("manim_gif_data/circulator_data/"+s+".csv", "wt")

        #     for line in fin:
	    #         fout.write(' '.join(line.split()).replace(' 1', '1').replace(' ', ',')+'\n')

        #     fin.close()
        #     fout.close()

        # ### Set x-axis limits to 13-18 GHz
        # self.play(
        #     Unwrite(dc_label),
        #     ReplacementTransform(ax, ax_highfreq)
        # )
        # #x_axis_config={"numbers_to_include": np.arange(13, 18.001, 1), "label_direction": UP},
        # create_csv('s11')
        # create_csv('s12')
        # create_csv('s13')
        # create_csv('s21')
        # create_csv('s22')
        # create_csv('s23')
        # create_csv('s31')
        # create_csv('s32')
        # create_csv('s33')
        # s11_circ = np.loadtxt(open("manim_gif_data/circulator_data/s11.csv", "rb"), delimiter=",", skiprows=2)
        # s12_circ = np.loadtxt(open("manim_gif_data/circulator_data/s12.csv", "rb"), delimiter=",", skiprows=2)
        # s13_circ = np.loadtxt(open("manim_gif_data/circulator_data/s13.csv", "rb"), delimiter=",", skiprows=2)
        # s21_circ = np.loadtxt(open("manim_gif_data/circulator_data/s21.csv", "rb"), delimiter=",", skiprows=2)
        # s22_circ = np.loadtxt(open("manim_gif_data/circulator_data/s22.csv", "rb"), delimiter=",", skiprows=2)
        # s23_circ = np.loadtxt(open("manim_gif_data/circulator_data/s23.csv", "rb"), delimiter=",", skiprows=2)
        # s31_circ = np.loadtxt(open("manim_gif_data/circulator_data/s31.csv", "rb"), delimiter=",", skiprows=2)
        # s32_circ = np.loadtxt(open("manim_gif_data/circulator_data/s32.csv", "rb"), delimiter=",", skiprows=2)
        # s33_circ = np.loadtxt(open("manim_gif_data/circulator_data/s33.csv", "rb"), delimiter=",", skiprows=2)

        # circulator_s11 = ax_highfreq.get_line_graph(s11_circ[:,0], s11_circ[:,1], add_vertex_dots=False, line_color=BLUE)
        # circulator_s12 = ax_highfreq.get_line_graph(s12_circ[:,0], s12_circ[:,1], add_vertex_dots=False, line_color=TEAL)
        # circulator_s13 = ax_highfreq.get_line_graph(s13_circ[:,0], s13_circ[:,1], add_vertex_dots=False, line_color=GREEN)
        # circulator_s21 = ax_highfreq.get_line_graph(s21_circ[:,0], s21_circ[:,1], add_vertex_dots=False, line_color=PURPLE)
        # circulator_s22 = ax_highfreq.get_line_graph(s22_circ[:,0], s22_circ[:,1], add_vertex_dots=False, line_color=LIGHT_PINK)
        # circulator_s23 = ax_highfreq.get_line_graph(s23_circ[:,0], s23_circ[:,1], add_vertex_dots=False, line_color=MAROON_D)
        # circulator_s31 = ax_highfreq.get_line_graph(s31_circ[:,0], s31_circ[:,1], add_vertex_dots=False, line_color=RED)
        # circulator_s32 = ax_highfreq.get_line_graph(s32_circ[:,0], s32_circ[:,1], add_vertex_dots=False, line_color=GOLD_A)
        # circulator_s33 = ax_highfreq.get_line_graph(s33_circ[:,0], s33_circ[:,1], add_vertex_dots=False, line_color=ORANGE)

        # # \left(0.2\log_{1.1}\left(x+0.06\right)\right)-23

        # framebox_s11 = SurroundingRectangle(m2_3port[0][0], buff = .2)
        # framebox_s12 = SurroundingRectangle(m2_3port[0][1], buff = .2)
        # framebox_s13 = SurroundingRectangle(m2_3port[0][2], buff = .2)
        # framebox_s21 = SurroundingRectangle(m2_3port[0][3], buff = .2)
        # framebox_s22 = SurroundingRectangle(m2_3port[0][4], buff = .2)
        # framebox_s23 = SurroundingRectangle(m2_3port[0][5], buff = .2)
        # framebox_s31 = SurroundingRectangle(m2_3port[0][6], buff = .2)
        # framebox_s32 = SurroundingRectangle(m2_3port[0][7], buff = .2)
        # framebox_s33 = SurroundingRectangle(m2_3port[0][8], buff = .2)

        # self.play(AnimationGroup(Create(framebox_s11),Write(circulator_s11),run_time=3,lag_ratio=0.5))
        # self.wait(3)
        # self.play(AnimationGroup(ReplacementTransform(framebox_s11,framebox_s12),Write(circulator_s13),run_time=3,lag_ratio=0.5))
        # self.play(AnimationGroup(ReplacementTransform(framebox_s12,framebox_s13),Write(circulator_s12),run_time=3,lag_ratio=0.5))
        # self.play(AnimationGroup(ReplacementTransform(framebox_s13,framebox_s21),Write(circulator_s31),run_time=3,lag_ratio=0.5))
        # self.play(AnimationGroup(ReplacementTransform(framebox_s21,framebox_s22),Write(circulator_s33),run_time=3,lag_ratio=0.5))
        # self.play(AnimationGroup(ReplacementTransform(framebox_s22,framebox_s23),Write(circulator_s32),run_time=3,lag_ratio=0.5))
        # self.play(AnimationGroup(ReplacementTransform(framebox_s23,framebox_s31),Write(circulator_s21),run_time=3,lag_ratio=0.5))
        # self.play(AnimationGroup(ReplacementTransform(framebox_s31,framebox_s32),Write(circulator_s23),run_time=3,lag_ratio=0.5))
        # self.play(AnimationGroup(ReplacementTransform(framebox_s32,framebox_s33),Write(circulator_s22),run_time=3,lag_ratio=0.5))
        
        # self.wait(3)

        # ### Isolator

        # # n^2 = 4
        # nsquared_isol=MathTex("n^2", #0
        # "=", #1
        # "4", #2
        # ).next_to(long_right_arrow_wave).scale(1.6).shift(LEFT*3.25+UP*0.9)

        # nsquared_isol[0].set_color(YELLOW)
        # nsquared_isol[1].set_color(WHITE)
        # nsquared_isol[2].set_color(YELLOW)

        # # 2-port matrix
        # m1_2port_isol = MathTex(r"\mathrm{S}").set_color(YELLOW)
        # eq_2port_isol = MathTex("=")
        # m2_2port_isol = Matrix([[r"\mathrm{S}_{11}", r"\mathrm{S}_{12}"],
        #                    [r"\mathrm{S}_{21}", r"\mathrm{S}_{22}"]], left_bracket="\\big(", right_bracket="\\big)", element_alignment_corner=DR-DR)
        # m1_2port_isol.shift(LEFT*2)
        # eq_2port_isol.next_to(m1_2port_isol)
        # m2_2port_isol.next_to(eq_2port_isol)
        # m2_2port_isol[0][0].set_color(BLUE)
        # m2_2port_isol[0][1].set_color(GREEN)
        # m2_2port_isol[0][2].set_color(RED)
        # m2_2port_isol[0][3].set_color(PURPLE)
        
        # g_2port_isol = VGroup(m1_2port_isol, m2_2port_isol, eq_2port_isol).next_to(long_right_arrow_wave).scale(2).shift(RIGHT*3.2+UP*0)


        # self.play(
        #     x.submobjects[4].animate.set_opacity(0.5),
        #     x.submobjects[5].animate.set_opacity(1)
        # )

        # # Display isolator circuit
        # circuit_isolator = ImageMobject("/Users/Coto/Documents/edu/isolator.png").scale(0.9).shift(LEFT*10.4+DOWN*12.9).set_z_index(-1)
        # isolator_s11 = circulator_s11.copy()
        # isolator_s13 = circulator_s13.copy()
        # isolator_s31 = circulator_s31.copy()
        # isolator_s33 = circulator_s33.copy().set_color(PURPLE)
        # self.play(
        #     ReplacementTransform(port3_num_circ, R_load),
        #     Uncreate(circulator_s11),
        #     Uncreate(circulator_s12),
        #     Uncreate(circulator_s13),
        #     Uncreate(circulator_s21),
        #     Uncreate(circulator_s22),
        #     Uncreate(circulator_s23),
        #     Uncreate(circulator_s31),
        #     Uncreate(circulator_s32),
        #     Uncreate(circulator_s33),
        #     FadeOut(framebox_s33),
        #     ReplacementTransform(g_3port, g_2port_isol),
        #     ReplacementTransform(nsquared, nsquared_isol),
        #     ReplacementTransform(circuit_circulator, circuit_isolator)
        # )
        # brace_isol = Brace(R_load, RIGHT, buff=0.1)
        # text_isol = brace_isol.get_text("Matched ","Load")
        # text_isol.scale(1.1) #.shift(LEFT*0.01)
        # self.wait(3)
        # self.play(GrowFromCenter(brace_isol))
        # self.play(Write(text_isol))
        # self.wait(3)
        # self.play(FadeOut(brace_isol),Unwrite(text_isol))
        # self.wait(3)

        # framebox_s11 = SurroundingRectangle(m2_2port_isol[0][0], buff = .2)
        # framebox_s12 = SurroundingRectangle(m2_2port_isol[0][1], buff = .2)
        # framebox_s21 = SurroundingRectangle(m2_2port_isol[0][2], buff = .2)
        # framebox_s22 = SurroundingRectangle(m2_2port_isol[0][3], buff = .2)

        # self.play(AnimationGroup(Create(framebox_s11),Write(isolator_s11),run_time=3,lag_ratio=0.5))
        # self.play(AnimationGroup(ReplacementTransform(framebox_s11,framebox_s12),Write(isolator_s13),run_time=3,lag_ratio=0.5))
        # self.play(AnimationGroup(ReplacementTransform(framebox_s12,framebox_s21),Write(isolator_s31),run_time=3,lag_ratio=0.5))
        # self.play(AnimationGroup(ReplacementTransform(framebox_s21,framebox_s22),Write(isolator_s33),run_time=3,lag_ratio=0.5))

        # self.wait(3)






        # ### Amplifier

        # # Display amplifier circuit
        # circuit_amplifier = ImageMobject("/Users/Coto/Documents/edu/amplifier.png").scale(0.6).shift(LEFT*10.6+DOWN*12.5).set_z_index(-1)

        # self.play(
        #     Uncreate(isolator_s11),
        #     Uncreate(isolator_s13),
        #     Uncreate(isolator_s31),
        #     Uncreate(isolator_s33),
        #     FadeOut(framebox_s22)
        # )
        # self.play(
        #     ReplacementTransform(ax_highfreq, ax_amp)
        # )

        # # Plus symbol next to battery (+)
        # plus=MathTex("+").set_color(WHITE)
        # plus.shift(DOWN * 10.5)
        # plus.shift(LEFT * 10.1)
        # plus.scale(0.9)
        # # Minus symbol next to battery (-)
        # minus=MathTex("-").set_color(WHITE)
        # minus.shift(DOWN * 10.5)
        # minus.shift(LEFT * 9.3)
        # minus.scale(0.9)

        # # +V
        # plusV=MathTex("\mathrm{+V}").set_color(WHITE)
        # plusV.shift(DOWN * 11.1)
        # plusV.shift(LEFT * 11.04)
        # plusV.scale(0.85)

        # # -V
        # minusV=MathTex("\mathrm{-V}").set_color(WHITE)
        # minusV.shift(DOWN * 14.1)
        # minusV.shift(LEFT * 11.04)
        # minusV.scale(0.85)

        # # Plus symbol next to battery (+)
        # voltage_num=MathTex("+").set_color(WHITE)
        # voltage_num.shift(DOWN * 10.5)
        # voltage_num.shift(LEFT * 10.1)
        # voltage_num.scale(0.9)

        # self.play(
        #     Unwrite(R_load),
        #     FadeOut(circuit_isolator, shift=DOWN),
        #     FadeIn(circuit_amplifier, shift=RIGHT),
        #     port1_num_circ.animate.shift(DOWN*0.8+LEFT*0.5),
        #     port2_num_circ.animate.shift(DOWN*0.8+RIGHT*0.1),
        #     x.submobjects[5].animate.set_opacity(0.5),
        #     x.submobjects[6].animate.set_opacity(1)
        # )
        # self.wait(3)
        # self.play(
        #     Write(plus),
        #     Write(minus),
        #     Write(plusV),
        #     Write(minusV)
        # )

        # s11_amp = np.loadtxt(open("manim_gif_data/amplifier/s11.csv", "rb"), delimiter=",")
        # s12_amp = np.loadtxt(open("manim_gif_data/amplifier/s12.csv", "rb"), delimiter=",")
        # s21_amp = np.loadtxt(open("manim_gif_data/amplifier/s21.csv", "rb"), delimiter=",")
        # s22_amp = np.loadtxt(open("manim_gif_data/amplifier/s22.csv", "rb"), delimiter=",")
        # s11_amp[:,0] /= 1e9
        # s12_amp[:,0] /= 1e9
        # s12_amp[:,1] += 10
        # s21_amp[:,0] /= 1e9
        # s21_amp[:,1] -= 10
        # s22_amp[:,0] /= 1e9

        # amplifier_s11 = ax_amp.get_line_graph(s11_amp[:,0], s11_amp[:,1], add_vertex_dots=False, line_color=BLUE)
        # amplifier_s12 = ax_amp.get_line_graph(s12_amp[:,0], s12_amp[:,1], add_vertex_dots=False, line_color=GREEN)
        # amplifier_s21 = ax_amp.get_line_graph(s21_amp[:,0], s21_amp[:,1], add_vertex_dots=False, line_color=RED)
        # amplifier_s22 = ax_amp.get_line_graph(s22_amp[:,0], s22_amp[:,1], add_vertex_dots=False, line_color=PURPLE)

        # framebox_s11 = SurroundingRectangle(m2_2port_isol[0][0], buff = .2)
        # framebox_s12 = SurroundingRectangle(m2_2port_isol[0][1], buff = .2)
        # framebox_s21 = SurroundingRectangle(m2_2port_isol[0][2], buff = .2)
        # framebox_s22 = SurroundingRectangle(m2_2port_isol[0][3], buff = .2)

        # self.play(AnimationGroup(Create(framebox_s11),Write(amplifier_s11),run_time=3,lag_ratio=0.5))
        # self.play(AnimationGroup(ReplacementTransform(framebox_s11,framebox_s12),Write(amplifier_s12),run_time=3,lag_ratio=0.5))
        # self.play(AnimationGroup(ReplacementTransform(framebox_s12,framebox_s21),Write(amplifier_s21),run_time=3,lag_ratio=0.5))
        # self.play(AnimationGroup(ReplacementTransform(framebox_s21,framebox_s22),Write(amplifier_s22),run_time=3,lag_ratio=0.5))
        # self.wait(3)
        # self.play(Uncreate(framebox_s22))

        # self.wait(3)

        # # 4.75-5.25 V DC tracker (counter)

        # start = 4.75
        # x_var = Variable(start, '', num_decimal_places=2).move_to(plus).shift(UP*0.6+LEFT*0.7).scale(1.2).set_color(TEAL)
        # vdc = Tex(".V DC").scale(1.2).set_color(TEAL)
        # # Hide '=' and '.'
        # rectangle_equals = Rectangle(height=0.4, width=0.5, stroke_width=0, color=BLACK, fill_color=BLACK, fill_opacity=1).move_to(x_var).shift(LEFT*0.62).set_z_index(10)
        # rectangle_dot = Rectangle(height=0.1, width=0.18, stroke_width=0, color=BLACK, fill_color=BLACK, fill_opacity=1).move_to(x_var).shift(RIGHT*0.91+DOWN*0.16).set_z_index(10)
        # vdc.add_updater(lambda x: x.next_to(x_var,RIGHT,buff=0.05))
        # self.play(
        #     FadeIn(rectangle_equals),
        #     FadeIn(rectangle_dot)
        # )

        # self.play(
        #     Write(x_var),
        #     Write(vdc)
        # )
        # self.wait(3)
        # x_var.tracker.set_value(4.75)
        # self.play(
        #     amplifier_s11.animate.shift(DOWN*0.2),
        #     amplifier_s12.animate.shift(DOWN*0.1), #at some frequencies it also goes up, barely varies
        #     amplifier_s21.animate.shift(DOWN*0.2),
        #     amplifier_s22.animate.shift(UP*0.1),
        #     x_var.tracker.animate.set_value(5.25), run_time=3, rate_func=smooth
        # )
        # self.play(
        #     amplifier_s11.animate.shift(UP*0.2),
        #     amplifier_s12.animate.shift(UP*0.1), #at some frequencies it also goes up, barely varies
        #     amplifier_s21.animate.shift(UP*0.2),
        #     amplifier_s22.animate.shift(DOWN*0.1),
        #     x_var.tracker.animate.set_value(4.75), run_time=3, rate_func=smooth
        # )
        # self.play(
        #     amplifier_s11.animate.shift(DOWN*0.1),
        #     amplifier_s12.animate.shift(DOWN*0.05), #at some frequencies it also goes up, barely varies
        #     amplifier_s21.animate.shift(DOWN*0.1),
        #     amplifier_s22.animate.shift(UP*0.05),
        #     x_var.tracker.animate.set_value(5), run_time=1.5, rate_func=smooth
        # )
        # self.wait(3)

        # # -20,+85 C temperature tracker (counter)
        # def interpolate_color(color1, color2, alpha):
        #     rgb = interpolate(color_to_rgb(color1), color_to_rgb(color2), alpha)
        #     return rgb_to_color(rgb)
        # def color_to_rgb(color):
        #     if isinstance(color, str):
        #         return hex_to_rgb(color)
        #     elif isinstance(color, Color):
        #         return np.array(color.get_rgb())
        #     else:
        #         raise Exception("Invalid color type")
        # def rgb_to_color(rgb):
        #     try:
        #         return Color(rgb=rgb)
        #     except ValueError:
        #         return Color(WHITE)
        # def get_alpha(Min,Max,Val):
        #     return (Val - Min)/(Max-Min)

        # temp = ValueTracker(25)
        # celcius = always_redraw(lambda: Tex("°C").scale(1.3).set_color(interpolate_color(BLUE,YELLOW,get_alpha(-20,0,temp.get_value()))) if (temp.get_value()<0) else Tex("°C").scale(1.3).set_color(interpolate_color(YELLOW,RED,get_alpha(0,85,temp.get_value()))))
        # celcius.add_updater(lambda x: x.next_to(temp_value,RIGHT,buff=0.05))
        # temp_text = always_redraw(lambda: Tex("$T=$").move_to(frequency_label).shift(RIGHT*3.9).scale(1.3).set_color(interpolate_color(BLUE,YELLOW,get_alpha(-20,0,temp.get_value()))) if (temp.get_value()<0) else Tex("$T=$").move_to(frequency_label).shift(RIGHT*3.9).scale(1.3).set_color(interpolate_color(YELLOW,RED,get_alpha(0,85,temp.get_value()))))
        # temp_value = always_redraw(lambda: DecimalNumber(num_decimal_places=0,include_sign=True).set_value(temp.get_value()).set_color(interpolate_color(BLUE,YELLOW,get_alpha(-20,0,temp.get_value()))).scale(1.3).next_to(temp_text, RIGHT, buff=0.1).shift(RIGHT*0.1) if (temp.get_value()<0) else DecimalNumber(num_decimal_places=0,include_sign=True).set_value(temp.get_value()).set_color(interpolate_color(YELLOW,RED,get_alpha(0,85,temp.get_value()))).scale(1.3).next_to(temp_text, RIGHT, buff=0.1).shift(RIGHT*0.1))
        # framebox_temp = Rectangle(height=0.82, width=3.5, color=YELLOW, fill_color=BLACK, fill_opacity=0.35, stroke_width=1.5).move_to(temp_text).shift(RIGHT*1)
        # self.play(
        #     Create(framebox_temp),
        #     Write(temp_text),
        #     Write(temp_value),
        #     Write(celcius)
        # )
        # self.wait(3)

        # self.play(
        #     amplifier_s11.animate.shift(DOWN*0.2),
        #     amplifier_s12.animate.shift(DOWN*0.1), # at some frequencies it also goes up, barely varies
        #     amplifier_s21.animate.shift(DOWN*0.4),
        #     amplifier_s22.animate.shift(UP*0.2),
        #     temp.animate.set_value(85), run_time=4, rate_func=smooth
        # )
        # self.wait(3)
        # self.play(
        #     amplifier_s11.animate.shift(UP*0.2),
        #     amplifier_s12.animate.shift(UP*0.1), #at some frequencies it also goes up, barely varies
        #     amplifier_s21.animate.shift(UP*0.4),
        #     amplifier_s22.animate.shift(DOWN*0.2),
        #     temp.animate.set_value(-20), run_time=5, rate_func=smooth
        # )
        # self.wait(3)
        # self.play(
        #     amplifier_s11.animate.shift(DOWN*0.1),
        #     amplifier_s12.animate.shift(DOWN*0.05), #at some frequencies it also goes up, barely varies
        #     amplifier_s21.animate.shift(DOWN*0.2),
        #     amplifier_s22.animate.shift(UP*0.1),
        #     temp.animate.set_value(25), run_time=1.5, rate_func=smooth
        # )

        # self.wait(3)

        # # s11 magnitude
        # s_func=MathTex("\mathrm{S}", #0
        # "(", #1
        # "f", #2
        # ",", #3
        # "V_s", #4
        # ",", #5
        # "T", #6
        # ")", #7
        # ).move_to(g_2port_isol).scale(2.2).shift(RIGHT*0.5)

        # s_func[0].set_color(YELLOW) #S
        # s_func[1].set_color(WHITE) #()
        # s_func[2].set_color(MAROON) #f
        # s_func[3].set_color(WHITE) #,
        # s_func[4].set_color(TEAL) #Vs
        # s_func[5].set_color(WHITE) #,
        # s_func[6].set_color(GOLD_E) #T
        # s_func[7].set_color(WHITE) #)

        # self.play(
        #     ReplacementTransform(g_2port_isol, s_func)
        # )
        # self.wait(3)
        # framebox_s = SurroundingRectangle(s_func, buff = .2)
        # self.play(Create(framebox_s))
        # self.wait(3)

        # s_func_p=MathTex("\mathrm{S}", #0
        # "(", #1
        # "f", #2
        # ",", #3
        # "V_s", #4
        # ",", #5
        # "T", #6
        # ",", #7
        # "P_\mathrm{in}", #8
        # ")", #9
        # ).move_to(g_2port_isol).scale(2.2).shift(RIGHT*0.8)
        # framebox_p = SurroundingRectangle(s_func_p, buff = .2)

        # s_func_p[0].set_color(YELLOW) #S
        # s_func_p[1].set_color(WHITE) #()
        # s_func_p[2].set_color(MAROON) #f
        # s_func_p[3].set_color(WHITE) #,
        # s_func_p[4].set_color(TEAL) #Vs
        # s_func_p[5].set_color(WHITE) #,
        # s_func_p[6].set_color(GOLD_E) #T
        # s_func_p[7].set_color(WHITE) #,
        # s_func_p[8].set_color(GREEN_B) #P_in
        # s_func_p[9].set_color(WHITE) #)

        # self.play(ReplacementTransform(framebox_s, framebox_p), ReplacementTransform(s_func, s_func_p))
        # self.wait(3)

        # # Move camera
        # self.play((self.camera.frame.animate).shift(DOWN*14),run_time=2, rate_func=smooth)
        # self.wait(3)

with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": False}):
    scene = ExampleNetworks()
    scene.render()