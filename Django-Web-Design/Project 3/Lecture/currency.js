document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('form').onsubmit = () => {

        // Send a GET request to the URL
        fetch('https://api.exchangeratesapi.io/latest?base=USD')
        // Put response into json form
        .then(response => response.json())
        // takes response as input and returns response.json
        .then(data => {
            // Log data to the console
            // console.log(data);
            const currency = document.querySelector('#currency').value.toUpperCase();

            // Get rate from data
            const rate = data.rates[currency];

            // Check if currency is valid:
            if (rate !== undefined) {
              //Display exchange on the screen
              document.querySelector('#result').innerHTML = `1 USD is equal to ${rate.toFixed(3)} ${currency}.`;
            }
            else {
              // Display error on the screen
              document.querySelector('#result').innerHTML = 'Invalid Currency.';
            }
        })
        // Catch any errors and log them to the console
        .catch(error => {
          console.log('Error:', error);
        });
        // Prevent default submission
        return false;
    }
});
