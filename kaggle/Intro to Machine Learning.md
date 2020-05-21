# Intro to Machine Learning



### 1. How Models Work

- **fitting or training** the model
  - step of capturing patterns from data
  - The data used to fit the model is called the **training data**.

- "deeper" trees
  - a tree that has more "splits"

- **leaf**
  - The point at the bottom where we make a prediction



---



### 2. Basic Data Exploration

- Pandas: the primary tool for exploring and manipulating data.
  - `import pandas as pd`
  - DataFrame: holds the type of data as a table

- `DataFrame.describe()`
  - count, mean, std, min, 25%, 50%, 75%, max



---



### 3. Your First Machine Learning Model

#### Selecting Data for Modeling

- `DataFrame.columns()`
  
- to see a list of all columns in the dataset
  
- `DataFrame.dropna(axis={num})`
  - drops missing values
  - ex) `DataFrame = DataFrame.dropna(axis=0)`

- Selecting the Prediction Target
  - The column we want to predict is called the **prediction target**.
    - The prediction target is called **y** by convention.
  - This single column is stored in a **Series**.
  - can be pulled out with dot-notation
    - ex) `melbourne_data.Price`

- Choosing "Features"

  - The columns that are inputted into our model are called **features**.

  - Features can be selected with a column list.

    - ```python
      melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
      X = melbourne_data[melbourne_features]
      # this data is called "X" by convention.
      ```

- `DataFrame.head()`
  
  - shows the top few rows

---

#### Building Your Model

- **scikit-learn** is used to create models. (It is written as sklearn when coding)

- The steps to building and using a model

  **1. Define**

  **2. Fit**

  **3. Predict**

  **4. Evaluate**

  ```python
  from sklearn.tree import DecisionTreeRegressor
  
  # Define model. Specify a number for random_state to ensure same results each run
  melbourne_model = DecisionTreeRegressor(random_state=1)
  
  # Fit model
  melbourne_model.fit(X, y)
  
  print("Making predictions for the following 5 houses:")
  print(X.head())
  print("The predictions are")
  print(melbourne_model.predict(X.head()))
  
  # output
  Making predictions for the following 5 houses:
     Rooms  Bathroom  Landsize  Lattitude  Longtitude
  1      2       1.0     156.0   -37.8079    144.9934
  2      3       2.0     134.0   -37.8093    144.9944
  4      4       1.0     120.0   -37.8072    144.9941
  6      3       2.0     245.0   -37.8024    144.9993
  7      2       1.0     256.0   -37.8060    144.9954
  The predictions are
  [1035000. 1465000. 1600000. 1876000. 1636000.]
  ```

  

---



### 4. Model Validation

#### What is Model Validation

- We need a single metric to evaluate models' quality.

  - The relevant measure of model quality is predictive accuracy.

- **Mean Absolute Error (MAE)** is one of metrics.

  - ```python
    from sklearn.metrics import mean_absolute_error
    
    predicted_home_prices = melbourne_model.predict(X)
    mean_absolute_error(y, predicted_home_prices)
    ```

---

#### The Problem with "In-Sample" Scores

- If a single data sample is used for both building and evaluating model, the model would be very inaccurate in practice.

  - The most straightforward way to solve this problem is by excluding some data from the model-building process to test the model's accuracy.

    - This excluded data is called **Validation data**.

  - ```python
    from sklearn.model_selection import train_test_split
    
    # split data into training and validation data, for both features and target
    # The split is based on a random number generator. Supplying a numeric value to
    # the random_state argument guarantees we get the same split every time we
    # run this script.
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
    # Define model
    melbourne_model = DecisionTreeRegressor()
    # Fit model
    melbourne_model.fit(train_X, train_y)
    
    # get predicted prices on validation data
    val_predictions = melbourne_model.predict(val_X)
    print(mean_absolute_error(val_y, val_predictions))
    ```

  - Once the model's accuracy turns out to be inadequate in practice, there are many ways to improve this model.

    - ex) experimenting to find better features or different model types



---



### 5. Underfitting and Overfitting

- **overfitting**
  - a model matches the training data almost perfectly, but does poorly in validation and other new data
  - capturing spurious patterns
  - The model has too many leaves, so fewer sample data are in each leaf
- **underfitting**
  - failing to capture relevant patterns
  - The model has too few leaves, so excessive amount of sample data are in each leaf

- These problems can be solved by controlling the tree depth.

  - There are a few alternatives for controlling the tree depth.

    - One is *max_leaf_nodes* argument.

    - ```python
      from sklearn.metrics import mean_absolute_error
      from sklearn.tree import DecisionTreeRegressor
      
      def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
          model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
          model.fit(train_X, train_y)
          preds_val = model.predict(val_X)
          mae = mean_absolute_error(val_y, preds_val)
          return(mae)
      
      # compare MAE with differing values of max_leaf_nodes
      for max_leaf_nodes in [5, 50, 500, 5000]:
          my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
          print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
          
      # result
      Max leaf nodes: 5  			 Mean Absolute Error:  347380
      Max leaf nodes: 50  		 Mean Absolute Error:  258171
      Max leaf nodes: 500  		 Mean Absolute Error:  243495
      Max leaf nodes: 5000  		 Mean Absolute Error:  254983
      ```

  - Once the optimal max_leaf_nodes (best_tree_size) is figured out, all of the data (not split) can be used to make the model even more accurate by keeping that tree size.



---



### 6. Random Forests

- **random forest**
  - It uses many trees and makes prediction by averaging the predictions of each component tree.
    - It has generally has much better predictive accuracy than a single decision tree.
    - It works well with default parameters.
      (Many models are sensitive to getting the right parameters.)
  - When coding, it can be used in the same way of using DecisionTreeRegressor.
    - `from sklearn.ensemble import RandomForestRegressor`