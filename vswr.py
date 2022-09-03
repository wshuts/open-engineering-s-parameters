from manim import *

class VSWR(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):
        ax = Axes(
            x_range=[1.001, 100, 20],
            y_range=[-60, 0, 10],
            x_length=10.5,
            y_length=5,
            x_axis_config={"numbers_to_include": [1, 20, 40, 60, 80, 100], "label_direction": UP},
            y_axis_config={"numbers_to_include": [-60, -50, -40, -30, -20, -10]},
            tips=False,
        )
        ax.shift(DOWN*0.85+RIGHT*0.2)
        zero_label = MathTex("0").next_to(ax).scale(0.75).shift(LEFT*11.45, UP*2.25).set_color(WHITE)
        vswr_label = MathTex("\mathrm{Voltage \ Standing \ Wave \ Ratio \ (VSWR)}").next_to(ax).scale(0.9).shift(LEFT*10, UP*3.2).set_color(WHITE)
        s11_label = MathTex("|\mathrm{S}_{11}| \ \mathrm{(dB)}}").next_to(ax).scale(0.9).shift(LEFT*13.3+DOWN*0.2).set_color(WHITE).rotate(PI/2)

        # Title
        title_properties = Text("Reflection Coefficient and VSWR", color=YELLOW)
        title_properties.scale(0.7)
        title_properties.to_edge(UP).shift(LEFT*3.2+UP*0.1)

        # Title underline
        underline_properties = Line(LEFT, RIGHT, color=YELLOW)
        underline_properties.set_width(1.1*title_properties.get_width())
        underline_properties.next_to(title_properties, DOWN)
        underline_properties.shift(UP * 0.1)
        self.play(Write(title_properties), GrowFromCenter(underline_properties))
        self.wait(3)
        self.play(Write(ax), Write(zero_label), Write(vswr_label), Write(s11_label), run_time=2.8, rate_func=smooth)
        vswr_graph_x = [1.002,1.0021,1.2021,1.4021,1.6021,1.8021,2.0021,2.2021,2.4021,2.6021,2.8021,3.0021,3.2021,3.4021,3.6021,3.8021,4.0021,4.2021,4.4021,4.6021,4.8021,5.0021,5.2021,5.4021,5.6021,5.8021,6.0021,6.2021,6.4021,6.6021,6.8021,7.0021,7.2021,7.4021,7.6021,7.8021,8.0021,8.2021,8.4021,8.6021,8.8021,9.0021,9.2021,9.4021,9.6021,9.8021,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
        vswr_graph_y = [-60.00868155,-59.58532942,-20.74541447,-15.5251402,-12.71310711,-10.86510228,-9.530281847,-8.509885869,-7.699361713,-7.037322899,-6.48489297,-6.016043409,-5.612586929,-5.261376414,-4.952641372,-4.678951391,-4.434544304,-4.214876116,-4.016310887,-3.835901831,-3.67123349,-3.520305815,-3.381447619,-3.253250991,-3.134520937,-3.024236254,-2.921518782,-2.825609016,-2.735846574,-2.651654424,-2.572526055,-2.49801495,-2.427725911,-2.361307853,-2.298447776,-2.238865718,-2.182310484,-2.128556026,-2.07739836,-2.028652929,-1.982152329,-1.937744359,-1.895290325,-1.854663568,-1.815748185,-1.778437904,-1.743003514,-1.583624921,-1.451013343,-1.338935793,-1.242958135,-1.15983894,-1.087153246,-1.023050449,-0.9660935915,-0.9151498112,-0.8693138756,-0.8278537032,-0.7901708257,-0.7557712178,-0.7242434531,-0.6952421252,-0.6684751097,-0.6436936674,-0.6206846748,-0.5992644675,-0.5792739187,-0.560574472,-0.5430449209,-0.5265787744,-0.5110820894,-0.4964716745,-0.4826735943,-0.469621917,-0.4572576592,-0.4455278942,-0.4343849939,-0.4237859814,-0.4136919772,-0.4040677218,-0.3948811639,-0.3861031039,-0.3777068832,-0.3696681139,-0.3619644419,-0.3545753392,-0.3474819214,-0.340666786,-0.3341138701,-0.3278083238,-0.3217363979,-0.3158853437,-0.3102433236,-0.3047993311,-0.2995431194,-0.2944651364,-0.2895564674,-0.2848087823,-0.2802142889,-0.2757656897,-0.2714561438,-0.2672792312,-0.2632289212,-0.2592995433,-0.2554857607,-0.2517825462,-0.2481851596,-0.2446891283,-0.241290228,-0.237984466,-0.2347680654,-0.231637451,-0.2285892356,-0.2256202082,-0.2227273224,-0.219907686,-0.2171585518,-0.2144773078,-0.2118614699,-0.2093086736,-0.2068166668,-0.2043833036,-0.2020065381,-0.1996844181,-0.1974150805,-0.1951967458,-0.1930277135,-0.1909063581,-0.1888311247,-0.1868005251,-0.1848131347,-0.1828675888,-0.1809625795,-0.1790968531,-0.1772692066,-0.1754784862,-0.1737235837]
        vswr_graph = ax.plot_line_graph(vswr_graph_x, vswr_graph_y, add_vertex_dots=False).set_color(TEAL)
        
        # Equations
        gamma_eq = MathTex(r'\Gamma',r'=',r'{{Z_{L}',r'-',r'Z_{0}}','\over',r'{Z_{L}',r'+',r'Z_{0}',r'}} = ',r'{{\mathrm{VSWR}',r'-1}','\over',r'{\mathrm{VSWR}',r' + 1}',r'}').next_to(ax).scale(1).shift(LEFT*8.7, UP*0.8).set_color(WHITE)
        #gamma_eq = MathTex(r"\Gamma = \frac{Z_{L}-Z_{0}}{Z_{L}+Z_{0}} = \frac{\mathrm{VSWR}-1}{\mathrm{VSWR}+1}").next_to(ax).scale(1).shift(LEFT*8.7, UP*0.8).set_color(WHITE)
        gamma_eq.set_color_by_tex_to_color_map({
        r'\Gamma': GREEN_B,
        r'Z': ORANGE,
        r'VSWR': TEAL,
        })
        s11_vswr_eq = MathTex(r'\Longrightarrow |',r'\mathrm{S}_{11}',r'| = 20\log_{10}',r'{\left(',r'{{\mathrm{VSWR}',r'-1}','\over',r'{\mathrm{VSWR}',r'+1}',r'}\right)}').next_to(ax).scale(1).shift(LEFT*9.5, DOWN*1.4).set_color(WHITE)
        s11_vswr_eq.set_color_by_tex_to_color_map({
        r'\mathrm{S}_{11}': YELLOW,
        r'VSWR': TEAL
        })
        self.wait(3)
        self.play(Write(gamma_eq))
        self.wait(3)
        self.play(Write(s11_vswr_eq))
        self.wait(3)
        framebox_gamam_eq = SurroundingRectangle(gamma_eq, buff = .3).set_color(MAROON)
        framebox_s11_vswr_eq = SurroundingRectangle(s11_vswr_eq, buff = .3).set_color(MAROON)
        self.play(Create(framebox_gamam_eq))
        self.wait(3)
        self.play(
            ReplacementTransform(framebox_gamam_eq, framebox_s11_vswr_eq)
        )
        self.wait(3)
        self.play(Create(vswr_graph), run_time=2, rate_func=rush_into)
        self.wait(3)


with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": True}):
    scene = VSWR()
    scene.render()