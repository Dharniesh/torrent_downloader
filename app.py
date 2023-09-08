import streamlit as st
import qbittorrentapi

# Initialize the qBittorrent client
qbt_client = qbittorrentapi.Client(host='localhost:8080')  # Replace with your qBittorrent Web UI address
qbt_client.login('your_username', 'your_password')  # Replace with your qBittorrent username and password

# Streamlit app title and description
st.title("Torrent Downloader App")
st.write("Upload a .torrent file or provide a magnet link to start downloading.")

# User input for torrent file or magnet link
uploaded_file = st.file_uploader("Upload a .torrent file", type=[".torrent"])
magnet_link = st.text_input("Enter a Magnet Link")

# Check if a file is uploaded or a magnet link is provided
if uploaded_file:
    # Add torrent from uploaded file
    st.write("Adding torrent from uploaded file...")
    torrent_data = uploaded_file.read()
    qbt_client.torrents.add(torrentdata=torrent_data)

if magnet_link:
    # Add torrent from magnet link
    st.write("Adding torrent from Magnet Link...")
    qbt_client.torrents.add(urls=magnet_link)

# List active torrents
st.write("Active Torrents:")
for torrent in qbt_client.torrents.info():
    st.write(f"- {torrent.name}")

# Logout from the qBittorrent client
qbt_client.logout()
