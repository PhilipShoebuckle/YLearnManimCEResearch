from manim import *

class NeuralNetwork(Scene):
    def construct(self):
        input_layer_nodes = 8
        hidden_layer_nodes = 8
        output_layer_nodes = 4

        # Create input layer nodes
        input_nodes = VGroup(*[Circle(radius=0.3, color=BLUE) for _ in range(input_layer_nodes)])
        input_nodes.arrange(DOWN, buff=1)
        input_nodes.shift(3 * LEFT)  # Move input layer to the left

        # Create hidden layer nodes
        hidden_nodes = VGroup(*[Circle(radius=0.3, color=YELLOW) for _ in range(hidden_layer_nodes)])
        hidden_nodes.arrange(DOWN, buff=1)

        # Create output layer nodes
        output_nodes = VGroup(*[Circle(radius=0.3, color=GREEN) for _ in range(output_layer_nodes)])
        output_nodes.arrange(DOWN, buff=1)
        output_nodes.shift(3 * RIGHT)  # Move output layer to the right

        # Connect input layer nodes to hidden layer nodes
        input_to_hidden_connections = VGroup()
        for input_node in input_nodes:
            connection_lines = VGroup()
            for hidden_node in hidden_nodes:
                connection_line = Line(input_node.get_right(), hidden_node.get_left(), color=WHITE)
                connection_lines.add(connection_line)
            input_to_hidden_connections.add(connection_lines)
        
        # Connect hidden layer nodes to output layer nodes
        hidden_to_output_connections = VGroup()
        for hidden_node in hidden_nodes:
            connection_lines = VGroup()
            for output_node in output_nodes:
                connection_line = Line(hidden_node.get_right(), output_node.get_left(), color=WHITE)
                connection_lines.add(connection_line)
            hidden_to_output_connections.add(connection_lines)

        # Create animation
        self.play(Create(input_nodes), Create(hidden_nodes), Create(output_nodes))
        self.play(Create(input_to_hidden_connections), Create(hidden_to_output_connections))
        self.wait(10)  # Display animation for 10 seconds

