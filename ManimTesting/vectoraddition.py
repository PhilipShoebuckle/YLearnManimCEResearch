from manim import *

class VectorAddition(Scene):
    def construct(self):
        A = Arrow(ORIGIN, [2, 1, 0], color=RED)
        B = Arrow(ORIGIN, [1, 2, 0], color=BLUE)
        C = Arrow(ORIGIN, [3, 3, 0], color=GREEN)

        A_label = Tex("A", color=RED).next_to(A, DOWN)
        B_label = Tex("B", color=BLUE).next_to(B, LEFT)
        C_label = Tex("A + B", color=GREEN).next_to(C, RIGHT)

        self.play(Create(A), Create(B))
        self.play(Create(A_label), Create(B_label))
        self.wait()
        self.play(TransformFromCopy(A, C), TransformFromCopy(B, C_label))
        self.wait()

        self.play(FadeOut(A_label), FadeOut(B_label))
        self.play(GrowArrow(C_label))
        self.wait()