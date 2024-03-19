import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

custom_css = """
<style>
/* Change background color to light gray */
body {
    background-color: #ffff; /* Light gray */
}

/* Change text color to dark gray */
div[data-testid="stTextInput"] > div > div > input {
    color: #333; /* Dark gray */
}

/* Change button color to light blue */
.stButton>button {
    background-color: #007bff; /* Light blue */
    color: white; /* White text */
}

/* Change sidebar color */
[data-testid="stSidebar"] {
    background-color: #87e9ff; /* White */
}

/* Change sidebar text color */
.css-17x50n7 {
    color: #000; /* Dark gray */
}
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)
st.title("Total Budget Revenue")

ye ,pr ,dis = st.columns(3)

with ye:
    df_la = pd.read_excel("la.xlsx")
    selected_year = st.selectbox('Select a budget_year',["2023","2024"])
with pr:
    selected_province = st.selectbox('Select a Province', df_la['province'].unique())

with dis:
    df_la = df_la[df_la['province'] == selected_province]
    selected_district = st.selectbox('Select a district', df_la['district'].unique())


st.markdown("""
<style>

.metric-container {
    text-align: center;
    width: 100%;
    max-width: 300px;
    border: 1px solid black;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 10px;
}

.metric-label {
    font-weight: bold;
}

.budgeted {
    background-color:#308ed1; 
}

.actual {
    background-color: #57d8ff; 
}

.percentage {
    background-color: #8fc9f2; 
}

</style>
""", unsafe_allow_html=True)

col = st.columns((0.6, 2, 2, 2, 2, 2), gap='small')
with col[0]:
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown("#### MC")
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown("#### UC")
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown("#### PS")
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown("#### TOTAL")

with col[1]:
    st.markdown('<div class="metric-container budgeted"><div class="metric-label">Budgeted</div>45</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container budgeted"><div class="metric-label">Budgeted</div>45</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container budgeted"><div class="metric-label">Budgeted</div>45</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container budgeted"><div class="metric-label">Budgeted</div>45</div>', unsafe_allow_html=True)

with col[2]:
    st.markdown('<div class="metric-container actual"><div class="metric-label">Actual this Month</div>45</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container actual"><div class="metric-label">Actual this Month</div>45</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container actual"><div class="metric-label">Actual this Month</div>45</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container actual"><div class="metric-label">Actual this Month</div>45</div>', unsafe_allow_html=True)

with col[3]:
    st.markdown('<div class="metric-container percentage"><div class="metric-label">Percentage</div>45%</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container percentage"><div class="metric-label">Percentage</div>45%</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container percentage"><div class="metric-label">Percentage</div>45%</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container percentage"><div class="metric-label">Percentage</div>45%</div>', unsafe_allow_html=True)

with col[4]:
    st.markdown('<div class="metric-container actual"><div class="metric-label">Actual up to</div>45</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container actual"><div class="metric-label">Actual up to</div>45</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container actual"><div class="metric-label">Actual up to</div>45</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container actual"><div class="metric-label">Actual up to</div>45</div>', unsafe_allow_html=True)

with col[5]:
    st.markdown('<div class="metric-container percentage"><div class="metric-label">Percentage</div>45%</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container percentage"><div class="metric-label">Percentage</div>45%</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container percentage"><div class="metric-label">Percentage</div>45%</div>', unsafe_allow_html=True)
    st.markdown('<div class="metric-container percentage"><div class="metric-label">Percentage</div>45%</div>', unsafe_allow_html=True)

col11, col12 = st.columns(2)
file_path = 'SampleAnalytics-DashboardLoGoMISv2.xlsx'
sheet_name = 'test2'
df = pd.read_excel(file_path, sheet_name=sheet_name)

def create_horizontal_bar_chart(data):
    """
    Create a horizontal bar chart using Plotly.

    Args:
        data (dict): Dictionary containing 'Category' and 'Value' keys.

    Returns:
        plotly.graph_objects.Figure: Plotly figure object.
    """
    # Define a list of blue colors
    blue_colors = ['#1f77b4', '#aec7e8', '#7fbfff', '#1a65ac']

    fig = go.Figure(go.Bar(
        x=data['Value'],
        y=data['Category'],
        orientation='h',
        marker=dict(color=blue_colors)
    ))

    # Customize the layout
    fig.update_layout(
        title='Horizontal Bar Chart',
        xaxis_title='Value',
        yaxis_title='Category',
        yaxis=dict(autorange="reversed"),  # Reverse the category order
        plot_bgcolor='rgba(219, 240, 255, 1)' # Set background color
    )

    return fig

# Data for the bar chart
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [40, 30, 20, 10]
}

# Create the horizontal bar chart
fig = create_horizontal_bar_chart(data)
with col11:
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; margin-left: 10%; margin-right: 25%;'>District Details</h4>", unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.write(df.iloc[0:1])
    st.markdown('<br>', unsafe_allow_html=True)
    st.write(df.iloc[2:5])
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.write(df.iloc[0:1])
    st.markdown('<br>', unsafe_allow_html=True)
    st.write(df.iloc[2:5])

with col12:
    st.markdown('<br>', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.plotly_chart(fig, use_container_width=True)
