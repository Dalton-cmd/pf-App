import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import datetime
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame(columns=['Date','Category','Amount','Description'])
data = df.to_dict('records')
columns = df.columns
#df = df.to_json()

options =   [{'label':'Grocery', 'value':'Grocery'},
            {'label':'Gas', 'value':'Gas'},
            {'label':'Eating Out', 'value':'Eating Out'}]

optionlist = [{'label':d['label']} for d in options]

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
                    html.Button('Submit', id='submit-button', n_clicks=0,
                        style={'paddingLeft':'7px'}
                            ),
                    ], className='four columns')
                ]),

            html.Div([
                html.H3('Output'),
                dash_table.DataTable(
                    id='datatable',
                    columns=[{
                        'name': '{}'.format(i),
                        'id': '{}'.format(i),
                        'deletable': False,
                        'renamable': False
                    } for i in df.columns],
                    data=[
                    {'column-{}'.format(i): (j + (i-1)*5) for i in range(1, 5)}
                        for j in range(5)],
                    editable=True,
                    row_deletable=True
                    #dropdown={
                    #    'valuetype': {
                    #        'options': optionlist
                    #}
                #}
            )], className="eight columns"),
        ], className="row")
])



@app.callback(
    Output('datatable', 'data'),
    [Input('submit-button', 'n_clicks')],
    [State('datatable', 'data'),
    State('datatable', 'columns'),
    State('dateinput', 'date'),
    State('typeinput', 'value'),
    State('dollarinput', 'value'),
    State('descinput', 'value')
    ])
def add_row(n_clicks, rows, columns, dateinput, typeinput, dollarinput, descinput):
    details = [dateinput, typeinput, dollarinput, descinput]
    details_dict=[{
        'name': '{}'.format(d),
        'id': '{}'.format(d),
        'deletable': False,
        'renamable': False
    } for d in details]

    if n_clicks > 0:
            rows.append({[c['id']    for c in columns] for c in details})
        #rows.append({c['id']: details_dict[0]['id'] for c in columns})
    return rows
'''
    entry=pd.DataFrame({"date": [dateinput], "valuetype": [typeinput], "valuedollar": [dollarinput], "valuedesc": [descinput]})
    entry = entry.set_index("date")
    entry = entry.to_dict("rows")
    entrydata = [dateinput, typeinput, dollarinput, descinput]
'''

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
