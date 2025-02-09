
from manim import *

# Assume example values for the vectors
vector_a = [3, 4, 0]
vector_b = [1, 2, 0]

class PythagoreanTheoremScene(Scene):
    def construct(self):
        # Create the vectors
        leg_a = Vector(vector_a, color=BLUE)
        leg_b = Vector(vector_b, color=BLUE)
        hypotenuse = Vector(vector_a[0]+vector_b[0], vector_a[1]+vector_b[1], 0, color=RED)

        # Create the right-angled triangle using the vectors
        triangle = Polygon(np.array([0,0,0]), vector_a, vector_a+vector_b, color=WHITE, fill_opacity=0.3)

        # Add the vectors and triangle to the scene
        self.play(ShowCreation(leg_a), ShowCreation(leg_b), ShowCreation(hypotenuse), ShowCreation(triangle))

        # Add labels for the vectors
        leg_a_label = Tex("A", color=BLUE).next_to(leg_a, UP)
        leg_b_label = Tex("B", color=BLUE).next_to(leg_b, LEFT)
        hypotenuse_label = Tex("C", color=RED).next_to(hypotenuse, RIGHT)
        self.play(Write(leg_a_label), Write(leg_b_label), Write(hypotenuse_label))

        # Add text with the Pythagorean theorem formula and calculate the squares of the lengths
        formula = MathTex("a^2 + b^2 = c^2").move_to([0, -2, 0])
        calculation = MathTex(f"{vector_a[0]}^2 + {vector_a[1]}^2", "+", f"{vector_b[0]}^2 + {vector_b[1]}^2", "=", f"{int((vector_a[0]+vector_b[0])**2 + (vector_a[1]+vector_b[1])**2)}^2").scale(0.7).move_to([0, -2.5, 0])
        self.play(Write(formula), Write(calculation))

        self.wait(1)
