import streamlit as st
import os
import base64

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Psicóloga Michelle Santos | Clínica",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 📝 DADOS REAIS
# ==========================================
LINK_WHATSAPP = "https://wa.me/5512992253598"
LINK_INSTAGRAM = "https://www.instagram.com/psi.michellesantos?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="
NUMERO_VISIVEL = "(12) 99225-3598"
CRP_MICHELLE = "CRP 06/223583"
EMAIL_CONTATO = "psimichellesantoss@gmail.com"
ENDERECO_REAL = "R. Enseada - Res. San Marino, Taubaté - SP"
LINK_MAPS = "https://www.google.com/maps/search/?api=1&query=R.+Enseada+-+Res.+San+Marino,+Taubaté+-+SP"

# --- AVALIAÇÕES REAIS (Atualizado) ---
NOME_AVALIACAO_1 = "Guilherme Monteiro"
TEXTO_AVALIACAO_1 = "Uma profissional excelente!!!! Meu primo está se sentindo super contente."

NOME_AVALIACAO_2 = "Renata Ferraz"
TEXTO_AVALIACAO_2 = "Michelle Santos é uma profissional muito boa, maravilhosa, tá me ajudando muito. Agradeço muito por tudo..."

NOME_AVALIACAO_3 = "Thais Milene"
TEXTO_AVALIACAO_3 = "Excelente profissional, me ajudou muito em momentos de crise."

# ==========================================

# --- PALETA DE CORES (Rose Premium) ---
COR_FUNDO = "#F9F3F5"       # Rosa Blush
COR_TEXTO = "#4A4A4A"       # Cinza Escuro
COR_TITULO = "#0E5E6F"      # Verde Petróleo
COR_BORDA = "#A67B5B"       # Bronze/Terracota

# --- SISTEMA INTELIGENTE DE IMAGENS ---
def carregar_imagem_inteligente(nome_base, url_reserva):
    caminhos_possiveis = [f"assets/{nome_base}.jpg", f"assets/{nome_base}.png"]
    for caminho in caminhos_possiveis:
        if os.path.exists(caminho): return caminho, True 
    return url_reserva, False 

def get_img_as_base64(file_path):
    try:
        with open(file_path, "rb") as f: data = f.read()
        return base64.b64encode(data).decode()
    except: return None

# --- CARREGAMENTO DAS FOTOS ---
FOTO_HERO, EH_LOCAL_HERO = carregar_imagem_inteligente("perfil", "https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=688&auto=format&fit=crop")
FOTO_SOBRE, _ = carregar_imagem_inteligente("apresentacao", "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=688&auto=format&fit=crop")
IMG_GALERIA_1, _ = carregar_imagem_inteligente("galeria1", "https://images.unsplash.com/photo-1600607686527-6fb886090705?q=80&w=600&auto=format&fit=crop")
IMG_GALERIA_2, _ = carregar_imagem_inteligente("sobre", "https://images.unsplash.com/photo-1596230622956-6f81e05d0505?q=80&w=600&auto=format&fit=crop")
IMG_GALERIA_3, _ = carregar_imagem_inteligente("sobre2", "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=600&auto=format&fit=crop")


# --- CSS ---
st.markdown(f"""
    <style>
    html {{ scroll-behavior: smooth; }}
    .stApp {{ background-color: {COR_FUNDO}; }}
    h1, h2, h3, h4, h5, h6 {{ color: {COR_TITULO} !important; }}
    p, li, div, span {{ color: {COR_TEXTO}; }}
    
    .btn-topo {{
        position: fixed; bottom: 30px; right: 30px;
        background-color: {COR_TITULO}; color: white !important;
        width: 50px; height: 50px; border-radius: 50%;
        text-align: center; line-height: 50px; font-size: 24px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2); z-index: 9999;
        text-decoration: none !important; transition: transform 0.3s;
    }}
    .btn-topo:hover {{ transform: translateY(-5px); background-color: {COR_BORDA}; }}

    a.nav-link {{
        color: {COR_TEXTO} !important; text-decoration: none !important;
        font-weight: 600; font-size: 14px; margin: 0 10px; padding: 8px 15px;
        border-radius: 20px; transition: all 0.3s ease; display: inline-block;
    }}
    a.nav-link:hover {{ color: {COR_TITULO} !important; background-color: rgba(14, 94, 111, 0.1); transform: translateY(-2px); }}

    .hero-img {{
        border-radius: 50%; border: 6px solid {COR_BORDA};
        width: 350px; height: 350px; object-fit: cover;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.15); display: block; margin: auto;
    }}

    .btn-agendar {{
        background-color: {COR_TITULO}; color: white !important;
        padding: 16px 40px; font-size: 16px; font-weight: bold;
        text-align: center; text-decoration: none !important;
        border-radius: 50px; display: inline-block; border: none;
        box-shadow: 0px 5px 15px rgba(14, 94, 111, 0.3); transition: all 0.3s ease; letter-spacing: 1px;
    }}
    .btn-agendar:hover {{ background-color: {COR_BORDA}; transform: translateY(-3px); box-shadow: 0px 8px 20px rgba(166, 123, 91, 0.4); }}

    .btn-insta {{
        background-color: white; color: {COR_BORDA} !important;
        border: 2px solid {COR_BORDA}; padding: 10px 25px;
        font-size: 14px; font-weight: bold; text-align: center;
        text-decoration: none !important; border-radius: 50px;
        display: inline-block; transition: all 0.3s ease; margin-top: 10px;
    }}
    .btn-insta:hover {{ background-color: {COR_BORDA}; color: white !important; transform: translateY(-2px); }}

    .card-branco {{ background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid {COR_BORDA}; }}
    .service-card {{ background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); text-align: center; height: 100%; border: 1px solid #eee; transition: transform 0.2s; }}
    .service-card:hover {{ transform: translateY(-5px); border-color: {COR_TITULO}; }}
    
    .google-card {{
        background-color: white; padding: 25px; border-radius: 12px;
        border: 1px solid #eee; text-align: center;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08); height: 100%;
        display: flex; flex-direction: column; justify-content: space-between;
    }}
    
    .footer {{ background: white; padding: 50px 0; border-top: 1px solid #e0e0e0; margin-top: 80px; }}
    </style>
""", unsafe_allow_html=True)

st.markdown(f"<a href='#inicio' class='btn-topo' title='Voltar ao Topo'>⬆</a>", unsafe_allow_html=True)

# 0. MENU
col_logo, col_menu = st.columns([1, 4])
with col_logo: st.markdown(f"<h3 style='margin:0; color:{COR_TITULO}'>Michelle Santos</h3>", unsafe_allow_html=True)
with col_menu: st.markdown("""<div style='text-align:right; padding-top:5px;'><a href='#inicio' class='nav-link'>INÍCIO</a><a href='#sobre' class='nav-link'>SOBRE</a><a href='#servicos' class='nav-link'>SERVIÇOS</a><a href='#depoimentos' class='nav-link'>DEPOIMENTOS</a><a href='#contato' class='nav-link'>CONTATO</a></div>""", unsafe_allow_html=True)
st.markdown("---")

# 1. HERO
st.markdown("<div id='inicio'></div>", unsafe_allow_html=True)
c1, c2 = st.columns([1.3, 1], gap="large")
with c1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("Psicologia Clínica Integrativa em Taubaté - SP")
    st.markdown(f"""
    #### Atendimento Online para todo Brasil 🇧🇷 e Presencial.
    
    Oferecemos um espaço seguro e sigiloso para **Crianças, Jovens e Adultos**.
    
    * 🌱 **Ansiedade e Estresse**
    * ☁️ **Depressão e Luto**
    * ⚖️ **Transtornos de Humor**
    * 🧠 **Neurodivergências (TEA/TDAH)**
    
    _Atendimentos Particulares com foco na sua evolução._
    """)
    st.markdown(f'<br><a href="{LINK_WHATSAPP}" target="_blank" class="btn-agendar">AGENDAR SESSÃO</a>', unsafe_allow_html=True)
with c2:
    if EH_LOCAL_HERO:
        img_b64 = get_img_as_base64(FOTO_HERO)
        src = f"data:image/jpeg;base64,{img_b64}" if img_b64 else "https://via.placeholder.com/350"
    else: src = FOTO_HERO
    st.markdown(f'<img src="{src}" class="hero-img">', unsafe_allow_html=True)
st.markdown("<br><br><br>", unsafe_allow_html=True)

# 2. SOBRE
st.markdown("<div id='sobre'></div>", unsafe_allow_html=True)
c_foto, c_texto = st.columns([1, 1.2], gap="large")
with c_foto: st.image(FOTO_SOBRE, use_container_width=True)
with c_texto:
    st.markdown(f"""<div class="card-branco"><h3 style="margin-top:0;">Muito Além da Terapia</h3><p><b>Uma abordagem educativa, científica e humanizada.</b></p></div><br>""", unsafe_allow_html=True)
    st.markdown("""A **Psicóloga Michelle Santos** possui uma trajetória única que une experiência clínica e visão corporativa.\n\n* 🎓 **Pós-graduanda em Saúde Mental**, Psicologia Organizacional e TCC.\n* 🏢 **30 anos de experiência** no setor corporativo (Expert em Estresse e Carreira).\n* 👩‍💼 **Apaixonada pelo tema da mulher** no mercado de trabalho.\n* 🏥 **Atendimento Particular** (Presencial e Online).""")
    st.markdown(f'<br><a href="{LINK_INSTAGRAM}" target="_blank" style="color:{COR_TITULO}; font-weight:bold; text-decoration:none;">📷 Acompanhe meu dia a dia no Instagram</a>', unsafe_allow_html=True)
st.markdown("<br><hr><br>", unsafe_allow_html=True)

# 3. SERVIÇOS
st.markdown("<div id='servicos'></div>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align:center; margin-bottom:40px;'>Áreas de Atuação</h2>", unsafe_allow_html=True)
def criar_card(i, t, txt): return f"<div class='service-card'><span style='font-size:40px; display:block; margin-bottom:15px;'>{i}</span><h4 style='color:{COR_TITULO}; margin:0;'>{t}</h4><p style='font-size:14px; margin-top:10px; color:#666;'>{txt}</p></div>"
col1, col2, col3, col4 = st.columns(4)
with col1: st.markdown(criar_card("💻", "Terapia Online", "Atendimento para todo o Brasil no conforto da sua casa."), unsafe_allow_html=True)
with col2: st.markdown(criar_card("☁️", "Depressão & Ansiedade", "Acolhimento para resgatar o sentido e a qualidade de vida."), unsafe_allow_html=True)
with col3: st.markdown(criar_card("⚖️", "Carreira & Trabalho", "Suporte para desafios profissionais e esgotamento (Burnout)."), unsafe_allow_html=True)
with col4: st.markdown(criar_card("🧸", "Infanto-Juvenil", "Ludoterapia e orientação de pais para desafios."), unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# 4. GALERIA
st.markdown(f"<h2 style='text-align:center; margin-bottom:20px;'>Conheça o Espaço</h2>", unsafe_allow_html=True)
g1, g2, g3 = st.columns(3)
with g1: 
    st.image(IMG_GALERIA_1, use_container_width=True)
    st.markdown("<p style='text-align:center; font-size:12px; color:#888;'>Consultório Acolhedor</p>", unsafe_allow_html=True)
with g2: 
    st.image(IMG_GALERIA_2, use_container_width=True)
    st.markdown("<p style='text-align:center; font-size:12px; color:#888;'>Conforto e Segurança</p>", unsafe_allow_html=True)
with g3: 
    st.image(IMG_GALERIA_3, use_container_width=True)
    st.markdown(f"<p style='text-align:center; font-size:12px; color:#888;'>Saiba mais sobre mim</p>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# 5. DEPOIMENTOS REAIS
st.markdown("<div id='depoimentos'></div>", unsafe_allow_html=True)
st.markdown(f"""
<div style='background:white; padding:40px; border-radius:15px; text-align:center; border:1px solid #eee;'>
    <h2>Excelência Comprovada</h2>
    <p style="font-size:18px;">⭐ <b>5.0 Estrelas no Google</b></p>
    <p style="color:#666;">Baseado em avaliações reais de pacientes.</p>
</div>
<br>
""", unsafe_allow_html=True)

d1, d2, d3 = st.columns(3)

def criar_depoimento(nome, texto):
    return f"""
    <div class="google-card">
        <div>
            <div style='color:#F4B400; font-size:18px; margin-bottom:10px;'>⭐⭐⭐⭐⭐</div>
            <p style="font-size:14px; color:#555; font-style:italic;">"{texto}"</p>
        </div>
        <div style="font-size:12px; color:#999; margin-top:15px; border-top:1px solid #eee; padding-top:10px;">
            <b>{nome}</b><br>Paciente Verificado
        </div>
    </div>
    """

with d1: st.markdown(criar_depoimento(NOME_AVALIACAO_1, TEXTO_AVALIACAO_1), unsafe_allow_html=True)
with d2: st.markdown(criar_depoimento(NOME_AVALIACAO_2, TEXTO_AVALIACAO_2), unsafe_allow_html=True)
with d3: st.markdown(criar_depoimento(NOME_AVALIACAO_3, TEXTO_AVALIACAO_3), unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 6. RODAPÉ
st.markdown("<div id='contato'></div>", unsafe_allow_html=True)
st.markdown('<div class="footer">', unsafe_allow_html=True)
f1, f2, f3 = st.columns([1, 1, 1.5])
with f1:
    st.markdown(f"<h3 style='color:{COR_TITULO}'>Michelle Santos</h3>", unsafe_allow_html=True)
    st.markdown(f"**Psicologia Clínica Integrativa**<br>{CRP_MICHELLE}", unsafe_allow_html=True)
    st.markdown(f'<a href="{LINK_INSTAGRAM}" target="_blank" class="btn-insta">📷 Siga no Instagram</a>', unsafe_allow_html=True)

with f2:
    st.markdown("#### Links Rápidos")
    st.markdown(f"<a href='#inicio' style='text-decoration:none; color:{COR_TEXTO}; display:block; margin-bottom:5px;'>• Voltar ao Início</a><a href='#servicos' style='text-decoration:none; color:{COR_TEXTO}; display:block; margin-bottom:5px;'>• Nossos Tratamentos</a>", unsafe_allow_html=True)
with f3:
    st.markdown("#### Contato & Localização")
    st.markdown(f"""
    📍 <b>Taubaté - SP</b><br>
    <a href="{LINK_MAPS}" target="_blank" style="color:{COR_TEXTO}; text-decoration:none;">{ENDERECO_REAL} (Ver no Mapa)</a><br>
    📞 {NUMERO_VISIVEL}<br>
    ✉️ {EMAIL_CONTATO}
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown(f"<div style='background-color:{COR_TITULO}; padding:15px; text-align:center; color:white;'><p style='color:white; margin:0; font-size:12px;'>© 2025 Michelle Santos Psicologia.</p></div>", unsafe_allow_html=True)
