import streamlit as st
import random

st.set_page_config(page_title="Gëzuar 7-8 Marsin 🌸")

st.title("🌷Kartolinë për 7–8 Marsin🌷")

opsion = st.radio("Zgjidhni festën:", ["7 Mars - Dita e Mësuesit", 
                                       "8 Mars - Dita e Nënës"])

emri = st.text_input("Shkruani emrin:")

if st.button("Shfaq Urimin 💌"):
    
    # Përzgjedhja e urimeve sipas festës
    if opsion.startswith("7"):
        urime = [
            "Ju jeni drita që ndriçon rrugën tonë drejt dijes.",
            "Faleminderit për përkushtimin dhe zemrën tuaj të madhe.",
            "Çdo mësim nga ju është një hap drejt suksesit tonë.",
            "Ju jeni drita që ndriçon rrugën tonë drejt dijes.",
            "Faleminderit për përkushtimin dhe zemrën tuaj të madhe.",
            "Çdo mësim nga ju është një hap drejt suksesit tonë.",
            "Mësues si ju bëjnë botën më të bukur.",
            "Mirënjohje për çdo ditë që ndani dije dhe buzëqeshje.",
            "Ju frymëzoni çdo nxënës të rritet me besim dhe kurajo.",
            "Një falënderim i madh për gjithë punën tuaj."
        ]
        titulli = "🌟GËZUAR 7 MARSIN!🌟"
        if emri:
            if emri.lower().endswith("a"):
                st.success(f"{titulli}\n\nE dashur mësuese {emri}, {random.choice(urime)}")
            else:
                st.success(f"{titulli}\n\nI dashur mësues {emri}, {random.choice(urime)}")
    else:
        urime = [
            "Dashuria dhe forca juaj na frymëzon çdo ditë.",
            "Ju jeni zemra e klasës dhe familja jonë e dytë.",
            "Mirënjohje për gjithçka që bëni me kaq përkushtim.",
            "Një mësuese si ju e bën botën më të bukur dhe nxënësit më të lumtur."
        ]
        titulli = "💖GËZUAR 8 MARSIN!💖"
        if emri:
            st.success(f"{titulli}\n\nE dashur mesuese {emri}, {random.choice(urime)}")

    st.balloons()
 












