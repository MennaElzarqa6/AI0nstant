#---------------------------------------------------------#
#                import needed libraries                  #
# --------------------------------------------------------#
# Import necessary libraries
# main libraries
import streamlit as st
import pandas as pd 
import numpy as np 

import os 
import pickle
import time 

# Visualization libraries
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('Agg')  # Use 'Agg' for non-GUI backend
# import seaborn as sns

# Pandas profiling for data analysis
import pandas_profiling as pdp
from streamlit_pandas_profiling import st_profile_report

# from ydata_profiling import ProfileReport

# PyCaret modules
from pycaret.classification import setup, compare_models, pull, save_model, tune_model, plot_model, load_model,evaluate_model, interpret_model, predict_model
from pycaret.regression import setup as reg_setup, compare_models as reg_compare_models,pull as reg_pull,save_model as reg_save_model, tune_model as reg_tune_model, plot_model as reg_plot_model, load_model as reg_load_model,evaluate_model as reg_evaluate_model, interpret_model as reg_interpret_model, predict_model as reg_predict_model
from pycaret.clustering import setup as clr_setup ,pull as clr_pull ,pull as clr_pull, save_model as clr_save_model,plot_model as clr_plot_model, load_model as clr_load_model, evaluate_model as clr_evaluate_model, create_model as clr_create_model, predict_model as clr_predict_model

import warnings
warnings.filterwarnings('ignore')

#---------------------------------------------------------#
# set page configuration & title
st.set_page_config(page_title= 'AutoML App', page_icon='D:\AI\AI instant Fire Gun\Tasks\ML modeling\AUTOML Streemlit\walle3.jpg')
st.title("👾 AUTOML APP")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

#---------------------------------------------------------#
#                set sidebar input parameters             #
# --------------------------------------------------------#
with st.sidebar:
    st.sidebar.title("Wall.E AUTOML APP")
    # st.header('sdfs',divider=True)
    st.image('walle2.jpg')
    choice = st.sidebar.selectbox("pick next step", ['Upload Dataset','Data Analysis','Modeling','Evaluation','Interpretation','plotting performance metrics','Download_model', 'Test'])
    st.sidebar.info("Automated Machine Learning development application")
    


# --------------- get data from exisiting file -----------#
if os.path.exists('data.csv'):
    df = pd.read_csv('data.csv', index_col=None)

# ------------------ upload data file --------------------#
if choice == 'Upload Dataset':
    file_uploaded = st.file_uploader("upload you dataset here[csv]",type=['csv'])
    if file_uploaded:
        df = pd.read_csv(file_uploaded, index_col=None)
        df.to_csv('data.csv',index=None) # save df in  csv file
        st.dataframe(df)  # Displays the df table
        
        st.balloons()  # Celebration balloons
# select model type 
st.info("select model type")
model_selection = st.selectbox("select model",['Regression','Classification','Clustering'])

# ------------------ Data Analysis ----------------------#
if choice == 'Data Analysis':
    st.progress(26)  # Progress bar
    with st.spinner('Wait for it...'):
        time.sleep(10)  # Simulating a process delay
    st.title("Exploratory Data Analysis")
    profile_report = df.profile_report()
    st_profile_report(profile_report)
    st.balloons()  # Celebration balloons

# -----------------------------------------------------#
# # Function to render manual tuning options in the sidebar
# def manual_tuning(BM, model_params):
#     param_inputs = {}
    
#     for param, default_value in model_params.items():
#         if isinstance(default_value, int):
#             param_inputs[param] = st.sidebar.number_input(f'{param}', value=default_value)
#         elif isinstance(default_value, float):
#             param_inputs[param] = st.sidebar.number_input(f'{param}', value=default_value, format="%.4f")
#         elif isinstance(default_value, str):
#             param_inputs[param] = st.sidebar.text_input(f'{param}', value=default_value)
#         elif isinstance(default_value, bool):
#             param_inputs[param] = st.sidebar.checkbox(f'{param}', value=default_value)
#         # You can add more types as needed (like lists for dropdowns)
    
#     return param_inputs
# ------------------ Modelling ------------------------#
if choice =='Modeling':
    target = st.selectbox("Choose [target column] for Classificatin or Regression || [No target] for classification", ["Select a target column"] + list(df.columns) +  ["No target"])
    if target == "Select a target column":
        st.error("Please select a target column for modeling.")
    elif target =='No target':
        # init 
        clr_setup(df,normalize=True)
        setup_df = clr_pull()
        # Show setup settings
        st.info('Setup settings:')
        st.dataframe(setup_df)

        # Create and train a clustering model (manually choose models to evaluate)
        model_list = ['kmeans', 'hclust', 'dbscan', 'optics']  # Example model options 'ap','meanshift','sc','birch','kmodes'
        clustering_models = {}
        for model in model_list:
            clustering_models[model] = clr_create_model(model=model)
        
        # Display results of each model
        result = clr_pull() # Pull model results after creation
        st.info('Model Results:')
        st.dataframe(result)
        # Save the best clustering model (you'll need to manually select or choose the best based on evaluation)
        BM = st.sidebar.selectbox("Select best_model", model_list)
        best_model = clustering_models[BM]
        clr_save_model(best_model,'best_model_clustering')


        # Select clustering model
        st.header('Manual Tuning for the Selected Model')
        model_name = st.selectbox("Select Clustering Model", ("KMeans", "Hierarchical", "DBSCAN", "OPTICS"))
        # Provide model selection for manual tuning
        if model_name == 'KMeans':
            # KMeans Parameters
            num_clusters = st.slider("Select Number of Clusters", min_value=2, max_value=10, value=3)
            model = clr_create_model('kmeans', num_clusters=num_clusters)

        elif model_name == 'Hierarchical':
            # Hierarchical Parameters
            model = clr_create_model('hclust')

        elif model_name == 'DBSCAN':
            # DBSCAN Parameters
            eps = st.number_input("Select Epsilon (eps)", min_value=0.0, value=0.5, step=0.1)
            min_samples = st.slider("Select Minimum Samples", min_value=1, max_value=10, value=5)
            model = clr_create_model('dbscan', eps=eps, min_samples=min_samples)

        elif model_name == 'OPTICS':
            # OPTICS Parameters
            min_samples_optics = st.slider("Select Minimum Samples", min_value=1, max_value=10, value=5)
            max_eps = st.number_input("Select Maximum Epsilon (max_eps)", min_value=0.0, value=0.5, step=0.1)
            model = clr_create_model('optics', min_samples=min_samples_optics, max_eps=max_eps)

        # Display the created model
        st.write(f"### Created {model_name} Model")
        st.write(model)     
        # Predict clusters on the original data
        clustered_data = clr_predict_model(model,data= df)

        # Display the clustered data
        st.write("### Clustered Data")
        st.write(clustered_data)

    else:
        # set select box for modelling type 
        # with st.sidebar:
        #     model_selection = st.sidebar.selectbox("select model",['Regression','Classification'])
        # Setup the model based on selection
        if model_selection == 'Regression':
            # init
            reg_setup(df, target=target)
            setup_df = reg_pull()
            st.info("Setup settings: ")
            st.dataframe(setup_df)

            # modelling and training
            best_model = reg_compare_models()
            result = reg_pull()
            st.info("Models: ")
            st.dataframe(result)

            # Save the regression model
            reg_save_model(best_model, "best_model_regressor") 

            # Tune the selected model
            tuned_model = reg_tune_model(best_model)
            st.info('Tuned Model:')
            st.write(tuned_model) 

            # Save the tuned regression model
            reg_save_model(tuned_model, "best_model_regressor_tuned")

        elif model_selection == 'Classification':
            # init
            setup(df, target=target)
            setup_df = pull()
            st.info("Setup settings: ")
            st.dataframe(setup_df)

            # model and train
            best_model = compare_models()
            result = pull()
            st.info("Models: ")
            st.dataframe(result)

            # Save the classification model
            save_model(best_model, "best_model_classifier") # Save the regression model

            # Tune the selected model
            tuned_model = tune_model(best_model)
            st.info('Tuned Model:')
            st.write(tuned_model) 

            # Save the tuned regression model
            save_model(tuned_model, "best_model_classification_tuned")
            
#------------------------------------------------------------#
#------------------ plotting Model metrics-------------------#
if choice == 'plotting performance metrics':
    # Select model type to plot
    # model_type = st.sidebar.selectbox("Select model type for plotting", ['Regression', 'Classification','Clustering'])

    # Load the saved model
    if model_selection == 'Regression':
        model_name = "best_model_regressor"

        # Load the model using PyCaret's load_model
        model = reg_load_model(model_name) 

        # Plot the best model
        plot_type = st.sidebar.selectbox("Select plot type",['residuals', 'error', 'cooks', 'rfe',
                                                             'learning', 'vc', 'manifold', 'feature',
                                                             'feature_all', 'parameter'])

        # Generate the plot
        fig = reg_plot_model(model, plot=plot_type,save=True)  # plot and save figure.
        st.image(fig) # Display image in streamlit platform

    elif model_selection == 'Classification':
        model_name = "best_model_classifier"

        # Load the model using PyCaret's load_model
        model = load_model(model_name) 

        # Plot the best model
        plot_type = st.sidebar.selectbox("Select plot type",['auc', 'threshold', 'pr', 'confusion_matrix',
                                                                           'error', 'class_report', 'boundary', 'rfe', 'learning',
                                                                            'manifold', 'calibration', 'vc', 'dimension', 'feature',
                                                                            'feature_all', 'parameter', 'lift', 'gain', 'ks'])
        # Generate the plot
        fig =plot_model(model, plot=plot_type,save=True)  # Plot the model without automatic display
        st.image(fig) # show image in streamlit 

    elif model_selection == 'Clustering':
        
        model_name = "best_model_clustering"
        # Load the model using PyCaret's load_model
        model = clr_load_model(model_name) 

        # Plot the best model
        plot_type = st.sidebar.selectbox("Select plot type",['cluster','tsne','elbow','silhouette','distance','distribution'])
        
        # Generate the plot
        # Save the plot to a file and display in Streamlit
        fig = clr_plot_model(model, plot=plot_type,save=True)  # plot and save figure
        st.image(fig)

#----------------------------------------------------------#
#------------------ Evaluating the Model-------------------#
if choice == 'Evaluation':
    if model_selection == 'Regression':
        model_name = "best_model_regressor"
        # Load the model using PyCaret's load_model
        model = reg_load_model(model_name) 
        # Evaluate the model
        reg_evaluate_model(model)  
        eval = reg_pull()
        st.info('Model Evaluation')
        st.write(eval)
        
    elif model_selection == 'Classification':
        model_name = "best_model_classifier"
        # Load the model using PyCaret's load_model
        model = load_model(model_name) 
        # Evaluate the model
        evaluate_model(model)  
        eval = pull()
        st.info('Model Evaluation')
        st.write(eval)
    elif model_selection == 'Clustering':
        model_name = "best_model_clustering"
        # Load the model using PyCaret's load_model
        model = clr_load_model(model_name) 
        # Evaluate the model
        clr_evaluate_model(model) 
        eval = clr_pull()
        st.info('Model Evaluation')
        st.write(eval) 
#----------------------------------------------------------#
#------------------ Interpret the Model-------------------#
if choice == 'Interpretation':
    plot_type = st.sidebar.selectbox('select plot type',['correlation','pdp','msa','pfi','reason'])
    if model_selection == 'Regression':
        model_name = "best_model_regressor"
        # Load the model using PyCaret's load_model
        model = reg_load_model(model_name) 
        # Evaluate the model
        reg_interpret_model(model, plot=plot_type)  
        
    elif model_selection == 'Classification':
        model_name = "best_model_classifier"
        # Load the model using PyCaret's load_model
        model = load_model(model_name) 
        # Evaluate the model
        interpret_model(model,plot_type=plot_type)  
    elif model_selection =='Clustering':
        st.warning("there is no interpretation availabele for Clustering as we are using pycaret automl library ;(")

#--------------------Model downloading-------------------#
if choice == 'Download_model':
    with open("best_model.pkl","rb") as f :
        st.download_button("Download Model", f, file_name="trained_model")

#------------------ Testing the Model-------------------#
if choice == 'Test':
    st.info('Testing Models on New Data')
    # Ask the user to upload the new test data
    uploaded_file = st.file_uploader("Upload New Test Data (CSV)", type=["csv"])

    if uploaded_file is not None:
        # Read the uploaded CSV file into a DataFrame
        new_data = pd.read_csv(uploaded_file)

        if model_selection == 'Regression':
            st.subheader("Regression Models Testing")
            # Load the trained regression model
            model = load_model('best_regression_model')  # Replace with your saved model's name
            # Make predictions on the new data
            predictions = reg_predict_model(model, data=new_data)
            # Display predictions
            st.write(predictions)

        elif model_selection == 'Classification':
            st.subheader("Classification Models Testing")
            # Load the trained classification model
            model = load_model('best_classification_model')  # Replace with your saved model's name
            # Make predictions on the new data
            predictions = predict_model(model, data=new_data)

            # Display predictions
            st.write(predictions)

        elif model_selection == 'Clustering':
            st.subheader("Clustering Models Testing")
            # Load the trained clustering model
            model = load_model('best_model_clustering')  # Replace with your saved model's name
            # Predict cluster assignments for the new data
            clusters = clr_predict_model(model, data=new_data)
            
            # Display cluster assignments
            st.write(clusters)

    else:
        st.warning("Please upload a CSV file to proceed.")