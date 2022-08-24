from manim import *

ANIMATIONS = 600
CYCLES = 5
RUN_TIME = 0.1

class VswrAnimation(Scene):
    def construct(self):
        axes = Axes(x_range=[0,2*PI], y_range=[-1,1])

        phase_shift = ValueTracker(0)
        sine_wave = axes.plot(lambda t: 1*np.sin(2*t))
        sine_wave.add_updater(lambda mob: mob.become(axes.plot(lambda t: 1*np.sin(2*t+phase_shift.get_value()))))

        self.add(axes, sine_wave, phase_shift)


        phase_shifts = np.linspace(0,(2*PI)*CYCLES,ANIMATIONS)
        for angle in phase_shifts:
            self.play(phase_shift.animate.set_value(angle), run_time=RUN_TIME)

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = VswrAnimation()
    scene.render()