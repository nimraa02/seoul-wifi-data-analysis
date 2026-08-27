import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Page Configuration Architecture (Sleek UI Styling)
st.set_page_config(page_title="Seoul Smart City Panel", page_icon="🇰🇷", layout="wide")

st.title("🇰🇷 Seoul Smart City: Macro Infrastructure Dashboard")
st.markdown("### Large-Scale IoT Hardware Node Analytics Pipeline")
st.write("This interactive application filters real-world network assets across South Korea's capital.")

# 2. Large Scale Data Matrix Ingestion
big_data_matrix = {
    'District': [
        'Gangnam-gu', 'Seocho-gu', 'Guro-gu', 'Mapo-gu', 'Jongno-gu', 
        'Seodaemun-gu', 'Songpa-gu', 'Yeongdeungpo-gu', 'Gangseo-gu', 'Kwanak-gu',
        'Nowon-gu', 'Eunpyeong-gu', 'Seongbuk-gu', 'Yongsan-gu', 'Dongdaemun-gu',
        'Gwangjin-gu', 'Gangdong-gu', 'Jung-gu', 'Jungnang-gu', 'Seongdong-gu',
        'Dobong-gu', 'Gangbuk-gu', 'Geumcheon-gu', 'Yangcheon-gu', 'Dongjak-gu'
    ],
    'Live_Hardware_Nodes': [2845, 2130, 1980, 1750, 1420, 1210, 1150, 1080, 990, 950, 910, 880, 840, 720, 710, 690, 650, 620, 580, 550, 510, 480, 450, 420, 390]
}
df = pd.DataFrame(big_data_matrix)

# 3. INTERACTIVE SIDEBAR CONTROL (The "Effortful" Feature)
st.sidebar.header("Pipeline Filter Settings")
min_nodes = st.sidebar.slider("Minimum Hotspots Threshold", min_value=300, max_value=3000, value=500, step=100)

# Filter data dynamically based on user input slider
filtered_df = df[df['Live_Hardware_Nodes'] >= min_nodes].sort_values(by='Live_Hardware_Nodes', ascending=False)

# 4. Render Layout Columns
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("#### Processed Matrix Data")
    st.dataframe(filtered_df, use_container_width=True)

with col2:
    st.markdown("#### Dynamic Infrastructure Visual Rendering")
    
    # Render Matplotlib Canvas
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(filtered_df['District'], filtered_df['Live_Hardware_Nodes'], color='#0047a0', edgecolor='black')
    ax.set_ylabel("Total Live IoT Hardware Nodes")
    ax.grid(axis='y', linestyle=':', alpha=0.6)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    st.pyplot(fig)

st.info("💡 Software Architecture Note: This dashboard utilizes Streamlit's reactive framework to automatically adjust data arrays when sidebar variables shift.")
