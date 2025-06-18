from datetime import datetime
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from pages.immatriculation import create_immatriculation_page
from dash import Input, Output, dcc, html, callback, _dash_renderer

_dash_renderer._set_react_version("18.2.0")


def create_delivery_page():

    layout = dmc.MantineProvider(
        html.Div([
            html.H4("Controle Preuve de Livraison"),
            dmc.Checkbox(checked=False, label="Document Présent", labelPosition="left"),
            html.Br(),
            dbc.Row([dbc.Col([html.P("Document conforme (e.g. pv livraison, décharge de responsabilité, bon de livraison...)")]),
                     dbc.Col([dcc.RadioItems(["Oui", "Non"], inline=True)])]),
            dmc.DateInput(label="Date de livraison",
                          value=datetime.now().date(),
                          valueFormat="DD/MM/YYYY"),
            dmc.Checkbox(checked=False, label="Facture avec mention 'livré le [date]' et signée par le bénéfiaire", labelPosition="left"),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Button(children="Retour", id="back_invoice", color="danger")
                ]),
                dbc.Col([
                    dbc.Button(children="Suivant", id="to_immatriculation_button")
                ])
            ])
        ], id="delivery_page")
    )

    return layout


@callback(
    Output(component_id="delivery_page", component_property="children"),
    Input(component_id="to_immatriculation_button", component_property="n_clicks"),
    prevent_initial_call=True
)
def to_delivery_page(_):
    return create_immatriculation_page()
