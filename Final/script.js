function handleSubmit(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the form data
    const name = document.getElementById('name-contact-form-3-uaz4g7GXVt').value;
    const email = document.getElementById('email-contact-form-3-uaz4g7GXVt').value;
    const input = document.getElementById('textarea-contact-form-3-uaz4g7GXVt').value;

    // Format the data as CSV
    const csvData = `${name},${email},${input}\n`;

    // Create a Blob with the CSV data
    const blob = new Blob([csvData], { type: 'text/csv' });

    // Create a link element to trigger the download
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    csv_name = name +'.csv'
    link.download = csv_name;
    link.click();
}
