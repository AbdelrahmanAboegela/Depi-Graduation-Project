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
