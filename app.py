import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Set up the chart
ratios_df = pd.read_csv('ratios.csv')
ratios_list = ratios_df.ratio[1:6].tolist()
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Some other beer']

bitterness = go.Bar(
    x=beers,
    y=[35, 60, 85, 65],
    name='IBU',
    marker={'color':'lightblue'}
)
alcohol = go.Bar(
    x=beers,
    y=[5.4, 7.1, 9.2, 11.3],
    name='ABV',
    marker={'color':'darkgreen'}
)
stream_ratio = go.Bar(
    x=ratios_list,
    y=['x1', 'x2', 'x3', 'x4', 'x5'],
    orientation='h'
)

beer_data = [bitterness, alcohol]
stream_ratio_data = [stream_ratio]
beer_layout = go.Layout(
    barmode='group',
    title = 'Beer Comparison'
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

########### Display the chart

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    children=[
        html.H1('Spotify'),
        dcc.Graph(
            id='flyingdog',
            figure=beer_fig
        ),
        dcc.Graph(
            figure={
                'data':stream_ratio_data
            })
    ]
)

if __name__ == '__main__':
    app.run_server()
