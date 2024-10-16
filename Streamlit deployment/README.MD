1. Prerequisites

Before starting the deployment process, ensure you have the following items:

.Docker installed on your machine or server. Docker Installation Guide

.Python 3.9 or a compatible version installed (if not using Docker).

.A requirements.txt file containing the required libraries:
                                              tensorflow==2.16.2
                                              keras==3.0.0  
                                              streamlit
                                              numpy
                                              joblib
2. Project Structure
                                               
Ensure that the project structure contains the following files and folders:
- app.py             # Main application file
- model_Female.h5    # AI model for female
- model_Male.h5      # AI model for male
- requirements.txt   # List of required libraries
- Dockerfile         # Docker setup


3. Docker Setup (If using Docker)
                                               
3.1. Dockerfile Configuration
Make sure you have a Dockerfile at the root of your project with the following configuration: 

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

3.2. Build Docker Image
Build the Docker image using the command line:
docker build -t stress-classification-app .

3.3. Run Docker Container
After building the image, run the container using the following command:
docker run -d -p 8501:8501 --name stress-classification-app stress-classification-app
                                            .   -d: Runs the container in detached mode.
                                            .   -p 8501:8501: Maps port 8501 of the container to the host.
                                            .   --name stress-classification-app: Names the container.

3.4. Access the Application
Once the container is running, you can access the Streamlit application from your browser using the following link:
 http://localhost:8501


4. Without Docker: Manual Deployment Steps
                                               
If you are not using Docker, you can follow these steps:

4.1. Install Python and Libraries
Ensure Python 3.9 or a compatible version is installed. After that, install the required libraries using the following command:  
pip install -r requirements.txt

4.2. Running the Application
To run the application manually, use the following command:
streamlit run app.py --server.port=8501 --server.address=0.0.0.0

4.3. Access the Application
After running the application, open your browser and enter the following address to access the app:
http://localhost:8501

5. Stopping and Removing Docker Container
                                               
-To stop the running container: 
docker stop stress-classification-app

-To remove the container:
docker rm stress-classification-app
       
