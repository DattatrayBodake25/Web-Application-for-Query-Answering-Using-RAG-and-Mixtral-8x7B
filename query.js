function submitQuery(event) {
    event.preventDefault();

    const userQuery = document.getElementById('userQuery').value;

    fetch('/answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'query': userQuery }),
    })
    .then(response => response.json())
    .then(data => {
        const answerText = document.getElementById('answerText');
        answerText.textContent = data.answer;
    })
    .catch(error => console.error('Error:', error));
}