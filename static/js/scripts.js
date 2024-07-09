function getWeather() {
    const city = document.getElementById('city-input').value;
    fetch('/weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ city })
    })
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById('weather-result');
            if (data.status === 'success') {
                const weatherData = data.data;
                resultDiv.innerHTML = `
                <p>Temperature: ${weatherData.temperature} °C</p>
                <p>Humidity: ${weatherData.humidity} %</p>
                <p>Pressure: ${weatherData.pressure} hPa</p>
                <p>Weather: ${weatherData.weather}</p>
                <p>Wind Speed: ${weatherData.wind_speed} m/s</p>
            `;
            } else {
                resultDiv.innerHTML = `<p>${data.message}</p>`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
