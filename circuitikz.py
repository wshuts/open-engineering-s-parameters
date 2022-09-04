from manim import *

class Circuitikz(MovingCameraScene):
    def construct(self):
        texTemplate = TexTemplate()
        texTemplate.add_to_preamble(r"\usepackage{circuitikz}")

        circuitString="""\\begin{circuitikz}[american]
                \draw (0, 4) node [anchor = south east] {$a$}
                    to [V, *-*, l_=$V_S$] ++(0, -4) node [anchor = north east] {$b$};
                \draw (0, 4)
                    to [short] ++(4, 0)
                    to [R, l=$R_1$, v=$V_1$] ++(0, -4)
                    to [I, l=$I_S$] ++(-4, 0);
                \draw [very thick, ->] (4.5, 3.5)
                    to  ++(0, 1) node [anchor = south west] {$I$}
                    to  ++(-1, 0);
                \node at (6, 6) {$X$ (some node)};
            \end{circuitikz}"""

        circuit=Tex(circuitString, tex_template=texTemplate, stroke_width=2, fill_opacity=0)
        self.add(circuit)

with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": False}):
    scene = Circuitikz()
    scene.render()