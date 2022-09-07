from manim import *


class Amplifier(MovingCameraScene):
    title_properties = None
    underline_properties = None
    networks = None

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
            return

        def animate():
            self.frame = self.camera.frame
            self.play(
                self.frame.animate.set_width(26).move_to(2.2 * LEFT + 8 * DOWN))
            self.play(FadeIn(self.title_properties, shift=LEFT), GrowFromCenter(self.underline_properties))
            self.wait(3)
            self.play(Write(self.networks))
            return

        create()
        stage()
        animate()


with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": False, "from_animation_number": 0}):
    scene = Amplifier()
    scene.render()
