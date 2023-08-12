// Get references to the screen and buttons
const screen = document.querySelector('.screen');
const buttons = document.querySelectorAll('.btn');
const clear = document.querySelector('.btn-clear');
const equal = document.querySelector('.btn-equal');

// Attach event listeners to the buttons
buttons.forEach(button => {
  button.addEventListener('click', event => {
    // Get the clicked button's value
    const value = event.target.dataset.num;
    // Append the value to the screen
    screen.value += value;
  });
});

// Attach event listener to the equal button
equal.addEventListener('click', () => {
  try {
    // Evaluate the expression and display the result
    const result = evaluateExpression(screen.value);
    screen.value = result;
  } catch (error) {
    // Display an error message if the expression is invalid
    screen.value = 'Error';
  }
});

// Attach event listener to the clear button
clear.addEventListener('click', () => {
  // Clear the screen
  screen.value = '';
});

// Function to evaluate the expression
function evaluateExpression(expression) {
  // Split the expression into an array of numbers and operators
  const tokens = expression.split(/(\+|\-|\*|\/)/);
  // Initialize the result to the first number in the array
  let result = parseFloat(tokens[0]);
  // Loop through the array of tokens and perform the appropriate operation
  for (let i = 1; i < tokens.length; i += 2) {
    const operator = tokens[i];
    const number = parseFloat(tokens[i + 1]);
    switch (operator) {
      case '+':
        result += number;
        break;
      case '-':
        result -= number;
        break;
      case '*':
        result *= number;
        break;
      case '/':
        result /= number;
        break;
    }
  }
  // Return the result
  return result;
}
