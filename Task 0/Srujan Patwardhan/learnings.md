## Text Summarization with Transformer Models

#### Two types of text summarization 
- Extractive
- Abstractive

##### Easiest way to summarize
- summarization pipeline
    - from transformers import pipeline
    - just provide a summarization task to it

### Using Pre-trained models
- Google's T5 model
    - various types of models in t5, we are going to choose t5-base

#### Limitations
- limit of 512 tokens
- the model sometimes adds sentences on its own because it is pretrained which may change the context of the text

***

## Decision Tree for Iris Flower Classification

##### Gini Impurity
- measure of randomness(entropy)
- calculated at each step of the decision tree 
- GI = 0(node is pure)
- GI = 1(highly impure or the data points are evenly distributed)
***
## Task 1
- #### Matplotlib vs Seaborn
    - Matplotlib
        - Low level
        - Versatility
        - Fine Grained Control
    - Seaborn
        - High level
        - Statistical Plotting
        - Built in themes and colour palettes
        - Less customization

- Use MatplotLib when you want full control over the apperance an layout of your plots 
- Use Seaborn when you want to create attractive, informative and statistically oriented plots with minimal code
***
- #### Numpy arrays
    - Numpy operations and functions are implemented internally in C++ (100 times faster)
<mark>zip function is used in Python to combin 2 lists, tuple, etc.</mark>
    - All the elements in a numpy array have the same data type. 
    - <mark> use @ between 2 arrays to perform matrix multiplication</mark>
    - `genfromtxt` function used for loading data from csv files to numpy arrays
    - `np.savetxt` to store the obtained result into a file
    - ###### Broadcasting
        - allows operation between 2 arrays with different dimensions
        - creates copies and improves performance by saving memory
    - comparison operators return an array of booleans with the 1 as True and 0 as False
    - rand generates random numbers from the uniform distribution [0,1)
    - randn generates random numbers from the normal distribution (mean = 0, standard deviation = 1)
---
### Pandas  
    
- Data read from a file using Pandas has type **Dataframe**
- `.info()` basic info
- `.describe()` view all statistical information
- dataframe format is similar to a dictionary containing column names as keys and values as list/array
- `first_valid_index()` method used to find the first non-NaN value
- `.sample()` random sample of rows from dataframe
- `sort_values()` sort the values of a particular column
- `merge()` this method is used to combine two datframes but they should have a column in common
- `to_csv()` write to a csv file

---
### Visualization
- `%matplotlib inline` plots are shown and embedded within the Jupytr notebook itself and not as a popup
- `plt.legend()` display a legend

---


