from colour import Color
from manim import *

PAN_CAMERA_DOWN = 0
PAN_CAMERA_LEFT = 0
DEFAULT_WIDTH = 8*(16/9)
FRAME_WIDTH = 2 * DEFAULT_WIDTH


class Amplifier(MovingCameraScene):

    def __init__(self, camera_class=MovingCamera):
        super().__init__(camera_class)
        self.frame = self.camera.frame
        self.number_plane = NumberPlane()
        self.title = None
        self.underline = None
        self.networks = None
        self.title_group = None
        self.ax_amp = None
        self.frequency_label = None
        self.magnitude_label = None
        self.axes_group = None
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
        self.amplifier_s11 = None
        self.amplifier_s12 = None
        self.amplifier_s21 = None
        self.amplifier_s22 = None
        self.s11_amp = None
        self.s21_amp = None
        self.s12_amp = None
        self.s22_amp = None
        self.frame_box_s11 = None
        self.frame_box_s21 = None
        self.frame_box_s12 = None
        self.frame_box_s22 = None

    def setup(self):
        MovingCameraScene.setup(self)
        self.frame.width = FRAME_WIDTH
        self.frame.move_to(PAN_CAMERA_LEFT * LEFT + PAN_CAMERA_DOWN * DOWN)
        self.add(self.number_plane)
        self.number_plane.width = FRAME_WIDTH
        self.number_plane.move_to(PAN_CAMERA_LEFT * LEFT + PAN_CAMERA_DOWN * DOWN)

    # noinspection PyTypeChecker
    def construct(self):
        def read_spar(path="manim_gif_data/amplifier/", parameter="s11", ext=".csv", mode="rb", delimiter=","):
            stream = open(path + parameter + ext, mode)
            return np.loadtxt(stream, delimiter=delimiter)

        def scale_array_column(array, column=0, scaling_factor=1e9):
            scaled_array = np.copy(array)
            scaled_array[:, column] /= scaling_factor
            return scaled_array

        def shift_array_column(array, column=1, offset=10):
            scaled_array = np.copy(array)
            scaled_array[:, column] += offset
            return scaled_array

        def create():
            self.title = Text("Example Networks", color=YELLOW)
            self.underline = Line(LEFT, RIGHT, color=YELLOW)
            self.networks = Tex("Antennas", "Dummy Loads", "Filters", "Attenuators", "Circulators", "Isolators",
                                "Amplifiers")
            for network in self.networks:
                dot = MathTex("\\cdot")
                dot.scale(3).next_to(network[0], LEFT * 0.4, buff=0.4)
                network.add_to_back(dot)
            self.title_group = VGroup(self.title, self.underline, self.networks)
            self.ax_amp = Axes(
                x_range=[13, 18, 1],
                y_range=[-40, 20, 10],
                x_length=10,
                y_length=6,
                x_axis_config={"numbers_to_include": np.arange(14, 19, 1), "label_direction": UP},
                y_axis_config={"numbers_to_include": np.arange(-40, 30, 10)},
                tips=False,
            )
            self.frequency_label = MathTex("\mathrm{Frequency \ (GHz)}")
            self.magnitude_label = MathTex("\mathrm{Magnitude \ (dB)}")
            self.axes_group = VGroup(self.ax_amp, self.frequency_label, self.magnitude_label)
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
                                      [r"\mathrm{S}_{21}", r"\mathrm{S}_{22}"]],
                                     left_bracket="(", right_bracket=")", element_alignment_corner=DR - DR)
            self.grouped_equation = VGroup(self.cap_s, self.eq, self.s2p_matrix)
            self.s11_amp = read_spar(parameter="s11")
            self.s21_amp = read_spar(parameter="s21")
            self.s12_amp = read_spar(parameter="s12")
            self.s22_amp = read_spar(parameter="s22")
            self.s11_amp = scale_array_column(self.s11_amp)
            self.s21_amp = scale_array_column(self.s21_amp)
            self.s12_amp = scale_array_column(self.s12_amp)
            self.s22_amp = scale_array_column(self.s22_amp)
            self.s21_amp = shift_array_column(self.s21_amp, offset=-10)
            self.s12_amp = shift_array_column(self.s12_amp)

            self.amplifier_s11 = self.ax_amp.plot_line_graph(self.s11_amp[:, 0], self.s11_amp[:, 1],
                                                             add_vertex_dots=False, line_color=Color(BLUE))
            self.amplifier_s12 = self.ax_amp.plot_line_graph(self.s12_amp[:, 0], self.s12_amp[:, 1],
                                                             add_vertex_dots=False, line_color=Color(GREEN))
            self.amplifier_s21 = self.ax_amp.plot_line_graph(self.s21_amp[:, 0], self.s21_amp[:, 1],
                                                             add_vertex_dots=False, line_color=Color(RED))
            self.amplifier_s22 = self.ax_amp.plot_line_graph(self.s22_amp[:, 0], self.s22_amp[:, 1],
                                                             add_vertex_dots=False, line_color=Color(PURPLE))
            self.frame_box_s11 = SurroundingRectangle(self.s2p_matrix[0][0], buff=.2)
            self.frame_box_s12 = SurroundingRectangle(self.s2p_matrix[0][1], buff=.2)
            self.frame_box_s21 = SurroundingRectangle(self.s2p_matrix[0][2], buff=.2)
            self.frame_box_s22 = SurroundingRectangle(self.s2p_matrix[0][3], buff=.2)
            return

        def stage():
            self.title.scale(1.2)
            self.title.to_edge(UP)

            self.underline.width = 1.1 * self.title.width
            self.underline.next_to(self.title, DOWN)

            self.networks.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            self.networks.scale(1.45)
            self.networks.next_to(self.underline, DOWN)
            self.networks.set_opacity(0.5)

            self.title_group.shift(8 * LEFT + 3.6 * UP)

            self.ax_amp.scale(1.25)
            self.frequency_label.next_to(self.ax_amp, UP).scale(1.1).set_color(WHITE)
            self.magnitude_label.next_to(self.ax_amp, LEFT).scale(1.1).set_color(WHITE)
            self.magnitude_label.rotate(PI / 2)

            self.axes_group.shift(6.5 * RIGHT + 3 * UP)

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

            self.frame_box_s11.move_to(ORIGIN)
            return

        def animate():
            self.play(FadeIn(self.title, shift=LEFT), GrowFromCenter(self.underline))
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
            self.play(
                AnimationGroup(
                    Create(self.frame_box_s11),
                    Write(self.amplifier_s11),
                    run_time=3, lag_ratio=0.5
                )
            )
            self.play(
                AnimationGroup(
                    ReplacementTransform(self.frame_box_s11, self.frame_box_s12),
                    Write(self.amplifier_s12),
                    run_time=3, lag_ratio=0.5
                )
            )
            self.play(
                AnimationGroup(
                    ReplacementTransform(self.frame_box_s12, self.frame_box_s21),
                    Write(self.amplifier_s21),
                    run_time=3, lag_ratio=0.5
                )
            )
            self.play(
                AnimationGroup(
                    ReplacementTransform(self.frame_box_s21, self.frame_box_s22),
                    Write(self.amplifier_s22),
                    run_time=3, lag_ratio=0.5
                )
            )
            self.play(Uncreate(self.frame_box_s22))
            return

        create()
        stage()
        animate()


with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": False, "from_animation_number": 6,
                 "upto_animation_number": 6}):
    scene = Amplifier()
    scene.render()
