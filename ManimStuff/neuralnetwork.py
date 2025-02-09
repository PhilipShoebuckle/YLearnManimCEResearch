
from manim import *

class NeuralNetwork(Scene):
    def construct(self):
        # Create the input layer with 3 nodes
        inputs = [Dot(color=BLUE).shift(3 * LEFT), Dot(color=BLUE), Dot(color=BLUE).shift(3 * RIGHT)]
        self.play(*[Create(dot) for dot in inputs])

        # Create the hidden layer with 4 nodes
        hidden_layer = [Dot(color=YELLOW).next_to(input_dot, direction=UP) for input_dot in inputs]
        self.play(*[Create(dot) for dot in hidden_layer])

        # Create the output layer with 2 nodes
        output_layer = [Dot(color=GREEN).next_to(hidden_dot, direction=UP) for hidden_dot in hidden_layer]
        self.play(*[Create(dot) for dot in output_layer])

        # Create the connections between layers
        connections = [VGroup(Line(input_dot, hidden_dot), Line(hidden_dot, output_dot)) 
                       for input_dot, hidden_dot, output_dot in zip(inputs, hidden_layer, output_layer)]
        self.play(*[Create(connection) for connection in connections])

        self.wait(2)