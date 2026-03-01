import streamlit as st

st.set_page_config(page_title="Kartolinë për Mësuesit 🌸")
st.title("🌷 Kartolinë për 7–8 Marsin 🌷")

# Fjalori me urime për secilin mësues
urime_mesuesve = {
    "Arta": "E dashur mësuese Arta, ju jeni frymëzim për çdo nxënës 🌸",
    "Blerim": "I dashur mësues Blerim, puna juaj na frymëzon çdo ditë 🌹",
    "Elira": "E dashur mësuese Elira, çdo ditë bëni ndryshim në klasë 🌼",
    "Gentian": "I dashur mësues Gentian, faleminderit për përkushtimin tuaj 🌷",
    "Mimoza": "E dashur mësuese Mimoza, ju jeni drita që ndriçon rrugën tonë 🌺"
}

# Mësuesi shkruan emrin e tij
emri = st.text_input("Shkruani emrin tuaj:")

if st.button("Shfaq Urimin 💌"):

    if not emri:
        st.warning("Ju lutem shkruani emrin tuaj.")
    elif emri not in urime_mesuesve:
        st.error("Emri nuk gjendet në listë.")
    else:
        urimi_personal = urime_mesuesve[emri]
        st.markdown(f"""
        <div style="
            text-align:center;
            background: linear-gradient(135deg, #ffe6f2, #fff0f5);
            padding:30px;
            border-radius:20px;
            border:3px solid #ff4da6;
            font-size:20px;
            box-shadow:0 6px 15px rgba(0,0,0,0.15);
        ">
            <h3>🌟 GËZUAR FESTËN! 🌟</h3><br><br>
            <p>{urimi_personal}</p><br><br>
            <p>Me dashuri nga Klubi i Kodimit</p>
            <p>Shkolla "22 Tetori"</p>
        </div>
        """, unsafe_allow_html=True)


























