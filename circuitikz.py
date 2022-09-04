from manim import *

class Circuitikz(MovingCameraScene):
    def construct(self):
        texTemplate = TexTemplate()
        texTemplate.add_to_preamble(r"\usepackage{circuitikz}")

        circuitString="""\\begin{circuitikz}[american]
                \draw (0, 4) node [anchor = south east] {$a$}
                    to [V, *-*, l_=$V_S$] ++(0, -4) node [anchor = north east] {$b$};
            \end{circuitikz}"""

        circuit=Tex(circuitString, tex_template=texTemplate, stroke_width=2, fill_opacity=0)
        self.add(circuit)

with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": False}):
    scene = Circuitikz()
    scene.render()