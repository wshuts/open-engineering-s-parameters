from manim import *


class Amplifier(MovingCameraScene):

    def __init__(self, camera_class=MovingCamera):
        super().__init__(camera_class)
        self.title_properties = None
        self.underline_properties = None
        self.networks = None
        self.ax_amp = None
        self.frequency_label = None
        self.magnitude_label = None
        self.circuit_amplifier = None
        self.port1_num = None
        self.port2_num = None
        self.plus = None
        self.minus = None
        self.plus_v = None
        self.minus_v = None
        self.long_right_arrow = None
        self.n_squared = None
        self.cap_s = None
        self.eq = None
        self.s2p_matrix = None
        self.grouped_equation = None

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
            self.ax_amp = Axes(
                x_range=[13, 18.001, 1],
                y_range=[-40.01, 20.5, 10],
                x_length=10.9,
                y_length=6.7,
                x_axis_config={"numbers_to_include": np.arange(14, 18.001, 1), "label_direction": UP},
                y_axis_config={"numbers_to_include": np.arange(-40.01, 20.5, 10)},
                tips=False,
            )
            self.frequency_label = MathTex("\mathrm{Frequency \ (GHz)}")
            self.magnitude_label = MathTex("\mathrm{Magnitude \ (dB)}")
            self.circuit_amplifier = ImageMobject("amplifier.png")
            self.port1_num = MathTex("1")
            self.port2_num = MathTex("2")
            self.plus = MathTex("+")
            self.minus = MathTex("-")
            self.plus_v = MathTex("\mathrm{+V}")
            self.minus_v = MathTex("\mathrm{-V}")
            self.long_right_arrow = Tex('$\Longrightarrow$')
            self.n_squared = MathTex("n^2", "=", "4")
            self.cap_s = MathTex(r"\mathrm{S}")
            self.eq = MathTex("=")
            self.s2p_matrix = Matrix([[r"\mathrm{S}_{11}", r"\mathrm{S}_{12}"],
                                      [r"\mathrm{S}_{21}", r"\mathrm{S}_{22}"]], left_bracket="(",
                                     right_bracket=")", element_alignment_corner=DR - DR)
            self.grouped_equation = VGroup(self.cap_s, self.eq, self.s2p_matrix)
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

            self.ax_amp.shift(DOWN * 5.9 + RIGHT * 2.45).scale(1.25)
            self.frequency_label.next_to(self.ax_amp).scale(1.1).shift(LEFT * 9 + UP * 5).set_color(WHITE)
            self.magnitude_label.next_to(self.ax_amp).scale(1.1).shift(LEFT * 18 + DOWN * 0)
            self.magnitude_label.set_color(WHITE).rotate(PI / 2)

            self.circuit_amplifier.scale(0.6).shift(
                LEFT * 10.6 + DOWN * 12.5).set_z_index(-1)

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

            self.long_right_arrow.scale(5).set_color(WHITE)
            self.long_right_arrow.shift(LEFT * 4 + DOWN * 12.5)

            self.n_squared.next_to(self.long_right_arrow).scale(1.6).shift(LEFT * 3.25 + UP * 0.9)
            self.n_squared[0].set_color(YELLOW)
            self.n_squared[1].set_color(WHITE)
            self.n_squared[2].set_color(YELLOW)

            self.cap_s.set_color(YELLOW)
            self.cap_s.shift(LEFT * 2)
            self.eq.next_to(self.cap_s)
            self.s2p_matrix.next_to(self.eq)
            self.s2p_matrix[0][0].set_color(BLUE)
            self.s2p_matrix[0][1].set_color(GREEN)
            self.s2p_matrix[0][2].set_color(RED)
            self.s2p_matrix[0][3].set_color(PURPLE)

            self.grouped_equation.next_to(self.long_right_arrow).scale(2).shift(RIGHT * 3.2 + UP * 0)
            return

        def animate():
            self.frame = self.camera.frame
            self.play(self.frame.animate.set_width(26).move_to(2.2 * LEFT + 8 * DOWN))
            self.play(FadeIn(self.title_properties, shift=LEFT), GrowFromCenter(self.underline_properties))
            self.play(Write(self.networks))
            self.play(Write(self.ax_amp), Write(self.frequency_label), Write(self.magnitude_label))
            self.play(
                FadeIn(self.circuit_amplifier, shift=RIGHT),
                self.port1_num.animate.shift(DOWN * 0.8 + LEFT * 0.5),
                self.port2_num.animate.shift(DOWN * 0.8 + RIGHT * 0.1),
                self.networks.submobjects[6].animate.set_opacity(1)
            )
            self.play(
                Write(self.plus),
                Write(self.minus),
                Write(self.plus_v),
                Write(self.minus_v)
            )
            self.play(
                FadeIn(self.long_right_arrow, shift=RIGHT),
                Write(self.n_squared)
            )
            self.play(Write(self.grouped_equation))
            return

        create()
        stage()
        animate()


with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": False, "from_animation_number": 0}):
    scene = Amplifier()
    scene.render()
