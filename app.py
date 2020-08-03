import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import datetime

#SETS THE SPECIFIC COLUMNS FOR OUR GRAPH AND DATATABLE
columns =   ['Transaction Date', 'Category', 'Amount', 'Description']

#CREATES THE VARIOUS CATEGORIES
categories = ['Grocery', 'Gas', 'Eating Out', 'Movies', 'Games', 'Misc.']

#DICTIONARY COMPREHENSION TO DEVELOP A KEY/VALUE FOR ALL CATEGORIES
options = [{'label': i, 'value': i} for i in categories]

#CREATES THE DATATABLE
table = dash_table.DataTable(columns=[{"name": column, "id": column} for column in columns],
        editable=False,
        row_deletable=True,
        data=[],
        dropdown={
            'category': {
                'options': options
            }
        },
        page_size=12,
        id='table')

#CREATES APPLICATION
app = dash.Dash(__name__)

#DEFINES THE LAYOUT OF OUR APPLICATION AND THE EMBEDDED CORE COMPONENTS
app.layout = html.Div([  #OUTSIDE DIV

    #SETTING TABS (ENCOMPASSES THE FRONT AND BACK PAGE DIVISION)
    dcc.Tabs([

    #FRONT PAGE DIVISION
    dcc.Tab(label='TAB ONE',
            children=[
        #INPUT DIVISION
        html.Div([
            #INPUT HEADER DESCRIPTION
            html.H3('Inputs'),

            #BEGIN CREATING INPUT CORE COMPONENTS
            #TRANSACTION DATE
            html.H6('Date of Transaction'),
            dcc.DatePickerSingle(
                className='dropdown',
                id=columns[0],
                max_date_allowed=datetime.date.today(),
                date = datetime.date.today(),
                style={'paddingLeft':'0px'}),

            #TRANSACTION CATEGORY
            html.H6('Transaction Category'),
            dcc.Dropdown(
                className="dropdown",
                id=columns[1],
                options=options),

            #TRANSACTION DOLLAR VALUE
            html.H6('Dollar Value'),
            dcc.Input(
                id=columns[2],
                type='number',
                debounce=True,
                placeholder=" Input Dollar Amount "),

            #TRANSACTION DESCRIPTION
            html.H6('Description of Transaction'),
            dcc.Input(
                id=columns[3],
                type='text',
                debounce=False,
                placeholder=" Add Optional Description "),

            #SUBMIT BUTTON
            html.H6("Submit Transaction Details"),
            html.Button("Submit", id="submit", className='dropdown'),
            dcc.Store(id='cache', data=[]),

            #CLOSES INPUT DIVISION WITH 1/3RD THE COLUMN WIDTH
            ], className='four columns'),

        #DATATABLE OUTPUT DIVISION
        html.Div([
            dcc.Tabs([

                #BEGIN INNER TAB ONE - DATATABLE
                dcc.Tab(label='DATATABLE',
                    children=[
                        html.H3("Transaction Detail"),
                        table
                 ]), #CLOSES OUT TAB ONE

                 #BEGIN INNER TAB TWO - GRAPH
                 dcc.Tab(label='GRAPH',
                    children=[
                        html.H3("Plotted Transactions"),
                        html.Div(id='table-graph-output'),
                  ]) #CLOSES OUT TAB TWO

                  ], className='custom-tab'), #CLOSES OUT TABS
            ], className='eight columns') #CLOSES OUT DATATABLE OUTPUT DIVISION


    ]), #CLOSES FRONT PAGE DIVISION

    #BEGIN TAB TWO
    dcc.Tab(label='TAB TWO', children=[
    dcc.Graph(
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [1, 4, 1],
                        'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [1, 2, 3],
                     'type': 'bar', 'name': u'Montréal'},
                    ]
                }
            )

    ]) #CLOSES TAB TWO

    ], className='custom-tabs' ), #CLOSES OUT TABS

],className='container') #CLOSES THE OUTER DIV


#CALLBACKS BEGIN HERE

#Update Datatable
@app.callback(Output("table", "data"),
            [Input("submit", "n_clicks")],
            [State("table", "data")]+
            [State(columns[0], "date")] +
            [State(column, "value") for column in columns[1:]])
def append(n_clicks, data, *args):
    data.append({columns[i]: arg for i, arg in enumerate(list(args))})
    return data

@app.callback(
Output('table-graph-output', "children"),
[Input('table', "data")])
def update_graph(rows):
    dff = pd.DataFrame(rows)
    return html.Div(
    [
        dcc.Graph(
            id=column,
            figure={
                "data": [
                    {
                        "x": dff["Transaction Date"],
                        "y": dff["Amount"],
                        "type": "bar",
                        "marker": {"color": "#0074D9"},
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {"automargin": True},
                    "height": 250,
                    "margin": {"t": 10, "l": 10, "r": 10},
                },
            },
        )
        for column in ["pop", "lifeExp", "gdpPercap"]
    ]
)

#RUN SERVER
if __name__ == "__main__":
    app.run_server(debug=True)
