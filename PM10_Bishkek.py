import pandas as pd
import plotly.graph_objects as go
import os

file_path = r'C:\Users\User\OneDrive\Desktop\DataSet_Bishkek_PM10.csv'

if os.path.exists(file_path):
    df = pd.read_csv(file_path, parse_dates=['Date'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['Date'], y=df['PM10_Min'],
        line=dict(width=0),
        showlegend=False,
        hoverinfo='skip'
    ))

    fig.add_trace(go.Scatter(
        x=df['Date'], y=df['PM10_Max'],
        fill='tonexty',
        fillcolor='rgba(135, 206, 250, 0.15)',
        line=dict(color='rgba(255,255,255,0.2)', width=1),
        name='Range (Min-Max)',
        hoverinfo='skip'
    ))

    fig.add_trace(go.Scatter(
        x=df['Date'], y=df['PM10_Avg'],
        mode='lines+markers',
        name='PM10 Average',
        line=dict(color='#A2D149', width=3.5, shape='spline'),
        marker=dict(
            size=11,
            color='#A2D149',
            symbol='circle',
            line=dict(color='white', width=1.5)
        ),
        hovertemplate='<b>%{y}</b> µg/m³<extra></extra>',
    ))

    fig.add_shape(
        type="line", x0=df['Date'].min(), y0=45, x1=df['Date'].max(), y1=45,
        line=dict(color="#4682B4", width=2, dash="dashdot"),
    )

    fig.add_annotation(
        x=df['Date'].max(), y=45,
        text="WHO 24h Limit (45 µg/m³)",
        showarrow=False,
        yshift=10,
        font=dict(color="#4682B4", size=11),
        xanchor="right"
    )

    peak_idx = df['PM10_Avg'].idxmax()
    fig.add_annotation(
        x=df['Date'][peak_idx], y=df['PM10_Avg'][peak_idx],
        text="Monthly<br>Peak",
        showarrow=True,
        arrowhead=2,
        arrowcolor='white',
        ax=0, ay=-50,
        font=dict(color='white', size=12),
        bordercolor='white', borderwidth=1, borderpad=4,
        bgcolor='rgba(162, 209, 73, 0.4)'
    )

    fig.update_layout(
        title={
            'text': "<b>Air Quality: Bishkek</b><br><sup>PM10 Concentration (µg/m³) — April 2026</sup>",
            'y': 0.95, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top',
            'font': dict(size=22, color='white')
        },
        plot_bgcolor='#161A1D',
        paper_bgcolor='#1E2128',
        font=dict(color='white'),
        xaxis=dict(
            showgrid=True, gridcolor='#2A3135',
            tickformat='%a, %d %b',
            dtick="86400000.0" * 2
        ),
        yaxis=dict(
            showgrid=True, gridcolor='#2A3135',
            title=dict(text="Concentration (µg/m³)", font=dict(size=14)),
            range=[0, df['PM10_Max'].max() + 10]
        ),
        legend=dict(
            orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5
        ),
        margin=dict(l=60, r=60, t=110, b=90),
        hovermode='x unified',
        template='plotly_dark'
    )

    fig.show()
else:
    print("File not found. Please check the path.")
