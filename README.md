# From Scratch: Neural Networks and Back Propogation

Learning Resource: [LINK](https://youtu.be/VMj-3S1tku0?si=qfz9OuDRKSzVn2nY)

>**Note**: All the `helper_xyz` folders contain code that were directly copied from the learning resource. 

## Prerequisites
- I start by importing the ***visualization functionality from the learning resource***. For this, I create a `helper_draw` folder from which I will be able to import `draw_dot` function from the learning resource.

## Basic Functionality
- Create a `Value` class with basic functionalities of initialization, representation, addition and mulitplication.
- Add the functionality of memory where a `Value` item will remember the ***`Value`/s*** and the ***operation*** used to produce the item.

## Gradients
- Create a `back_propogation` function in the `Value` class where each `Value`'s gradient is calculated with respect to the end-value. The process starts from end-value and goes towards the initial input values.
> **Note**: I implemented the `back_propogation` function. Then, I compared the files from the learning resource which had a more efficient implementation of the function. I proceeded with the learning resource implementation.
- 