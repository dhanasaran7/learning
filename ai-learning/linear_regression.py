sizes = [1.0, 2.0, 3.0]
prices = [3.0, 5.0, 7.0]

weight = 0.0
bias = 0.0
learning_rate = 0.1
steps = 100


def predict(size, weight, bias):
    return weight * size + bias


for step in range(steps):
    predictions = [predict(size, weight, bias) for size in sizes]

    errors = [
        prediction - actual_price
        for prediction, actual_price in zip(predictions, prices)
    ]

    loss = sum(error ** 2 for error in errors) / len(errors)

    weight_gradient = (
        2 * sum(error * size for error, size in zip(errors, sizes)) / len(sizes)
    )
    bias_gradient = 2 * sum(errors) / len(sizes)

    weight = weight - learning_rate * weight_gradient
    bias = bias - learning_rate * bias_gradient

    if step in [0, 1, 9, 99]:
        print(
            f"step={step + 1}, loss={loss:.6f}, "
            f"weight={weight:.6f}, bias={bias:.6f}"
        )

final_prediction = predict(4.0, weight, bias)

print(f"Prediction for house size 4: {final_prediction:.6f}")

assert final_prediction > 8.9
assert final_prediction < 9.1
print("Checks passed.")