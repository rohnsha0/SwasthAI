# Setting Up Dataset

This guide will walk you through the process of downloading data from Kaggle.

## Prerequisites

Before you begin, make sure you have the following:

- An account on Kaggle (Sign up at [kaggle.com](https://www.kaggle.com))
- Kaggle API credentials (Refer to the [Kaggle API documentation](https://www.kaggle.com/docs/api) for instructions on how to obtain your credentials)

## Steps

Follow these steps to download data from Kaggle:

1. Install the Kaggle API by running the following command in your terminal:

    ```
    pip install kaggle
    ```

2. Choose a dataset from the list below and execute the corresponding command to download it:

    - [pneumonia](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia): `kaggle datasets download -d pneumonia`
    - [tuberculosis](https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset): `kaggle datasets download -d tuberculosis``

    Replace `pneumonia`, `tuberculosis`, etc. with the actual names of the variables with the link provided, you want to download.

3. The downloaded data will be saved to your current directory.

## Example

Here's an example of how to download the "Titanic: Machine Learning from Disaster" dataset and save it to the current directory:

- Dataset: [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic)
- Command: `kaggle datasets download -d titanic`

## Additional Resources

For more information on using the Kaggle API and managing datasets, refer to the [Kaggle API documentation](https://www.kaggle.com/docs/api).
