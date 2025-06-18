from datetime import datetime
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from pages.preuve_engagement import create_pe_page
from dash import Input, Output, dcc, html, callback, _dash_renderer

_dash_renderer._set_react_version("18.2.0")


def create_cc_page():

    layout = dmc.MantineProvider(
        html.Div([
            html.H4("Controle Cadre de Contribution"),
            dmc.Checkbox(checked=False, label="Document Présent", labelPosition="left"),
            html.Br(),
            dbc.Card([
                dbc.CardBody([
                    dmc.Stack([

                        dmc.DateInput(label="Date de Signature (date du jour si non renseigné).",
                                      value=datetime.now().date(),
                                      valueFormat="DD/MM/YYYY"),
                        dmc.Checkbox(checked=False, label="3 logos apparent", labelPosition="left"),
                        dmc.NumberInput(label="Montant de la prime CEE (0 si non renseignée)", value=0),
                        dmc.Checkbox(checked=False, label="Daté et signé par le professionnel", labelPosition="left"),
                        dmc.Checkbox(checked=False, label="Daté et signé par le beneficiaire", labelPosition="left"),
                        dmc.Checkbox(checked=False, label="Daté et signé par le professionnel", labelPosition="left"),
                        dmc.TextInput(label="Nom bénéficiaire"),
                        dmc.TextInput(label="Prénom bénéficiaire"),
                        dmc.Checkbox(checked=False, label="Coordonnée du professionnel apparent", labelPosition="left"),
                    ])
                ])
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Button(children="Retour", id="back_main_page", color="danger")
                ]),
                dbc.Col([
                    dbc.Button(children="Suivant", id="to_pe_button")
                    ])
            ])
        ], id="cc_page")
    )

    return layout


@callback(
    Output(component_id="cc_page", component_property="children"),
    Input(component_id="to_pe_button", component_property="n_clicks"),
    prevent_initial_call=True
)
def to_pe_page(_):
    return create_pe_page()
