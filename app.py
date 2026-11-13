import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  # <--- Make sure this line is included at the top!
import plotly.express as px
import numpy as np
st.set_page_config(page_title = "Drive Eco",
                   page_icon = '🚗',
                   layout='wide')
                  

st.title (":green[Drive Eco]")
st.image ("/Users/bharatsingh/Downloads/images.jpeg")
st.write (":blue[!! Welcome to Drive Eco! Choose your next Ride Wisely and Responsibly. !!]")



st.write (":green[## Drive Eco is a platform that aims to provide insights into the European Electric Vehicle (EV) market, focusing on the environmental impact of transportation and the evolution of EVs in Europe. The platform offers data visualizations and filtering options to help users explore various aspects of EVs, including their contribution to reducing greenhouse gas emissions. ##]")
###################################
# Understanding European land mass and population density.

st.markdown("## :violet[Understanding Europe in Mass]")

st.write (":orange[First lets try to understand the contintent with respect to the land mass and the population density.]")


# Ploting European Land Mass


st.set_page_config(page_title="EU Country Land Area Map", layout="wide")

st.markdown("<h2 style='color: #8A2BE2;'>🌍 European Countries by Land Area</h2>", unsafe_allow_html=True)
st.subheader("Interactive Choropleth Map of Europe showing Land Area (km²)")
@st.cache_data
def load_data():
    df = pd.read_csv('/Users/bharatsingh/Downloads/EV-Project/cleaned_data/europe_land_mass.csv')
    return df

df = load_data()

# 2. Generate Interactive Map
fig = px.choropleth(
    df,
    locations='country',
    locationmode='country names',
    color='land_area_km2',
    hover_name='country',
    hover_data={'land_area_km2': ':,'},  # Format with thousands comma separator
    color_continuous_scale='Viridis',
    labels={'land_area_km2': 'Land Area (km²)'},
    title='European Land Area (km²)'
)

# 3. Focus Map Specifically on Europe
fig.update_geos(
    scope='europe',
    showcountries=True,
    countrycolor="LightGray",
    showcoastlines=True,
    coastlinecolor="Black",
    showland=True,
    landcolor="whitesmoke"
)

fig.update_layout(
    height=700,
    margin={"r": 0, "t": 40, "l": 0, "b": 0}
)

# 4. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Data Table Expander with 1-to-N indexing
with st.expander("📋 View Data Table"):
    display_df = df.copy().reset_index(drop=True)
    display_df.index = display_df.index + 1
    st.dataframe(display_df, use_container_width=True)

#Understanding European Population by Country


st.markdown("## :violet[Understanding Europe Population]")

st.set_page_config(page_title="EU Country Land Area Map", layout="wide")

st.markdown("<h2 style='color: #8A2BE2;'>🌍 Population Density in European Countries</h2>", unsafe_allow_html=True)
st.subheader("Interactive Choropleth Map of Europe showing Total Population in a Country")
@st.cache_data
def load_data():
    df_1 = pd.read_csv('/Users/bharatsingh/Downloads/EV-Project/cleaned_data/europe_population_country.csv')
    return df_1

df_1 = load_data()

# 2. Generate Interactive Map
fig = px.choropleth(
    df_1,
    locations='country',
    locationmode='country names',
    color='population',
    hover_name='country',
    hover_data={'population': ':,'},  # Format with thousands comma separator
    color_continuous_scale='Viridis',
    labels={'population': 'Population Density'},
    title='European Population Density'
)

# 3. Focus Map Specifically on Europe
fig.update_geos(
    scope='europe',
    showcountries=True,
    countrycolor="LightGray",
    showcoastlines=True,
    coastlinecolor="Black",
    showland=True,
    landcolor="whitesmoke"
)

fig.update_layout(
    height=700,
    margin={"r": 0, "t": 40, "l": 0, "b": 0}
)

# 4. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Data Table Expander with 1-to-N indexing
with st.expander("📋 View Data Table"):
    display_df = df_1.copy().reset_index(drop=True)
    display_df.index = display_df.index + 1
    st.dataframe(display_df, use_container_width=True)

###################################
# Various Sectors contributing to greenhouse gas emissions in Europe.

st.markdown ("## :red[Contribution by sectors towards Greenhouse Gas Emissions in Europe.]")
st.write (":grey[Understanding the contribution of different sectors towards Greenhouse Gas Emissions in Europe is crucial to understand the impact on nature and make a right decision]")
eu_emission_contribution = pd.read_csv("/Users/bharatsingh/Downloads/EV-Project/cleaned_data/emission_contribution_sector.csv")
st.title (":red[EU Greenhouse Gas Emission]")
st.subheader ("Emission by major sectors")
st.dataframe(eu_emission_contribution)

fig = px.pie(eu_emission_contribution, values = 'Approximate Share of EU Emissions (%)', names = 'Major Sector', title= 'Approximate share of Emission by major sector')
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(height=600,width=800,              
    legend=dict(
        orientation="h",    # Places the legend horizontally at the bottom to save space
        yanchor="bottom",
        y=-0.2,
        xanchor="center",
        x=0.5))
st.plotly_chart(fig, use_container_width=True)
st.write(":grey[The above chart indicates that the sector - Transport is the major contributor towards the Greenhouse gases in Europe followed by Energy supply and Manufacturing & Industry." \
" Let's now dive into understaing the impact caused by the Transport sector.]")
###################################
# Contribution of greenhouse gas emissions by various modes of transportation in Europe.

transportation_emission_contribution = pd.read_csv("/Users/bharatsingh/Downloads/EV-Project/cleaned_data/eu_transport_emissions_breakdown.csv")
st.title (":violet[Emission by Transportation modes]")
st.subheader ("Share of EU transport")
st.dataframe(transportation_emission_contribution)

fig = px.pie(transportation_emission_contribution, values = 'Share of EU Transport Emissions (%)', names = 'Transport Mode', title= 'Share of Transportation modes in EU')
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(height=600,width=800,              
    legend=dict(
        orientation="h",    # Places the legend horizontally at the bottom to save space
        yanchor="bottom",
        y=-0.2,
        xanchor="center",
        x=0.5))
st.plotly_chart(fig, use_container_width=True)
st.write(":grey[The above two charts indicates that the Mode of Transport: Road transport is the major contributor of the Greenhouse gases in Europe as compared to other modes of transportation. Hence, is a clear indication that we need to focus on the Road transport sector and make it more eco-friendly. Considering Co2 being the major part of the emitted greenhouse gases, lets now understand the Co2 emission by various categories of vehicles using different fuel types.]")


########################

st.set_page_config(page_title="CO2 Emissions Comparison", layout="wide")

st.markdown("<h2 style='color: #8A2BE2;'>🌱 CO₂ Emissions Comparison by Vehicle Category & Powertrain</h2>", unsafe_allow_html=True)
st.subheader("Interactive comparison across vehicle segments and powertrain technologies.")
emission_comp=pd.read_csv("/Users/bharatsingh/Downloads/EV-Project/cleaned_data/vehicle_lifecycle_emissions_comp.csv")

col_select, col_mode = st.columns([2, 1])

with col_select:
    metric_options = {
        'Lifetime_Emissions_200k_km_tCO2e': 'Lifetime Emissions over 200k km (tCO₂e)',
        'Manufacturing_Emissions_tCO2e': 'Manufacturing Emissions (tCO₂e)',
        'Total_Lifecycle_Intensity_gCO2e_km': 'Total Lifecycle Intensity (gCO₂e/km)',
        'end_of_lifecycle_co2': 'End of Life CO₂ (tCO₂e)'
    }
    selected_metric = st.selectbox(
        "Select CO₂ Metric to Plot:",
        options=list(metric_options.keys()),
        format_func=lambda x: metric_options[x]
    )

with col_mode:
    barmode_option = st.radio("Bar Display Mode:", ["Grouped", "Stacked"], index=0)
    barmode_val = "group" if barmode_option == "Grouped" else "stack"

# 3. Create Grouped Bar Chart
fig = px.bar(
    emission_comp,
    x='Vehicle_Segment',
    y=selected_metric,
    color='Powertrain',
    barmode=barmode_val,
    text_auto='.1f',
    title=f"CO₂ Emissions Comparison: {metric_options[selected_metric]}",
    labels={
        'Vehicle_Segment': 'Vehicle Segment',
        selected_metric: metric_options[selected_metric],
        'Powertrain': 'Powertrain Type'
    },
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig.update_layout(
    height=600,
    xaxis_title="Vehicle Category",
    yaxis_title=metric_options[selected_metric],
    legend_title="Powertrain",
    margin={"r": 0, "t": 50, "l": 0, "b": 0}
)

# 4. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)
###############################
# 1. Page Configuration
st.set_page_config(page_title="EV Lifecycle & Cost Curves", layout="wide")

st.markdown("<h2 style='color: #8A2BE2;'>📈 Vehicle Lifecycle CO₂ and Cost Analysis</h2>", unsafe_allow_html=True)

# 2. Load Data (Cached for performance)
@st.cache_data
def load_data():
    return pd.read_csv("/Users/bharatsingh/Downloads/EV-Project/cleaned_data/vehicle_country_lifecycle.csv")

try:
    merged_vehicle_country = load_data()
except FileNotFoundError:
    st.error("⚠️ Error: '/Users/bharatsingh/Downloads/EV-Project/cleaned_data/vehicle_country_lifecycle.csv' file not found. Please verify the file is in your project directory.")
    st.stop()

# 3. Main Page Dropdown Selection (Placed side-by-side)
col1, col2 = st.columns(2)

segments = sorted(merged_vehicle_country["segment"].dropna().unique())
countries = sorted(merged_vehicle_country["country"].dropna().unique())

with col1:
    selected_segment = st.selectbox("Select Segment:", options=segments, key="segment_select")

with col2:
    selected_country = st.selectbox("Select Country:", options=countries, key="country_select")

st.markdown("---")

# 4. Parameters
lifetime_km = 250000  # Parameter
km = np.linspace(0, lifetime_km, 501)

# 5. Filter Data based on selections
sub = merged_vehicle_country[
    (merged_vehicle_country["segment"] == selected_segment) & 
    (merged_vehicle_country["country"] == selected_country)
].set_index("energy")

# Check if data exists for this combination
if sub.empty:
    st.warning(f"No data available for Segment: **{selected_segment}** in Country: **{selected_country}**.")
else:
    # 6. Generate Matplotlib Figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    for energy, row in sub.iterrows():
        # CO2 calculation: A + x*B + C (tCO2e) ; A = manufacturing, x = gCO2/km, B = kilometers, C = recyclage
        g_per_km = (
            row["petrol_l"] * row["co2_petrol_g_l"] + 
            row["diesel_l"] * row["co2_diesel_g_l"] + 
            row["elec_kwh"] * row["grid_gco2e_kwh"]
        ) / lifetime_km  # g/km
        
        eol = np.where(km >= lifetime_km, row["end_of_life_(tco2e)"], 0.0)
        ax1.plot(km, row["manufacturing_(tco2e)"] + g_per_km * km / 1e6 + eol, label=energy, linewidth=2)

        # Cost calculation: A + x*B (EUR) ; A = cost of buying, x = EUR/km, B = kilometers
        eur_per_km = (
            row["petrol_l"] * row["sp95_price_eur_l"] + 
            row["diesel_l"] * row["diesel_price_eur_l"] + 
            row["elec_kwh"] * row["elec_price_eur_kwh"]
        ) / lifetime_km
        
        ax2.plot(km, row["price_eur"] + eur_per_km * km, label=energy, linewidth=2)

    # Chart 1 formatting
    ax1.set_title(f"Lifetime CO₂ Emitted\n{selected_segment} - {selected_country}", fontsize=11, fontweight='bold')
    ax1.set_xlabel("Kilometers (km)")
    ax1.set_ylabel("Emissions (tCO₂e)")
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.6)

    # Chart 2 formatting
    ax2.set_title(f"Cumulated Cost\n{selected_segment} - {selected_country}", fontsize=11, fontweight='bold')
    ax2.set_xlabel("Kilometers (km)")
    ax2.set_ylabel("Cost (EUR)")
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()

    # 7. Render Plot in Streamlit
    st.pyplot(fig)

    # 8. Optional Data Table Expander
    with st.expander("📄 View Filtered Underlying Data"):
        display_sub = sub.reset_index()
        display_sub.index = display_sub.index + 1
        st.dataframe(display_sub, use_container_width=True)

###############################

ev_sales_trend = pd.read_csv("/Users/bharatsingh/Downloads/EV-Project/cleaned_data/european_ev_market_trends.csv")
st.title (":violet[EVOLUTION OF EV'S IN EUROPE]")
st.subheader ("Total of EV's sold in Europe from 2010 to 2024")
fig = px.bar(ev_sales_trend, x='year', y='total_ev_new_registrations', color='total_ev_new_registrations', title='EV Evolution in Europe')
st.plotly_chart(fig, use_container_width=True)
st.write(":grey[The above graph shows the total number of EV's sold in Europe from 2010 to 2024. The sales of EV's started in the year 2010 with only 591 units sold and have significantly been increasing since then. The highest being 2.3 millions of EV's sold in the year 2023.]")


ev_sales_by_country = pd.read_csv("/Users/bharatsingh/Downloads/EV-Project/cleaned_data/europe_ev_sales_data.csv")
st.title (":violet[EV SALES BY COUNTRY IN EUROPE]")
st.subheader ("Major countries contributing to the EV sales in Europe")
st.write(":grey[Below is the list of major countries with the total number of EV's sold in Europe.]")
# heatmap_data = ev_sales_by_country.pivot_table(index='Country', values='Units_Sold', aggfunc='sum', fill_value=0)
# fig = px.imshow(
#         heatmap_data,
#         text_auto=',.0f',          # Formats numbers cleanly with commas
#         aspect="auto",
#         color_continuous_scale='Blues',
#         labels=dict(x='Units_Sold', y="Country", color="Units Sold")
#     )
    
# fig.update_layout(
#         height=650,
#         xaxis_tickangle=-45,
#         title=f"Total EV Units Sold by Country "
#     )
    
#     #Display the heatmap
# st.plotly_chart(fig, use_container_width=True)
# 1. Group and sort sales data
sales_by_country = (ev_sales_by_country.groupby("Country", as_index=False)["Units_Sold"].sum().sort_values("Units_Sold", ascending=False))

# 2. Build the bar chart with explicitly forced category ordering
fig = px.bar(
    sales_by_country,
    x='Country',
    y='Units_Sold',
    color='Units_Sold',
    title='Countries with Maximum EV Sales',
    color_continuous_scale='Viridis',
    labels={'Units_Sold': 'Units Sold', 'Country': 'Country'},
    category_orders={'Country': sales_by_country['Country'].tolist()}
)

# 3. Display formatted values directly on top of bars (optional enhancement)
fig.update_traces(texttemplate='%{y:,}', textposition='outside')
fig.update_layout(height=500, xaxis_title="Country", yaxis_title="Total Units Sold")

# 4. Render in Streamlit
st.plotly_chart(fig, use_container_width=True)
###################################
# Vehicle Explorer

st.set_page_config(page_title="EV Vehicle Explorer", layout="wide")

st.markdown("<h2 style='color: #8A2BE2;'><ins>🚗 ELECTRIC VEHICLE CATALOG & FILTER EXPLORER</ins></h2>", unsafe_allow_html=True)
st.subheader("Filter and explore vehicles by Luxury Tier, Brand, Price Range, Battery Capacity and Driving Range.")

df=pd.read_csv("/Users/bharatsingh/Downloads/EV-Project/cleaned_data/europe_ev_sales_data.csv")
    

st.markdown("### 🔍 Filter Options")
# Search Bar across top of filters
search_query = st.text_input("🔎 Search Model Name (e.g., 'i5', 'Han', 'Air'):", "")

col_f1, col_f2 = st.columns(2)

with col_f1:
    # Filter by Luxury Tier
    all_tiers = sorted(df['Luxury_Tier'].unique())
    selected_tiers = st.multiselect("Select Luxury Tier(s):", all_tiers, default=all_tiers)
    
    # Filter by Price Range (Slider)
    min_price, max_price = int(df['Price_EUR'].min()), int(df['Price_EUR'].max())
    price_range = st.slider(
        "Select Price Range (€):",
        min_value=min_price,
        max_value=max_price,
        value=(min_price, max_price),
        step=1000
    )
    
    # Filter by Battery Size (kWh)
    min_bat, max_bat = float(df['Battery_kWh'].min()), float(df['Battery_kWh'].max())
    battery_range = st.slider(
        "Select Battery Capacity (kWh):",
        min_value=min_bat,
        max_value=max_bat,
        value=(min_bat, max_bat),
        step=1.0
    )

with col_f2:
    # Filter by Brand
    all_brands = sorted(df['Brand'].unique())
    selected_brands = st.multiselect("Select Brand(s):", all_brands, default=all_brands)
    
    # Filter by Estimated Range in km (Slider)
    min_range, max_range = int(df['Est_Range_km'].min()), int(df['Est_Range_km'].max())
    range_slider = st.slider(
        "Select Minimum Estimated Range (km):",
        min_value=min_range,
        max_value=max_range,
        value=min_range,
        step=10
    )

# 3. Apply Filters to DataFrame
filtered_df = df[
    (df['Luxury_Tier'].isin(selected_tiers)) &
    (df['Brand'].isin(selected_brands)) &
    (df['Price_EUR'] >= price_range[0]) &
    (df['Price_EUR'] <= price_range[1]) &
    (df['Battery_kWh'] >= battery_range[0]) &
    (df['Battery_kWh'] <= battery_range[1]) &
    (df['Est_Range_km'] >= range_slider)
]

# Apply Text Search if user typed something
if search_query:
    filtered_df = filtered_df[filtered_df['Model'].str.contains(search_query, case=False, na=False)]

# 4. Display Summary Metrics of Filtered Results
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Matching Models Found", len(filtered_df))
with col2:
    avg_price = filtered_df['Price_EUR'].mean() if not filtered_df.empty else 0
    st.metric("Average Price (€)", f"€{avg_price:,.0f}")
with col3:
    total_units = filtered_df['Units_Sold'].sum() if not filtered_df.empty else 0
    st.metric("Total Units Sold", f"{total_units:,.0f}")

st.markdown("---")

# 5. Display Filtered Data Table
st.subheader("📋 Filtered Vehicle List")
if not filtered_df.empty:
    
    display_df=filtered_df[['Brand', 'Model', 'Battery_kWh', 'Luxury_Tier', 'Price_EUR', 'Est_Range_km',]].sort_values(by='Price_EUR').reset_index(drop=True)
    display_df.index = display_df.index + 1
    st.dataframe(display_df,use_container_width=True)
    
else:
    st.warning("No vehicles match the selected search/filter criteria. Please adjust your inputs.")

###################################
# Charging Stations in Europe

st.set_page_config(page_title="EU Country Land Area Map", layout="wide")

st.markdown("<h2 style='color: #8A2BE2;'>🌍 Total Charging Stations in European Countries</h2>", unsafe_allow_html=True)
st.subheader("Interactive Choropleth Map of Europe")
@st.cache_data
def load_data():
    df_2 = pd.read_csv('/Users/bharatsingh/Downloads/EV-Project/cleaned_data/europe_chargingstation_country.csv')
    return df_2

df_2 = load_data()

# 2. Generate Interactive Map
fig = px.choropleth(
    df_2,
    locations='country',
    locationmode='country names',
    color='number_of_charging_points',
    hover_name='country',
    hover_data={'number_of_charging_points': ':,'},  # Format with thousands comma separator
    color_continuous_scale='Viridis',
    labels={'number_of_charging_points': 'Number of EV Charging Stations'},
    title='Charging Stations Density per Country'
)

# 3. Focus Map Specifically on Europe
fig.update_geos(
    scope='europe',
    showcountries=True,
    countrycolor="LightGray",
    showcoastlines=True,
    coastlinecolor="Black",
    showland=True,
    landcolor="whitesmoke"
)

fig.update_layout(
    height=700,
    margin={"r": 0, "t": 40, "l": 0, "b": 0}
)

# 4. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Data Table Expander with 1-to-N indexing
with st.expander("📋 View Data Table"):
    display_df = df_2.copy().reset_index(drop=True)
    display_df.index = display_df.index + 1
    st.dataframe(display_df, use_container_width=True)
   
###################################

st.markdown("## :rainbow[THANK YOU for visiting this page and Hope you MAKE A RIGHT CHOICE]")
st.write("<ins>Project By:</ins> " \
                    "Matthieu Mondain - Project Manager, " \
                    "Paakwesi Yankson - Project Consultant & " \
                    "Bharat Singh - Project Co-ordinator", unsafe_allow_html=True)