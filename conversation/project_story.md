# Project Story

## Step 1 – Understanding the task
The goal was to build a neural network that takes two binary numbers as input and returns their binary sum.

At first, the problem was simplified to 4-bit numbers:
- input: two 4-bit binary numbers
- output: one 5-bit binary number

This makes the task manageable and allows testing all possible cases.

## Step 2 – Representing numbers as bits
The first helper function converted integers into fixed-length binary lists.

Example:
- 5 -> [0, 1, 0, 1]
- 17 -> [1, 0, 0, 0, 1]

## Step 3 – Building one training example
A single example was defined as:
- input: concatenation of the two binary numbers
- output: binary representation of the sum

Example:
- 11 -> [1, 0, 1, 1]
- 6  -> [0, 1, 1, 0]
- input -> [1, 0, 1, 1, 0, 1, 1, 0]
- output -> [1, 0, 0, 0, 1]

## Step 4 – Building the whole dataset
All pairs of 4-bit numbers were generated.
This produced 256 examples.

## Step 5 – Converting data into PyTorch tensors
The data was transformed into tensors of type float32.

## Step 6 – Building the neural network
A simple MLP was used:
- input size: 8
- hidden layers: 32, 32
- output size: 5
- ReLU activations
- Sigmoid output

## Step 7 – Training
The model was trained using:
- BCELoss
- Adam optimizer
- learning rate = 0.01
- epochs = 3000

The loss dropped close to zero.

## Step 8 – Evaluation
After rounding the predictions to 0 or 1, the network reached perfect accuracy on all 256 examples.

## Step 9 – Reflection
The model solves the 4-bit version of the problem very well.
However, an important question remains:

Did the network learn the general rule of binary addition,
or did it only fit the complete table of all 4-bit combinations?

This leads to the next question:
what happens for larger binary numbers?