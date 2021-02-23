# Genetic Algorithms 

This is the code for Genetic Algorithms by @Sirajology on Youtube. In this demo code we use the MAGIC Gamma Telescope dataset to build a classifer. The classifier will train on the dataset and then be able to classify whether or not some energy is either Gamma Radiation or Hadron Radiation. Instead of guessing and checking the best ML model and hyperparameters to use, we use a genetic programming library called tpot to do that for us by trying out a bunch of them. 

### Code and Resources Used

**Language:** Python 3.8

**Dataset:** [MAGIC Gamma Telescope Dataset](https://archive.ics.uci.edu/ml/datasets/MAGIC+Gamma+Telescope)

**Libraries and Modules:** Numpy, tpot, scikit-learn, pandas

**Keywords:** Classification, tpot, radiation, machine learning

**Procedure**

**Step 1:** Download this MAGIC GAMMA telescope Dataset. Clean the data from the csv file and check if there is any missing or irrelevant data.

**Step 2:** Use TPOT and built an Machine Learning classification Pipleine for sorting it in 2 classes.

**Step 3:** Split training, testing, and validation data. 

**Step 4:** Let Genetic Programming find best ML model and hyperparameters

**Step 5:** Export Generated accuracy score. 

**References:**

1. https://www.youtube.com/watch?v=dSofAXnnFrY
2. https://github.com/nhrigby/genetic_algorithm_challenge
3. https://github.com/llSourcell/genetic_algorithm_challenge
