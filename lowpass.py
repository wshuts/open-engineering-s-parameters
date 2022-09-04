from manim import *

class LowPass(MovingCameraScene):
    def construct(self):
        texTemplate = TexTemplate()
        texTemplate.add_to_preamble(r"\usepackage{circuitikz}")

        circuitString="""\\begin{circuitikz}
            \draw (0,0) to[R, l=$R_1$, f=$i_1$] (2,0);
            \end{circuitikz}"""

        circuit=Tex(circuitString, tex_template=texTemplate, stroke_width=2, fill_opacity=0)
        self.add(circuit)

with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": False}):
    scene = LowPass()
    scene.render()