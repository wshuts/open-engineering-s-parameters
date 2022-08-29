from manim import *

RUN_TIME = 0.1
CYCLES = 2
POINTS_PER_CYCLE = 64
PHASE_STEP = 2*PI/POINTS_PER_CYCLE

class VswrAnimation(Scene):
    def construct(self):
        valueTracker = ValueTracker(0)
        axes = Axes(x_range=[0,2*PI], y_range=[-2.5,2.5], tips=False)

        def sine_wave(t, phase_shift=0.0, peak=1.0): 
            return peak*np.sin(2*t+phase_shift)

        def forward(t):
            return sine_wave(t, valueTracker.get_value())

        def reverse(t):
            return sine_wave(t, -valueTracker.get_value(), 0.7)

        def total(t):
            return sine_wave(t, valueTracker.get_value()) + sine_wave(t, -valueTracker.get_value(), 0.7)

        sine_wave_forward = axes.plot(sine_wave, color=BLUE)
        sine_wave_forward.add_updater(lambda mob: mob.become(axes.plot(forward, color=BLUE)))

        sine_wave_reverse = axes.plot(sine_wave)
        sine_wave_reverse.add_updater(lambda mob: mob.become(axes.plot(reverse, color=RED)))

        sine_wave_total = axes.plot(sine_wave)
        sine_wave_total.add_updater(lambda mob: mob.become(axes.plot(total, color=GREEN)))
        
        V_min_point = axes.coords_to_point(2*PI,0.3)
        V_min_line = axes.get_horizontal_line(V_min_point, line_func=DashedLine, stroke_width=4).set_color(YELLOW_E)

        V_max_point = axes.coords_to_point(2*PI,1.7)
        V_max_line = axes.get_horizontal_line(V_max_point, line_func=DashedLine, stroke_width=4).set_color(YELLOW_E)

        V_max_label = (
            MathTex(r'|',r'V_\mathrm{max}',r'|')
            .next_to(V_max_line, direction=UP)
            .shift(RIGHT*5.06+DOWN*0.12)
            .scale(1)
            .set_color(WHITE)
        )
        V_max_label.set_color_by_tex_to_color_map(
            {
                r'V_\mathrm{max}': YELLOW_D
            }
        )

        V_min_label = (
            MathTex(r'|',r'V_\mathrm{min}',r'|')
            .next_to(V_min_line, direction=UP)
            .shift(RIGHT*5.06+DOWN*0.12)
            .scale(1)
            .set_color(WHITE)
        )
        V_min_label.set_color_by_tex_to_color_map(
            {
                r'V_\mathrm{min}': YELLOW_D
            }
        )

        vswr_V_eq_long = (
            MathTex(
                r'\mathrm{Voltage \ Standing \ Wave \ Ratio}', r'=',
                r'{{|', r'V_\mathrm{max}', r'|}',
                '\over',
                r'{|', r'V_\mathrm{min}', r'|}}'
            )
            .scale(1)
            .shift(LEFT*0+DOWN*3.12)
            .set_color(WHITE)
        )
        vswr_V_eq_long.set_color_by_tex_to_color_map(
            {
                r'V_\mathrm{max}': YELLOW_D,
                r'V_\mathrm{min}': YELLOW_D,
                r'\mathrm{Voltage \ Standing \ Wave \ Ratio}': TEAL
            }
        )

        vswr_V_eq = (
            MathTex(r'\mathrm{VSWR}',r'=',r'{{|',r'V_\mathrm{max}',r'|}','\over',r'{|',r'V_\mathrm{min}',r'|}}')
            .scale(1)
            .shift(LEFT*0+DOWN*3.12)
            .set_color(WHITE)
        )
        vswr_V_eq.set_color_by_tex_to_color_map(
            {
                r'V_\mathrm{max}': YELLOW_D,
                r'V_\mathrm{min}': YELLOW_D,
                r'VSWR': TEAL
            }
        )

        def scene_updater(dt):
            phase_shift = valueTracker.get_value()
            if phase_shift==0: self.add(axes, sine_wave_forward)
            if phase_shift==PI/2: self.add(sine_wave_reverse)
            if phase_shift==PI: self.add(sine_wave_total)
            if phase_shift==3*PI/2: self.add(V_min_line)
            if phase_shift==2*PI: self.add(V_max_line)

        self.add_updater(scene_updater)

        phase_shifts = [n*PHASE_STEP for n in range(0,POINTS_PER_CYCLE*CYCLES+1)]
        for phase_shift in phase_shifts:
            self.play(valueTracker.animate.set_value(phase_shift), run_time=RUN_TIME)
        #self.play(Write(V_min_label))
        #self.wait(3)
        #self.play(Write(V_max_label))
        #self.wait(3)
        #self.play(Write(vswr_V_eq_long))
        #self.wait(3)
        #self.play(ReplacementTransform(vswr_V_eq_long, vswr_V_eq))

with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": True}):
    scene = VswrAnimation()
    scene.render()