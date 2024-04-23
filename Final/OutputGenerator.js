document.addEventListener('DOMContentLoaded', function() {
    fetch('path/to/output.csv')
        .then(response => response.text())
        .then(data => {
            processData(data);
        })
        .catch(error => console.error('Error loading the CSV file:', error));

    function processData(csvData) {
        const rows = csvData.split('\n');
        const headers = rows[0].split(',');
        const values = rows[1].split(',');

        document.getElementById('OutputText').textContent = values[0];
        document.getElementById('OutputImage').src = values[1];
        
        const linksContainer = document.getElementById('links');
        linksContainer.innerHTML = ''; // Clear previous links if any

        // Start from 2 because the first two columns are for text and image
        for (let i = 2; i < headers.length; i++) {
            const linkElement = document.createElement('a');
            linkElement.href = values[i];
            linkElement.textContent = `Link ${i-1}: ${values[i]}`;
            linkElement.className = 'mbr-text mbr-fonts-style display-7'; // Style class
            linkElement.target = '_blank'; // Opens link in new tab
            linksContainer.appendChild(linkElement);
            linksContainer.appendChild(document.createElement('br')); // New line after each link
        }
    }
});
