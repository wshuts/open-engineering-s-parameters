from manim import *

class Outro(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-15, 15, 1],
            y_range=[-2, 2, 1],
            x_length=20,
            tips=False,
        ).shift(UP*20)
        wavelet = axes.plot(lambda x: np.cos(2*np.pi*x-2*np.pi*5)*np.exp(-x**2), color=BLUE).shift(DOWN*20.3).set_z_index(20)

        rectangle_outro = Rectangle(height=50, width=20, stroke_width=0, fill_color=BLACK, fill_opacity=0.6, z_index=-1).set_z_index(10)
        self.play(FadeIn(rectangle_outro))
        # Title
        title = Text("Special Thanks", gradient=(ORANGE,RED_D)).set_z_index(20)
        title.scale(1.5)
        title.to_edge(UP)

        # Title underline
        underline = Line(LEFT, RIGHT).set_z_index(20)
        underline.set_color(color_gradient([RED_D,ORANGE],10))
        underline.width=1.1*title.width
        underline.next_to(title, DOWN)
        underline.shift(UP * 0.1)

        # Names
        thanks1 = Text("Athanasios Kanatas", color=YELLOW_D).set_z_index(20).scale(0.8).shift(LEFT*3.5+UP*1.55)
        thanks2 = Text("Leonidas Marantis", color=YELLOW_D).set_z_index(20).scale(0.8).shift(LEFT*3.5+UP*0.45)
        thanks3 = Text("Dimitrios Rongas", color=YELLOW_D).set_z_index(20).scale(0.8).shift(RIGHT*3.5+UP*1.55)
        thanks4 = Text("Cameron Van Eck", color=YELLOW_D).set_z_index(20).scale(0.8).shift(RIGHT*3.5+UP*0.45)
        thanks_manim = Text("Manim Community & Developers", color=GOLD).set_z_index(20).scale(0.7).shift(LEFT*0.8+DOWN*2.1)
        thanks_3b1b = Text("Grant Sanderson (3Blue1Brown)", color=GOLD).set_z_index(20).scale(0.7).shift(LEFT*0.7+DOWN*3.2)

        # Manim Community
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#e7e0da"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN).set_z_index(20)
        logo.scale(0.2).shift(RIGHT*3.3+DOWN*2.1)

        #3b1b logo
        logo_3b1b = (
            SVGMobject(r"C:\Users\BillShuts\Desktop\2022\Repos\open-engineering-s-parameters\media\images\outro\3B1B_Logo.svg")
            .set_z_index(20).scale(0.42).shift(DOWN*3.2+RIGHT*3.2)
        )

        t = ValueTracker(0)

        def func1(x):
            w = lambda p: 0.35*np.array([p[1]*np.cos(x)-p[0]*np.sin(x),-p[1]*np.sin(x)-p[0]*np.cos(x),0])
            return w

        field1 = ArrowVectorField(func1(float(t.get_value()))).set_z_index(0)
        field1.set_color_by_gradient(BLUE_D, BLUE_E)
        field1.add_updater(lambda j: j.become(ArrowVectorField(func1(float(t.get_value())))))
        
        #Logo = Text("Special thanks...").scale(1).move_to([0,-0.2,0])
        #Logo2 = Text("EE", color = BLUE).scale(4).move_to([2,-1.5,0])
        self.add(field1)

        # 8-sec
        self.play(t.animate.set_value(0+8), run_time = 16, rate_func=linear)
        # title
        self.play(Write(title),GrowFromCenter(underline), t.animate.set_value(8+0.5), run_time = 1, rate_func=linear)
        # 1-sec
        self.play(t.animate.set_value(8.5+0.5), run_time = 1, rate_func=linear)
        # thanks 1-4
        self.play(AnimationGroup(Write(thanks1),Write(thanks2),Write(thanks3),Write(thanks4),lag_ratio=0.4),t.animate.set_value(9+0.5),run_time=1, rate_func=linear)
        # 1-sec
        self.play(t.animate.set_value(9.5+0.5), run_time = 1, rate_func=linear)
        # wavelet
        self.play(Write(wavelet),t.animate.set_value(10+2),run_time=4, rate_func=linear)
        # 0.5-sec
        self.play(t.animate.set_value(12+0.25), run_time = 0.5, rate_func=linear)
        # manim thanks
        self.play(GrowFromCenter(logo_3b1b),Write(thanks_manim),Write(thanks_3b1b),Create(logo),FadeIn(axes),t.animate.set_value(12.25+0.5),run_time=1, rate_func=linear)
        # 8-sec
        self.play(t.animate.set_value(12.75+4), run_time = 8, rate_func=linear)

        ###self.play(Rotate(field1.scale(2),PI),run_time = 6)

with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": True}):
    scene = Outro()
    scene.render()