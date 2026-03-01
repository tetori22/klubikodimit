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
        if emri:
            if emri.lower().endswith("a"):
                st.success(f"E dashur mësuese {emri}, {random.choice(urime)}")
            else:
                st.success(f"I dashur mësues {emri}, {random.choice(urime)}")
    else:
        urime = [
            "Dashuria dhe forca juaj na frymëzon çdo ditë.",
            "Ju jeni zemra e familjes tuaj dhe familja jonë e dytë.",
            "Mirënjohje për gjithçka që bëni me kaq përkushtim."
        ]
        titulli = "💖 GËZUAR 8 MARSIN! 💖"
        if emri:
            st.success(f"E dashur {emri}, {random.choice(urime)}")

    st.markdown(f"## {titulli}")

# Animacion lulesh me efekte më të lëvizshme
st.markdown("""
<style>
@keyframes ngrihu {
    0% {transform: translateY(100vh);}
    100% {transform: translateY(-50px);}
}
.lule {
    font-size: 40px;
    animation: ngrihu 5s linear infinite;
    display: inline-block;
    margin: 0 10px;
}
</style>

<div style="text-align:center;">
<span class="lule">🌸</span>
<span class="lule">🌷</span>
<span class="lule">🌹</span>
<span class="lule">🌺</span>
<span class="lule">🌼</span>
<span class="lule">💐</span>
<span class="lule">🌸</span>
</div>
""", unsafe_allow_html=True)





