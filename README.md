# game_of_life

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/26e69c12f35d4fad8463d6677865f60b)](https://app.codacy.com/gh/AntoineRbd/game_of_life?utm_source=github.com&utm_medium=referral&utm_content=AntoineRbd/game_of_life&utm_campaign=Badge_Grade_Settings)

[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/757b202a75664cd29a629b014142767f)](https://www.codacy.com/gh/AntoineRbd/game_of_life/dashboard?utm_source=github.com&utm_medium=referral&utm_content=AntoineRbd/game_of_life&utm_campaign=Badge_Coverage)

# Table of content
* [Definition](#definition)
* [history](#history)
* [game of life](#game-of-life)
* [one-dimensional automaton](#one-dimensional-automaton)
* [Langton's ant](#langton-s-ant)

# Definition
A cellular automaton is a grid of "cells" each containing a "state" (black or white) and which can evolve over time. The state of a cell at time `t + 1` (next "generation") is a function of the state at time `t` of a finite number of cells called its "neighbourhood". At each new generation, the same rules are applied simultaneously to all cells in the grid (and all cells in a single row for one-dimensional automata), producing a new generation of cells that depends entirely on the previous generation.

# History
Created and developed in the 1970s, cellular automata can illustrate certain physical phenomena.
The most famous automaton was invented in 1970, a cellular automaton in two parts by Jhon Conway: The Game of Life