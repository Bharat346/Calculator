function sigma(expr, lower, upper) {
    let sum = 0;
    for (let y = lower; y <= upper; y++) {
        sum += eval(expr);
    }
    return sum;
}

// Example usage:
console.log(eval(sigma('y^2', 1, 5))); 