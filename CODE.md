Project Setup
1. Clone and Prepare Repository
```bash
git pull origin main
```

Create required project folders:
```bash
mkdir model
mkdir server
mkdir client
```

Move your trained notebook into the model directory:
```bash
mv banglore_house_price.ipynb model
```

2. Set Up Python Environment

Create and activate a virtual environment using Conda:
```bash
conda create -n bprice python=3.12.12
conda activate bprice
```

Install required dependencies:
```bash
pip install pandas numpy matplotlib kagglehub scikit-learn flask ipykernel
```

Save dependencies to a requirements file:
```bash
pip freeze > requirements.txt
```

3. Backend Setup (Flask Server)

Navigate to the server directory and create an artifacts folder:

```bash
cd server
mkdir artifacts
cd ..
```

Move trained model files into the server:
```bash
cp model/banglore_house_price_model.pkl server/artifacts
cp model/columns.json server/artifacts
```

4. Frontend Setup (Client UI)

Create frontend files inside the client folder:
```bash
touch client/app.html
touch client/app.js
touch client/app.css
```

Add your HTML, CSS, and JavaScript code to these files.

5. Run the Application

Start the Flask backend server:

```bash
cd server
python server.py
```

Once the server is running, open app.html in your browser to use the application.