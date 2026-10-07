# Concrete Crack Segmentation

This project trains a YOLO segmentation model to identify cracks in concrete images. Model training and evaluation are done in Google Colab; a small Streamlit app runs predictions on uploaded images.

## Files

- `train_model_colab.ipynb` - downloads and prepares the dataset, trains the model, and evaluates it.
- `streamlit_app.py` - loads `best.pt` and displays a segmentation prediction for an uploaded image.
- `requirements.txt` - dependencies for the local Streamlit app.

## Train in Google Colab

1. Open `train_model_colab.ipynb` in Google Colab and select a GPU runtime.
2. Add a Colab Secret named `ROBOFLOW_API_KEY` with a Roboflow API key that can access the project.
3. Run the notebook cells in order. It downloads the source crack dataset with KaggleHub, prepares a dataset through Roboflow, trains YOLO26n-seg for 100 epochs, and evaluates the test split.
4. Download the trained `best.pt` from the Colab training output and place it in this project folder.

The notebook installs its training dependencies as it runs. Dataset access requires a working Roboflow account and API key; keep the key in Colab Secrets rather than in the notebook.

## Run predictions locally

From this project folder, install the app dependencies and start Streamlit:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

Open the local URL printed by Streamlit, upload a JPG or PNG image, and select **Predict**. The app expects the trained weights at `best.pt`.

## Notes

- The project does not include the dataset or trained weights. Train the model in Colab or provide your own compatible YOLO segmentation weights.
- The app predicts at image size 640 with a confidence threshold of 0.40.
- Training results can vary with the selected dataset, Roboflow export, and runtime.
