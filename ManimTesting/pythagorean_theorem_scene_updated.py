
from manim import *

class PythagoreanTheoremScene(Scene):
    def construct(self):
        # Define the vectors representing the legs of the right-angled triangle
        vector_a = np.array([0, 3, 0])
        vector_b = np.array([4, 0, 0])
        origin = np.array([0, 0, 0])
        
        # Create the vectors
        leg_a = Arrow(origin, vector_a, color=BLUE)
        leg_b = Arrow(origin, vector_b, color=BLUE)
        
        # Calculate the hypotenuse vector
        hypotenuse = Arrow(vector_a, vector_a+vector_b, color=RED)
        
        # Create the right-angled triangle using the vectors
        triangle = Polygon(origin, vector_a, vector_a+vector_b, color=WHITE, fill_opacity=0.3)

        # Add the vectors and triangle to the scene
        self.play(ShowCreation(leg_a), ShowCreation(leg_b), ShowCreation(hypotenuse), ShowCreation(triangle))

        # Add labels for the vectors
        leg_a_label = Tex("A", color=BLUE).next_to(leg_a.get_end(), UP+LEFT)
        leg_b_label = Tex("B", color=BLUE).next_to(leg_b.get_end(), DOWN+RIGHT)
        hypotenuse_label = Tex("C", color=RED).next_to(hypotenuse.get_end(), RIGHT)
        self.play(Write(leg_a_label), Write(leg_b_label), Write(hypotenuse_label))

        # Add text with the Pythagorean theorem formula and calculate the squares of the lengths
        formula = MathTex("a^2 + b^2 = c^2").move_to([0, -2, 0])
        calculation = MathTex(f"{vector_a[1]}^2 + {vector_b[0]}^2", "=", f"{int(np.linalg.norm(vector_a)**2 + np.linalg.norm(vector_b)**2)}^2").scale(0.7).move_to([0, -2.5, 0])
        self.play(Write(formula), Write(calculation))

        self.wait(1)
