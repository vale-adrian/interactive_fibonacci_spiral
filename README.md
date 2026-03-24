# Interactive Fibonacci Spiral Generator

A Python-based visualization tool that generates the Fibonacci sequence and draws its corresponding geometric spiral. A tool to be used for personal satisfaction and can also be useful to teach a class. 

## Features

* **Interactive Scaling:** Features a UI slider to dynamically build the spiral from $n=1$ up to $n=80$.
* **Dynamic Viewport:** Automatically calculates the tightest bounding box to keep the shape perfectly centered and framed, regardless of how large the spiral grows.

## The Math

The visualization is based on the Fibonacci sequence, where each number is the sum of the two preceding ones:
$$F_n = F_{n-1} + F_{n-2}$$
with seed values $F_1 = 1$ and $F_2 = 1$. 

As $n$ increases, the ratio of successive Fibonacci numbers ($F_n / F_{n-1}$) converges on the Golden Ratio ($\phi \approx 1.618$), and the bounding boxes of the visualization perfectly model a Golden Rectangle.

## Prerequisites

You will need Python 3 and the `matplotlib` library installed on your system. 

## Note

The spiral will get tighter and tighter as you go higher in the Fibonacci sequence, thus becoming harder to visualize. I recommend using the zooming tool to zoom in on the central spiral to watch it closely. This code generates upto 80th Fibonacci number and its corresponding geometrical visualization, but this value can be increased by setting the desired value of the variable 'MAX_N'.
