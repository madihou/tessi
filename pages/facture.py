from datetime import datetime
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from pages.contrat_location import create_leasing_page
from pages.livraison import create_delivery_page
from dash import Input, Output, dcc, html, callback, _dash_renderer

_dash_renderer._set_react_version("18.2.0")


def create_invoice_page():

    layout = dmc.MantineProvider(
        html.Div([
            html.H4("Controle Facture"),
            dmc.Checkbox(checked=False, label="Document Présent", labelPosition="left"),
            html.Br(),
            dbc.Card([
                dbc.CardBody([
                    dmc.Stack([
                        dmc.DateInput(label="Date d'émission",
                                      value=datetime.now().date(),
                                      valueFormat="DD/MM/YYYY"),
                        dmc.Checkbox(checked=False, label="Informations client complet", labelPosition="left"),
                        dmc.Checkbox(checked=False, label="SIRET et/ou RCS présent (attention 14 chiffres)", labelPosition="left"),
                        dmc.Checkbox(checked=False, label="Mention 'véhicule neuf' ou 'VN'", labelPosition="left"),
                        dbc.Row([dbc.Col([html.P("Type de transaction")]),
                                 dbc.Col([dcc.RadioItems(["Achat", "Location", "Non renseignée"], inline=True)])]),
                        dmc.Checkbox(checked=False, label="Date et signature manuscrite", labelPosition="left"),
                        dmc.Checkbox(checked=False, label="Rôle actif et incitatif mentionné avec montant*",
                                     labelPosition="left"),
                        dmc.Text(
                            "*Prime CertiNergy d'un montant de ...€ dans le cadre du dispositif des Certificats d'Economie D'Energie (n° SIREN CertiNergy: 798 641 999)"),
                    ])
                ])
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Button(children="Retour", id="back_pe", color="danger")
                ]),
                dbc.Col([
                    dbc.Button(children="Suivant", id="to_delivery_button")
                ])
            ])
        ], id="invoice_page")
    )

    return layout


@callback(
    Output(component_id="invoice_page", component_property="children"),
    Input(component_id="to_delivery_button", component_property="n_clicks"),
    prevent_initial_call=True
)
def to_delivery_page(_):
    return create_delivery_page()
