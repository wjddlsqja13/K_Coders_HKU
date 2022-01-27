def minimumLoss(price):
  loss = sorted(price,reverse=True)
  min_value = 1e9
  for i in range(len(price)-1):
    if loss[i] - loss[i+1] < min_value and price.index(loss[i]) < price.index(loss[i+1]):
      min_value = loss[i] - loss[i+1]
  return min_value
