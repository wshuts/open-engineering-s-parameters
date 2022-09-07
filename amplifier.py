from manim import *


class Amplifier(MovingCameraScene):

    def __init__(self, camera_class=MovingCamera):
        super().__init__(camera_class)
        self.title_properties = None
        self.underline_properties = None
        self.networks = None
        self.circuit_amplifier = None
        self.ax_amp = None

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
                dot = MathTex("\\cdot").scale(3)
                dot.next_to(network[0], LEFT * 0.4, buff=0.4)
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
                # port1_num_circ.animate.shift(DOWN * 0.8 + LEFT * 0.5),
                # port2_num_circ.animate.shift(DOWN * 0.8 + RIGHT * 0.1),
                self.networks.submobjects[6].animate.set_opacity(1)
            )
            self.wait(3)
            # self.play(
            #     Write(plus),
            #     Write(minus),
            #     Write(plus_v),
            #     Write(minus_v)
            # )
            return

        create()
        stage()
        animate()


with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": False, "from_animation_number": 0}):
    scene = Amplifier()
    scene.render()
