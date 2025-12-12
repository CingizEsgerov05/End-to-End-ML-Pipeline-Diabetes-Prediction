# End-to-End Machine Learning Pipeline: Diabetes Prediction

This project demonstrates a full end-to-end ML system including:
- Data loading and training
- Model saving/loading
- API deployment (FastAPI)
- Web interface (Streamlit)

## 🧠 Model
Logistic Regression trained on the Diabetes dataset.

## 🔧 Technologies
- Python
- Scikit-Learn
- FastAPI
- Streamlit
- Pickle

## 🚀 Pipeline
1. Train the model (`train_model.ipynb`)
2. Run API:
   uvicorn main:app --reload
3. Run frontend:
   streamlit run streamlit_app.py

## 🎯 Features
- End-to-end ML pipeline
- Deployed model
- Interactive UI
