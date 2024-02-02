from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = dcc.Markdown('''
    # Hello World
''')

if __name__ == '__main__':
    app.run(debug=True)