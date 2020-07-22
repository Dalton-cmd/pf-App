import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(r'C:\Users\Dalton\Desktop\Python Projects\pf-App\testdf.csv')
#df = df.to_json()

options =   [{'label':'Grocery', 'value':'Grocery'},
            {'label':'Gas', 'value':'Gas'},
            {'label':'Eating Out', 'value':'Eating Out'}]

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.H3('Inputs'),

                    html.H6('Date of Transaction'),
                    dcc.DatePickerSingle(
                        id='dateinput',
                        max_date_allowed=datetime.date.today(),
                        date=datetime.date.today(),
                        style={'paddingLeft':'0px'}
                            ),

                    html.H6('Transaction Category'),
                    dcc.Dropdown(
                        id='typeinput',
                        options=options
                        ),

                    html.H6('Dollar Value'),
                    dcc.Input(
                        id='dollarinput',
                        type='number',
                        debounce=True,
                        placeholder=" Input Dollar Amount ",
                        style={'paddingLeft':'5px',
                                'paddingRight':'40px'}
                            ),

                    html.H6('Description of Transaction'),
                    dcc.Input(
                        id='descinput',
                        type='text',
                        debounce=False,
                        placeholder=" Add Optional Description ",
                        style={'paddingLeft':'5px',
                                'paddingRight':'40px'},
                            ),

                    html.H6('Submit Transaction'),
                    html.Button('Submit', id='submit-button',
                        style={'paddingLeft':'7px'}
                            ),
                    ], className='four columns')
                ]),

            html.Div([
                html.H3('Output'),
                dash_table.DataTable(
                    id='datatable',
                    columns=[{'name':i, 'id':i} for i in df.columns],
                    data=df.to_dict('records'),
                    editable=True,
                    dropdown={
                        'valuetype': {
                            'options': [{'label':i, 'value':i} for i in df['valuetype'].unique()]
                    }
                }
            )], className="eight columns"),
        ], className="row")
])


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})



@app.callback(
    Output('datatable', 'data'),
    [
    Input('submit-button', 'n_clicks')],
    [
    State('dateinput', 'date'),
    State('datatable', 'data'),
    State('typeinput', 'value'),
    State('dollarinput', 'value'),
    State('descinput', 'value')])
def refreshdata(n_clicks, dateinput, datatable, typeinput, dollarinput, descinput):
    print(n_clicks)
    print("n_clicks")
    print(dateinput)
    print("date")
    print(typeinput)
    print(dollarinput)
    print(descinput)
    return data
'''
    print(date),
    print(valuetype),
    print(valuedollar),
    print(valuedesc),
    print(data),
#    data.append({'name':i, 'id':i} for i in df.columns)
'''



'''
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])
'''

if __name__ == "__main__":
    app.run_server(debug=True)
