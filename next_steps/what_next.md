# What Next?

The model solves binary addition for 4-bit numbers very well.
However, this raises a more interesting question:

## Open question
Can the same approach handle larger binary numbers effectively?

## Possible directions
1. Increase the input width to 6-bit or 8-bit numbers
2. Compare training time and accuracy
3. Check whether the MLP really generalizes
4. Try sequence-based models such as RNN or LSTM
5. Investigate whether the network learns carry propagation

## Main reflection
For 4-bit numbers, the network may simply learn the complete mapping.
For larger binary numbers, the challenge becomes more algorithmic.

So the next step is not just "train longer",
but to ask whether the architecture is appropriate for the structure of binary addition.