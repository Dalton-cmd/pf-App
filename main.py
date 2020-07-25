import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import datetime
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

columns =   ['Transaction Date', 'Category', 'Amount', 'Description']

options =   [{'label':'Grocery', 'value':'Grocery'},
            {'label':'Gas', 'value':'Gas'},
            {'label':'Eating Out', 'value':'Eating Out'}]

optionlist = [{'label':d['label']} for d in options]

table = dash_table.DataTable(columns=[{"name": column, "id": column} for column in columns],
        data=[],
        id='table')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, prevent_initial_callbacks=True)

today = datetime.date.today()

app.layout = html.Div([  #OUTSIDE DIV
    #FRONT PAGE DIVISION
    html.Div([
        #INPUT DIVISION
        html.Div([
            #INPUT HEADER DESCRIPTION
            html.H3('Inputs'),

            #BEGIN CREATING INPUT CORE COMPONENTS
            #TRANSACTION DATE
            html.H6('Date of Transaction'),
            dcc.DatePickerSingle(
                id=columns[0],
                max_date_allowed=datetime.date.today(),
                date = today,
                style={'paddingLeft':'0px'}),

            #TRANSACTION CATEGORY
            html.H6('Transaction Category'),
            dcc.Dropdown(
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
            html.Button("Submit", id="submit"),
            dcc.Store(id='cache', data=[]),

            #CLOSES INPUT DIVISION WITH 1/3RD THE COLUMN WIDTH
            ], className='four columns'),

        #DATATABLE OUTPUT DIVISION
        html.Div([
            html.H6("Plotted Transactions"),
             table
             ], className='eight columns') #CLOSED OUT THE DATATABLE DIV

    ]) #CLOSES FRONT PAGE DIVISION

    #BEGIN PAGE TWO

]) #CLOSES THE OUTER DIV


#CALLBACKS BEGIN HERE:
@app.callback(Output("table", "data"), [Input("submit", "n_clicks")], [State("table", "data")] + [State(columns[0], "date")] +
              [State(column, "value") for column in columns[1:]])
def append(n_clicks, data, *args):
    print(args)
    data.append({columns[i]: arg for i, arg in enumerate(list(args))})
    sample = ({columns[i]: arg for i, arg in enumerate(list(args))})
    print(sample)
    return data


#RUN SERVER
if __name__ == "__main__":
    app.run_server(debug=True)
