from manim import *

class DesignatingSParameters(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):
        self.play(
            self.camera.frame.animate.set_width(26).move_to(2.2*LEFT+8*DOWN)
        )
        self.play((self.camera.frame.animate).shift(DOWN*5))

        # Title
        title_classifying = Text("Designating S-Parameters", color=YELLOW)
        title_classifying.scale(1.2)
        title_classifying.to_edge(UP).shift(LEFT*9.8+DOWN*9.9)

        # Title underline
        underline_classifying = Line(LEFT, RIGHT, color=YELLOW)
        underline_classifying.width=1.1*title_classifying.width
        underline_classifying.next_to(title_classifying, DOWN)
        underline_classifying.shift(UP * 0.1)
        self.play(FadeIn(title_classifying, shift=LEFT), GrowFromCenter(underline_classifying))

        m1_map = MathTex(r"\mathrm{S}").set_color(YELLOW)
        eq_map = MathTex("=").set_color(WHITE)
        m2_map = Matrix([[r"\mathrm{S}_{11}", r"\cdots", r"\mathrm{S}_{1n}"],
                     [r"\vdots", r"\ddots", r"\vdots"],
                     [r"\mathrm{S}_{n1}", r"\cdots", r"\mathrm{S}_{nn}"]], left_bracket="(", right_bracket=")", element_alignment_corner=DR-DR)
        m1_map.shift(DOWN*13.15) #RIGHT*1.2
        eq_map.next_to(m1_map)
        m2_map.next_to(eq_map)

        m2_map[0][0].set_color(BLUE)
        m2_map[0][1].set_color(RED)
        m2_map[0][2].set_color(RED)
        m2_map[0][3].set_color(RED)
        m2_map[0][4].set_color(BLUE)
        m2_map[0][5].set_color(RED)
        m2_map[0][6].set_color(RED)
        m2_map[0][7].set_color(RED)
        m2_map[0][8].set_color(BLUE)
        g_map = VGroup(m1_map, m2_map, eq_map).scale(2.2).shift(LEFT*5.5)
        m1_map_clear = MathTex(r"\mathrm{S}").set_color(YELLOW)
        eq_map_clear = MathTex("=").set_color(WHITE)
        m2_map_clear = Matrix([[r"\mathrm{S}_{11}", r"\cdots", r"\mathrm{S}_{1n}"],
                     [r"\vdots", r"\ddots", r"\vdots"],
                     [r"\mathrm{S}_{n1}", r"\cdots", r"\mathrm{S}_{nn}"]], left_bracket="(", right_bracket=")", element_alignment_corner=DR-DR)
        m1_map_clear.shift(DOWN*13.15) #RIGHT*1.2
        eq_map_clear.next_to(m1_map_clear)
        m2_map_clear.next_to(eq_map_clear)
        m2_map_clear[0][0].set_color(YELLOW)
        m2_map_clear[0][1].set_color(WHITE)
        m2_map_clear[0][2].set_color(YELLOW)
        m2_map_clear[0][3].set_color(WHITE)
        m2_map_clear[0][4].set_color(WHITE)
        m2_map_clear[0][5].set_color(WHITE)
        m2_map_clear[0][6].set_color(YELLOW)
        m2_map_clear[0][7].set_color(WHITE)
        m2_map_clear[0][8].set_color(YELLOW)
        g_map_clear = VGroup(m1_map_clear, m2_map_clear, eq_map_clear).scale(2.2).shift(LEFT*5.5).shift(RIGHT*(5.5+1.2))
        m1_map_t = MathTex(r"\mathrm{S}^\mathrm{T}").set_color(YELLOW)
        eq_map_t = MathTex("=").set_color(WHITE)
        m2_map_t = Matrix([[r"\mathrm{S}_{11}", r"\cdots", r"\mathrm{S}_{n1}"],
                     [r"\vdots", r"\ddots", r"\vdots"],
                     [r"\mathrm{S}_{1n}", r"\cdots", r"\mathrm{S}_{nn}"]], left_bracket="(", right_bracket=")", element_alignment_corner=DR-DR)
        m1_map_t.shift(DOWN*13.15) #RIGHT*1.2
        eq_map_t.next_to(m1_map_t)
        m2_map_t.next_to(eq_map_t)
        m2_map_t[0][0].set_color(YELLOW)
        m2_map_t[0][1].set_color(WHITE)
        m2_map_t[0][2].set_color(YELLOW)
        m2_map_t[0][3].set_color(WHITE)
        m2_map_t[0][4].set_color(WHITE)
        m2_map_t[0][5].set_color(WHITE)
        m2_map_t[0][6].set_color(YELLOW)
        m2_map_t[0][7].set_color(WHITE)
        m2_map_t[0][8].set_color(YELLOW)
        self.play(Write(g_map))
        self.wait(3)
        self.play(g_map.animate.shift(RIGHT*(5.5+1.2)))
        g_map_t = VGroup(m1_map_t, m2_map_t, eq_map_t).scale(2.2).shift(LEFT*5.5).shift(RIGHT*(5.5+1.2))

        # Title refl
        title_refl = Tex(r"Reflection Coefficients ",r"$(i = j)$", color=BLUE)
        title_refl.set_color_by_tex_to_color_map({
        "j": YELLOW_D
        })
        title_refl.scale(1.5)
        title_refl.to_edge(UP).shift(LEFT*9.09+DOWN*(13-0.5))
        # Title refl underline
        underline_refl = Line(LEFT, RIGHT, color=BLUE)
        underline_refl.width=1.1*title_refl.width
        underline_refl.next_to(title_refl, DOWN)
        underline_refl.shift(UP * 0.1)

        s11_txt = Tex(r"$\cdot$ $\mathrm{S}_{11}$ | Input return loss, VSWR", color=BLUE_B)
        s11_txt.scale(1.4)
        s11_txt.to_edge(UP).shift(LEFT*9.05+DOWN*(14.3-0.5))
        s22_txt = Tex(r"$\cdot$ $\mathrm{S}_{22}$ | Output return loss, VSWR", color=BLUE_B)
        s22_txt.scale(1.4)
        s22_txt.to_edge(UP).shift(LEFT*8.75+DOWN*(15.3-0.5))

        # Title tran
        title_tran = Tex(r"Transmission Coefficients ",r"$(i \neq j)$", color=RED)
        title_tran.set_color_by_tex_to_color_map({
        "j": YELLOW_D
        })
        title_tran.scale(1.5)
        title_tran.to_edge(UP).shift(LEFT*8.5+DOWN*(12+6))
        # Title tran underline
        underline_tran = Line(LEFT, RIGHT, color=RED)
        underline_tran.width=1.1*title_tran.width
        underline_tran.next_to(title_tran, DOWN)
        underline_tran.shift(UP * 0.1)

        s21_txt = Tex(r"$\cdot$ $\mathrm{S}_{21}$ | Gain ($>0 \mathrm{ \ dB}$), Loss ($\leq0 \mathrm{ \ dB}$)", color=RED_B)
        s21_txt.scale(1.4)
        s21_txt.to_edge(UP).shift(LEFT*8.35+DOWN*(13.3+6))
        s12_txt = Tex(r"$\cdot$ $\mathrm{S}_{12}$ | Reverse Isolation", color=RED_B)
        s12_txt.scale(1.4)
        s12_txt.to_edge(UP).shift(LEFT*10.3+DOWN*(14.3+6))

        self.play(FadeIn(title_refl, shift=LEFT), GrowFromCenter(underline_refl))
        self.play(Write(s11_txt))
        self.play(Write(s22_txt))
        self.wait(3)
        self.play(FadeIn(title_tran, shift=LEFT), GrowFromCenter(underline_tran))
        self.play(Write(s21_txt))
        self.play(Write(s12_txt))
        self.wait(3)

        # Reciprocity & Losslessness
        title_rec = Text("Reciprocity & Losslessness", color=YELLOW)
        title_rec.scale(1.2)
        title_rec.to_edge(UP).shift(LEFT*9.6+DOWN*9.9)
        # Title rec underline
        underline_rec = Line(LEFT, RIGHT, color=YELLOW)
        underline_rec.width=1.1*title_rec.width
        underline_rec.next_to(title_rec, DOWN)
        underline_rec.shift(UP * 0.1)

        self.play(
            FadeOut(title_refl),
            FadeOut(title_tran),
            FadeOut(s11_txt),
            FadeOut(s22_txt),
            FadeOut(s21_txt),
            FadeOut(s12_txt),
            FadeOut(underline_refl),
            FadeOut(underline_tran),
            ReplacementTransform(title_classifying, title_rec),
            ReplacementTransform(underline_classifying, underline_rec),
            ReplacementTransform(g_map, g_map_clear)
        )
        self.wait(3)
        # Title recipr
        title_recipr = Tex(r"Reciprocal Networks", color=TEAL)
        title_recipr.scale(1.5)
        title_recipr.to_edge(UP).shift(LEFT*(9.09+1.7)+DOWN*(13-0.5)).shift(DOWN*0.2)
        # Title recipr underline
        underline_recipr = Line(LEFT, RIGHT, color=TEAL)
        underline_recipr.width=1.1*title_recipr.width
        underline_recipr.next_to(title_recipr, DOWN)
        underline_recipr.shift(UP * 0.1)

        rec1_txt = Tex(r"$\cdot$ ",r"$\mathrm{S}_{ij}$",r"$\mathrm{}=\mathrm{}$",r"$\mathrm{S}_{ji}$",r"$, \mathrm{ \ } $",r"$i \neq j$", color=TEAL_B)
        rec1_txt.set_color_by_tex_to_color_map({
        r"ij": YELLOW,
        r"=": WHITE,
        r"ji": YELLOW,
        r",": WHITE,
        r"i \neq j": YELLOW_D
        })
        rec1_txt.scale(1.4)
        rec1_txt.to_edge(UP).shift(LEFT*(9.05+2.5)+DOWN*(15.3-0.45)).shift(DOWN*0.2)
        rec2_txt = Tex(r"$\cdot$ ",r"$\mathrm{S}$",r"$\mathrm{}=\mathrm{}$",r"$\mathrm{S}^{\mathrm{T}}$",r"$\mathrm{}\Leftrightarrow$", color=TEAL_B)
        rec2_txt.set_color_by_tex_to_color_map({
        r"S": YELLOW,
        r"=": WHITE,
        r"\Leftrightarrow": WHITE
        })
        rec2_txt.scale(1.4)
        rec2_txt.to_edge(UP).shift(LEFT*(8.3+4.1)+DOWN*(14.3-0.45)).shift(DOWN*0.2)
        self.play(FadeIn(title_recipr, shift=LEFT), GrowFromCenter(underline_recipr))
        self.play(Write(rec2_txt))
        self.play(g_map_clear.animate.shift(UP*3.5),
        TransformFromCopy(g_map_clear, g_map_t.shift(DOWN*3.5+LEFT*0.3))
        )
        self.play(Write(rec1_txt))

        self.wait(3)

        # Title loss
        title_loss = Tex(r"Lossless Networks", color=PURPLE)
        title_loss.scale(1.5)
        title_loss.to_edge(UP).shift(LEFT*(9.09+2.18)+DOWN*(19-0.5)).shift(UP*0.6)
        # Title loss underline
        underline_loss = Line(LEFT, RIGHT, color=PURPLE)
        underline_loss.width=1.1*title_loss.width
        underline_loss.next_to(title_loss, DOWN)
        underline_loss.shift(UP * 0.1)

        loss1_txt = Tex(r"$\cdot$ ",r"$P$",r"$\mathrm{} \propto \mathrm{}$",r"$V^2$",r"$\mathrm{}\Longrightarrow$", color=PURPLE_B)
        loss1_txt.set_color_by_tex_to_color_map({
        r"P": MAROON,
        r"\propto": WHITE,
        r"V": GREEN,
        r"$\mathrm{}\Longrightarrow$": WHITE,
        })
        loss1_txt.scale(1.4)
        loss1_txt.to_edge(UP).shift(LEFT*(8.88+3.2)+DOWN*(20.3-0.6)).shift(UP*0.6)
        loss2_txt = Tex(r"$\cdot$ ",r"$\sum\limits_{i=1}^{n} |$",r"$\mathrm{S}_{ij}$",r"$|^2$",r"$\mathrm{}=\mathrm{}$",r"$1$",r"$, \forall $",r"$j\mathrm{\ }$",r"$ \in $",r"$\mathrm{\ }[1, n]\mathrm{\ }$",r"$ \cap $",r"$\mathrm{\ }\mathbb{Z}$", color=WHITE)
        loss2_txt.set_color_by_tex_to_color_map({
        r"$\cdot$ ": PURPLE_B,
        r"S": YELLOW,
        r"$\mathrm{}=\mathrm{}$ ": WHITE,
        r"$\mathrm{\ }[1, n]\mathrm{\ }$": PURPLE,
        r"$1$": YELLOW,
        r"$\mathrm{\ }\mathbb{Z}$": ORANGE,
        r"$j\mathrm{\ }$": GOLD
        })
        loss2_txt.scale(1.4)
        loss2_txt.to_edge(UP).shift(LEFT*(5.45+4.1)+DOWN*(21.3-0.6)).shift(UP*0.6)
        self.play(FadeIn(title_loss, shift=LEFT), GrowFromCenter(underline_loss))
        self.wait(3)
        framebox1_scene6 = Rectangle(height=5.2, width=2, stroke_width=3, color=PURPLE_A, fill_color=PURPLE, fill_opacity=0.25).move_to(g_map_clear).shift(DOWN*0+LEFT*1.75)
        self.play(Write(loss1_txt))
        self.wait(3)
        self.play(Create(framebox1_scene6))
        self.wait(3)
        self.play(framebox1_scene6.animate.shift(RIGHT*2.88))
        self.wait(3)
        self.play(framebox1_scene6.animate.shift(RIGHT*2.86))
        self.wait(3)
        self.play(Uncreate(framebox1_scene6))
        self.wait(3)
        self.play(Write(loss2_txt))
        self.wait(3)

with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": True}):
    scene = DesignatingSParameters()
    scene.render()