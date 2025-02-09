from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create vectors representing the legs of the triangle
        vector_a = Arrow(start=ORIGIN, end=3 * LEFT, color=BLUE)
        vector_b = Arrow(start=ORIGIN, end=4 * DOWN, color=RED)

        # Create the hypotenuse vector by adding vector_a and vector_b
        vector_hypotenuse = Arrow(start=vector_a.get_end(), end=vector_a.get_end() + vector_b.get_end(), color=GREEN)

        # Calculate the lengths of the vectors
        length_a = vector_a.get_length()
        length_b = vector_b.get_length()
        length_hypotenuse = vector_hypotenuse.get_length()

        # Calculate the squared lengths
        length_a_squared = length_a ** 2
        length_b_squared = length_b ** 2
        length_hypotenuse_squared = length_hypotenuse ** 2

        # Display the vectors and labels
        self.play(GrowArrow(vector_a), GrowArrow(vector_b), GrowArrow(vector_hypotenuse))
        self.wait()

        # Display the labels for the vectors
        label_a = MathTex("a").next_to(vector_a, direction=LEFT)
        label_b = MathTex("b").next_to(vector_b, direction=DOWN)
        label_c = MathTex("c").next_to(vector_hypotenuse, direction=UR)

        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait()

        # Display the squared lengths labels
        label_a_squared = MathTex("a^2 =", f"{length_a_squared:.2f}").set_color(BLUE).next_to(vector_a, direction=UP)
        label_b_squared = MathTex("b^2 =", f"{length_b_squared:.2f}").set_color(RED).next_to(vector_b, direction=RIGHT)
        label_c_squared = MathTex("c^2 =", f"{length_hypotenuse_squared:.2f}").set_color(GREEN).next_to(vector_hypotenuse, direction=UP)

        self.play(Write(label_a_squared), Write(label_b_squared), Write(label_c_squared))
        self.wait()

        # Display the Pythagorean theorem formula
        theorem_formula = MathTex("a^2", "+", "b^2", "=", "c^2").next_to(label_c_squared, direction=RIGHT)

        self.play(Write(theorem_formula))
        self.wait()

        # Fade out the vectors and labels
        self.play(FadeOut(vector_a), FadeOut(vector_b), FadeOut(vector_hypotenuse),
                  FadeOut(label_a), FadeOut(label_b), FadeOut(label_c),
                  FadeOut(label_a_squared), FadeOut(label_b_squared), FadeOut(label_c_squared),
                  FadeOut(theorem_formula))
        self.wait()
