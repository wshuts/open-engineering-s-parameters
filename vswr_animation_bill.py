from manim import *

ANIMATIONS = 10
CYCLES = 0.03
RUN_TIME = 0.1

class VswrAnimation(Scene):
    def construct(self):

        def sine_wave(t, phase_shift=0.0, peak=1.0): 
            return peak*np.sin(2*t+phase_shift)

        axes = Axes(x_range=[0,2*PI], y_range=[-2.5,2.5])

        phase_shift = ValueTracker(0)

        sine_wave_forward = axes.plot(sine_wave)
        sine_wave_forward.add_updater(lambda mob: mob.become(axes.plot(lambda t: sine_wave(t, phase_shift.get_value()))))

        sine_wave_reverse = axes.plot(sine_wave)
        sine_wave_reverse.add_updater(lambda mob: mob.become(axes.plot(lambda t: sine_wave(t, -phase_shift.get_value(), 0.7))))

        sine_wave_total = axes.plot(sine_wave)
        sine_wave_total.add_updater(lambda mob: mob.become(axes.plot(lambda t: sine_wave(t, phase_shift.get_value()) + sine_wave(t, -phase_shift.get_value(), 0.7))))
        
        self.add(axes, sine_wave_forward, sine_wave_reverse, sine_wave_total, phase_shift)

        phase_shifts = np.linspace(0,(2*PI)*CYCLES,ANIMATIONS)
        for angle in phase_shifts:
            self.play(phase_shift.animate.set_value(angle), run_time=RUN_TIME)

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = VswrAnimation()
    scene.render()