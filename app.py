from dash import Dash, html, dcc, dash_table
import pandas as pd

gsheetid="135cX5zTfeL0NJfN_uxFWi5W91Jf2WdddBp76sdOMh60"
sheet_name="Bugdata"
gsheet_url="https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

df = pd.read_csv(gsheet_url)

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Salubrity App'),
    dash_table.DataTable(data=df.to_dict('records'))
])

if __name__ == '__main__':
    app.run(debug=True)