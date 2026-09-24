import urllib.parse
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title='ShopXpress - Catálogo Oficial', page_icon='🛒', layout='wide'
)

# Estilização Visual (Tema Laranja e Escuro ShopXpress)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f1115;
        color: #f3f4f6;
    }
    /* Ocultar elementos padrão do Streamlit para deixar com cara de site */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""",
    unsafe_allow_html=True,
)

# Cabeçalho do Site
col_logo, col_wa = st.columns([4, 1])
with col_logo:
    st.markdown(
        '### 🛒 Shop<span style="color: #ff6600;">Xpress</span>',
        unsafe_allow_html=True,
    )
with col_wa:
    wa_header_url = 'https://wa.me/5522992580079?text=' + urllib.parse.quote(
        'Olá! Vim pelo site ShopXpress e gostaria de tirar dúvidas.'
    )
    st.markdown(
        f'<a href="{wa_header_url}" target="_blank" style="background-color: #25d366; color: white; padding: 0.5rem 1rem; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block; text-align: center; width: 100%;">💬 WhatsApp</a>',
        unsafe_allow_html=True,
    )

st.markdown('---')

# Hero Section
st.markdown(
    "<h1 style='text-align: center; font-weight: 800;'>Sua Vitrine Digital"
    " Exclusiva</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #9ca3af; font-size: 1.1rem;'>"
    "Explore nossos produtos disponíveis a pronta entrega e por encomenda. Faça"
    " seu pedido diretamente pelo WhatsApp!"
    '</p>',
    unsafe_allow_html=True,
)
st.markdown('<br>', unsafe_allow_html=True)

# Base de Dados de Produtos com SKUs e Caminho das Imagens
products = [
    {
        'sku': 'REL-SMP-001',
        'title': 'Relógio Simples',
        'category': 'Relógios',
        'price': 'R$ 15,00',
        'desc': 'Várias cores coloridas disponíveis. Pronta entrega imediata!',
        'status': 'Em Estoque (4 un.)',
        'image': 'assets/relogio_simples.jpg',
    },
    {
        'sku': 'REL-MIN-001',
        'title': 'Relógio Moderno Minimalista (Sem Pulseiras)',
        'category': 'Relógios',
        'price': 'R$ 40,00',
        'desc': (
            'Design sofisticado, moderno e versátil. Ponteiros funcionais.'
        ),
        'status': 'Sob Encomenda',
        'image': 'assets/relogio_minimalista.jpg',
    },
    {
        'sku': 'REL-MIN-002',
        'title': 'Relógio Moderno Minimalista + Kit Pulseiras',
        'category': 'Relógios',
        'price': 'R$ 50,00',
        'desc': 'Kit acompanha o relógio e pulseiras de couro e pedras.',
        'status': 'Sob Encomenda',
        'image': 'assets/relogio_minimalista.jpg',
    },
    {
        'sku': 'REL-CSH-001',
        'title': 'Relógio Digital C-Shock',
        'category': 'Relógios',
        'price': 'R$ 55,00',
        'desc': 'Visor digital de alta definição, resistente a impactos.',
        'status': 'Sob Encomenda',
        'image': 'assets/relogio_cshock.jpg',
    },
    {
        'sku': 'KIT-RCK-001',
        'title': 'Kit Relógio + Pulseira + Cordão (Sem Caixa)',
        'category': 'Kits & Acessórios',
        'price': 'R$ 70,00',
        'desc': 'Relógio moderno, pulseira de prata resistente e cordão.',
        'status': 'Sob Encomenda',
        'image': 'assets/kit_relogio.jpg',
    },
    {
        'sku': 'KIT-RCK-002',
        'title': 'Kit Relógio + Pulseira + Cordão (Com Caixa)',
        'category': 'Kits & Acessórios',
        'price': 'R$ 80,00',
        'desc': 'Kit completo em caixa especial.',
        'status': 'Sob Encomenda',
        'image': 'assets/kit_relogio.jpg',
    },
    {
        'sku': 'SMW-NFC-001',
        'title': 'Smart Watch Completo com NFC',
        'category': 'Smartwatches',
        'price': 'R$ 120,00',
        'desc': (
            'Com NFC para abertura de portas, apps diversos, sincronização e'
            ' monitor de saúde.'
        ),
        'status': 'Sob Encomenda',
        'image': 'assets/smartwatch.jpg',
    },
    {
        'sku': 'REL-INT-001',
        'title': 'Relógio Interativo Moderno',
        'category': 'Relógios',
        'price': 'R$ 40,00',
        'desc': 'Display digital moderno com design limpo.',
        'status': 'Sob Encomenda',
        'image': 'assets/tabela_geral.jpg',
    },
    {
        'sku': 'UTI-GAR-001',
        'title': 'Garrafas de Água',
        'category': 'Utilidades',
        'price': 'R$ 20,00 a R$ 60,00',
        'desc': 'Disponível em várias cores e modelos.',
        'status': 'Sob Encomenda',
        'image': 'assets/tabela_geral.jpg',
    },
    {
        'sku': 'AUD-TWS-001',
        'title': 'Fones Bluetooth TWS',
        'category': 'Áudio',
        'price': 'R$ 60,00',
        'desc': 'Fones sem fio com case de carregamento.',
        'status': 'Sob Encomenda',
        'image': 'assets/tabela_geral.jpg',
    },
    {
        'sku': 'AUD-P2-001',
        'title': 'Fones de Ouvido com Fio P2',
        'category': 'Áudio',
        'price': 'R$ 20,00',
        'desc': 'Conexão P2 universal.',
        'status': 'Sob Encomenda',
        'image': 'assets/tabela_geral.jpg',
    },
    {
        'sku': 'FER-CHV-001',
        'title': 'Chave Elétrica Holda (Recarregável)',
        'category': 'Ferramentas',
        'price': 'R$ 50,00',
        'desc': 'Recarregável 4.2V com ponteiras.',
        'status': 'Sob Encomenda',
        'image': 'assets/tabela_geral.jpg',
    },
    {
        'sku': 'UTI-GTR-001',
        'title': 'Garrafa Térmica + 3 Canecas Térmicas',
        'category': 'Utilidades',
        'price': 'R$ 75,00',
        'desc': 'Mantém a temperatura por muito mais tempo.',
        'status': 'Sob Encomenda',
        'image': 'assets/tabela_geral.jpg',
    },
    {
        'sku': 'ELE-AIR-001',
        'title': 'Air Fryer Gaabor 2.8L',
        'category': 'Eletroportáteis',
        'price': 'R$ 250,00',
        'desc': 'Frita sem óleo, aquecimento rápido. Disponível em 127V e 220V.',
        'status': 'Sob Encomenda',
        'image': 'assets/airfryer.jpg',
    },
    {
        'sku': 'AUD-CSM-001',
        'title': 'Caixa de Som Bluetooth Portátil Beltdow',
        'category': 'Áudio',
        'price': 'R$ 100,00',
        'desc': 'Som potente, Bluetooth 5.3, iluminação colorida e TWS.',
        'status': 'Sob Encomenda',
        'image': 'assets/caixa_som.jpg',
    },
]

# Filtros e Pesquisa na Interface do Streamlit
c_search, c_filter = st.columns([2, 1])
with c_search:
    search_query = st.text_input(
        'Pesquisar produtos',
        placeholder='🔍 Pesquise por nome, descrição ou SKU...',
    )
with c_filter:
    status_filter = st.selectbox(
        'Filtrar por disponibilidade', ['Todos', 'Em Estoque', 'Sob Encomenda']
    )

st.markdown('<br>', unsafe_allow_html=True)

# Lógica de Filtragem
filtered_products = []
for p in products:
    matches_search = (
        search_query.lower() in p['title'].lower()
        or search_query.lower() in p['sku'].lower()
        or search_query.lower() in p['category'].lower()
        or search_query.lower() in p['desc'].lower()
    )
    matches_status = True
    if status_filter == 'Em Estoque':
        matches_status = 'Estoque' in p['status']
    elif status_filter == 'Sob Encomenda':
        matches_status = 'Encomenda' in p['status']

    if matches_search and matches_status:
        filtered_products.append(p)

# Exibição em Grid de 3 colunas
if not filtered_products:
    st.info('Nenhum produto encontrado.')
else:
    cols = st.columns(3)
    for i, p in enumerate(filtered_products):
        with cols[i % 3]:
            is_stock = 'Estoque' in p['status']
            badge_bg = (
                'rgba(16, 185, 129, 0.15)'
                if is_stock
                else 'rgba(245, 158, 11, 0.15)'
            )
            badge_color = '#10b981' if is_stock else '#f59e0b'

            with st.container(border=True):
                st.markdown(
                    f"""
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <span style="font-family: monospace; font-size: 0.75rem; background: rgba(255,255,255,0.05); padding: 2px 6px; border-radius: 4px; color: #9ca3af;">🏷️ {p['sku']}</span>
                        <span style="font-size: 0.7rem; font-weight: 700; color: {badge_color}; background: {badge_bg}; padding: 3px 8px; border-radius: 12px; text-transform: uppercase;">{p['status']}</span>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

                try:
                    st.image(p['image'], use_container_width=True)
                except Exception:
                    st.warning('Imagem não encontrada na pasta assets')

                st.markdown(
                    f"""
                    <span style="font-size: 0.7rem; font-weight: 600; color: #ff6600; text-transform: uppercase; letter-spacing: 0.5px;">{p['category']}</span>
                    <h3 style="font-size: 1.05rem; font-weight: 700; color: white; margin: 4px 0 6px 0;">{p['title']}</h3>
                    <p style="font-size: 0.85rem; color: #9ca3af; margin-bottom: 1rem; line-height: 1.4;">{p['desc']}</p>
                """,
                    unsafe_allow_html=True,
                )

                col_price, col_btn = st.columns([1, 1])
                with col_price:
                    st.markdown(
                        f"""
                        <div style="font-size: 1.15rem; font-weight: 800; color: white; padding-top: 6px;">{p['price']}</div>
                    """,
                        unsafe_allow_html=True,
                    )
                with col_btn:
                    whatsapp_msg = urllib.parse.quote(
                        f"Olá! Gostaria de encomendar / comprar o produto [SKU: {p['sku']}]: *{p['title']}* ({p['price']}). Poderia me passar mais detalhes?"
                    )
                    whatsapp_link = (
                        f'https://wa.me/5522992580079?text={whatsapp_msg}'
                    )
                    st.markdown(
                        f"""
                        <a href="{whatsapp_link}" target="_blank" style="background-color: #ff6600; color: white; padding: 0.45rem 0.8rem; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 0.8rem; display: flex; align-items: center; justify-content: center; gap: 5px;">
                            💬 Pedir
                        </a>
                    """,
                        unsafe_allow_html=True,
                    )

st.markdown('<br><hr>', unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #9ca3af; font-size: 0.85rem;'>©"
    ' 2026 <b>ShopXpress</b> - Campos dos Goytacazes, RJ. Todos os direitos'
    ' reservados.</p>',
    unsafe_allow_html=True,
)
