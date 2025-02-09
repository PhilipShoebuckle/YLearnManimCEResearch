from manim import *


class NeuralNetwork(Scene):
    def construct(self):
        # Add input layer
        input_layer = VGroup(*[Circle(radius=0.4, color=BLUE).shift(LEFT * 3 + UP * i) for i in range(3)])
        input_labels = VGroup(*[Tex(str(i+1)).next_to(input_layer[i], DOWN) for i in range(3)])
        input_group = VGroup(input_layer, input_labels)

        # Add hidden layer
        hidden_layer = VGroup(*[Circle(radius=0.4, color=YELLOW).shift(UP * i) for i in range(4)])
        hidden_labels = VGroup(*[Tex("H").next_to(hidden_layer[i], DOWN) for i in range(4)])
        hidden_group = VGroup(hidden_layer, hidden_labels)

        # Add output layer
        output_layer = VGroup(*[Circle(radius=0.4, color=GREEN).shift(RIGHT * 3 + UP * i) for i in range(2)])
        output_labels = VGroup(*[Tex("O").next_to(output_layer[i], DOWN) for i in range(2)])
        output_group = VGroup(output_layer, output_labels)

        # Connect layers
        connections = VGroup(*[
            Line(input_layer[i].get_right(), hidden_layer[j].get_left()) for i in range(3) for j in range(4)
        ] + [
            Line(hidden_layer[i].get_right(), output_layer[j].get_left()) for i in range(4) for j in range(2)
        ])

        # Create animations
        self.play(Create(input_group))
        self.wait(0.5)
        self.play(Create(hidden_group))
        self.wait(0.5)
        self.play(Create(output_group))
        self.wait(0.5)
        self.play(Create(connections))
        self.wait()

        # Remove elements
        self.play(Uncreate(input_group), Uncreate(hidden_group), Uncreate(output_group), Uncreate(connections))
