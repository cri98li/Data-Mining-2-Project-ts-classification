# Project Data Mining 2 Course @ UniPi

Course description:
Recent tremendous technical advances in processing power, storage capacity, and interconnectivity are creating unprecedented quantities of digital data. Data mining, the
science of extracting useful knowledge from such huge data repositories, has emerged as an interdisciplinary field in computer science. Data mining techniques have
been widely applied to problems in industry, science, engineering and government,
and it is believed that data mining will have profound impact on our society. The
course is divided into two modules. The first presents an introduction to the basic
concepts of data mining and the knowledge discovery process, and associated analytical models and algorithms. The second module provides an account of advanced
techniques for analysis and mining of novel forms of data, and the main application
areas and prototypical case studies.

Syllabus:
- Mining Time-Series and Spatio-Temporal Data.
- Mining Sequential Data, Mining Large Graphs and Networks.
- Advanced Association, Correlation and Frequent Pattern Analysis.
- Advanced Classification, Cluster Analysis and Outlier Detection.
- Data Mining Languages, Standards and System Architectures.
- Ethical aspects of data mining.
- Privacy-Preserving Data Mining.
- Applications: Retail Industry, Marketing, CRM, Telecommunication Industry,
Financial Data Analysis, Risk Analysis, Fraud Detection,
Mobility and Transportation, Public Administration and Health.

## The Project

This year the dataset for the project is for some information extracted from the [FMA](https://freemusicarchive.org/) archive.

The data is both tabular and time series, also, having the audio file available, additional feature extraction was performed via liborsa.

The task to solve is to label each song with its genre. For further information I report below the guidelines of the project.

### Project Guidelines

1. **Module 1 - Introduction, Imbalanced Learning and Anomaly Detection**
    1. Explore and prepare the dataset. You are allowed to take inspiration from the associated         GitHub repository and figure out your personal research perspective (from choosing a subset of       variables to the class to predict…). You are welcome in creating new variables and performing all     the pre-processing steps the dataset needs.
    2. Define one or more (simple) classification tasks and solve it with Decision Tree and KNN. You decide the target variable.
    3. Identify the top 1% outliers: adopt at least three different methods from different families (e.g., density-based, angle-based… ) and compare the results. Deal with the outliers by removing them from the dataset or by treating the anomalous variables as missing values and employing replacement techniques. In this second case, you should check that the outliers are not outliers anymore. Justify your choices in every step.
    4. Analyze the value distribution of the class to predict with respect to point 2; if it is unbalanced leave it as it is, otherwise turn the dataset into an imbalanced version (e.g., 96% - 4%, for binary classification). Then solve the classification task using the Decision Tree or the KNN by adopting various techniques of imbalanced learning.
    5. Draw your conclusions about the techniques adopted in this analysis.

2. **Module 2 - Advanced Classification Methods**
    1. Solve the classification task defined in Module 1 (or define new ones) with the other classification methods analyzed during the course: Naive Bayes Classifier, Logistic Regression, Rule-based Classifiers, Support Vector Machines, Neural Networks, Ensemble Methods and evaluate each classifier with the techniques presented in Module 1 (accuracy, precision, recall, F1-score, ROC curve). Perform hyper-parameter tuning phases and justify your choices.
    2. Besides the numerical evaluation draw your conclusions about the various classifiers, e.g. for Neural Networks: what are the parameter sets or the convergence criteria which avoid overfitting? For Ensemble classifiers how the number of base models impacts the classification performance? For any classifier which is the minimum amount of data required to guarantee an acceptable level of performance? Is this level the same for any classifier? What is revealing the feature importance of Random Forests?
    3. Select two continuous attributes, define a regression problem and try to solve it using different techniques reporting various evaluation measures. Plot the two-dimensional dataset. Then generalize to multiple linear regression and observe how the performance varies.

3. **Module 3 - Time Series Analysis**
    1. Select the feature(s) you prefer and use it (them) as a time series. You can use the temporal information provided by the authors’ datasets, but you are also welcome in exploring the .mp3 files to build your own dataset of time series according to your purposes. You should prepare a dataset on which you can run time series clustering; motif/anomaly discovery and classification.
    2. On the dataset created, compute clustering based on Euclidean/Manhattan and DTW distances and compare the results. To perform the clustering you can choose among different distance functions and clustering algorithms. Remember that you can reduce the dimensionality through approximation. Analyze the clusters and highlight similarities and differences.
    3. Analyze the dataset for finding motifs and/or anomalies. Visualize and discuss them and their relationship with other features.
    4. Solve the classification task on the time series dataset(s) and evaluate each result. In particular, you should use shapelet-based classifiers. Analyze the shapelets retrieved and discuss if there are any similarities/differences with motifs and/or shapelets.

4. **Module 4 - Sequential Patterns and Advanced Clustering**
   1. Sequential Pattern Mining: Convert the time series into a discrete format (e.g., by using SAX) and extract the most frequent sequential patterns (of at least length 3/4) using different values of support, then discuss the most interesting sequences.
   2. Advanced Clustering: On a dataset already prepared for one of the previous tasks in Module 1 or Module 2, run at least one clustering algorithm presented in the advanced clustering lectures (e.g. X-Means, Bisecting K-Means, OPTICS). Discuss the results that you find analyzing the clusters and reporting external validation measures (e.g SSE, silhouette).
   3. Transactional Clustering: By using categorical features, or by turning a dataset with continuous variables into a dataset with categorical variables (e.g. by using binning), run at least two clustering algorithms presented in the transactional clustering lectures (e.g. CLOPE, ROCK). Discuss the results that you find analyzing the clusters and reporting external validation measures (e.g SSE, silhouette).

5. **Module 5 - Explainability (optional)**
   1. Try to use one or more explanation methods (e.g., LIME, LOR, SHAP, etc.) to illustrate the reasons for the classification in one of the steps of the previous tasks.

N.B. When “solving the classification task”, remember, (i) to test, when needed, different criteria for the parameter estimation of the algorithms, and (ii) to evaluate the classifiers (e.g., Accuracy, F1, Lift Chart) in order to compare the results obtained with an imbalanced technique against those obtained from using the “original” dataset.

### Altre note (in italian)

Per estrarre gli spettrogrammi ti potrebbero essere utili i notebook "Features Extraction TS" e "Prova con MEL spectrograms". L'unica cosa prova a rendere il primo notebook uno script e metti un ProcessPoolExecutor.

I vari notebook "Fase X.Y" contengono il codice per i vari task del progetto secondo le "Project Guidelines". Quelli con nomi in formato diverso sono vari esperimenti che (probabilmente) non sono finiti nel workflow finale

Tutti i dati che ho generato durante il progetto sono inclusi nella repo, ma compressi con 7z per il limite dell'upload massimo di 100mb/file. L'unica cosa che ti devi scaricare è il dataset delle canzoni
