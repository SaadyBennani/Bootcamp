function lists_to_dict(keys, values) {
  let combined = {}
  keys.map((elem, idx) => {
    Object.assign(combined, {[elem]: values[idx]})
  })
  return combined
}

function average(d) {
  let prices = Object.values(d)
  let sum = prices.reduce((total, amount) => total + amount)
  return sum/prices.length
}
