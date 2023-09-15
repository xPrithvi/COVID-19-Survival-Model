# COVID Survival Model
This artificial neural network (ANN) was trained on patients with COVID-19 based on pre-conditions such as age, obesity, hypertension, etc.
The model was created with PyTorch on Juypter Notebook and was trained on the following [dataset](https://www.kaggle.com/datasets/meirnizri/covid19-dataset) 
on Kaggle which was adapted from this [database](https://datos.gob.mx/busca/dataset/informacion-referente-a-casos-covid-19-en-mexico) released by the government of Mexico:
In particular, "Model-8V3V2" was trained with a 80/20 split concerning the training and test datasets. These datasets were created by selecting all patients 
entries marked as deceased from the original dataset and then randomly sampling the same number patients which were not marked as deceased. In total, the model 
was trained on approximately 120,000 examples and was tested on almost 30,000 examples with an accuracy of 91%.

**NOTE: This project was created for learning purposes and not practical application.**

![alt text](Isolated.png "Title")
