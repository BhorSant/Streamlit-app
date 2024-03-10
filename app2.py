import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Include custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")
# add title
st.title("Data Analysis Application")
st.subheader("This is a simple app created by @BhorSant")

# create a dropdown list to choose dataset
dataset_names = ["Iris", "Tips", "Diamonds"]
dataset = st.sidebar.selectbox("Select Dataset", dataset_names)

# load the selected dataset
try:
    if dataset.lower() == "iris":
        df = sns.load_dataset("iris")
    elif dataset.lower() == "tips":
        df = sns.load_dataset("tips")
    elif dataset.lower() == "diamonds":
        df = sns.load_dataset("diamonds")
except Exception as e:
    st.error(f"Error loading dataset: {e}")

# button to upload custom dataset
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
    except Exception as e:
        st.error(f"Error: {e}")

# display the dataset preview
st.markdown("**Data Preview**", unsafe_allow_html=True)
st.write(df.head())

# display data summary
st.markdown("**Data Summary**", unsafe_allow_html=True)
st.write(df.describe())

# display the columns name and data type
st.markdown("**Columns and Datatypes**", unsafe_allow_html=True)
st.write(df.dtypes)

# Check the null values 
st.markdown("**Null Values**", unsafe_allow_html=True)
st.write(df.isnull().sum())

# display different types of plots using sidebar 
st.sidebar.markdown("**Plots**", unsafe_allow_html=True)
plot_type = st.sidebar.selectbox("Select Plot Type", ["Scatter", "Line", "Bar", "Histogram", "Pie"])

if plot_type == "Scatter":
    st.subheader("Scatter Plot")
    x = st.selectbox("Select X Variable", df.columns)
    y = st.selectbox("Select Y Variable", df.columns)
    fig = sns.scatterplot(data=df, x=x, y=y)
    plt.savefig("scatter_plot.png")  # Save the figure
    st.image("scatter_plot.png")     # Display the saved image

elif plot_type == "Line":
    st.subheader("Line Plot")
    x = st.selectbox("Select X Variable", df.columns)
    y = st.selectbox("Select Y Variable", df.columns)
    fig = sns.lineplot(data=df, x=x, y=y)
    plt.savefig("line_plot.png")     # Save the figure
    st.image("line_plot.png")        # Display the saved image

elif plot_type == "Bar":
    st.subheader("Bar Plot")
    x = st.selectbox("Select X Variable", df.columns)
    y = st.selectbox("Select Y Variable", df.columns)
    fig = sns.barplot(data=df, x=x, y=y)
    plt.savefig("bar_plot.png")      # Save the figure
    st.image("bar_plot.png")         # Display the saved image

elif plot_type == "Histogram":
    st.subheader("Histogram")
    x = st.selectbox("Select Variable", df.columns)
    fig = sns.histplot(data=df, x=x)
    plt.savefig("histogram.png")     # Save the figure
    st.image("histogram.png")        # Display the saved image

elif plot_type == "Pie":
    st.subheader("Pie Plot")
    x = st.selectbox("Select Variable", df.columns)
    fig = sns.countplot(data=df, x=x)
    plt.savefig("pie_plot.png")      # Save the figure
    st.image("pie_plot.png")         # Display the saved image

# create a pairplot
st.subheader("Pair Plot")
fig = sns.pairplot(df)
st.pyplot(fig)
# themes change and used unique theme
st.set_option('deprecation.showPyplotGlobalUse', False)
