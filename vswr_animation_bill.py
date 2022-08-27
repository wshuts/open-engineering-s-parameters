from manim import *

ANIMATIONS = 20
CYCLES = 1
RUN_TIME = 0.1

class VswrAnimation(Scene):
    def construct(self):
        valueTracker = ValueTracker(0)
        axes = Axes(x_range=[0,2*PI], y_range=[-2.5,2.5])

        def sine_wave(t, phase_shift=0.0, peak=1.0): 
            return peak*np.sin(2*t+phase_shift)

        def forward(t):
            return sine_wave(t, valueTracker.get_value())

        def reverse(t):
            return sine_wave(t, -valueTracker.get_value(), 0.7)

        def total(t):
            return sine_wave(t, valueTracker.get_value()) + sine_wave(t, -valueTracker.get_value(), 0.7)

        sine_wave_forward = axes.plot(sine_wave)
        sine_wave_forward.add_updater(lambda mob: mob.become(axes.plot(forward, color=BLUE)))

        sine_wave_reverse = axes.plot(sine_wave)
        sine_wave_reverse.add_updater(lambda mob: mob.become(axes.plot(reverse, color=RED)))

        sine_wave_total = axes.plot(sine_wave)
        sine_wave_total.add_updater(lambda mob: mob.become(axes.plot(total, color=GREEN)))
        
        self.add(axes, sine_wave_forward, sine_wave_reverse, sine_wave_total, valueTracker)

        V_min_point = axes.coords_to_point(2*PI,0.3)
        V_min_line = axes.get_horizontal_line(V_min_point, line_func=DashedLine, stroke_width=4).set_color(YELLOW_E)

        phase_shifts = np.linspace(0,(2*PI)*CYCLES,ANIMATIONS)
        size = phase_shifts.size
        count = 0
        for phase_shift in phase_shifts:
            self.play(valueTracker.animate.set_value(phase_shift), run_time=RUN_TIME)
            if count == size/2: self.add(V_min_line)
            count = count + 1

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = VswrAnimation()
    scene.render()