from manim import *

class VectorAddition(Scene):
    def construct(self):
        # Create vectors
        vector1 = Vector(color=RED)
        vector2 = Vector(color=BLUE)
        vector_result = Vector(color=GREEN)

        # Set initial positions and lengths
        vector1.shift(LEFT)
        vector2.shift(RIGHT)
        vector_result.shift(2 * DOWN)

        # Show vectors on screen
        self.play(Create(vector1), Create(vector2))
        self.wait()

        # Animate addition
        self.play(vector1.animate.shift(UP), vector2.animate.shift(UP))
        self.play(vector1.animate.scale(0.5), 
                  vector2.animate.scale(0.5),
                  vector1.animate.shift(LEFT),
                  vector2.animate.shift(LEFT))

        # Calculate and show result vector
        vector_result.put_start_and_end_on(vector1.get_end(), vector2.get_end())
        self.play(Create(vector_result))
        self.wait()

        # Clean up
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
