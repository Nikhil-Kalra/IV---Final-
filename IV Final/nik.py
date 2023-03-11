import streamlit as st
import streamlit.components.v1 as components 
from PIL import Image
import os 
import matplotlib.pyplot as plt 

# Using object notation

option = st.sidebar.selectbox(
    "Projects",
    ("About","Tableau", "Gephi", "Python" , "D3")
)

if option == "About" : 
    st.title("18CSE301J-RA2011003011058 - Nikhil")
    st.text("")
    st.text("")
    st.header("DATASET-IPL AUCTION 2022")
    st.text("")
    st.text("")
    st.write("The IPL auction is an annual event where teams participating in the Indian Premier League (IPL) bid for players to add to their squad for the upcoming season. The auction for the 2022 IPL was held on February 12, 2022, in Bengaluru, India. A total of 292 players were included in the auction, out of which 123 were bought by the eight participating teams.")
    st.text("")     
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    st.image("https://english.cdn.zeenews.com/sites/default/files/styles/zm_700x400/public/2022/02/01/1010809-ipl-2022-auction.jpg")

if option == "Tableau": 

    st.title("Tableau Project")

    components.html(
        """
        <div class='tableauPlaceholder' id='viz1678396335764' style='position: relative'><noscript><a href='#'><img
                alt='Dashboard 2 '
                src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IP&#47;IPL_2022_Auction_16783962728710&#47;Dashboard2&#47;1_rss.png'
                style='border: none' /></a></noscript><object class='tableauViz' style='display:none;'>
                <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                <param name='embed_code_version' value='3' />
                <param name='site_root' value='' />
                <param name='name' value='IPL_2022_Auction_16783962728710&#47;Dashboard2' />
                <param name='tabs' value='no' />
                <param name='toolbar' value='yes' />
                <param name='static_image'
                    value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;IP&#47;IPL_2022_Auction_16783962728710&#47;Dashboard2&#47;1.png' />
                <param name='animate_transition' value='yes' />
                
                <param name='display_static_image' value='yes' />
                <param name='display_spinner' value='yes' />
                <param name='display_overlay' value='yes' />
                <param name='display_count' value='yes' />
                <param name='language' value='en-US' />
                <param name='filter' value='publish=yes' />
            </object></div>
        
        <script type='text/javascript'> 
            var divElement = document.getElementById('viz1678396335764'); 
            var vizElement = divElement.getElementsByTagName('object')[0]; 
            if (divElement.offsetWidth > 800) { 
                vizElement.style.width = '1900px'; 
                vizElement.style.height = '1062px'; 
            } 
            else if (divElement.offsetWidth > 500) { 
                vizElement.style.width = '1900px'; 
                vizElement.style.height = '1062px'; 
            } 
            else { 
                vizElement.style.width = '100%'; 
                vizElement.style.height = '2377px'; 
            } 
            var scriptElement = document.createElement('script'); 
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js'; 
            vizElement.parentNode.insertBefore(scriptElement, vizElement);                
        </script> """, height=2000,width=4000)
    
if option == "Gephi" : 
    st.title("Gephi")
    st.text("")
    st.text("")
    filename = "gephi-2.pdf"

    with open(filename, "rb") as f:
        data = f.read()
        st.download_button(
            label="Download GEPHI PDF",
            data=data,
            file_name=filename
        )

    st.image("gephi-2.png")

if option == "Python" : 
    st.title("Python")

    option = st.selectbox("TypeS of Players Bought by Teams in IPL 2022", 
                 ("CSK", "DC" , "GT","KKR","MI","PK","SH","RCB","RR"))
    
    if option == "CSK" :
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [36, 32, 20, 12]
        explode = (0.1, 0, 0, 0)  

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)

    if option == "DC" :
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [37.5, 29.2, 20.8, 12.5]
        explode = (0.1, 0, 0, 0)  

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)

    if option == "GT" :
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [36.4, 36.4, 18.2, 9.09]
        explode = (0.1,0.1, 0, 0)  

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1) 

    if option == "RR" :
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [25, 41.7, 20.8, 12.5]
        explode = (0, 0.1, 0, 0)  

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)
    
    if option == "RCB" :
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [40.9, 31.8, 13.6, 13.6]
        explode = (0.1, 0, 0, 0)  

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)

    if option == "SH" :
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [26.1, 39.1, 21.7, 13]
        explode = (0, 0.1, 0, 0)  

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)

    if option == "PK" :
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [44, 32, 12, 12]
        explode = (0.1, 0, 0, 0)  

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)
    
    if option == "MI" :
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [44, 28, 20, 6]
        explode = (0.1, 0, 0, 0)  

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)

    if option == "KKR" :
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [40, 28, 20, 12]
        explode = (0.1, 0, 0, 0)  

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)

