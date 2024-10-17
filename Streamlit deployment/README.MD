<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stress Detection Model Deployment Guide</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 4px;
            font-family: Consolas, "Courier New", monospace;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-left: 5px solid #ccc;
            overflow-x: auto;
        }
        .section {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

    <h1>Stress Detection Model Deployment Guide</h1>

    <div class="section">
        <h2>Prerequisites</h2>
        <p>Before starting the deployment process, ensure you have the following items:</p>
        <ul>
            <li><strong>Docker</strong> installed on your machine or server. <a href="https://docs.docker.com/get-docker/">Docker Installation Guide</a></li>
            <li><strong>Python 3.9</strong> or a compatible version installed (if not using Docker).</li>
            <li>A <code>requirements.txt</code> file containing the required libraries:
                <pre>tensorflow==2.16.2<br>keras==3.0.0<br>streamlit<br>numpy<br>joblib</pre>
            </li>
        </ul>
    </div>

    <div class="section">
        <h2>Project Structure</h2>
        <p>Ensure that the project structure contains the following files and folders:</p>
        <ul>
            <li><code>app.py</code> - Main application file</li>
            <li><code>model_Female.h5</code> - AI model for female</li>
            <li><code>model_Male.h5</code> - AI model for male</li>
            <li><code>requirements.txt</code> - List of required libraries</li>
            <li><code>Dockerfile</code> - Docker setup</li>
        </ul>
    </div>

    <div class="section">
        <h2>Docker Setup (If using Docker)</h2>

        <h3>3.1. Dockerfile Configuration</h3>
        <p>Make sure you have a <code>Dockerfile</code> at the root of your project with the following configuration:</p>
        <pre><code>FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]</code></pre>

        <h3>3.2. Build Docker Image</h3>
        <p>Build the Docker image using the command line:</p>
        <pre><code>docker build -t stress-classification-app .</code></pre>

        <h3>3.3. Run Docker Container</h3>
        <p>After building the image, run the container using the following command:</p>
        <pre><code>docker run -d -p 8501:8501 --name stress-classification-app stress-classification-app</code></pre>
        <p>Explanation of the flags:</p>
        <ul>
            <li><code>-d</code>: Runs the container in detached mode.</li>
            <li><code>-p 8501:8501</code>: Maps port 8501 of the container to the host.</li>
            <li><code>--name stress-classification-app</code>: Names the container.</li>
        </ul>

        <h3>3.4. Access the Application</h3>
        <p>Once the container is running, you can access the Streamlit application from your browser using the following link:</p>
        <p><a href="http://localhost:8501" target="_blank">http://localhost:8501</a></p>
    </div>

    <div class="section">
        <h2>Without Docker: Manual Deployment Steps</h2>

        <h3>4.1. Install Python and Libraries</h3>
        <p>Ensure Python 3.9 or a compatible version is installed. After that, install the required libraries using the following command:</p>
        <pre><code>pip install -r requirements.txt</code></pre>

        <h3>4.2. Running the Application</h3>
        <p>To run the application manually, use the following command:</p>
        <pre><code>streamlit run app.py --server.port=8501 --server.address=0.0.0.0</code></pre>

        <h3>4.3. Access the Application</h3>
        <p>After running the application, open your browser and enter the following address to access the app:</p>
        <p><a href="http://localhost:8501" target="_blank">http://localhost:8501</a></p>
    </div>

    <div class="section">
        <h2>Stopping and Removing Docker Container</h2>
        <p>To stop the running container:</p>
        <pre><code>docker stop stress-classification-app</code></pre>

        <p>To remove the container:</p>
        <pre><code>docker rm stress-classification-app</code></pre>
    </div>

</body>
</html>

       
