from manim import *

ANIMATIONS = 60
CYCLES = 2
RUN_TIME = 0.1

class VswrAnimation(Scene):
    def construct(self):
        axes = Axes(x_range=[0,2*PI], y_range=[-2.5,2.5])

        phase_shift = ValueTracker(0)

        sine_wave_forward = axes.plot(lambda t: 1*np.sin(2*t))
        sine_wave_forward.add_updater(lambda mob: mob.become(axes.plot(lambda t: 1*np.sin(2*t+phase_shift.get_value()))))

        sine_wave_reverse = axes.plot(lambda t: 1*np.sin(2*t))
        sine_wave_reverse.add_updater(lambda mob: mob.become(axes.plot(lambda t: 0.7*np.sin(2*t-phase_shift.get_value()))))

        sine_wave_total = axes.plot(lambda t: 1*np.sin(2*t))
        sine_wave_total.add_updater(lambda mob: mob.become(axes.plot(lambda t: 1*np.sin(2*t+phase_shift.get_value()) + 0.7*np.sin(2*t-phase_shift.get_value()))))
        
        self.add(axes, sine_wave_forward, sine_wave_reverse, sine_wave_total, phase_shift)

        phase_shifts = np.linspace(0,(2*PI)*CYCLES,ANIMATIONS)
        for angle in phase_shifts:
            self.play(phase_shift.animate.set_value(angle), run_time=RUN_TIME)

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = VswrAnimation()
    scene.render()