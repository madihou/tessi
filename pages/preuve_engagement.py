from datetime import datetime
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from pages.facture import create_invoice_page
from dash import Input, Output, dcc, html, callback, _dash_renderer

_dash_renderer._set_react_version("18.2.0")


def create_pe_page():

    layout = dmc.MantineProvider(
        html.Div([
            html.H4("Controle Preuve d'Engagement"),
            dmc.Checkbox(checked=False, label="Document Présent", labelPosition="left"),
            html.Br(),
            dbc.Row([dbc.Col([html.P("Document conforme (e.g. bon de commande, devis...)")]),
                     dbc.Col([dcc.RadioItems(["Oui", "Non"], inline=True)])]),
            html.Br(),
            dbc.Card([
                dbc.CardBody([
                    dmc.Stack([
                        dmc.DateInput(label="Date d'édition (date du jour si non renseignée)",
                                      value=datetime.now().date(),
                                      valueFormat="DD/MM/YYYY"),
                        dbc.Row([dbc.Col([html.P("Type de transaction")]),
                                 dbc.Col([dcc.RadioItems(["Achat", "Location", "Non renseignée"], inline=True)])]),
                        dmc.Checkbox(checked=False, label="Date et signature manuscrite", labelPosition="left"),
                        dmc.Checkbox(checked=False, label="Rôle actif et incitatif mentionné avec montant*", labelPosition="left"),
                        dmc.Text("*Prime CertiNergy d'un montant de ...€ dans le cadre du dispositif des Certificats d'Economie D'Energie (n° SIREN CertiNergy: 798 641 999)"),
                        dmc.Checkbox(checked=False, label="Signature du bénéficiaire avec nom et prénom", labelPosition="left"),
                    ])
                ])
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Button(children="Retour", id="back_cc", color="danger")
                ]),
                dbc.Col([
                    dbc.Button(children="Suivant", id="to_invoice_button")
                ])
            ])
        ], id="pe_page")
    )

    return layout


@callback(
    Output(component_id="pe_page", component_property="children"),
    Input(component_id="to_invoice_button", component_property="n_clicks"),
    prevent_initial_call=True
)
def to_pe_page(_):
    return create_invoice_page()
