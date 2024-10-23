//Event Listener
document.getElementById('predict-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get values of inputs
    var age = document.getElementById('age').value;
    var breed = document.getElementById('breed').value;
    var gender = document.getElementById('gender').value;
    var weight = document.getElementById('weight').value;
    var environment = document.getElementById('environment').value;
    var symptom1 = document.getElementById('symptom1').value;
    var symptom2 = document.getElementById('symptom2').value;
    var symptom3 = document.getElementById('symptom3').value;

    // Create data object
    var data = {
        'Age (Years)': age,
        'Breed': breed,
        'Gender': gender,
        'Weight (lbs)': weight,
        'Environment': environment,
        'Symptom 1': symptom1,
        'Symptom 2': symptom2,
        'Symptom 3': symptom3,
    };

    fetch('http://localhost:5001/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction').textContent = 'Predicted Illness: ' + data.prediction;
        document.getElementById("myModal").style.display = "block";
    })
    .catch((error) => console.error('Error:', error));
});

// Get the modal
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};
