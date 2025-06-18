from datetime import datetime
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from pages.statement_page import create_ah_page
from dash import Input, Output, dcc, html, callback, _dash_renderer

_dash_renderer._set_react_version("18.2.0")


def create_immatriculation_page():

    layout = dmc.MantineProvider(
        html.Div([
            html.H4("Controle Certificat d'Immatriculation"),
            dmc.Checkbox(checked=False, label="Document Présent", labelPosition="left"),
            html.Br(),
            dmc.Stack([
                dmc.DateInput(label="Date de 1ère immatriculation",
                              value=datetime.now().date(),
                              valueFormat="DD/MM/YYYY"),
                dmc.Checkbox(checked=False, label="Catégorie M1 ou N1 présent", labelPosition="left"),
                dmc.Checkbox(checked=False, label="Energie électrique", labelPosition="left"),
                dmc.Checkbox(checked=False, label="Numéro d'immatriculation valide (ne commence pas par 'WW')", labelPosition="left"),

            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Button(children="Retour", id="back_cc", color="danger")
                ]),
                dbc.Col([
                    dbc.Button(children="Suivant", id="to_ah_button")
                ])
            ])
        ], id="immatriculation_page")
    )

    return layout


@callback(
    Output(component_id="immatriculation_page", component_property="children"),
    Input(component_id="to_ah_button", component_property="n_clicks"),
    prevent_initial_call=True
)
def to_ah_page(_):
    return create_ah_page()
