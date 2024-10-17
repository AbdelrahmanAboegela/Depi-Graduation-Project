<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>

<h1>Stress Detection and Analysis Project</h1>

<h2>Table of Contents</h2>
<ol>
    <li><a href="#project-overview">Project Overview</a></li>
    <li><a href="#key-components">Key Components</a></li>
    <ul>
        <li><a href="#1-azure-blob-storage">Azure Blob Storage</a></li>
        <li><a href="#2-data-mounting-in-databricks">Data Mounting in Databricks</a></li>
        <li><a href="#3-data-preprocessing">Data Preprocessing</a></li>
    </ul>
    <li><a href="#how-to-run-the-blob-storage-app">How to Run the Blob Storage App</a></li>
    <li><a href="#security-considerations">Security Considerations</a></li>
    <li><a href="#sql-queries">SQL Queries</a></li>
    <li><a href="#Model-Development">Model Development </a></li>
    <li><a href="#Visualization">Visualization </a></li>
    <li><a href="#Pipeline&Deploy">Pipeline&Deploy </a></li>
    <li><a href="#contact-information">Contact Information</a></li>
</ol>

<h2 id="project-overview">Project Overview</h2>
<p>This project focuses on <strong>Stress Detection and Analysis</strong> using EEG (Electroencephalogram) and ECG (Electrocardiogram) data. The goal is to preprocess this data and use it for developing machine learning models that can classify stress levels in individuals. We are leveraging Azure services for storage, computation, and model development.</p>

<h3>Current Stage:</h3>
<p>We have completed the data collection, storage setup, and preprocessing. The next steps involve model development and deployment.</p>

<h2 id="key-components">Key Components</h2>

<h3 id="1-azure-blob-storage">1. Azure Blob Storage</h3>

<h4>Storage Setup:</h4>
<p>Two containers have been created:</p>
<ul>
    <li><strong>raw-data</strong>: Contains the original EEG and ECG files.</li>
    <li><strong>processed-data</strong>: Contains the processed data, which has been cleaned and organized for analysis.</li>
</ul>
<p>You can check out the code for managing Azure Blob Storage here: <a href="https://github.com/AbdelrahmanAboegela/Depi-Graduation-Project/tree/main/Docker_Apps/azure_blob_manager">Azure Blob Manager</a></p>

<h4>Security:</h4>
<ul>
    <li>OAuth 2.0 authentication is used to ensure secure access.</li>
    <li>Credentials are managed via environment variables.</li>
</ul>

<h3 id="2-data-mounting-in-databricks">2. Data Mounting in Databricks</h3>

<h4>Mounting Process:</h4>
<p>The <strong>raw data</strong> and <strong>processed data</strong> containers were mounted to Databricks for direct access to the data without needing manual downloads.</p>
<p>You can find the data mounting scripts here: <a href="https://github.com/AbdelrahmanAboegela/Depi-Graduation-Project/tree/main/DataBricks_PreProcessing">Databricks PreProcessing</a></p>

<h4>Mount Points:</h4>
<ul>
    <li><code>/mnt/stressdata</code>: For raw data.</li>
    <li><code>/mnt/processedstressdata</code>: For processed data.</li>
</ul>

<h4>Security:</h4>
<p>The Azure credentials (client ID, tenant ID, and client secret) were securely used for mounting the Blob Storage.</p>

<h3 id="3-data-preprocessing">3. Data Preprocessing</h3>

<h4>Data Types:</h4>
<p>The project deals with two primary types of data:</p>
<ul>
    <li><strong>ECG Data</strong>: Heart rate variability and other metrics.</li>
    <li><strong>EEG Data</strong>: Brainwave frequencies (Delta, Theta, Alpha, Beta, Gamma).</li>
</ul>
<p>You can find the preprocessing scripts here: <a href="https://github.com/AbdelrahmanAboegela/Depi-Graduation-Project/tree/main/DataBricks_PreProcessing">Preprocessing Code</a></p>

<h4>Processing:</h4>
<p>Both datasets were cleaned, merged, and exported back to the processed-data container. Important metrics, such as the ratio of Alpha and Beta power in EEG, were calculated.</p>

<h2 id="how-to-run-the-blob-storage-app">How to Run the Blob Storage App</h2>

<p>We developed a Python application for easy access to the Azure Blob Storage containers, allowing for the upload, download, and deletion of files.</p>
<p>You can find the application here: <a href="https://github.com/AbdelrahmanAboegela/Depi-Graduation-Project/tree/main/Docker_Apps/azure_blob_manager">Azure Blob Manager App</a></p>

<h4>Steps:</h4>
<ol>
    <li>Clone the repository containing the app.</li>
    <li>Ensure Docker is installed on your machine.</li>
    <li>To run the app, use the following command:
    <pre><code>docker run -p 5000:5000 -e DISPLAY=host.docker.internal:0.0 apdoelepe/azure_blob_manager</code></pre></li>
    <li>If the app requires Azure credentials for access, contact me via GitHub or LinkedIn to provide the <code>azure_credentials.txt</code>.</li>
</ol>

<h2 id="security-considerations">Security Considerations</h2>

<ul>
    <li><strong>OAuth 2.0 Authentication</strong> ensures that only authorized users can access the Azure Blob Storage.</li>
    <li><strong>Environment Variables</strong> are used for handling sensitive information like client secrets, ensuring that they are not exposed in the codebase.</li>
    <li><strong>Docker Deployment</strong>: The app is containerized using Docker for easy deployment across different environments, ensuring that the same version is available to the entire team.</li>
</ul>

<h2 id="sql-queries">SQL Queries</h2>

<p>This section of the project contains the SQL queries and stored procedures that are used to create tables, insert data, and execute queries in the database. The following SQL files are included in this folder:</p>

<h3>1. Create Tables</h3>
<ul>
    <li><strong>ECG Tables</strong>: SQL queries to create tables for storing ECG data.</li>
    <li><strong>EEG Tables</strong>: SQL queries to create tables for storing EEG data.</li>
    <li><strong>EEG Ratio Tables</strong>: SQL queries to create tables for storing the ratio of EEG Alpha to Beta power.</li>
</ul>

<h3>2. Create Schemas</h3>
<p>SQL queries for creating schemas in the database, ensuring proper data organization.</p>

<h3>3. Stored Procedure Execution</h3>
<p>Scripts for creating and executing stored procedures that automate table creation and data insertion tasks.</p>

<h3>4. Insert Data into Tables</h3>
<p>SQL queries to insert ECG and EEG data into the respective tables after preprocessing.</p>

<p>You can view and use the SQL scripts from the following folder: <a href="https://github.com/AbdelrahmanAboegela/Depi-Graduation-Project/tree/main/SQL%20queries">SQL Queries Folder</a></p>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stress Detection using LSTM Networks</title>
</head>
<body>
    <h1>Stress Detection using LSTM Networks</h1>
    <p>This project leverages Long Short-Term Memory (LSTM) networks to detect stress levels using EEG and ECG data. The model is designed to handle sequential time-series data and classify whether the subject is under stress or not. The development is guided by principles of deep learning and signal processing, with an emphasis on model accuracy and generalization.</p>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#model-architecture">Model Architecture</a></li>
        <li><a href="#why-lstm">Why LSTM?</a></li>
        <li><a href="#data-preprocessing">Data Preprocessing</a></li>
        <li><a href="#training-evaluation">Training & Evaluation</a></li>
        <li><a href="#results">Results</a></li>
        <li><a href="#system-requirements">System Requirements</a></li>
        <li><a href="#usage-instructions">Usage Instructions</a></li>
        <li><a href="#future-directions">Future Directions</a></li>
        <li><a href="#contributors">Contributors</a></li>
    </ul>

    <h2 id="overview">Overview</h2>
    <p>This project aims to develop a robust system that identifies stress levels by analyzing physiological signals, specifically EEG and ECG. The system employs a binary classification approach to predict stress conditions, leveraging deep learning architectures tailored for time-series data.</p>

    <h2 id="model-architecture">Model Architecture</h2>
    <p>The LSTM-based model is built with the following components:</p>
    <ul>
        <li><strong>LSTM Layers:</strong> Extract sequential patterns from the data, using both temporal dependencies and context.</li>
        <li><strong>Dense Layers:</strong> Fully connected layers that process the extracted features into condensed representations for final predictions.</li>
        <li><strong>Dropout Layers:</strong> Implemented after key layers to reduce overfitting by deactivating random neurons during training.</li>
        <li><strong>Output Layer:</strong> A sigmoid function produces the binary stress classification.</li>
        <li><strong>Adam Optimizer:</strong> Optimizes the network’s weights with a learning rate of 0.0003, and gradient clipping is applied for training stability.</li>
    </ul>
    <p><strong>Key Layer Specifications:</strong></p>
    <pre>
LSTM(128 units, return_sequences=True) → Dropout(50%) → LSTM(64 units) → 
Dense(128 units, ReLU) → Dropout(40%) → Dense(64 units) → Sigmoid Output Layer
    </pre>

    <h2 id="why-lstm">Why LSTM?</h2>
    <p>EEG and ECG data are inherently time-dependent, and LSTMs are designed to address the challenges of sequential data processing. LSTM networks can preserve important information across long sequences, making them superior to traditional feed-forward neural networks for this type of task. Additionally, LSTMs effectively mitigate the vanishing gradient problem, ensuring stable and reliable training.</p>

    <h2 id="data-preprocessing">Data Preprocessing</h2>
    <p>Given the nature of EEG and ECG data, several preprocessing steps were applied:</p>
    <ul>
        <li><strong>Feature Selection:</strong> Recursive Feature Elimination (RFE) was used to identify the most relevant signals.</li>
        <li><strong>Normalization:</strong> Data was normalized to ensure consistency across different input features.</li>
        <li><strong>Sequence Reshaping:</strong> Data was reshaped into sequences to align with the LSTM’s input format.</li>
    </ul>

    <h2 id="training-evaluation">Training & Evaluation</h2>
    <p>To optimize the model's performance, the following training setup was employed:</p>
    <ul>
        <li><strong>Epochs:</strong> 150</li>
        <li><strong>Batch Size:</strong> 16</li>
        <li><strong>Loss Function:</strong> Binary Cross-Entropy</li>
        <li><strong>Metrics:</strong> Accuracy and F1 Score</li>
    </ul>
    <p><strong>Training Callbacks:</strong></p>
    <ul>
        <li><strong>ReduceLROnPlateau:</strong> Dynamically reduces the learning rate when the validation loss plateaus.</li>
        <li><strong>EarlyStopping:</strong> Stops training when no improvements are seen for 10 consecutive epochs, restoring the best model weights.</li>
    </ul>

    <h2 id="results">Results</h2>
    <p>The model’s performance was evaluated using accuracy and F1 score. Each model was trained and evaluated separately for both male and female subjects across different activity states (e.g., EO, AC1). These results demonstrate the model's effectiveness in detecting stress patterns from physiological signals.</p>

    <h2 id="system-requirements">System Requirements</h2>
    <p>To run this project, ensure the following dependencies are installed:</p>
    <ul>
        <li>Python 3.x</li>
        <li>TensorFlow 2.x</li>
        <li>NumPy</li>
        <li>Pandas</li>
        <li>Scikit-learn</li>
        <li>Matplotlib (optional, for data visualization)</li>
    </ul>
    <p>Install the required packages via:</p>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h2 id="usage-instructions">Usage Instructions</h2>
    <p>Clone the repository and execute the model training script:</p>
    <pre><code>git clone https://github.com/AbdelrahmanAboegela/Depi-Graduation-Project.git</code></pre>
    <pre><code>python train_model.py</code></pre>
    <p>The script handles the data split into training and validation sets and applies callbacks for learning rate scheduling and early stopping based on validation loss.</p>

    <h2 id="future-directions">Future Directions</h2>
    <p>There are several areas for future exploration:</p>
    <ul>
        <li>Implementing more advanced neural architectures such as Gated Recurrent Units (GRU) or combining LSTM with Convolutional Neural Networks (CNNs).</li>
        <li>Expanding the model to handle real-time stress detection using live EEG/ECG streams.</li>
        <li>Improving model generalization through larger and more diverse datasets.</li>
        <li>Exploring multi-class classification to detect different levels of stress severity.</li>
    </ul>

    <h2 id="contributors">Contributors</h2>
    <p>Project maintained by <strong>Abdelrahman Aboegela</strong>.</p>

</body>
</html>



<h2 id="contact-information">Contact Information</h2>

<p>For any questions or access to the credentials, you can reach out to me via:</p>
<ul>
    <li><strong>GitHub</strong>: <a href="https://github.com/AbdelrahmanAboegela">AbdelrahmanAboegela</a></li>
    <li><strong>LinkedIn</strong>: <a href="https://www.linkedin.com/in/abdelrahman-alshames-635aa3277/">Abdelrahman Alshames</a></li>
</ul>

<h3>Contributions</h3>
<p>This project was also contributed to by:</p>
<ul>
    <li><strong>Ahmed Ismail Fraig</strong> - <a href="https://github.com/ahmedfraig">GitHub Profile</a></li>
    <li><strong>Tasneem Mahmoud</strong> - <a href="https://github.com/TasnemMahmoud">GitHub Profile</a></li>
    <li><strong>Esraa Mamdouh Omar</strong> - <a href="https://github.com/EsraaMamdouh1">GitHub Profile</a></li>
    
</ul>

</body>
</html>
