from datetime import datetime
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback, _dash_renderer

_dash_renderer._set_react_version("18.2.0")


def create_ah_page():

    layout = dmc.MantineProvider(
        html.Div([
            html.H4("Controle Attestation sur l'Honneur"),
            dmc.Checkbox(checked=False, label="Document Présent", labelPosition="left"),
            html.Br(),
            dbc.Card([])
        ])
    )

    return layout
