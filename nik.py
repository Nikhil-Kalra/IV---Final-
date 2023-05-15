import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os
import matplotlib.pyplot as plt
from streamlit_d3graph import d3graph
import base64

# Using object notation

option = st.sidebar.selectbox(
    "Projects",
    ("About","Assignment-1", "Tableau", "Gephi", "Python", "D3")
)

if option == "About":
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

if option == "Assignment-1" : 
    st.title("Assignment-1")

    st.text("")
    st.text("")
    filename = "Information_Visualization_report (12) (1).pdf"

    with open(filename, "rb") as f:
        data = f.read()
        st.download_button(
            label="Download Assignment-1 PDF",
            data=data,
            file_name=filename
        )

    components.html("""<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; object-src 'self' blob:; style-src 'self'; frame-src 'self'">""")

    with open(filename, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML

    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
	
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
        </script> """, height=2000, width=4000)

if option == "Gephi":
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


if option == "Python":
    st.title("Python")

    option = st.selectbox("TypeS of Players Bought by Teams in IPL 2022",
                          ("CSK", "DC", "GT", "KKR", "MI", "PK", "SH", "RCB", "RR"))

    if option == "CSK":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [36, 32, 20, 12]
        explode = (0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

    if option == "DC":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [37.5, 29.2, 20.8, 12.5]
        explode = (0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

    if option == "GT":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [36.4, 36.4, 18.2, 9.09]
        explode = (0.1, 0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

    if option == "RR":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [25, 41.7, 20.8, 12.5]
        explode = (0, 0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

    if option == "RCB":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [40.9, 31.8, 13.6, 13.6]
        explode = (0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

    if option == "SH":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [26.1, 39.1, 21.7, 13]
        explode = (0, 0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

    if option == "PK":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [44, 32, 12, 12]
        explode = (0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

    if option == "MI":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [44, 28, 20, 6]
        explode = (0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

    if option == "KKR":
        labels = 'All Rounder', 'Bowler', 'Batsman', 'WicketKeeper'
        sizes = [40, 28, 20, 12]
        explode = (0.1, 0, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.axis('equal')
        st.pyplot(fig1)

if option == "D3":

    st.title("D3.js Project")

    components.html(
        """
        
<!DOCTYPE html>
<html>
<head>
  <title>D3.js Tutorial</title>
  <script src="https://d3js.org/d3.v5.min.js"></script>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
	color:white;
    }

    .rect:hover { opacity: 0.5; }
  </style>
</head>
<body>
  <div style="text-align: center;">
    <div id="d3-container" />
  </div>
  <script type="text/javascript">
	const data = [
  { name: 'DC', score: 50 },
  { name: 'RR', score: 45 },
  { name: 'RCB', score: 51 },
  { name: 'SRH', score: '21'},
  { name: 'MI', score: 70 },
  { name: 'GT', score: 35 },
  { name: 'CSK', score: 48 },
  { name: 'LSG', score: 29 },
  { name: 'KKR', score: 39 },
  { name: 'PBKS', score: 46 },
  
];

const width = 800;
const height = 600;
const margin = { top: 50, bottom: 50, left: 50, right: 50 };

const svg = d3.select('#d3-container')
  .append('svg')
  .attr('width', width - margin.left - margin.right)
  .attr('height', height - margin.top - margin.bottom)
  .attr("viewBox", [0, 0, width, height]);

const x = d3.scaleBand()
  .domain(d3.range(data.length))
  .range([margin.left, width - margin.right])
  .padding(0.3)

const y = d3.scaleLinear()
  .domain([0, 100])
  .range([height - margin.bottom, margin.top])

svg
  .append("g")
  .attr("fill", 'royalblue')
  .selectAll("rect")
  .data(data.sort((a, b) => d3.descending(a.score, b.score)))
  .join("rect")
    .attr("x", (d, i) => x(i))
    .attr("y", d => y(d.score))
    .attr('title', (d) => d.score)
    .attr("class", "rect")
    .attr("height", d => y(0) - y(d.score))
    .attr("width", x.bandwidth());

function yAxis(g) {
  g.attr("transform", `translate(${margin.left}, 0)`)
    .call(d3.axisLeft(y).ticks(null, data.format))
    .padding(1)
    .attr("font-size", '20px')
}

function xAxis(g) {
  g.attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x).tickFormat(i => data[i].name))
    .attr("font-size", '20px')
}

svg.append("g").call(xAxis);
svg.append("g").call(yAxis);
svg.node();
</script>
</body>
</html>
        
        
X-Axis- Teams
Y-Axis- Fund Spent in Crs     
        
        """ ,height=650)
