# Linear regression foundations

Feature: the input information the model uses (house size)

Target: the correct answer the model is trying to predict (house price)

Prediction: the model's estimated answer for the given input

Parameter: a value the model adjusts during training. We choose its starting value; training updates it. In this model, the parameters are weight and bias.

Loss: one non-negative number that measures how wrong the model's predictions are across the training examples. Lower loss means predictions are closer to the targets.

Training: giving the model inputs and known correct targets, then adjusting parameters to reduce loss.

Inference: using the trained weight and bias to predict an output for a new input. Parameters do not change during inference.

## Example

I want to predict house price from house size.

size 1 → price 3
size 2 → price 5
size 3 → price 7

Feature: size
Target: price

Suppose my model starts as:

price = 0 × size + 0

For size 2:

Prediction: 0
Actual target: 5
Error: prediction - target = 0 - 5 = -5

The negative error means the model predicted too low.

If loss uses squared error:
loss = (-5)² = 25

After successful training, this dataset should learn:

price = 2 × size + 1

After training, the model should learn a better weight and bias.

---

Think of the model as a new employee who must learn to estimate house prices.

The employee receives this training sheet:

```text
House size 1 → price 3
House size 2 → price 5
House size 3 → price 7
```

They do not yet know the pricing rule. Their job is to discover it.

## The rule the model is trying to learn

The model always uses this rule:

```text
predicted price = weight × house size + bias
```

Read it like this:

```text
predicted price = (price increase per size unit × house size) + starting amount
```

There are two adjustable numbers:

```text
weight
bias
```

They are called **parameters**.

### Weight

`weight` answers:

> “When house size goes up by 1, how much should price increase?”

For this data:

```text
size 1 → price 3
size 2 → price 5
size 3 → price 7
```

Every extra size unit adds `2` to the price.

So the correct weight is:

```text
weight = 2
```

### Bias

`bias` is the extra starting value added after multiplication.

If the rule is:

```text
price = 2 × size + 1
```

then `1` is the bias.

For house size 1:

```text
2 × 1 + 1 = 3
```

For house size 2:

```text
2 × 2 + 1 = 5
```

For house size 3:

```text
2 × 3 + 1 = 7
```

So the correct finished rule is:

```text
price = 2 × size + 1
```

The model does not receive that answer directly. It must learn `weight = 2` and `bias = 1` from the examples.

## The model starts knowing nothing

At the beginning, we give the model poor starting values:

```text
weight = 0
bias = 0
```

Its current rule becomes:

```text
predicted price = 0 × size + 0
```

Anything multiplied by zero is zero. So it guesses:

```text
size 1 → predicted price 0
size 2 → predicted price 0
size 3 → predicted price 0
```

It is wrong for every house. That is okay: training exists to improve these guesses.

## Error: how wrong one prediction is

For each example, the program calculates:

```text
error = prediction - actual price
```

For house size 2:

```text
prediction = 0
actual price = 5

error = 0 - 5
error = -5
```

The minus sign means:

> The model guessed lower than the real price.

Keep this small rule in mind:

```text
error < 0 → prediction is too low
error > 0 → prediction is too high
error = 0 → prediction is exactly correct
```

At the start, the three errors are:

```text
size 1: 0 - 3 = -3
size 2: 0 - 5 = -5
size 3: 0 - 7 = -7
```

## Loss: one score for all mistakes

The model needs one number that says, “How badly am I doing across all training examples?”

That number is called **loss**.

The program squares each error:

```text
error -3 → (-3)² = 9
error -5 → (-5)² = 25
error -7 → (-7)² = 49
```

Then it averages them:

```text
loss = (9 + 25 + 49) / 3
loss = 27.666667
```

Why square the errors?

1. A negative error becomes positive. A mistake is still a mistake whether the model guessed too low or too high.

2. Errors cannot cancel each other. For example:

```text
-5 + 5 = 0
```

This would wrongly suggest “no problem,” even though the model made two large mistakes.

3. Big mistakes matter more:

```text
error 2  → squared error 4
error 10 → squared error 100
```

The model is strongly encouraged to fix large mistakes.

So:

```text
large loss → model is making large mistakes
small loss → model is making small mistakes
loss near 0 → model is predicting very well
```

## How the model improves

The model has two settings it can change:

```text
weight
bias
```

It asks:

> “Should I increase or decrease weight?”
>
> “Should I increase or decrease bias?”
>
> “How much should I change them?”

The calculation that answers these questions is called the **gradient**.

A simple image to remember it:

```text
Loss is like standing on a hill in fog.
The lowest point of the hill is the best model.
A gradient tells the model which direction goes uphill.
The model walks in the opposite direction to go downhill.
```

Going downhill means reducing loss.

The model starts here:

```text
weight = 0
bias = 0
loss = 27.666667
```

After one learning update, it changes to approximately:

```text
weight = 2.266667
bias = 1
```

Its new rule is now:

```text
predicted price = 2.266667 × size + 1
```

This is not perfect yet, but it is much closer to the correct rule:

```text
predicted price = 2 × size + 1
```

## Learning rate: how big each learning step is

The program uses a **learning rate**.

This means:

> “How much should I trust the gradient and move during one update?”

```text
small learning rate → small careful steps, slower learning
good learning rate  → steady progress toward a low loss
huge learning rate  → jumps too far and may miss the best values
```

A learning rate that is too large can make the model jump back and forth:

```text
too low → too high → too low → too high
```

Then loss may grow instead of shrink.

## Why the first output line has two different moments

The program does these actions in this order:

```text
1. Use current weight and bias.
2. Make predictions.
3. Calculate errors.
4. Calculate loss.
5. Calculate gradients.
6. Update weight and bias.
7. Print the result.
```

So the first printed line contains:

```text
loss = 27.666667
```

This loss belongs to the old starting model:

```text
weight = 0
bias = 0
```

But the same line prints the newly updated values:

```text
weight = 2.266667
bias = 1
```

So think of the line as saying:

> “Before this update, my loss was 27.666667. After this update, my new parameters are weight 2.266667 and bias 1.”

## After 100 learning steps

The model reaches approximately:

```text
weight = 2.003887
bias = 0.991163
```

Those values are very close to:

```text
weight = 2
bias = 1
```

The model has learned the pattern from the examples.

## Inference: using the trained model

Now we ask about a new house that was not part of the training examples:

```text
house size = 4
```

Training has finished, so the model does not change its weight or bias anymore.

It only uses them:

```text
predicted price = 2.003887 × 4 + 0.991163
predicted price ≈ 9.006713
```

So it predicts price `9.006713`, which is very close to `9`.

The full story is:

```text
Training data
   ↓
Start with poor parameter values
   ↓
Make predictions
   ↓
Compare predictions with actual answers
   ↓
Calculate error and loss
   ↓
Use gradients to adjust weight and bias
   ↓
Repeat many times
   ↓
Get a trained model
   ↓
Use it for inference on new input
```

The most important memory sentence is:

> Training changes parameters to reduce loss. Inference uses the learned parameters to make a prediction.