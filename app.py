import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from pages.cadre_contribution import create_cc_page
from dash import Dash, Input, Output, dcc, html, callback, _dash_renderer
_dash_renderer._set_react_version("18.2.0")


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP] + dmc.styles.ALL)

app.layout = dmc.MantineProvider(
    html.Div([
        html.H1("Certinergy C1 Contrat Validation"),
        html.Br(),
        html.Hr(),
        html.Div([
            html.H4("Initialisation Nouveau Contrat"),
            html.Br(),
            html.H6("Type de document: "),
            dcc.RadioItems(["TRA-EQ-114", "TRA-EQ-117"]),
            html.Br(),
            html.H6("Type de transaction: "),
            dcc.RadioItems(["Achat", "Location", "Non renseigné"], inline=True),
            html.Br(),
            dbc.Row([
                dbc.Col([dbc.Card(
                    dbc.CardBody([
                        html.H6("Informations Bénéficiaire:"),
                        dmc.TextInput(label="Nom"),
                        dmc.TextInput(label="Prénom"),
                        dmc.TextInput(label="Adresse")
                    ])
                )]),
                dbc.Col([dbc.Card(
                    dbc.CardBody([
                        html.H6("Informations Professionnel:"),
                        dmc.TextInput(label="Raison sociale")
                    ])
                )])
            ]),
            html.Br(),
            dbc.Button(children="Suivant", id="to_cc_button")
        ], id="main_page")
    ])
)


@callback(
    Output(component_id="main_page", component_property="children"),
    Input(component_id="to_cc_button", component_property="n_clicks"),
    prevent_initial_call=True
)
def to_cc_page(_):
    return create_cc_page()


if __name__ == "__main__":
    app.run(debug=True)
