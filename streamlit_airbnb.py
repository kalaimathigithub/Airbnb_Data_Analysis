import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(layout="wide")
st.title("AIRBNB DATA ANALYSIS")
st.write("")

def data_frame():
    df = pd.read_csv("E:/python/Project_4/aairbnb.csv")
    return df

df = data_frame()

with st.sidebar:
    select = option_menu("MENU",["HOME","DATA EXPLORATION"])

if select == "HOME":

    image1= Image.open("E:/python/Project_4/download.jpg")
    st.image(image1)

    st.header("ABOUT AIRBNB")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    st.write("")
    st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***''')
    
    st.header("Background of Airbnb")
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')




if select == "DATA EXPLORATION":
    tab1,tab2,tab3,tab4 = st.tabs(["***PRICE ANALYSIS***","***AVAILABILITY ANALYSIS***","***LOCATION BASED***", "***GEOSPATIAL VISUALIZATION***"])

    with tab1:
        st.title("***PRICE ANALYSIS***")
        col1,col2 = st.columns(2)

        with col1:

            
            country = st.selectbox("Select the Country",df["country"].unique())
            df1 = df[df["country"]==country]
            df1.reset_index(drop=True,inplace=True)

            room_type = st.selectbox("Select the Room Type",df1["room_type"].unique())

            
            df2 = df1[df1["room_type"]== room_type]
            df2.reset_index(drop=True,inplace=True)

            df_bar = pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
            df_bar.reset_index(inplace=True)

            fig_bar= px.bar(df_bar, x='property_type', y = "price", title="PRICE FOR PROPERTY_TYPES",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Redor_r,width=600,height=500)
            st.plotly_chart(fig_bar)

        with col2:

            property_type = st.selectbox("Select the property Type",df2["property_type"].unique())

            
            df3 = df2[df2["property_type"]== property_type]
            df3.reset_index(drop=True,inplace=True)

             

            

            df_pie= pd.DataFrame(df3.groupby("host_neighbourhood")[["price","bedrooms"]].sum())
            df_pie.reset_index(inplace= True)

            fig_pi= px.pie(df_pie, values="price", names= "host_neighbourhood",
                            hover_data=["bedrooms"],
                            color_discrete_sequence=px.colors.sequential.BuPu_r,
                            title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                            width= 600, height= 500)
            st.plotly_chart(fig_pi)

        col1,col2 = st.columns(2)

        with col1:

            host_neighbourhood = st.selectbox("select the host_neighbourhood",df3["host_neighbourhood"].unique())

            df4 = df3[df3["host_neighbourhood"]==host_neighbourhood]
            df4.reset_index(drop=True,inplace=True)

            df_bar2 = pd.DataFrame(df4.groupby("bed_type")[["price","beds","bedrooms"]].sum())
            df_bar2.reset_index(inplace=True)

            fig_bar2= px.bar(df_bar2, x='bed_type', y =["price","beds","bedrooms"], title="PRICE BASED ON BED_TYPES",barmode="group",
                             color_discrete_sequence=px.colors.sequential.Rainbow_r,width=600,height=500)
            st.plotly_chart(fig_bar2)

        with col2: 

            df_bar3=pd.DataFrame(df4.groupby("cancellation_policy")[["price","minimum_nights","maximum_nights"]].sum())
            df_bar3.reset_index(inplace=True)

            fig_bar3= px.bar(df_bar3, x="cancellation_policy", y =["price"], title="PRICE BASED ON CANCELLATION POLICY",barmode="group",
                             hover_data="minimum_nights",color_discrete_sequence=px.colors.sequential.Rainbow_r,width=600,height=500)
            st.plotly_chart(fig_bar3)

    with tab2:

        def data_frame2():
         df_aa = pd.read_csv("E:/python/Project_4/aairbnb.csv")
         return df_aa
            
        df_aa=data_frame2()
        st.title("***AVAILABILITY ANALYSIS***")
        col1,col2 = st.columns(2)


        with col1:
                country = st.selectbox("Select the Country_a",df["country"].unique())
                df_aa1 = df_aa[df_aa["country"]==country]
                df_aa1.reset_index(drop=True,inplace=True)

                room_type = st.selectbox("Select the Room Type_a",df_aa1["room_type"].unique())

                
                df_aa2 = df_aa1[df_aa1["room_type"]== room_type]
                df_aa2.reset_index(drop=True,inplace=True)

                figaa_sun= px.sunburst(df_aa2, path=["room_type","bed_type","is_location_exact"],values="availability_30", title="availability_30",color_discrete_sequence=px.colors.sequential.Redor_r,width=600,height=500)
                st.plotly_chart(figaa_sun)

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
                
                
                

            figaa_sun2= px.sunburst(df_aa2, path=["room_type","bed_type","cancellation_policy"], values="availability_60",width=600,height=500,title="Availability_60",color_discrete_sequence=px.colors.sequential.ice_r)
            st.plotly_chart(figaa_sun2)

        col1,col2=st.columns(2)

        with col1:

            figaa_sun3= px.sunburst(df_aa2, path=["room_type","bed_type","cancellation_policy"], values="availability_90",width=600,height=500,title="Availability_90",color_discrete_sequence=px.colors.sequential.ice_r)
            st.plotly_chart(figaa_sun3)

        with col2:
            figaa_sun4= px.sunburst(df_aa2, path=["room_type","bed_type","cancellation_policy"], values="availability_365",width=600,height=500,title="Availability_365",color_discrete_sequence=px.colors.sequential.gray_r)
            st.plotly_chart(figaa_sun4)
            
            property_type = st.selectbox("Select the property Type_a",df_aa1["property_type"].unique())
            df_aa3 = df_aa2[df_aa2["property_type"]== property_type]
            df_aa3.reset_index(drop=True,inplace=True)

            fig_bar_aa = px.bar(df_aa3, x='bed_type', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
                                     title='AVAILABILITY BASED ON BEDTYPEFV./A',hover_data="price",
                                     barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
            st.plotly_chart(fig_bar_aa)
    
    with tab3:

        st.title("***LOCATION BASED***")
        st.write()

        def data_frame3():
            df_la = pd.read_csv("E:/python/Project_4/aairbnb.csv")
            return df_la
        
        df_la = data_frame3()

        col1,col2 = st.columns(2)

        with col1:
            country_la = st.selectbox("select the country_la",df_la["country"].unique())
            df_la1 = df[df["country"]==country_la]
            df_la1.reset_index(drop=True,inplace=True)

            room_type_la = st.selectbox("select the room_type_la",df_la["room_type"].unique())
            df_la2 = df_la1[df_la1["room_type"]==room_type_la]
            df_la2.reset_index(drop=True,inplace=True)

            st.write("")

            property_type_la = st.selectbox("select the property_type_la",df_la2["property_type"].unique())
            df_la3 = df_la2[df_la2["property_type"]==property_type_la]
            df_la3.reset_index(drop=True,inplace=True) 
            
            # checking the correlation

            df_la3_cor = df_la3.drop(columns=["listing_url","name", "property_type",                 
                                            "room_type", "bed_type","cancellation_policy",
                                            "images","host_url","host_name", "host_location",                   
                                            "host_response_time", "host_thumbnail_url",            
                                            "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                            "host_picture_url","host_neighbourhood",
                                            "host_identity_verified","host_verifications",
                                            "street", "suburb", "government_area", "market",                        
                                            "country", "country_code","location_type","is_location_exact",
                                            "amenities"]).corr()
            st.dataframe(df_la3_cor)

            df_la_sel= pd.DataFrame(df_la3.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
            df_la_sel.reset_index(inplace= True)

            fig_1a= px.bar(df_la_sel, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], title="ACCOMMODATES",
                    hover_data= "extra_people", barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
            st.plotly_chart(fig_1a)

            fig_la2= px.bar(df_la2, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
                    hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
            st.plotly_chart(fig_la2)

            fig_la3= px.bar(df_la2, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
                          hover_data= ["guests_included","location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
            st.plotly_chart(fig_la3)


    with tab4:

        st.title("GEOSPATIAL VISUALIZATION")
        st.write("")

        fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='accommodates',
                                 color_continuous_scale= "rainbow",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                                 zoom=1)
        fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
        st.plotly_chart(fig_4)  


        