from manim import *

class NeuralNetwork(Scene):
    def construct(self):
        # Create nodes for each layer
        input_layer = self.create_layer(12, "Input Layer")
        hidden_layer1 = self.create_layer(8, "Hidden Layer 1")
        hidden_layer2 = self.create_layer(8, "Hidden Layer 2")
        output_layer = self.create_layer(4, "Output Layer")

        # Position the layers
        input_layer.scale(0.8)
        hidden_layer1.next_to(input_layer, RIGHT, buff=1)
        hidden_layer1.shift(UP*0.5)
        hidden_layer2.next_to(hidden_layer1, RIGHT, buff=1)
        hidden_layer2.shift(UP*0.5)
        output_layer.next_to(hidden_layer2, RIGHT, buff=1)
        output_layer.shift(UP*0.5)

        # Connect the layers
        connections = self.connect_layers(input_layer, hidden_layer1)
        connections += self.connect_layers(hidden_layer1, hidden_layer2)
        connections += self.connect_layers(hidden_layer2, output_layer)

        # Animate the creation of layers and connections
        self.play(Create(input_layer), Create(hidden_layer1), Create(hidden_layer2), Create(output_layer))
        for connection in connections:
            self.play(Create(connection))
        self.wait(2)

    def create_layer(self, num_nodes, label):
        layer = VGroup()
        for i in range(num_nodes):
            node = Circle(radius=0.4, color=BLUE)
            layer.add(node)
        label = Text(label).scale(0.6)
        label.next_to(layer, DOWN)
        layer.add(label)
        return layer

    def connect_layers(self, layer1, layer2):
        connections = VGroup()
        for node1 in layer1:
            for node2 in layer2:
                line = Line(node1.get_edge_center(RIGHT), node2.get_edge_center(LEFT), buff=0.1)
                connections.add(line)
        return connections