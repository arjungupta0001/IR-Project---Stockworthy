// Import the 'fs' (file system) module for file operations
const fs = require('fs');
const readline = require('readline');

// Create a readline interface to read input from the console
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function to ask for user input
function askQuestion(question) {
    return new Promise((resolve, reject) => {
        rl.question(question, (answer) => {
            resolve(answer);
        });
    });
}

// Function to save data to a CSV file
function saveToCSV(data) {
    // Define the CSV file path
    const csvFilePath = 'data.csv';

    // Prepare the CSV content
    const csvContent = `${data}\n`;

    // Append the data to the CSV file
    fs.appendFile(csvFilePath, csvContent, (err) => {
        if (err) throw err;
        console.log('Data saved to CSV file.');
        rl.close();
    });
}

// Main function to run the program
async function main() {
    try {
        // Ask for user input
        const userInput = await askQuestion('Enter data to save to CSV file: ');

        // Save the input to a CSV file
        saveToCSV(userInput);
    } catch (err) {
        console.error('Error:', err);
    }
}

// Call the main function to start the program
main();
