import streamlit as st
import random

st.set_page_config(page_title="Gëzuar 7-8 Marsin 🌸")

st.title("🌷 Kartolinë Digjitale për 7–8 Marsin")

opsion = st.radio("Zgjidhni festën:", ["7 Mars - Dita e Mësuesit", 
                                       "8 Mars - Dita e Nënës"])

emri = st.text_input("Shkruani emrin:")

if st.button("Shfaq Urimin 💌"):
    
    if opsion.startswith("7"):
        urime = [
            "Ju jeni drita që ndriçon rrugën tonë drejt dijes.",
            "Faleminderit për përkushtimin dhe zemrën tuaj të madhe.",
            "Çdo mësim nga ju është një hap drejt suksesit tonë."
        ]
        titulli = "🌟 GËZUAR 7 MARSIN! 🌟"
    else:
        urime = [
            "Dashuria dhe forca juaj na frymëzon çdo ditë.",
            "Ju jeni zemra e familjes tuaj dhe familja jone e dyte.",
            "Mirënjohje për gjithçka që bëni me kaq përkushtim."
        ]
        titulli = "💖 GËZUAR 8 MARSIN! 💖"

    st.markdown(f"## {titulli}")
 if str.endswith("a",A):
   st.success(f" E dashur mesuese {emri}, {random.choice(urime)}")
 else:
      st.success(f" I dashur mesues {emri}, {random.choice(urime)}")


    #st.balloons()
  st.markdown("""
<div style="text-align: center; font-size: 40px;">
🌸 🌷 🌹 🌺 🌼 🌸 🌷 🌹 🌺 🌼
</div>
""", unsafe_allow_html=True)

for i in range(3):
    st.markdown("🌸 🌷 🌹 🌺 🌼")

