# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:29:38 2024
Enhanced Credit Risk Modeling Application

@author: Admin
"""

import streamlit as st
from utils import predict

# Set the page configuration and title with enhanced styling
st.set_page_config(
    page_title="OPTI RECOURSE", 
    page_icon="💰", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    /* Main header styling */
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Section headers */
    .section-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1.5rem 0 1rem 0;
        text-align: center;
        font-weight: bold;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    /* Metric cards styling */
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Sidebar styling */
    .sidebar-content {
        background: linear-gradient(180deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1rem;
        border-radius: 15px;
        margin-bottom: 1rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(79, 172, 254, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(79, 172, 254, 0.4);
    }
    
    /* Results styling */
    .results-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }
    
    /* Input field styling */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > div,
    .stSlider > div > div > div {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        transition: border-color 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > div:focus {
        border-color: #4facfe;
        box-shadow: 0 0 0 0.2rem rgba(79, 172, 254, 0.25);
    }
    
    /* Warning and success styling */
    .custom-warning {
        background: linear-gradient(90deg, #ff9a9e 0%, #fecfef 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #ff6b6b;
        margin: 1rem 0;
    }
    
    .custom-success {
        background: linear-gradient(90deg, #a8edea 0%, #fed6e3 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #51cf66;
        margin: 1rem 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Main header with enhanced styling
st.markdown("""
<div class="main-header">
    <h1>💰OPTI RECOURSE💰</h1>
    <p style="font-size: 1.2rem; margin-top: 0.5rem;"> 💰Advanced AI-Powered Credit Assessment Tool💰</p>
</div>
""", unsafe_allow_html=True)

# Enhanced Sidebar with better styling
with st.sidebar:
    st.markdown("""
    <div class="sidebar-content">
        <h2 style="color: #333; text-align: center; margin-bottom: 1rem;">📋 Instructions</h2>
        <div style="background: white; padding: 1rem; border-radius: 10px; margin: 1rem 0;">
            <ol style="color: #333; padding-left: 1.2rem;">
                <li style="margin-bottom: 0.5rem;">Fill in all required customer details</li>
                <li style="margin-bottom: 0.5rem;">Adjust sliders and dropdowns carefully</li>
                <li style="margin-bottom: 0.5rem;">Review all inputs before calculation</li>
                <li style="margin-bottom: 0.5rem;">Click 'Calculate Risk' for assessment</li>
            </ol>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Try to display logo with error handling
    try:
        st.image("project-root/logo.png", caption="Your Trusted Finance Partner", width=200)
    except:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%); 
                    color: white; padding: 2rem; border-radius: 15px; text-align: center;">
            <h3>🏦</h3>
            <p>Your Trusted Finance Partner</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Additional sidebar info
    st.markdown("""
    <div style="background: linear-gradient(135deg, #fd79a8 0%, #e84393 100%); 
                color: white; padding: 1.5rem; border-radius: 15px; margin-top: 2rem; text-align: center;">
        <h4>💡 Pro Tips</h4>
        <p style="font-size: 0.9rem;">Accurate information leads to better risk assessment</p>
    </div>
    """, unsafe_allow_html=True)

# Main content area with enhanced sections
col_main1, col_main2 = st.columns([3, 1])

with col_main1:
    # Customer Details Section
    st.markdown('<div class="section-header">💼 Customer Profile Information</div>', unsafe_allow_html=True)
    
    # Row 1: Basic Information
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("🎂 Age", min_value=18, max_value=100, value=28, 
                             help="Enter customer's age (18-100 years)")
    
    with col2:
        income = st.number_input("💵 Annual Income", min_value=0, max_value=5000000, 
                               value=290875, step=50000, 
                               help="Annual income in your local currency")
    
    with col3:
        loan_amount = st.number_input("🏦 Loan Amount", min_value=0, value=2560000, 
                                    help="Total loan amount requested")

    # Loan-to-Income Ratio Display
    st.markdown('<div class="section-header">📊 Financial Ratio Analysis</div>', unsafe_allow_html=True)
    
    lti = loan_amount / income if income > 0 else 0
    
    col_ratio1, col_ratio2, col_ratio3 = st.columns(3)
    
    with col_ratio1:
        st.metric(label="💹 Loan-to-Income Ratio", value=f"{lti:.2f}", 
                 delta=f"{'High Risk' if lti > 5 else 'Moderate Risk' if lti > 3 else 'Low Risk'}")
    
    with col_ratio2:
        risk_indicator = "🔴 High" if lti > 5 else "🟡 Medium" if lti > 3 else "🟢 Low"
        st.metric(label="🎯 Risk Level", value=risk_indicator)
    
    with col_ratio3:
        affordability = f"{(income/12/loan_amount*100):.1f}%" if loan_amount > 0 else "N/A"
        st.metric(label="💰 Monthly Affordability", value=affordability)

    # Loan Details Section
    st.markdown('<div class="section-header">📑 Loan Configuration Details</div>', unsafe_allow_html=True)
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        loan_tenure_months = st.slider("📅 Loan Tenure (Months)", min_value=6, max_value=240, 
                                     step=6, value=36, help="Select loan duration in months")
    
    with col5:
        avg_dpd_per_dm = st.number_input("⚠️ Average DPD", min_value=0, value=0, 
                                       help="Average Days Past Due (0 for new customers)")
    
    with col6:
        dmtlm = st.slider("📈 DMTLM Ratio (%)", min_value=0, max_value=100, value=0, 
                        help="Delinquent Months to Loan Months ratio")

    # Credit and Loan History
    st.markdown('<div class="section-header">🏦 Credit History & Loan Purpose</div>', unsafe_allow_html=True)
    
    col7, col8, col9 = st.columns(3)
    
    with col7:
        credit_utilization_ratio = st.slider("💳 Credit Utilization (%)", min_value=0, max_value=100, 
                                           value=0, help="Percentage of credit limit used")
    
    with col8:
        total_loan_months = st.number_input("📊 Total Loan History (Months)", min_value=0, value=0, 
                                          help="Total months across all previous loans")
    
    with col9:
        loan_purpose = st.selectbox("🎯 Loan Purpose", 
                                  ['Education', 'Home', 'Auto', 'Personal'], 
                                  help="Primary purpose of the loan")

    # Loan and Residence Type
    st.markdown('<div class="section-header">🏠 Loan & Residence Classification</div>', unsafe_allow_html=True)
    
    col10, col11 = st.columns(2)
    
    with col10:
        loan_type = st.radio("🔒 Loan Security Type", ['Unsecured', 'Secured'], 
                           help="Whether the loan is backed by collateral")
    
    with col11:
        residence_type = st.selectbox("🏡 Residence Status", 
                                    ['Owned', 'Rented', 'Mortgage'], 
                                    help="Current living situation")

# Right sidebar for additional information
with col_main2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); 
                padding: 1.5rem; border-radius: 15px; margin-top: 2rem;">
        <h4 style="color: #333; text-align: center;">📊 Assessment Criteria</h4>
        <div style="background: white; padding: 1rem; border-radius: 10px; margin: 1rem 0;">
            <p style="color: #333; font-size: 0.9rem; margin-bottom: 0.5rem;"><strong>Credit Score Range:</strong></p>
            <p style="color: #333; font-size: 0.8rem; margin: 0.2rem 0;">🟢 Excellent: 750-850</p>
            <p style="color: #333; font-size: 0.8rem; margin: 0.2rem 0;">🟡 Good: 650-749</p>
            <p style="color: #333; font-size: 0.8rem; margin: 0.2rem 0;">🟠 Fair: 550-649</p>
            <p style="color: #333; font-size: 0.8rem; margin: 0.2rem 0;">🔴 Poor: Below 550</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%); 
                padding: 1.5rem; border-radius: 15px; margin-top: 1rem;">
        <h4 style="color: #333; text-align: center;">⚡ Quick Facts</h4>
        <div style="background: white; padding: 1rem; border-radius: 10px;">
            <p style="color: #333; font-size: 0.85rem;">Lower DPD = Better Score</p>
            <p style="color: #333; font-size: 0.85rem;">LTI Ratio < 3 = Preferred</p>
            <p style="color: #333; font-size: 0.85rem;">Credit Utilization < 30%</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Enhanced Action Button
st.markdown("<br>", unsafe_allow_html=True)
col_button = st.columns([2, 1, 2])

with col_button[1]:
    calculate_button = st.button("🚀 Calculate Credit Risk", use_container_width=True)

# Results Section with Enhanced Styling
if calculate_button:
    with st.spinner('🔄 Analyzing credit profile...'):
        # Call the predict function
        probability, credit_score, rating = predict(age, avg_dpd_per_dm, credit_utilization_ratio, dmtlm, income,
                                                  loan_amount, loan_tenure_months, total_loan_months,
                                                  loan_purpose, loan_type, residence_type)
    
    # Enhanced Results Display
    st.markdown("""
    <div class="results-container">
        <h2 style="text-align: center; margin-bottom: 2rem;">📊 Credit Risk Assessment Results</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Results metrics in columns
    result_col1, result_col2, result_col3 = st.columns(3)
    
    with result_col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ff7675 0%, #fd79a8 100%); 
                    color: white; padding: 2rem; border-radius: 15px; text-align: center;">
            <h3>⚡ Default Risk</h3>
            <h1>{probability:.2%}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with result_col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #00b894 0%, #00cec9 100%); 
                    color: white; padding: 2rem; border-radius: 15px; text-align: center;">
            <h3>🎯 Credit Score</h3>
            <h1>{credit_score}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with result_col3:
        rating_color = "#e17055" if rating in ['Poor', 'Average'] else "#00b894"
        rating_emoji = "🔴" if rating in ['Poor', 'Average'] else "🟢"
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {rating_color}aa 0%, {rating_color} 100%); 
                    color: white; padding: 2rem; border-radius: 15px; text-align: center;">
            <h3>{rating_emoji} Rating</h3>
            <h1>{rating}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    # Enhanced Risk Insights
    st.markdown("<br>", unsafe_allow_html=True)
    
    if rating in ['Poor', 'Average']:
        st.markdown("""
        <div class="custom-warning">
            <h3>⚠️ High Risk Profile Detected</h3>
            <p><strong>Recommendation:</strong> This borrower presents elevated risk factors. Consider:</p>
            <ul>
                <li>Additional documentation requirements</li>
                <li>Higher interest rates or collateral</li>
                <li>Credit improvement guidance</li>
                <li>Shortened loan tenure options</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="custom-success">
            <h3>🌟 Low Risk Profile - Excellent Candidate</h3>
            <p><strong>Recommendation:</strong> This borrower shows strong creditworthiness:</p>
            <ul>
                <li>Loan approval highly recommended</li>
                <li>Competitive interest rates applicable</li>
                <li>Consider premium service offerings</li>
                <li>Potential for higher loan amounts</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Additional insights
    st.markdown("""
    <div style="background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%); 
                color: white; padding: 1.5rem; border-radius: 15px; margin: 2rem 0;">
        <h3 style="text-align: center;">🔍 Detailed Analysis Summary</h3>
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin-top: 1rem;">
            <p><strong>Assessment Date:</strong> Generated using advanced machine learning models</p>
            <p><strong>Confidence Level:</strong> High accuracy based on comprehensive data analysis</p>
            <p><strong>Next Steps:</strong> Review additional documentation and finalize loan terms</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%); 
            color: white; padding: 2rem; border-radius: 15px; margin-top: 3rem; text-align: center;">
    <h4>🚀 Advanced Credit Risk Modeling Platform</h4>
    <p>By - Rakshit Jain | Secure & Reliable | Real-time Analysis</p>
</div>
""", unsafe_allow_html=True)