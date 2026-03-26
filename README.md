# Binary Addition with a Neural Network (PyTorch)

This repository documents a step-by-step attempt to solve the following problem:

> Try to learn a neural network adding two binary numbers or performing multiplication by two (note that result should also be some binary number).

This project focuses on the first part of the task:
**learning binary addition with a neural network**.

## What this repository contains

This is not only a final solution.
It is a record of the whole process:

- understanding the task,
- building the program step by step,
- testing and improving the code,
- training a neural network in PyTorch,
- evaluating the results,
- asking what should come next.

## Repository structure

- `task/` – original task description
- `conversation/` – step-by-step project story
- `code/` – 8 Python files showing how the program evolved
- `results/` – selected outputs and observations
- `next_steps/` – open questions and future directions

## Final result

For 4-bit binary numbers, the MLP model achieved perfect accuracy on all 256 possible input pairs.

## Main question at the end

Does this approach still work well for larger binary numbers, or do we need a different architecture that better captures binary carry propagation?
