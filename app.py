import streamlit as st
import math

# ==============================
# WAJIB PALING ATAS
# ==============================
st.set_page_config(
    page_title="Kalkulator Kombinasi & Permutasi",
    layout="centered"
)

# ==============================
# Custom CSS
# ==============================
st.markdown("""
<style>
.result-text {
    font-size: 2.3rem;
    font-weight: 600;
    margin: 1.2rem 0;
    text-align: center;
    color: #ffffff;
}

.footer-text {
    text-align: center;
    color: #999;
    margin-top: 0.5rem;
    font-size: 0.7rem;
    opacity: 0.75;
    letter-spacing: 0.3px;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# Header
# ==============================
st.markdown(
    '<h1 style="text-align: center;">Kalkulator Kombinasi & Permutasi</h1>',
    unsafe_allow_html=True
)
st.markdown(
    '<p style="text-align: center; color: #888; margin-bottom: 2rem;">'
    'Muhammad Rafli Rusdiansyah - 5042905 - 2IA01</p>',
    unsafe_allow_html=True
)
st.markdown("---")

# ==============================
# Pilih Jenis Perhitungan
# ==============================
pilihan = st.radio(
    "Pilih jenis perhitungan:",
    ("Permutasi", "Kombinasi"),
    horizontal=True
)

# ==============================
# Input Nilai
# ==============================
col1, col2 = st.columns(2)
with col1:
    n = st.number_input("Nilai n", min_value=0, max_value=100, value=5, step=1)
with col2:
    r = st.number_input("Nilai r", min_value=0, max_value=100, value=3, step=1)

# ==============================
# Tombol Hitung
# ==============================
clicked = st.button("Hitung", type="primary", use_container_width=True)

# ==============================
# Footer (SEBELUM HITUNG)
# ==============================
if not clicked:
    st.markdown(
        '<p class="footer-text">Tugas Mata Kuliah Statistika 2026</p>',
        unsafe_allow_html=True
    )

# ==============================
# Proses Hitung
# ==============================
if clicked:
    if r > n:
        st.error("❌ Nilai r tidak boleh lebih besar dari n")
    else:
        try:
            if pilihan == "Permutasi":
                hasil = math.factorial(n) // math.factorial(n - r)
                st.markdown(
                    f'<p class="result-text">Hasil: P({n},{r}) = {hasil:,}</p>',
                    unsafe_allow_html=True
                )
            else:
                hasil = math.factorial(n) // (
                    math.factorial(r) * math.factorial(n - r)
                )
                st.markdown(
                    f'<p class="result-text">Hasil: C({n},{r}) = {hasil:,}</p>',
                    unsafe_allow_html=True
                )

            st.markdown(
                '<p class="footer-text">Tugas Mata Kuliah Statistika 2026</p>',
                unsafe_allow_html=True
            )

        except Exception:
            st.error("❌ Nilai terlalu besar untuk dihitung!")

