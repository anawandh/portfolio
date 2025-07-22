---
title: "Learning ML Week 1"
date: 2025-07-21T23:24:13
draft: false
tags: ["jupyter", "data-science"]
categories: ["blog"]
---

# Learning ML Week 1
This notebook contains my learnings from week one of experiencing the world of ML

## Machine Learning
- Start:
    - ML = Using Data to Answer Questions
    - Most important part needed for ML: Data
    - Quality and Quantity of Data is very imp
- Steps:
    - Data Gathering:
        - Get the data somehow
    - Data Preparation:
        - Data imbalances needs to be not present
        - Data is split into two parts:
    - Training
        - Evaluation
        - Choosing a Model
        - For simplicity where only one or two features. 
        - Choose a linear model
        - Other model exists that are made for very specific needs as well
    - Training
        - Y = m*x + b
        - M represents a feature (slope)
        - Y is the output, x is input and b is the Y-intercept
        - There can be many M’s for various features
            - Collection of  these M’s is done in a matrix and this is called a Weight Matrix
        - Baises: Arranging the b together 
            - Collection again of B’s for respective M’s 
        - Training process is initialising random values for W and B and training to attempt to predict the output
            - Compare the prediction with real output and adjust W and b to get much accurate predictions next time around
                - Repeat this process
                - Each cycle of updating the weights and biases is one training step
            - **Note: the random W and b is only for the first choice of W and b
                - With each step we adjust the random W and b to reduce error when compared to the output
    - Evaluation
        - Test the model against data it has not seen before
        - Representative of how it might perform in the real world
        - Usually  80/20 split of the data between training and evaluation
    - Parameter Tuning
        - Fine tuning parts of the training values
            - Example: running the same old training data multiple times
            - How far we shift the line each step based on previous training step
    - Prediction
        - Answer the question using the model

📘 Explanation of Terms in a Simple ML Model

![image.png](attachment:image.png)

where: 
- 𝑦′ is the predicted label—the output. 
- 𝑏 is the bias of the model. Bias is the same concept as the y-intercept in the algebraic equation for a line. In ML, bias is sometimes referred to as 𝑤₀. Bias is a parameter of the model and is calculated during training. 
- 𝑤₁ is the weight of the feature. Weight is the same concept as the slope 𝑚 in the algebraic equation for a line. Weight is a parameter of the model and is calculated during training. 
- 𝑥₁ is a feature—the input.



## Example usage:

