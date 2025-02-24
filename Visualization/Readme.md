# Data Visualizations

This section focuses on the visual exploration and analysis of various physiological signals and metrics collected across different stress conditions. The goal is to understand patterns, relationships, and distributions within the data, especially regarding heart rate variability (HRV), EEG brainwave activity, and gender-based differences.

## Visualizations Included

### 1. **Gender Distribution**
   - This plot shows the distribution of participants by gender to give an overview of the dataset's demographic makeup.

### 2. **Distribution of Stress Conditions (Segments)**
   - This visualization displays the distribution of data points across different stress conditions (segments), such as baseline (EO), low stress (AC1), and high stress (AC2).

### 3. **Heart Rate Distribution by Gender and Stress Condition**
   - A combined boxplot that visualizes how heart rate varies across different stress conditions, segmented by gender. This helps to identify potential gender-based differences in heart rate response under stress.

### 4. **AVNN by Stress Condition**
   - Boxplot showing the **Average of Normal-to-Normal intervals (AVNN)** across different stress conditions. It helps in understanding how the heart's resting state changes from baseline to high-stress conditions.

### 5. **SDNN (ms) by Gender**
   - A boxplot comparing the **Standard Deviation of NN intervals (SDNN)** by gender across all segments, giving insight into how heart rate variability differs between male and female participants.

### 6. **RMSSD vs Alpha Power Across Segments**
   - A scatter plot showing the relationship between **Root Mean Square of the Successive Differences (RMSSD)** and **Alpha Power** across different brain regions. It explores the possible connection between heart rate variability and brainwave activity.

### 7. **LF/HF Ratio Across Stress Conditions**
   - This plot visualizes the **Low-Frequency (LF) to High-Frequency (HF) ratio**, which is a key metric for understanding autonomic nervous system balance across stress conditions.

### 8. **LF/HF Ratio by Gender**
   - Similar to the LF/HF Ratio plot, but this one compares values by gender to observe potential gender differences in autonomic nervous system responses.

### 9. **Correlation Heatmap of HRV Measures**
   - A heatmap that shows correlations between various **Heart Rate Variability (HRV)** measures. It helps in understanding how different HRV metrics relate to one another.

### 10. **Correlation Heatmap of EEG and ECG Features**
   - A comprehensive correlation heatmap showing the relationship between EEG (brainwave activity) and ECG (heart rate) features, revealing the connections between brain and heart responses.

### 11. **Power Across Stress Conditions**
   - Visualizes how brainwave power changes across different stress conditions for various EEG bands (Alpha, Beta, etc.).

### 12. **Alpha Power Distribution and Average Alpha Power Across Stress Conditions**
   - This plot explores the distribution of **Alpha Power** (8-12 Hz) in specific brain regions (Fp1, Fp2) and shows the average alpha power across stress conditions. It provides insights into the relaxation and focus states of participants.

### 13. **Beta Power by Gender**
   - A boxplot displaying **Beta Power** across gender, allowing for the observation of any gender-related differences in cognitive load and attention.

### 14. **Frequency Distribution of Fp1 and Fp2 Beta Power**
   - This visual explores how **Beta Power** is distributed across two brain regions (Fp1 and Fp2) and across different segments, giving insights into mental engagement and stress.

### 15. **Alpha vs Beta Power Across Segments**
   - A scatter plot that compares **Alpha** and **Beta Power** across different brain regions and stress segments, providing insights into the interplay between relaxation and attention.

### 16. **Relationship between Mean HR and LF/HF Ratio by Gender**
   - This visual explores the relationship between **Mean Heart Rate** and the **LF/HF Ratio**, segmented by gender, to study how heart rate and autonomic nervous system balance are related.

---

## Key Insights

- **Heart Rate Variability (HRV) and Stress:** Several HRV metrics (such as AVNN, SDNN, RMSSD) show distinct variations between baseline, low-stress, and high-stress conditions, revealing the impact of stress on cardiac function.
- **Brainwave Activity and Stress:** EEG power (particularly Alpha and Beta bands) varies across stress conditions and shows gender-specific patterns, especially in frontal regions (Fp1, Fp2).
- **Gender-Based Differences:** The visualizations reveal some notable differences in heart rate and EEG activity between male and female participants under different stress conditions.
- **Correlations:** The heatmaps provide useful insights into how EEG and ECG features are interconnected, contributing to the broader understanding of how stress affects both the brain and heart.
