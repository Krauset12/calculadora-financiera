import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Calculadora Financiera Pro",
    page_icon="📈",
    layout="wide"
)

# --- ESTILOS CSS PROFESIONALES (THEME PREMIUM) ---
st.markdown("""
<style>
    /* FONDO PREMIUM CON GRADIENTE PROFUNDO */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        background-attachment: fixed;
    }
    
    /* ESTILOS GLOBALES DE TEXTO */
    h1, h2, h3 {
        color: #ffffff !important;
        font-family: 'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif;
        font-weight: 700;
        letter-spacing: -0.03em;
    }
    
    h1 {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    p, label, .stMarkdown, .caption {
        color: #cbd5e1 !important;
        font-family: 'Inter', system-ui, sans-serif;
    }
    
    /* SIDEBAR CON GLASSMORPHISM */
    section[data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.8) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(251, 191, 36, 0.1);
    }
    
    section[data-testid="stSidebar"] > div {
        background: transparent !important;
    }
    
    /* INPUTS PREMIUM CON BRILLO DORADO */
    .stNumberInput input, .stDateInput input, .stSelectbox div[data-baseweb="select"] {
        background: linear-gradient(145deg, #1e293b, #334155) !important;
        color: #f1f5f9 !important; 
        border: 1px solid rgba(251, 191, 36, 0.3) !important;
        border-radius: 8px;
        font-weight: 500;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        transition: all 0.3s ease;
    }
    
    .stNumberInput input:focus, .stDateInput input:focus {
        border-color: #fbbf24 !important;
        box-shadow: 0 0 0 3px rgba(251, 191, 36, 0.2), 0 4px 12px rgba(251, 191, 36, 0.3);
        transform: translateY(-1px);
    }
    
    /* SELECTBOX MEJORADO */
    .stSelectbox div[data-baseweb="select"] > div {
        background: linear-gradient(145deg, #1e293b, #334155) !important;
    }
    
    /* EXPANDER CON EFECTO PREMIUM */
    .streamlit-expanderHeader {
        background: linear-gradient(145deg, #1e293b, #2d3748) !important;
        border: 1px solid rgba(251, 191, 36, 0.2) !important;
        border-radius: 10px !important;
        color: #fbbf24 !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: rgba(251, 191, 36, 0.5) !important;
        box-shadow: 0 4px 12px rgba(251, 191, 36, 0.2);
    }
    
    /* TABS CON DISEÑO MODERNO */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(145deg, #1e293b, #334155);
        border: 1px solid rgba(251, 191, 36, 0.2);
        border-radius: 8px;
        color: #cbd5e1;
        padding: 8px 16px;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(145deg, #334155, #475569);
        border-color: rgba(251, 191, 36, 0.4);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #fbbf24, #f59e0b) !important;
        color: #0f172a !important;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(251, 191, 36, 0.4);
    }
    
    /* BOTONES CON ESTILO PREMIUM */
    .stButton > button {
        background: linear-gradient(135deg, #fbbf24, #f59e0b);
        color: #0f172a;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 12px 24px;
        box-shadow: 0 4px 12px rgba(251, 191, 36, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(251, 191, 36, 0.5);
    }
    
    /* DATAFRAME CON ESTILO OSCURO */
    .stDataFrame {
        background: rgba(30, 41, 59, 0.6);
        border-radius: 12px;
        border: 1px solid rgba(251, 191, 36, 0.2);
        overflow: hidden;
    }
    
    /* MÉTRICAS MEJORADAS */
    div[data-testid="metric-container"] {
        background: linear-gradient(145deg, #1e293b, #334155);
        border: 1px solid rgba(251, 191, 36, 0.2);
        border-radius: 10px;
        padding: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    
    /* ALERTAS CON BRILLO */
    .stAlert {
        background: linear-gradient(145deg, #1e293b, #334155) !important;
        border-left: 4px solid #fbbf24 !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* PADDING OPTIMIZADO */
    .block-container {
        padding-top: 2rem;
        max-width: 1400px;
    }
    
    /* SCROLLBAR PERSONALIZADO */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1e293b;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #fbbf24, #f59e0b);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #f59e0b, #d97706);
    }
</style>
""", unsafe_allow_html=True)

# --- TÍTULOS CON DISEÑO PREMIUM ---
st.markdown("""
<div style="margin-bottom: 2rem;">
    <h1 style="
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        line-height: 1.2;
    ">
        Simulador de Inversión Avanzado
    </h1>
    <p style="
        font-size: 1.1rem;
        color: #94a3b8;
        margin: 0;
        font-weight: 400;
    ">
        Proyecta el crecimiento de tu patrimonio con 
        <span style="color: #fbbf24; font-weight: 600;">aportes mensuales</span> y 
        <span style="color: #10b981; font-weight: 600;">extraordinarios</span>
    </p>
</div>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (CONTROLES) ---
with st.sidebar:
    st.header("1. Tu Inversión")
    
    fecha_inicio = st.date_input("Fecha de Inicio", value=date.today())
    saldo_inicial = st.number_input("Saldo Inicial (₡)", value=0, min_value=0, step=100000, format="%d")
    aporte_mensual = st.number_input("Aporte Mensual (₡)", value=20000, min_value=0, step=5000, format="%d")
    plazo_anos = st.number_input("Plazo (Años)", value=30, min_value=1, max_value=50, step=1)
    
    # VALIDACIÓN: Al menos uno debe ser mayor a 0
    if saldo_inicial == 0 and aporte_mensual == 0:
        st.error("⛔ Debes ingresar un **Saldo Inicial** o un **Aporte Mensual** (o ambos)")
        st.stop()
    
    st.markdown("---")
    
    st.header("2. Variables del Entorno")
    inflacion = st.number_input("Inflación Anual (%)", value=3.0, min_value=0.0, max_value=50.0, step=0.1, format="%.1f")
    comision = st.number_input("Comisión Rendimientos (%)", value=10.0, min_value=0.0, max_value=100.0, step=0.5, format="%.1f", help="Se cobra sobre las ganancias")

    st.markdown("---")
    st.header("3. Tasas de Escenarios (Brutas)")
    st.caption("Rendimiento anual esperado antes de comisiones.")
    
    tasa_conservador = st.number_input("🛡️ Conservador (%)", value=9.0, min_value=0.0, step=0.25, format="%.2f")
    tasa_moderado = st.number_input("⚖️ Moderado (%)", value=10.0, min_value=0.0, step=0.25, format="%.2f")
    tasa_optimista = st.number_input("🚀 Optimista (%)", value=17.0, min_value=0.0, step=0.25, format="%.2f")

    st.markdown("---")
    
    # SECCIÓN: Abonos Extraordinarios
    st.header("4. Abonos Extraordinarios")
    st.caption("Añade fechas específicas para inyectar capital extra (ej. Aguinaldos).")
    
    with st.expander("Gestionar Tabla de Abonos", expanded=False):
        df_base = pd.DataFrame(columns=["Fecha", "Monto"])
        
        abonos_df = st.data_editor(
            df_base,
            num_rows="dynamic",
            column_config={
                "Fecha": st.column_config.DateColumn("Fecha", format="DD/MM/YYYY", required=True),
                "Monto": st.column_config.NumberColumn("Monto (₡)", format="%d", min_value=0, required=True)
            },
            key="abonos_editor"
        )
        
        # MEJORA: Mostrar resumen de abonos
        if not abonos_df.empty:
            df_valido = abonos_df.dropna(subset=["Fecha", "Monto"])
            if not df_valido.empty:
                total_abonos = df_valido['Monto'].sum()
                st.success(f"✅ **{len(df_valido)} abonos** programados por **₡{total_abonos:,.0f}**")
    
    st.markdown("---")
    
    # Control de Visualización
    st.header("5. Visualización")
    escenario_view = st.selectbox(
        "Seleccionar Escenario a Detallar", 
        ["Todos", "Conservador", "Moderado", "Optimista"]
    )

# --- LÓGICA DE CÁLCULO ---

def calcular_escenario_completo(tasa_bruta_pct, anos, aporte, inicial, comision_pct, inflacion_pct, abonos_extra_df, start_date):
    meses = int(anos * 12)
    
    # --- Procesamiento de Abonos Extraordinarios ---
    abonos_map = {}
    abonos_ignorados = []
    
    if start_date is None:
        start_date = date.today()
    
    # MEJORA: Validación robusta de abonos
    if not abonos_extra_df.empty:
        df_limpio = abonos_extra_df.dropna(subset=["Fecha", "Monto"]).copy()
        
        for index, row in df_limpio.iterrows():
            try:
                fecha_abono = pd.to_datetime(row["Fecha"]).date()
                monto_abono = float(row["Monto"])
                
                # Validar que la fecha sea futura o igual al inicio
                if fecha_abono < start_date:
                    abonos_ignorados.append(f"Fila {index+1}: Fecha {fecha_abono} anterior al inicio")
                    continue
                
                # Calcular meses de diferencia
                diff_meses = (fecha_abono.year - start_date.year) * 12 + (fecha_abono.month - start_date.month)
                
                # Solo sumar si cae dentro del plazo
                if 0 <= diff_meses < meses:
                    if diff_meses in abonos_map:
                        abonos_map[diff_meses] += monto_abono
                    else:
                        abonos_map[diff_meses] = monto_abono
                else:
                    abonos_ignorados.append(f"Fila {index+1}: Fecha fuera del plazo ({anos} años)")
                    
            except ValueError as e:
                abonos_ignorados.append(f"Fila {index+1}: Error al convertir datos - {str(e)}")
            except Exception as e:
                abonos_ignorados.append(f"Fila {index+1}: Error desconocido - {str(e)}")

    # --- Tasas ---
    tasa_neta_nominal_anual = (tasa_bruta_pct / 100) * (1 - (comision_pct / 100))
    tasa_real_neta_anual = ((1 + tasa_neta_nominal_anual) / (1 + (inflacion_pct / 100))) - 1
    tasa_mensual_efectiva = (1 + tasa_neta_nominal_anual)**(1/12) - 1
    
    # OPTIMIZACIÓN: Calcular inflación mensual UNA SOLA VEZ
    inflacion_mensual = (1 + inflacion_pct/100)**(1/12) - 1
    
    # --- Proyección Mes a Mes ---
    valores_nominales = [inicial]
    serie_aportes = [inicial] 
    serie_real = [inicial]   
    
    total_depositado = inicial
    
    for i in range(meses):
        interes = valores_nominales[-1] * tasa_mensual_efectiva
        
        # Verificar abono extra este mes
        extra_este_mes = abonos_map.get(i, 0)
        
        # Totales
        nuevo_saldo = valores_nominales[-1] + interes + aporte + extra_este_mes
        nuevo_aporte_acumulado = total_depositado + aporte + extra_este_mes
        
        # OPTIMIZACIÓN: Calculo de Valor Real mes a mes (sin recalcular inflacion_mensual)
        factor_inflacion_acumulado = (1 + inflacion_mensual)**(i+1)
        nuevo_saldo_real = nuevo_saldo / factor_inflacion_acumulado

        # Guardar en listas
        valores_nominales.append(nuevo_saldo)
        serie_aportes.append(nuevo_aporte_acumulado)
        serie_real.append(nuevo_saldo_real)
        
        total_depositado += (aporte + extra_este_mes)
        
    saldo_final_nominal = valores_nominales[-1]
    saldo_final_real = serie_real[-1]
    
    return {
        "serie_nominal": valores_nominales,
        "serie_aportes": serie_aportes,
        "serie_real": serie_real,
        "saldo_nominal": saldo_final_nominal,
        "saldo_real": saldo_final_real,
        "tasa_real_neta": tasa_real_neta_anual,
        "total_depositado": total_depositado,
        "abonos_ignorados": abonos_ignorados  # NUEVO: Retornar advertencias
    }

escenarios_data = {
    "Conservador": tasa_conservador,
    "Moderado": tasa_moderado,
    "Optimista": tasa_optimista
}

# --- VISUALIZACIÓN ---
# --- VISUALIZACIÓN CON HEADER PREMIUM ---
st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(251, 191, 36, 0.1), rgba(245, 158, 11, 0.05));
    border-left: 4px solid #fbbf24;
    border-radius: 12px;
    padding: 16px 20px;
    margin: 2rem 0 1.5rem 0;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
">
    <h2 style="
        margin: 0;
        font-size: 1.8rem;
        color: #fbbf24;
        font-weight: 700;
    ">
        💰 Resultados de tu Inversión
    </h2>
    <p style="
        margin: 8px 0 0 0;
        color: #94a3b8;
        font-size: 0.95rem;
    ">
        Compara tres escenarios y visualiza el potencial de crecimiento de tu patrimonio
    </p>
</div>
""", unsafe_allow_html=True)

# MEJORA: Mostrar advertencias de abonos ignorados (solo una vez)
advertencias_mostradas = False

cols = st.columns(3)
datos_grafico = pd.DataFrame()
resultados_completos = {}

for (nombre, tasa_input), col in zip(escenarios_data.items(), cols):
    res = calcular_escenario_completo(
        tasa_input, plazo_anos, aporte_mensual, saldo_inicial, comision, inflacion, abonos_df, fecha_inicio
    )
    resultados_completos[nombre] = res
    
    # MEJORA: Mostrar advertencias solo una vez (son iguales para todos los escenarios)
    if not advertencias_mostradas and res["abonos_ignorados"]:
        st.warning(f"⚠️ **{len(res['abonos_ignorados'])} abonos ignorados:**\n\n" + "\n".join(res["abonos_ignorados"][:3]))
        if len(res["abonos_ignorados"]) > 3:
            st.caption(f"... y {len(res['abonos_ignorados']) - 3} más")
        advertencias_mostradas = True
    
    puntos = [res["serie_nominal"][i*12] for i in range(plazo_anos + 1)]
    datos_grafico[nombre] = puntos
    
    with col:
        # --- DISEÑO DE TARJETA UNIFICADO ---
        is_selected = (escenario_view == nombre)
        
        if is_selected:
            border_color = "#4ade80"  
            bg_color = "rgba(74, 222, 128, 0.15)" 
            shadow = "0 0 20px rgba(74, 222, 128, 0.2)"
            icon_header = "🌟"
            opacity = "1"
        else:
            border_color = "rgba(255, 255, 255, 0.15)"
            bg_color = "rgba(30, 41, 59, 0.60)"
            shadow = "0 4px 6px rgba(0, 0, 0, 0.1)"
            icon_header = "🔹"
            opacity = "0.95"

        # MEJORA: Calcular ROI
        ganancia = res['saldo_nominal'] - res['total_depositado']
        roi = (ganancia / res['total_depositado']) * 100 if res['total_depositado'] > 0 else 0

        card_html = f"""
<div style="background-color: {bg_color}; border: 1px solid {border_color}; border-radius: 12px; padding: 20px; box-shadow: {shadow}; margin-bottom: 20px; transition: all 0.3s ease; opacity: {opacity}; backdrop-filter: blur(5px);">
    <h3 style="margin-top: 0; font-size: 1.3rem; color: #fff; border-bottom: 1px solid {border_color}; padding-bottom: 10px; margin-bottom: 15px;">
        {icon_header} {nombre} <span style="font-size: 0.8rem; color: #aaa; font-weight: normal;">({tasa_input}%)</span>
    </h3>
    <div style="margin-bottom: 15px;">
        <div style="font-size: 0.85rem; color: #a0aec0; text-transform: uppercase; letter-spacing: 1px;">Saldo Nominal Futuro</div>
        <div style="font-size: 2rem; font-weight: 700; color: #fff;">₡ {res['saldo_nominal']:,.0f}</div>
    </div>
    <div style="margin-bottom: 20px;">
        <div style="font-size: 0.85rem; color: #a0aec0;">Valor Real (Poder de compra hoy)</div>
        <div style="font-size: 1.4rem; font-weight: 600; color: #48bb78;">₡ {res['saldo_real']:,.0f}</div>
    </div>
    <div style="background-color: rgba(0,0,0,0.2); border-radius: 8px; padding: 12px; font-size: 0.9rem;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
            <span style="color: #cbd5e0;">Inversión:</span>
            <span style="color: #fff; font-weight: 500;">₡ {res['total_depositado']:,.0f}</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
            <span style="color: #cbd5e0;">Ganancia:</span>
            <span style="color: #63b3ed; font-weight: 500;">₡ {ganancia:,.0f}</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 8px; padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.1);">
            <span style="color: #cbd5e0;">📊 ROI:</span>
            <span style="color: #68d391; font-weight: 600; font-size: 1.1rem;">{roi:.1f}%</span>
        </div>
    </div>
</div>
"""
        st.markdown(card_html, unsafe_allow_html=True)

st.markdown("---")

# PESTAÑAS AMPLIADAS
tab1, tab2, tab3, tab4 = st.tabs(["📈 Crecimiento", "🍰 Composición (Interés vs Capital)", "💸 Impacto Inflación", "📋 Tabla Detallada"])

# TAB 1: Gráfico de Crecimiento con estilo premium
with tab1:
    if escenario_view == "Todos":
        st.subheader("📊 Evolución Comparativa de Escenarios")
        
        # Crear gráfico con colores premium
        chart_data = datos_grafico.copy()
        chart_data.index.name = "Año"
        
        st.line_chart(
            chart_data, 
            use_container_width=True,
            color=["#6366f1", "#fbbf24", "#10b981"]  # Índigo, Dorado, Verde
        )
        
        # Panel informativo con diseño premium
        st.markdown("""
        <div style="
            background: linear-gradient(145deg, rgba(30, 41, 59, 0.6), rgba(51, 65, 85, 0.4));
            border: 1px solid rgba(251, 191, 36, 0.2);
            border-radius: 12px;
            padding: 16px;
            margin-top: 16px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        ">
            <div style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                📌 <strong style="color: #fbbf24;">Líneas de proyección:</strong><br>
                <span style="color: #6366f1;">━━</span> <strong>Conservador</strong> | 
                <span style="color: #fbbf24;">━━</span> <strong>Moderado</strong> | 
                <span style="color: #10b981;">━━</span> <strong>Optimista</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.subheader(f"📈 Proyección Detallada - {escenario_view}")
        
        # Color según escenario
        color_map = {
            "Conservador": "#6366f1",
            "Moderado": "#fbbf24", 
            "Optimista": "#10b981"
        }
        
        st.line_chart(
            datos_grafico[escenario_view], 
            use_container_width=True,
            color=color_map[escenario_view]
        )

# Lógica para determinar qué escenario mostrar en los detalles
if escenario_view == "Todos":
    target_escenario = "Moderado"
    aviso_escenario = "Mostrando escenario **Moderado** por defecto (selecciona uno específico en el menú para cambiar)."
else:
    target_escenario = escenario_view
    aviso_escenario = f"Analizando escenario: **{target_escenario}**"

# TAB 2: Gráfico de Área con diseño premium
with tab2:
    st.subheader(f"💎 Composición de Tu Patrimonio - {target_escenario}")
    
    # Banner informativo
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(251, 191, 36, 0.1), rgba(245, 158, 11, 0.05));
        border-left: 4px solid #fbbf24;
        border-radius: 8px;
        padding: 12px 16px;
        margin-bottom: 20px;
        color: #cbd5e1;
        font-size: 0.9rem;
    ">
        {aviso_escenario}
    </div>
    """, unsafe_allow_html=True)
    
    res_target = resultados_completos[target_escenario]
    
    datos_area = pd.DataFrame({
        "💵 Tu Capital": [res_target["serie_aportes"][i*12] for i in range(plazo_anos + 1)],
        "✨ Intereses Compuestos": [(res_target["serie_nominal"][i*12] - res_target["serie_aportes"][i*12]) for i in range(plazo_anos + 1)]
    })
    
    st.area_chart(
        datos_area, 
        color=["#475569", "#fbbf24"],  # Gris oscuro y Dorado
        use_container_width=True
    )
    
    # Insight con diseño premium
    st.markdown("""
    <div style="
        background: linear-gradient(145deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.05));
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 12px;
        padding: 16px;
        margin-top: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    ">
        <div style="color: #10b981; font-weight: 600; font-size: 1rem; margin-bottom: 8px;">
            💡 El Poder del Interés Compuesto
        </div>
        <div style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
            La zona <strong style="color: #fbbf24;">dorada</strong> representa el dinero que trabaja para ti. 
            Con el tiempo, tus intereses generan más intereses, superando incluso tus aportes iniciales.
        </div>
    </div>
    """, unsafe_allow_html=True)

# TAB 3: Nominal vs Real con diseño premium
with tab3:
    st.subheader(f"⚖️ Valor Real vs Nominal - {target_escenario}")
    
    # Banner de advertencia premium
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(251, 191, 36, 0.1), rgba(245, 158, 11, 0.05));
        border-left: 4px solid #fbbf24;
        border-radius: 8px;
        padding: 12px 16px;
        margin-bottom: 20px;
        color: #cbd5e1;
        font-size: 0.9rem;
    ">
        {aviso_escenario}
    </div>
    """, unsafe_allow_html=True)
    
    res_target = resultados_completos[target_escenario]
    
    datos_realidad = pd.DataFrame({
        "💵 Saldo Nominal": [res_target["serie_nominal"][i*12] for i in range(plazo_anos + 1)],
        "💎 Poder de Compra Real": [res_target["serie_real"][i*12] for i in range(plazo_anos + 1)]
    })
    
    st.line_chart(
        datos_realidad, 
        color=["#60a5fa", "#10b981"],  # Azul cielo y Verde esmeralda
        use_container_width=True
    )
    
    # Cálculo de la pérdida por inflación
    perdida_inflacion = res_target["serie_nominal"][-1] - res_target["serie_real"][-1]
    porcentaje_perdida = (perdida_inflacion / res_target["serie_nominal"][-1]) * 100
    
    # Panel de análisis premium
    st.markdown(f"""
    <div style="
        background: linear-gradient(145deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 38, 0.05));
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin-top: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    ">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
            <div style="
                font-size: 2rem;
            ">⚠️</div>
            <div>
                <div style="color: #fbbf24; font-weight: 700; font-size: 1.1rem;">
                    Impacto de la Inflación
                </div>
                <div style="color: #94a3b8; font-size: 0.85rem;">
                    Inflación anual: {inflacion}%
                </div>
            </div>
        </div>
        
        <div style="
            background: rgba(0, 0, 0, 0.3);
            border-radius: 8px;
            padding: 14px;
            margin-top: 12px;
        ">
            <div style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.8;">
                📉 <strong style="color: #ef4444;">Pérdida de poder adquisitivo:</strong><br>
                <span style="font-size: 1.3rem; color: #f87171; font-weight: 700;">₡{perdida_inflacion:,.0f}</span>
                <span style="color: #94a3b8; margin-left: 8px;">({porcentaje_perdida:.1f}% del saldo nominal)</span>
            </div>
        </div>
        
        <div style="
            color: #cbd5e1;
            font-size: 0.85rem;
            margin-top: 14px;
            line-height: 1.6;
            padding-top: 14px;
            border-top: 1px solid rgba(148, 163, 184, 0.2);
        ">
            💡 <strong>Lo que significa:</strong> Aunque tengas ₡{res_target["serie_nominal"][-1]:,.0f} 
            en el futuro, tu poder de compra será equivalente a ₡{res_target["serie_real"][-1]:,.0f} 
            de hoy. La brecha entre ambas líneas representa el "costo invisible" de la inflación.
        </div>
    </div>
    """, unsafe_allow_html=True)

# TAB 4: Tabla con diseño premium y exportación
with tab4:
    st.subheader("📊 Proyección Detallada Año por Año")
    
    # Crear tabla más completa
    tabla_completa = pd.DataFrame()
    tabla_completa["Año"] = range(plazo_anos + 1)
    
    for nombre in escenarios_data.keys():
        res = resultados_completos[nombre]
        tabla_completa[f"{nombre} (Nominal)"] = [res["serie_nominal"][i*12] for i in range(plazo_anos + 1)]
        tabla_completa[f"{nombre} (Real)"] = [res["serie_real"][i*12] for i in range(plazo_anos + 1)]
    
    # Mostrar tabla con formato premium
    st.dataframe(
        tabla_completa.style.format({
            col: "₡ {:,.0f}" for col in tabla_completa.columns if col != "Año"
        }).background_gradient(
            subset=[col for col in tabla_completa.columns if "Nominal" in col],
            cmap="YlOrBr",
            vmin=0
        ),
        use_container_width=True,
        height=400
    )
    
    # Panel de exportación premium
    st.markdown("""
    <div style="
        background: linear-gradient(145deg, rgba(30, 41, 59, 0.6), rgba(51, 65, 85, 0.4));
        border: 1px solid rgba(251, 191, 36, 0.2);
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    ">
        <div style="color: #fbbf24; font-weight: 600; font-size: 1rem; margin-bottom: 12px;">
            📥 Exportar Datos
        </div>
        <div style="color: #cbd5e1; font-size: 0.85rem; margin-bottom: 16px;">
            Descarga la proyección completa en formato CSV para análisis avanzado en Excel o Google Sheets
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Botón de descarga con estilo mejorado
    csv = tabla_completa.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Descargar Proyección Completa (CSV)",
        data=csv,
        file_name=f"proyeccion_inversion_{date.today()}.csv",
        mime="text/csv",
        use_container_width=True
    )
