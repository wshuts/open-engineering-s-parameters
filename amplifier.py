from manim import *


class Amplifier(MovingCameraScene):

    def __init__(self, camera_class=MovingCamera):
        super().__init__(camera_class)
        self.title_properties = None
        self.underline_properties = None
        self.networks = None
        self.circuit_amplifier = None
        self.ax_amp = None
        self.port1_num = None
        self.port2_num = None
        self.plus = None
        self.minus = None
        self.plus_v = None
        self.minus_v = None
        self.long_right_arrow_wave = None
        self.n_squared_isolation = None
        self.m1_2port_isolation = None
        self.eq_2port_isolation = None
        self.m2_2port_isolation = None
        self.g_2port_isolation = None

    def setup(self):
        MovingCameraScene.setup(self)

    # noinspection PyTypeChecker
    def construct(self):
        def create():
            self.title_properties = Text("Example Networks", color=YELLOW)
            self.underline_properties = Line(LEFT, RIGHT, color=YELLOW)
            self.networks = Tex("Antennas", "Dummy Loads", "Filters", "Attenuators", "Circulators", "Isolators",
                                "Amplifiers")
            for network in self.networks:
                dot = MathTex("\\cdot")
                dot.scale(3).next_to(network[0], LEFT * 0.4, buff=0.4)
                network.add_to_back(dot)
            self.circuit_amplifier = ImageMobject("amplifier.png")
            self.ax_amp = Axes(
                x_range=[13, 18.001, 1],
                y_range=[-40.01, 20.5, 10],
                x_length=10.9,
                y_length=6.7,
                x_axis_config={"numbers_to_include": np.arange(13, 18.001, 1), "label_direction": UP},
                y_axis_config={"numbers_to_include": np.arange(-40.01, 20.5, 10)},
                tips=False,
            )
            self.port1_num = MathTex("1")
            self.port2_num = MathTex("2")
            self.plus = MathTex("+")
            self.minus = MathTex("-")
            self.plus_v = MathTex("\mathrm{+V}")
            self.minus_v = MathTex("\mathrm{-V}")
            self.long_right_arrow_wave = Tex('$\Longrightarrow$')
            self.n_squared_isolation = MathTex("n^2", "=", "4")
            self.m1_2port_isolation = MathTex(r"\mathrm{S}")
            self.eq_2port_isolation = MathTex("=")
            self.m2_2port_isolation = Matrix([[r"\mathrm{S}_{11}", r"\mathrm{S}_{12}"],
                                              [r"\mathrm{S}_{21}", r"\mathrm{S}_{22}"]], left_bracket="(",
                                             right_bracket=")", element_alignment_corner=DR - DR)
            self.g_2port_isolation = VGroup(self.m1_2port_isolation, self.m2_2port_isolation, self.eq_2port_isolation)
            return

        def stage():
            self.title_properties.scale(1.2)
            self.title_properties.to_edge(UP).shift(LEFT * 11 + DOWN * 5)

            self.underline_properties.width = 1.1 * self.title_properties.width
            self.underline_properties.next_to(self.title_properties, DOWN)
            self.underline_properties.shift(UP * 0.1)

            self.networks.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            self.networks.scale(1.45)
            self.networks.shift(LEFT * 11.4 + DOWN * 6.1)
            self.networks.set_opacity(0.5)

            self.circuit_amplifier.scale(0.6).shift(
                LEFT * 10.6 + DOWN * 12.5).set_z_index(-1)

            self.ax_amp.shift(DOWN * 5.9 + RIGHT * 2.45).scale(1.25)

            self.port1_num.set_color(YELLOW)
            self.port1_num.shift(DOWN * 11.4)
            self.port1_num.shift(LEFT * 12.75)
            self.port1_num.scale(1.8)

            self.port2_num.set_color(YELLOW)
            self.port2_num.shift(DOWN * 11.4)
            self.port2_num.shift(LEFT * 8.1)
            self.port2_num.scale(1.8)

            self.plus.set_color(WHITE)
            self.plus.shift(DOWN * 10.5)
            self.plus.shift(LEFT * 10.1)
            self.plus.scale(0.9)

            self.minus.set_color(WHITE)
            self.minus.shift(DOWN * 10.5)
            self.minus.shift(LEFT * 9.3)
            self.minus.scale(0.9)

            self.plus_v.set_color(WHITE)
            self.plus_v.shift(DOWN * 11.1)
            self.plus_v.shift(LEFT * 11.04)
            self.plus_v.scale(0.85)

            self.minus_v.set_color(WHITE)
            self.minus_v.shift(DOWN * 14.1)
            self.minus_v.shift(LEFT * 11.04)
            self.minus_v.scale(0.85)

            self.long_right_arrow_wave.scale(5).set_color(WHITE)
            self.long_right_arrow_wave.shift(DOWN * 12.5 + RIGHT * 1)

            self.n_squared_isolation.next_to(self.long_right_arrow_wave).scale(1.6).shift(LEFT * 3.25 + UP * 0.9)
            self.n_squared_isolation[0].set_color(YELLOW)
            self.n_squared_isolation[1].set_color(WHITE)
            self.n_squared_isolation[2].set_color(YELLOW)

            self.m1_2port_isolation.set_color(YELLOW)
            self.m1_2port_isolation.shift(LEFT * 2)
            self.eq_2port_isolation.next_to(self.m1_2port_isolation)
            self.m2_2port_isolation.next_to(self.eq_2port_isolation)
            self.m2_2port_isolation[0][0].set_color(BLUE)
            self.m2_2port_isolation[0][1].set_color(GREEN)
            self.m2_2port_isolation[0][2].set_color(RED)
            self.m2_2port_isolation[0][3].set_color(PURPLE)

            self.g_2port_isolation.next_to(self.long_right_arrow_wave).scale(2).shift(RIGHT * 3.2 + UP * 0)
            return

        def animate():
            self.frame = self.camera.frame
            self.play(
                self.frame.animate.set_width(26).move_to(2.2 * LEFT + 8 * DOWN))
            self.play(FadeIn(self.title_properties, shift=LEFT), GrowFromCenter(self.underline_properties))
            self.wait(3)
            self.play(Write(self.networks))
            self.play(Write(self.ax_amp))
            self.play(
                FadeIn(self.circuit_amplifier, shift=RIGHT),
                self.port1_num.animate.shift(DOWN * 0.8 + LEFT * 0.5),
                self.port2_num.animate.shift(DOWN * 0.8 + RIGHT * 0.1),
                self.networks.submobjects[6].animate.set_opacity(1)
            )
            self.wait(3)
            self.play(
                Write(self.plus),
                Write(self.minus),
                Write(self.plus_v),
                Write(self.minus_v)
            )
            self.play(
                FadeIn(self.long_right_arrow_wave, shift=RIGHT)
            )
            self.play(
                Write(self.n_squared_isolation),
                Write(self.g_2port_isolation)
            )
            return

        create()
        stage()
        animate()


with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": False, "from_animation_number": 0}):
    scene = Amplifier()
    scene.render()
