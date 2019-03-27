import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Set up the chart
ratios_df = pd.read_csv('ratios.csv').dropna()
ratios_vals = ratios_df.ratio[0:5].tolist()
ratios_labels = ratios_df.Artist[0:5].tolist()
len = ratios_df.ratio.size
low_ratios_vals = ratios_df.ratio[len-5:len].tolist()
low_ratios_labels = ratios_df.Artist[len-5:len].tolist()
ratios_content = (
    'We were interested in seeing which artist’s listeners tend to stream their music more on weekends than weekdays. We focused on the most popular artists on the Top 200 chart and calculated the ratio of average streams on the weekends to the average streams on weekdays. This means that the larger numbers in this graph represent a higher difference in average number of streams on the weekends than weekdays. For example, people tended to stream Post Malone 8% more on weekends than weekdays.'
)
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
    x=ratios_vals,
    y=ratios_labels,
    text=[str(i)[0:3] + ' times more weekend streams' for i in ratios_vals],
    textposition='auto',
    orientation='h',
    marker=dict(
        color='rgba(158,202,225,0.6)',
        line=dict(
            color='rgba(8,48,107,0.7)',
            width=1
        ),
    )
)
low_stream_ratio = go.Bar(
    x=low_ratios_vals,
    y=low_ratios_labels,
    text=[str(i)[0:3] + ' times more weekday streams' for i in low_ratios_vals],
    textposition='auto',
    orientation='h',
    marker=dict(
        color='rgba(158,202,225,0.6)',
        line=dict(
            color='rgba(8,48,107,0.7)',
            width=1
        ),
    )
)

beer_data = [bitterness, alcohol]
stream_ratio_data = [stream_ratio]
low_stream_ratio_data = [low_stream_ratio]
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
        html.P(ratios_content),
        dcc.Graph(
            figure={
                'data':stream_ratio_data
            }
        ),
        dcc.Graph(
            figure={
                'data':low_stream_ratio_data
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server()
