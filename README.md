# SwasthAI

This repository contains backend code for [SwasthAI-android](https://github.com/rohnsha0/medbuddyAI). The server is powered by FastAPI for performing various server-side tasks like handling chatbot questions, etc. It also includes IPython Notebook files for training the CNN models, dataset handling, and exported models.

## Overview

The FastAPI server facilitates the deployment of NLP-based models for various tasks such as chatbots, sentiment analysis, etc. It utilizes FastAPI, a modern, high-performance web framework for building APIs with Python 3.11+.

## Structure

- `/deployment`: Contains the FastAPI server implementation for handling model inference requests.
  - `main.py`: Main FastAPI file handling API endpoints and model inference.
  - `requirements.txt`: Dependencies required for the FastAPI server.
- `/exports`: Stores exported and serialized CNN models after training.
- `/notebooks`: IPython Notebook files used for training the CNN models based upon infected-organs.

## Getting Started

### Setting Up Datasets

- Ensure the datasets for respective organs (lungs, brain, skin, heart, etc.) are available in the `/datasets` directory using the datasets mentioned in the [file](data_sources.md).
- Organize the datasets in separate folders, maintaining a consistent structure for training.

### Training CNN Models

- Navigate to the `/notebooks` directory.
- Run the specific IPYNB notebook corresponding to the organ you wish to train the model for.
- Adjust hyperparameters, dataset paths, and other configurations as needed.

### Exporting Trained Models

- After training, the models will be serialized and saved in the `/exports` directory.

### FastAPI Server Deployment

#### Local Deployment

- Clone this repository onto your local machine.
- Install the required dependencies using `pip install -r app/requirements.txt`.
- Run the FastAPI server using `uvicorn`.

```bash
cd app
uvicorn main:app --host 0.0.0.0 --port 8000
```

- Access the FastAPI server at `http://localhost:8000/docs` for interactive API documentation.

<!--#### Docker Deployment

- Use the provided `Dockerfile` to create a Docker image containing the FastAPI server.
- Build the Docker image and run a containerized instance of the FastAPI server.

```bash
docker build -t fastapi-cnn-server .
docker run -p 8000:8000 fastapi-cnn-server
```

- Access the FastAPI server at `http://localhost:8000/docs` for interactive API documentation.-->

## Contributing

Contributions are welcomed! Please follow the guidelines in CONTRIBUTING.md for contributing to this project.

## License

This project is licensed under the GNU GPLv2 - see the [LICENSE](LICENSE) file for details.
