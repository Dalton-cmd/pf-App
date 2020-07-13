import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.H3('Inputs'),
                    html.H6('Transaction Category'),
                    dcc.Dropdown(
                        id='type-input',
                        options=[
                            {'label':'Grocery', 'value':'Grocery'},
                            {'label':'Gas', 'value':'Gas'},
                            {'label':'Eating Out', 'value':'Eating Out'},
                                ]),

                    html.H6('Dollar Value'),
                    dcc.Input(
                        id='dollar-input',
                        type='number',
                        debounce=True,
                        placeholder=" Input Dollar Amount ",
                        style={'paddingLeft':'5px',
                                'paddingRight':'40px'}
                            ),

                    html.H6('Date of Transaction'),
                    dcc.Input(
                        id='desc-input',
                        type='text',
                        debounce=False,
                        placeholder=" Add Optional Description ",
                        style={'paddingLeft':'5px',
                                'paddingRight':'40px'},
                            ),

                    html.H6('Date of Transaction'),
                    dcc.DatePickerSingle(
                        id='date-input',
                        max_date_allowed=datetime.date.today(),
                        date=datetime.date.today(),
                        style={'paddingLeft':'0px'}
                            ),

                    html.H6('Submit Transaction'),
                    html.Button('Submit', id='submit-input',
                        style={'paddingLeft':'7px'}
                            ),
                    ], className='four columns')
                ]),

            html.Div([
                html.H3('Output'),
                dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}]})
            ], className="eight columns"),
        ], className="row")
])


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


if __name__ == "__main__":
    app.run_server()
