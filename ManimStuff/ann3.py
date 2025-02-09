from manim import *

class NeuralNetworkAnimation(Scene):
    def construct(self):
        # Create the input layer
        input_layer = self.create_layer(3, "Input")

        # Create the hidden layers
        hidden_layers = []
        num_hidden_layers = 2
        num_nodes_in_layer = [4, 4]

        for i in range(num_hidden_layers):
            layer = self.create_layer(num_nodes_in_layer[i], "Hidden")
            hidden_layers.append(layer)

        # Create the output layer
        output_layer = self.create_layer(2, "Output")

        # Position the layers
        layers = [input_layer] + hidden_layers + [output_layer]
        num_layers = len(layers)
        layers_spacing = 2.5

        for i, layer in enumerate(layers):
            layer.move_to((i - (num_layers - 1) / 2) * layers_spacing * RIGHT)

        # Draw the connections between layers
        connections = []
        for i in range(num_layers - 1):
            for node in layers[i]:
                for next_node in layers[i+1]:
                    connection = self.create_connection(node, next_node)
                    connections.append(connection)

        # Add everything to the scene
        self.play(Create(input_layer))
        for layer in hidden_layers:
            self.play(Create(layer))
        self.play(Create(output_layer))

        # Animate the connections
        self.play(Create(VGroup(*connections)))

        self.wait()

    def create_layer(self, num_nodes, label):
        layer = VGroup()
        radius = 0.25
        node_spacing = 0.5

        for i in range(num_nodes):
            node = Circle(radius=radius)
            node.shift((i - (num_nodes - 1) / 2) * node_spacing * UP)
            layer.add(node)

        label_text = Text(label)
        label_text.next_to(layer, DOWN)
        layer.add(label_text)

        return layer

    def create_connection(self, start_node, end_node):
        connection = Line(start_node.get_center(), end_node.get_center(), color=WHITE)
        return connection
