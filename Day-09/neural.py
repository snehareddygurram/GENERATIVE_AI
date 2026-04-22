# Day-06/neural.py

# This function acts like a single neuron
def neuron(input_value, weight, bias):
    # Multiply input with weight and add bias
    output = (input_value * weight) + bias
    return output


# Input data
x = 2          # example input
w = 0.5        # importance (weight)
b = 1          # bias

# Pass through neuron
result = neuron(x, w, b)

# Print output
print("Neuron output:", result)