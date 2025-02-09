from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create the triangle and label its vertices
        triangle = Polygon(
            np.array([-2, -1, 0]),
            np.array([2, -1, 0]),
            np.array([-2, 3, 0]),
        )
        label_a = MathTex("a").next_to(triangle.get_vertices()[0], LEFT)
        label_b = MathTex("b").next_to(triangle.get_vertices()[2], LEFT)
        label_c = MathTex("c").next_to(triangle.get_vertices()[1], RIGHT)

        # Create vectors a and b
        vector_a = Arrow((-2, -1, 0), (-2, 3, 0), buff=0, color=BLUE_A)
        vector_b = Arrow((-2, 3, 0), (2, -1, 0), buff=0, color=BLUE_B)

        # Create vector c as the sum of vectors a and b
        vector_c = Vector(np.add(vector_a.get_end(), vector_b.get_end()), color=BLUE_C)

        # Show labels, triangle, and vectors
        self.play(Create(triangle), Write(label_a))
        self.play(Create(vector_a), Write(label_b))
        self.play(Create(vector_b), Write(label_c))

        # Show vector addition animation
        self.play(Create(vector_c))

        # Label the vector c
        label_c = MathTex("c").next_to(vector_c.get_end(), RIGHT)
        self.play(Write(label_c))

        self.wait()