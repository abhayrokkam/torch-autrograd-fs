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

## Understanding DAG and Topological Sort
- Had an issue with the calculation of the backward propogation.
- All elements at the current heirarchy must be in the list before moving on to the lower hierarchy.
- Directed Acyclic Graphs (DAG) are the only graphs that can have a topological order.
- Topological sort needs direction and becomes ambiguous for cyclic graphs.
- Understood the topological sort and switched to it from the previous implementation of Depth-first Traversal.

## Torch Implementation and Neural Network
- Building the torch version of our previously built neuron.
- This is to compare a industry-grade solution and our implementation.

## Building Neurons, Layers and Multi-layer Perceptrons
- Built the fundamental classes for neurons, layers and multi-layer perceptrons.
- Saw a potential error for [ object of type int has no len() ] during the output of `Layers` class.
- The above error would occur if there is a flow from one layer with a single neuron to another layer.
- Surprised at the simplicity of these classes. Very excited to continue with this project.

## Training the MLP on Dataset
- Creating an example dataset and calculating predictions using the MLP model.
- All the predictions of the model are stored in a list. This is due to the fix mentioned in the above section regarding the potential error.
- The `Value` class had an addition of a reverse-subtract function.
- Loss value is not going too low. Pretty bad predictions even after gradient descent.

## Building a Training Flow
- Important information about setting zero grad.
- I was wondering why the loss is not reaching zero irrespective of the learning rate.
- Found the culprit in the form of `setting zero grad for parameters` after Mr. Andrej Karpathy mentioned it at the end of the video.
- Training process can be simply broken into three stages - Forward Pass, Backward Pass and Gradient Descent.