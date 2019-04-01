import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd
import datetime

ratios_df = pd.read_csv('ratios.csv').dropna()
streams_df = pd.read_csv('streams.csv').reset_index(drop=True)
top_df = pd.read_csv('top.csv')
options_list = [{'label':artist,'value':artist} for artist in top_df.Artist.unique()]

len = ratios_df.ratio.size
low_ratios_vals = ratios_df.ratio[len-5:len].tolist()
low_ratios_labels = ratios_df.Artist[len-5:len].tolist()

ratios_content = (
    'We were interested in seeing which artist’s listeners tend to stream their music more on weekends than weekdays. We focused on the most popular artists on the Top 200 chart and calculated the ratio of average streams on the weekends to the average streams on weekdays. This means that the larger numbers in this graph represent a higher difference in average number of streams on the weekends than weekdays. For example, people tended to stream Post Malone 8% more on weekends than weekdays.'
)
intro_content = (
    'As a group of ambitious statistics and computer science students first stepping foot into the world of data analysis and visualization, it would be an understatement to describe us as a group of kids in a candy shop. With a fresh understanding of statistical analysis softwares in a world where datasets are as plentiful as tweets about Donald Trump, we are excited to present our findings from our little niche of Spotify data.'
)
user_beh_content = (
    'Inspired by our own avid use of Spotify, we first wanted to delve into user behavior of Spotify, including streaming trends in response to significant events and day to day listening patterns.'
)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

ozuna = go.Scatter(
                x=streams_df[streams_df.Artist == "Ozuna"].Date,
                y=streams_df[streams_df.Artist == "Ozuna"].Streams,
                name = "Ozuna",
                line = dict(color = '#90DAB5'),
                opacity = 0.8)

sheeran = go.Scatter(
                x=streams_df[streams_df.Artist == "Ed Sheeran"].Date,
                y=streams_df[streams_df.Artist == "Ed Sheeran"].Streams,
                name = "Ed Sheeran",
                line = dict(color = '#3F94AB'),
                opacity = 0.8)

malone = go.Scatter(
                x=streams_df[streams_df.Artist == "Post Malone"].Date,
                y=streams_df[streams_df.Artist == "Post Malone"].Streams,
                name = "Post Malone",
                line = dict(color = '#6285B2'),
                opacity = 0.8)

drake = go.Scatter(
                x=streams_df[streams_df.Artist == "Drake"].Date,
                y=streams_df[streams_df.Artist == "Drake"].Streams,
                name = "Drake",
                line = dict(color = '#4B4782'),
                opacity = 0.8)

chainsmokers = go.Scatter(
                x=streams_df[streams_df.Artist == "The Chainsmokers"].Date,
                y=streams_df[streams_df.Artist == "The Chainsmokers"].Streams,
                name = "The Chainsmokers",
                line = dict(color = '#3E3E3E'),
                opacity = 0.8)


stream_ratio = go.Bar(
    x=ratios_df.ratio[0:5].tolist(),
    y=ratios_df.Artist[0:5].tolist(),
    text=[str(i)[0:3] + ' times more weekend streams' for i in ratios_df.ratio[0:5].tolist()],
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

stream_ratio_data = [stream_ratio]
low_stream_ratio_data = [low_stream_ratio]
data = [ozuna,sheeran,chainsmokers,malone,drake]

beer_layout = go.Layout(
    barmode='group',
    title = 'Beer Comparison'
)

layout = go.Layout(
    title = "Streams per Day of Top 5 Artists",
    xaxis = dict(
        range = ['2017-01-01','2017-12-31'])
)

jumbotron = dbc.Jumbotron(
    [
        html.H1("Spotify Through the Ears", className="display-3"),
        html.P(
            "An exploration of bops, beats, bangers, and the listeners who play them"
        )
    ],
    className = 'my-div text-center',
)

stock_fig = go.Figure(data=data, layout=layout)

date_obj = datetime.datetime.today()
date_str = "-".join([str(date_obj.year), str(date_obj.month), str(date_obj.day)])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#artist = streams_df[streams_df.Date == date_str].nlargest(columns=["Streams"], n=1).Artist.values[0]


tab1_content = (
    dbc.Container([
        dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H2("User Behavior"),
                            html.P("On today's date last year, " + str(months[date_obj.month - 1]) + " " + str(date_obj.day) + ", you woud most likely be listening to " + "Drake."),
                            html.P(user_beh_content),
                            dcc.Dropdown(
                                options=options_list,
                                placeholder="Select an artist"
                            )
                        ],
                        md=12,
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H3('Weekend to Weekday Stream Ratios'),
                            html.P(ratios_content),
                            html.P(streams_df.Streams[0:3].tolist())
                        ],
                        md=12,
                    )
                ]
            ),
            dcc.Graph(
                figure={
                    'data':stream_ratio_data
                }
            ),
            dcc.Graph(
                figure={
                    'data':low_stream_ratio_data
                }
            ),
            dcc.Graph(
                id='flyingdog',
                config={
                    "displaylogo": False,
                    'modeBarButtonsToRemove': ['pan2d', 'lasso2d']
                },
                figure=stock_fig
            )
   ]
)
)

tab2_content = (
    html.H2("Our Favorite Artists")
)

tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="User Behavior"),
        dbc.Tab(tab2_content, label="Our Fave Artists")
    ]
)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Introduction"),
                        html.P(intro_content),
                        tabs
                    ],
                    md=12,
                )
            ]
        )
    ],
    className="mt-4",
)

app = dash.Dash(__name__, external_scripts=['https://raw.githubusercontent.com/robin-dela/hover-effect/master/example/js/three.min.js','https://raw.githubusercontent.com/robin-dela/hover-effect/master/example/js/TweenMax.min.js','https://raw.githubusercontent.com/robin-dela/hover-effect/master/dist/hover-effect.umd.js'], external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = html.Div(
    children=[
        jumbotron,
        #html.Video(src="https://streamable.com/s/t5tf2/tklool", autoPlay="True", loop="True", width="100vw"),
        body
    ]
)

if __name__ == '__main__':
    app.run_server()
