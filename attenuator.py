from manim import *

class Attenuator(MovingCameraScene):
    def construct(self):
        texTemplate = TexTemplate()
        texTemplate.add_to_preamble(r"\usepackage{circuitikz}")

        circuitString="""\\begin{circuitikz}[american, scale=0.5, transform shape]
            \draw (0, 0)
                to [sV] ++(0, -4) node[ground]{};
            \draw (0, 0)
                to [R, -*] ++(4, 0);
            \draw (4, 0)
                to [short] ++(2, 0);
            \draw (6, 0)
                to [R] ++(0, -4) node[ground]{};
            \draw (6, 0)
                to [R] ++(4, 0);
            \draw (10, 0)
                to [R] ++(0, -4) node[ground]{};
            \draw (10, 0)
                to [short, -*] ++(2, 0);
            \draw (12, 0)
                to [short] ++(2, 0);
            \draw (14, 0)
                to [R] ++(0, -4) node[ground]{};
	    \end{circuitikz}"""

        circuit=Tex(circuitString, tex_template=texTemplate, stroke_width=2, fill_opacity=0)
        self.add(circuit)

with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": False}):
    scene = Attenuator()
    scene.render()