const server = "http://127.0.0.1:5000";

window.onload = function () {
    fetch(server + "/get_location_names")
        .then(response => response.json())
        .then(data => {

            const locations = data.locations;
            const locationSelect = document.getElementById("location");

            locations.forEach(location => {

                let option = document.createElement("option");
                option.value = location;
                option.text = location;

                locationSelect.appendChild(option);
            });

        });
};


function predictPrice() {

    const sqft = document.getElementById("sqft").value;
    const bhk = document.getElementById("bhk").value;
    const bath = document.getElementById("bath").value;
    const location = document.getElementById("location").value;

    const formData = new FormData();

    formData.append("total_sqft", sqft);
    formData.append("bhk", bhk);
    formData.append("bath", bath);
    formData.append("location", location);

    fetch(server + "/predict_home_price", {
        method: "POST",
        body: formData
    })
        .then(response => response.json())
        .then(data => {

            const price = data.estimated_price;

            document.getElementById("result").innerHTML =
                "Estimated Price: ₹ " + price + " Lakh";

        });

}