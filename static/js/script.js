async function calculate(operation) {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const resultElement = document.getElementById('result');
    const messageElement = document.getElementById('message');
    const historyElement = document.getElementById('history');

    resultElement.textContent = '';
    messageElement.textContent = '';

    if (isNaN(num1) || isNaN(num2)) {
        messageElement.textContent = 'Por favor ingresa números válidos';
        return;
    }

    try {
        const response = await fetch(`/${operation}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ num1, num2 })
        });
        const result = await response.json();
        if (response.ok) {
            resultElement.textContent = result.result;
            const listItem = document.createElement('li');
            listItem.textContent = `Operación: ${operation}, Número 1: ${num1}, Número 2: ${num2}, Resultado: ${result.result}`;
            listItem.classList.add('opacity-0');
            historyElement.appendChild(listItem);
            setTimeout(() => {
                listItem.classList.remove('opacity-0');
                listItem.classList.add('opacity-100');
            }, 10);
        } else {
            messageElement.textContent = result.result || 'Error al realizar la operación';
        }
    } catch (error) {
        messageElement.textContent = 'Error al realizar la operación';
    }
}

function toggleDarkMode() {
    document.body.classList.toggle('dark');
}
