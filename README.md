# Real_Estate_Price_Prediction_End_to_End
A redo of the banglore House Pricing Dataset project I did a few years ago



cloned it in my system

create a venv
```bash
python -m venv bprice-env
source bprice-env/Scripts/activate
deactivate
rm irf bprice-env
```

instead of python env, i'll run a conda env
```bash
conda update -n base -c defaults conda
conda create -n bprice python=3.11
conda env list
conda activate bprice
conda deactivate
conda remove --name bprice --all
conda list
```

```bash
pip install fastapi uvicorn
pip install pandas numpy malplotlib scikit-learn seaborn
pip freeze > requirements.txt

pip show fastapi
which python
where python
uvicorn --version
python --version
flask --version

```

------------------------


**“Artifacts”**:
 In machine learning, artifacts are the outputs produced during training or preprocessing that are required later for inference or deployment.

Typical ML artifacts include:

* Trained model (.pkl, .joblib, .pt, .h5)

* Feature encoders

* Scalers

* Label mappings

* JSON config files

* Metadata (feature names, metrics, version info)   

Artifacts are often stored in:

AWS S3

MLflow artifact store

GCS bucket

Model registry

During deployment:

The server downloads required artifacts

Or bundles them in the container
-----------------------------
.

📁 3️⃣ Client/ Folder (Empty)

This is actually very interesting 👀

An empty Client folder usually means:

The system was designed to support a frontend layer, but it hasn’t been implemented yet.

Possible intentions:

A React frontend

HTML form

Streamlit app

Mobile app interface

Architecture intended:

User → Client → Server API → Model → Response

Right now, maybe they test using:

Postman

Curl

Direct localhost calls

But the folder exists because:

👉 They planned a UI layer but haven’t built it yet.

It’s architectural foresight.

----------------------------

I changed my mind... I'll make my model on google colab. and then do the web app building on vs code

```bash
git pull origin main
mkdir model
mv banglore_house_price.ipynb model
mkdir server

conda create -n bprice python=3.12.12
conda activate bprice

pip install pandas numpy matplotlib kagglehub scikit-learn ipykernel

pip freeze > requirements.txt

cd server
mkdir artifacts
cd ..
cp model/banglore_house_price_model.pkl server/artifacts
cp model/columns.json server/artifacts
```

