from manim import *


class Pendulum(Scene):
    def construct(self):
        # Set up the pendulum
        pendulum_rod = Line(start=[-4, 3, 0], end=[-3, 0, 0], color=YELLOW, stroke_width=5)
        pendulum_ball = Dot(point=[-3, -2, 0], color=RED, radius=0.3)
        pendulum = VGroup(pendulum_rod, pendulum_ball)
        self.add(pendulum)

        # Pendulum motion parameters
        theta = PI / 3  # Initial angular displacement
        length = 2.5  # Length of the pendulum rod
        period = 2  # Period of the pendulum motion

        # Motion of the pendulum
        def update_pendulum(pendulum, dt):
            alpha = -theta * np.cos((2 * PI * self.time) / period)
            pendulum.shift(length * (np.sin(alpha + theta) - np.sin(theta)) * UP)
            pendulum.rotate(alpha, about_point=pendulum_rod.get_start())

        # Create the animation of the pendulum motion
        self.play(UpdateFromFunc(pendulum, update_pendulum), run_time=4, rate_func=linear)