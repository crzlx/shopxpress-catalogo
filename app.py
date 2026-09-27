import streamlit as st
import gspread
import pandas as pd
import json
import urllib.parse

# Configuração da Página
st.set_page_config(page_title='ShopXpress - Catálogo Oficial', page_icon='🛒', layout='wide')

# --- CONFIGURAÇÃO DO BANCO DE DADOS (GOOGLE SHEETS) ---
@st.cache_resource
def init_connection():
    # Lê a chave secreta de dentro do cofre do Streamlit
    creds_dict = json.loads(st.secrets["GOOGLE_CREDENTIALS"])
    gc = gspread.service_account_from_dict(creds_dict)
    return gc

# Conecta e puxa os dados
try:
    gc = init_connection()
    url_planilha = st.secrets["URL_PLANILHA"]
    sheet = gc.open_by_url(url_planilha).sheet1
    dados = sheet.get_all_records()
    df_produtos = pd.DataFrame(dados)
except Exception as e:
    st.error(f"Erro ao conectar ao banco de dados. Verifique os Secrets. Erro: {e}")
    st.stop()

# --- VERIFICAÇÃO DE ROTA OCULTA ---
# Se o link tiver ?admin=1 no final, ele abre o painel. Se não, abre a vitrine.
is_admin = st.query_params.get("admin") == "1"

# ==========================================
# PÁGINA ADMIN (VISÃO DESENVOLVEDOR - OCULTA)
# ==========================================
if is_admin:
    st.title("⚙️ Painel de Controle - ShopXpress")
    st.write("Acesso restrito para gerenciamento de estoque e catálogo.")
    
    senha = st.text_input("Digite a senha de acesso:", type="password")
    
    if senha == "admin123": # <--- Mude sua senha aqui!
        st.success("Acesso Liberado!")
        st.markdown("### Banco de Dados Atual (Google Sheets)")
        st.dataframe(df_produtos, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### Adicionar Novo Produto")
        with st.form("form_novo_produto"):
            col1, col2 = st.columns(2)
            with col1:
                novo_sku = st.text_input("SKU (Ex: NOV-001)")
                novo_nome = st.text_input("Nome do Produto")
                novo_cat = st.text_input("Categoria")
                novo_preco = st.text_input("Preço (Ex: 45.00)")
            with col2:
                novo_status = st.selectbox("Status", ["Sob Encomenda", "Em Estoque", "Esgotado"])
                nova_img = st.text_input("Caminho da Imagem (Ex: assets/novo_item.jpg)")
                nova_desc = st.text_area("Descrição do Produto")
            
            submit = st.form_submit_button("Salvar na Planilha")
            
            if submit:
                if novo_sku and novo_nome:
                    sheet.append_row([novo_sku, novo_nome, novo_cat, novo_preco, nova_desc, novo_status, nova_img])
                    st.success(f"Produto {novo_nome} adicionado com sucesso! Atualize a página.")
                else:
                    st.error("Por favor, preencha pelo menos o SKU e o Nome.")
    elif senha != "":
        st.error("Senha incorreta!")

# ==========================================
# PÁGINA VITRINE (VISÃO DO CLIENTE - PADRÃO)
# ==========================================
else:
    # Estilização
    st.markdown("""
        <style>
        .stApp { background-color: #0f1115; color: #f3f4f6; }
        #MainMenu, footer, header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # Cabeçalho
    col_logo, col_wa = st.columns([4, 1])
    with col_logo:
        st.markdown('### 🛒 Shop<span style="color: #ff6600;">Xpress</span>', unsafe_allow_html=True)
    with col_wa:
        wa_header_url = 'https://wa.me/5522992580079?text=' + urllib.parse.quote('Olá! Vim pelo site ShopXpress e gostaria de tirar dúvidas.')
        st.markdown(f'<a href="{wa_header_url}" target="_blank" style="background-color: #25d366; color: white; padding: 0.5rem 1rem; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block; text-align: center; width: 100%;">💬 WhatsApp</a>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h1 style='text-align: center; font-weight: 800;'>Sua Vitrine Digital Exclusiva</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #9ca3af; margin-bottom:2rem;'>Explore nossos produtos disponíveis a pronta entrega e por encomenda!</p>", unsafe_allow_html=True)

    # Filtros
    c_search, c_filter = st.columns([2, 1])
    search_query = c_search.text_input('Pesquisar produtos', placeholder='🔍 Pesquise por nome, SKU...')
    status_filter = c_filter.selectbox('Filtrar por disponibilidade', ['Todos', 'Em Estoque', 'Sob Encomenda'])

    # Lógica de Filtro
    df_filtrado = df_produtos.copy()
    if search_query:
        df_filtrado = df_filtrado[df_filtrado.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
    if status_filter != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Status'].str.contains(status_filter, case=False, na=False)]

    st.markdown('<br>', unsafe_allow_html=True)

    # Grid de Produtos
    if df_filtrado.empty:
        st.info('Nenhum produto encontrado.')
    else:
        cols = st.columns(3)
        for i, row in df_filtrado.iterrows():
            with cols[i % 3]:
                is_stock = 'Estoque' in str(row['Status'])
                badge_bg = 'rgba(16, 185, 129, 0.15)' if is_stock else 'rgba(245, 158, 11, 0.15)'
                badge_color = '#10b981' if is_stock else '#f59e0b'

                with st.container(border=True):
                    # SKU e Status
                    st.markdown(f"""
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <span style="font-family: monospace; font-size: 0.75rem; background: rgba(255,255,255,0.05); padding: 2px 6px; border-radius: 4px; color: #9ca3af;">🏷️ {row['SKU']}</span>
                            <span style="font-size: 0.7rem; font-weight: 700; color: {badge_color}; background: {badge_bg}; padding: 3px 8px; border-radius: 12px; text-transform: uppercase;">{row['Status']}</span>
                        </div>
                    """, unsafe_allow_html=True)

                    # Imagem
                    try:
                        st.image(row['Imagem_URL'], use_container_width=True)
                    except:
                        st.warning('Imagem não encontrada')

                    # Textos
                    st.markdown(f"""
                        <span style="font-size: 0.7rem; font-weight: 600; color: #ff6600; text-transform: uppercase;">{row['Categoria']}</span>
                        <h3 style="font-size: 1.05rem; font-weight: 700; color: white; margin: 4px 0 6px 0;">{row['Nome']}</h3>
                        <p style="font-size: 0.85rem; color: #9ca3af; margin-bottom: 1rem; line-height: 1.4; height: 50px; overflow: hidden;">{row['Descricao']}</p>
                    """, unsafe_allow_html=True)

                    # Botão WhatsApp e Preço
                    col_price, col_btn = st.columns([1, 1])
                    with col_price:
                        try:
                            preco_val = str(row['Preco']).replace(',', '.')
                            preco_formatado = f"R$ {float(preco_val):.2f}".replace('.', ',')
                        except ValueError:
                            preco_formatado = f"R$ {row['Preco']}"
                            
                        st.markdown(f"<div style='font-size: 1.15rem; font-weight: 800; color: white; padding-top: 6px;'>{preco_formatado}</div>", unsafe_allow_html=True)
                    with col_btn:
                        whatsapp_msg = urllib.parse.quote(f"Olá! Gostaria de encomendar o produto [SKU: {row['SKU']}]: *{row['Nome']}*. Poderia me passar mais detalhes?")
                        st.markdown(f"""
                            <a href="https://wa.me/5522992580079?text={whatsapp_msg}" target="_blank" style="background-color: #ff6600; color: white; padding: 0.45rem 0.8rem; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 0.8rem; display: flex; align-items: center; justify-content: center; gap: 5px;">
                                💬 Pedir
                            </a>
                        """, unsafe_allow_html=True)
