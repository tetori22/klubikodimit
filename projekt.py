import streamlit as st

st.set_page_config(page_title="Kartolinë për Mësuesit 🌸")
st.subheader("🌷Një kartolinë për ty🌷")

# Fjalori me urime për secilin mësues
urime_mesuesve = {
    "Egla": "E dashur mësuese Egla! Urime për 7 Marsin! Ju falënderojmë që na hapni botën e librave dhe na mësoni të mendojmë thellë. 🌹",
    "Majlinda": "E dashur mësuese Majlinda! Gëzuar Ditën e Mësuesit! Me durimin dhe përkushtimin tuaj na frymëzoni çdo ditë. 🌷",
    "Erida": "E dashur mësuese Erida! Gëzuar 7 Marsin! Faleminderit që na mësoni të duam gjuhën dhe letërsinë dhe të shprehemi bukur me fjalë. 🌸",
    "Luiza": "E dashur mësuese Liza! Gëzuar 7 Marsin! Faleminderit që na mësoni të zgjidhim jo vetëm ushtrime, por edhe sfida. 🌺",
    "Laura": "E dashur mësuese Laura! Gëzuar 7 Marsin! Ju falënderojmë për durimin dhe përkushtimin tuaj në çdo orë mësimi. 🌻",
    "Gladiola": "E dashur mësuese Gladiola! Gëzuar 7 Marsin! Faleminderit që na mësoni një nga gjuhët më të rëndësishme në botë. 🌼",
    "Yllka": "E dashur mësuese Yllka! Urime për Ditën e Mësuesit! Me ju zbulojmë mrekullitë e trupit dhe të botës së gjallë. 💐",
    "Andon": "Mësues Andoni! Gëzuar 7 Marsin! Ju falënderojmë për frymëzimin dhe kreativitetin që na jepni. 🪻",
    "Loreta": "E dashur mësuese Loreta! Gëzuar 7 Marsin! Faleminderit që na tregoni bukuritë dhe misteret e botës. 🌺",
    "Anila": "E dashur mësuese Anila! Urime për Ditën e Mësuesit! Me ju udhëtojmë në çdo kontinent përmes dijes. 🌹",
    "Rexhina": "E dashur mësuese Rexhina! Gëzuar 7 Marsin! Faleminderit që na ndihmoni të kuptojmë ligjet e natyrës dhe të universit. 🌷",
    "Zeni": "E dashur mësuese Zeniu! Gëzuar 7 Marsin! Faleminderit që na motivoni të jemi aktivë dhe të shëndetshëm. 🌸",
    "Avenir": "E dashur mësuese Aveniri! Urime për Ditën e Mësuesit! Me ju sporti bëhet argëtim dhe energji. 🌻",
    "Andi": "Mësues Andi! Urime për Ditën e Mësuesit! Me ju çdo notë bëhet më e bukur. 🌼",
    "Irvena": "E dashur mësuese Irvena! Gëzuar 7 Marsin! Faleminderit që na mësoni një gjuhë kaq të bukur si italishtja. 💐",
    "Aibana": "E dashur mësuese Ajbana! Urime për Ditën e Mësuesit! Me ju çdo fjalë e re bëhet më e lehtë për t’u mësuar. 🪻",
    "Vojsava": "E dashur mësuese Sava! Gëzuar 7 Marsin! Faleminderit që na mësoni të njohim të kaluarën dhe të kuptojmë më mirë të tashmen. 🌺",
    "Xheni": "E dashur mësuese Xheni!Gëzuar 7 Marsin! Faleminderit që na mësoni botën e teknologjisë dhe dijet e informatikes.Një mësuese si ju e bën botën më të bukur dhe nxënësit më të lumtur.🌺",
    "Luljeta": "E nderuar nëndrejtore Luljeta! Gëzuar 7 Marsin! Ju falenderojmë për njohuritë që na jepni në biologji dhe kimi.🌺",
    "Genta":" E nderuar nëndrejtore Genta! Gëzuar 7 Marsin! Ju falenderojmë për prezencën e ngrohtë që sillni në shkollë.🪻 ",
    "Arta":"E nderuar Oficere, ju falenderojmë për sigurinë dhe mbështetjen që na jep.💐",
    "Parashqevi":"E dashur mësuese Parashqevi! Urime për Ditën e Mësuesit! Mirënjohje për gjithçka që bëni me kaq përkushtim.💐",
    "Margarita":"E dashur mësuese Margarita! Urime për Ditën e Mësuesit! Me ju mësojmë fuqinë e fjalës!🌼",
    "Albana Bega":"E nderuar drejtore Albana! Gëzuar 7 Marsin! Ju falënderojmë për përkushtimin, drejtimin dhe mbështetjen tuaj të vazhdueshme. Falë jush, shkolla jonë është një vend ku dijet, respekti dhe bashkëpunimi rriten çdo ditë.💐",
    "Albana Agalliu":"Ju falënderojmë për kujdesin, mirëkuptimin dhe mbështetjen që na jepni çdo ditë. Falë jush ndihemi më të dëgjuar, më të kuptuar dhe më të fortë për të përballuar sfidat.🌸",
    "Arlinda":"Ju falënderojmë për përkujdesjen, mirëkuptimin dhe mbështetjen që na jepni çdo ditë. Me përkushtimin tuaj na ndihmoni të ndihemi më të sigurt dhe të vlerësuar në shkollë. 🌹",
    "Olta":"Mësuese Olta! Faleminderit që na mësoni një nga gjuhët më të rëndësishme në botë dhe na ndihmoni të hapim dritare të reja drejt dijes dhe komunikimit. 🌹",
    "Naunkela":"Mësuese Naunkela! Me ju mësojmë një nga gjuhët më të rëndësishme në botë. Mirënjohje për gjithçka që bëni me kaq përkushtim.🌹",
    "Esmeralda":"Mësuese Esmeralda! Një mësuese si ju e bën botën më të bukur dhe nxënësit më të lumtur!🌹",
    
}

# Mësuesi shkruan emrin e tij
emri = st.text_input("Shkruani emrin tuaj (shembull: Valbona)")

if st.button("Shfaq Urimin 💌"):

    if not emri:
        st.warning("Ju lutem shkruani emrin tuaj.")
    elif emri not in urime_mesuesve:
        st.error("Ky mësues nuk punon në shkollën 22 Tetori.")
    else:
        urimi_personal = urime_mesuesve[emri]
        st.markdown(f"""
        <div style="
            text-align:center;
            background: linear-gradient(135deg, #d4edda, #e6f7e6);
            padding:20px;
            border-radius:20px;
            border:3px solid #28a745;
            font-size:20px;
            box-shadow:0 6px 15px rgba(0,0,0,0.15);
        ">
            <h4>🌟 GËZUAR FESTËN! 🌟</h4><br><br>
            <p><b>{urimi_personal}</b></p><br><br>
            <p>Me dashuri nga Klubi i Kodimit</p>
            <p>Shkolla "22 Tetori"</p>
            st.balloons()
        </div>
        """, unsafe_allow_html=True)







































