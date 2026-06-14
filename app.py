import streamlit as st
import sqlite3
import pandas as pd
from main import scrape, make_link
import time

def load_data_from_db():
    try:
        conn = sqlite3.connect('database.db')
        query = "SELECT name, adress, phone_number, reviews, average, website FROM users"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.sidebar.warning(f"Database not loaded yet (Using fallback template): {e}")
        return pd.DataFrame() 

def creating_the_page(db_df):

    if not db_df.empty:
        st.title("🏢 Live Business Explorer (Database Connected)")
        st.subheader("Select a scraped business to view its live details")
        st.markdown("---")
        
        company_list = db_df['name'].tolist()
        selected_company = st.selectbox("🔍 Step 1: Select a Company", options=company_list)
        
        st.markdown("### 📋 Company Profile")
        
        profile = db_df[db_df['name'] == selected_company].iloc[0]
        
        with st.expander("📍 View Address Details"):
            st.write(profile["adress"])
            
        with st.expander("📞 View Phone Number"):
            st.write(str(profile["phone_number"]))
            
        with st.expander("🌐 View Official Website"):
            url = profile["website"]
            if url and url != "N/A" and str(url).startswith("http"):
                st.markdown(f"[{url}]({url})")
            else:
                st.write(url)
                
        with st.expander("⭐ View Ratings & Reviews"):
            st.write(f"Average Rating: {profile['average']} | Total Reviews: {profile['reviews']}")

    else:
        st.title("🏢 Business Explorer (Template Mode)")
        st.subheader("Select a template business to view its details")
        st.markdown("---")
    
        COMPANY_DATA = {
            "Bella Italia Pizza": {
                "Address": "Ανδρούτσου & Αριστοτέλους Γωνία, Κατερίνη 601 00",
                "Phone": "+30 2351 0XXXXX",
                "Website": "https://www.bellaitaliapizza.gr",
                "Rating": "4.7 Stars (1,178 reviews)"
            },
            "Example Business B": {
                "Address": "123 Main Street, Athens 104 31",
                "Phone": "+30 210 1234567",
                "Website": "https://www.example-b.com",
                "Rating": "4.2 Stars (450 reviews)"
            }
        }
        
        company_list = list(COMPANY_DATA.keys())
        selected_company = st.selectbox("🔍 Step 1: Select a Company", options=company_list, index=0)
        
        st.markdown("### 📋 Company Profile")
        profile = COMPANY_DATA[selected_company]
        
        with st.expander("📍 View Address Details"):
            st.write(profile["Address"])
        with st.expander("📞 View Phone Number"):
            st.write(profile["Phone"])
        with st.expander("🌐 View Official Website"):
            if profile["Website"] != "N/A" and profile["Website"].startswith("http"):
                st.markdown(f"[{profile['Website']}]({profile['Website']})")
            else:
                st.write(profile["Website"])
        with st.expander("⭐ View Ratings & Reviews"):
            st.write(profile["Rating"])
    st.markdown("---")
    st.caption("Data Explorer MVP • Connected to live database storage engine.")

if __name__ == "__main__":
    loading_msg = st.empty()
    loading_msg.write("Loading the data...")

    query = st.text_input("What should the search query be? (e.g. Pizza, City)", value="Pizza, Katerini")
    n_leads = st.number_input("How many leads do you wanna scrape?", min_value=1, max_value=20, value=5)
    link = make_link(query)

    db_df = load_data_from_db()

    loading_msg.empty()
    run = st.button("Click me to start scraping!!!")
    creating_the_page(db_df)

    if run:
        time.sleep(0.5)
        scrape(link, n_leads)
        st.rerun()