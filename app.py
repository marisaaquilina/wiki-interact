import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd
import datetime
from plotly import tools
#from dash.dependencies import Input, Output

ratios_df = pd.read_csv('ratios.csv').dropna()
streams_df = pd.read_csv('streams.csv').reset_index(drop=True)
top_streams_df = pd.read_csv('top_streams.csv')
top_df = pd.read_csv('top.csv')
lil_peep_df = pd.read_csv('lil_peep.csv')
x_df = pd.read_csv('x.csv')
f_df = pd.read_csv('mean_features.csv')
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
                x=top_streams_df[top_streams_df.artist == "Ozuna"].date,
                y=top_streams_df[top_streams_df.artist == "Ozuna"].total_streams,
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

lil_peep = go.Scatter(
                x=lil_peep_df["date"],
                y=lil_peep_df["mean_streams"]
)

lil_peep_pos = go.Scatter(
                x=lil_peep_df["date"],
                y=lil_peep_df["max_position"]
)

x_streams = go.Scatter(
                x=x_df["date"],
                y=x_df["mean_streams"]
)

x_pos = go.Scatter(
                x=x_df["date"],
                y=x_df["max_position"]
)

trace0 = go.Scatter(
    x=["2017-11-15", "18-11-09", "18-09-19"],
    y=[0.5, 0.5, 0.5],
    text=['Death', 'Falling Down', 'Album'],
    mode='text',
)

trace_x = go.Scatter(
    x=["17-08-25", "18-03-16", "18-06-18", "18-12-07"],
    y=[0.5, 0.5, 0.5, 0.5],
    text=['17 drops', '? drops', 'XXXTentacion passes', 'Skins drops posthumously'],
    mode='text',
)

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

trace_acou = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_acousticness
)

trace_danc = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_danceability
)

trace_ener = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_energy
)

trace_instr = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_instrumentalness
)

trace_live = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_liveness
)

trace_loud = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_loudness
)

trace_spee = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_speechiness
)

trace_vale = go.Scatter(
    x=f_df.weekday,
    y=f_df.mean_valence
)

fig = tools.make_subplots(rows=4, cols=2, subplot_titles=(
    'Acousticness','Danceability', 'Energy',
    'Instrumentalness', 'Liveness', 'Loudness',
    'Speechiness', 'Valence'
), print_grid=False)

fig.append_trace(trace_ener, 1, 1)
fig.append_trace(trace_loud, 1, 2)

fig.append_trace(trace_acou, 2, 1)
fig.append_trace(trace_danc, 2, 2)

fig.append_trace(trace_spee, 3, 1)
fig.append_trace(trace_instr, 3, 2)

fig.append_trace(trace_live, 4, 1)
fig.append_trace(trace_vale, 4, 2)

fig['layout'].update(height=1200, width=800)

stream_ratio_data = [stream_ratio]
low_stream_ratio_data = [low_stream_ratio]
top_data = [ozuna,sheeran,chainsmokers,malone,drake]
lil_peep_data = [lil_peep, trace0]
lil_peep_pos_data = [lil_peep_pos, trace0]
x_streams_data = [x_streams, trace_x]
x_pos_data = [x_pos, trace_x]

beer_layout = go.Layout(
    barmode='group',
    title = 'Beer Comparison'
)

top_layout = go.Layout(
    title = "Streams per Day of Top 5 Artists",
    xaxis = dict(
        range = ['2017-01-01','2017-12-31']
    )
)

lil_peep_layout = {
    'xaxis': {
        'range': ['2017-10-01','2019-06-01']
    },
    'yaxis': {
        'range': [0, 2500000]
    },
    'shapes': [
        # Line Vertical Death
        {
            'type': 'line',
            'x0': "2017-11-15",
            'y0': 0,
            'x1': "2017-11-15",
            'y1': 2500000,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        # Line Vertical Falling Down
        {
            'type': 'line',
            'x0': "18-11-09",
            'y0': 0,
            'x1': "18-11-09",
            'y1': 2500000,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        # Line Vertical Album
        {
            'type': 'line',
            'x0': "18-09-19",
            'y0': 0,
            'x1': "18-09-19",
            'y1': 2500000,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
    ]
}

lil_peep_pos_layout = {
    'xaxis': {
        'range': ['2017-10-01','2019-06-01']
    },
    'yaxis': {
        'range': [0, 250]
    },
    'shapes': [
        # Line Vertical Death
        {
            'type': 'line',
            'x0': "2017-11-15",
            'y0': 0,
            'x1': "2017-11-15",
            'y1': 250,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        # Line Vertical Falling Down
        {
            'type': 'line',
            'x0': "18-11-09",
            'y0': 0,
            'x1': "18-11-09",
            'y1': 250,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        # Line Vertical Album
        {
            'type': 'line',
            'x0': "18-09-19",
            'y0': 0,
            'x1': "18-09-19",
            'y1': 250,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
    ]
}

x_streams_layout = {
    'xaxis': {
        'range': ['2017-01-01','2019-06-01']
    },
    'yaxis': {
        'range': [0, 2500000]
    },
    'shapes': [
        # Line Vertical Death
        {
            'type': 'line',
            'x0': "18-06-18",
            'y0': 0,
            'x1': "18-06-18",
            'y1': 1100000,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        # Line Vertical ?
        {
            'type': 'line',
            'x0': "18-03-16",
            'y0': 0,
            'x1': "18-03-16",
            'y1': 1100000,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        # Line Vertical Skins
        {
            'type': 'line',
            'x0': "18-12-7",
            'y0': 0,
            'x1': "18-12-7",
            'y1': 1100000,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        # Line Vertical 17
        {
            'type': 'line',
            'x0': "17-08-25",
            'y0': 0,
            'x1': "17-08-25",
            'y1': 1100000,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
    ]
}

jumbotron = dbc.Jumbotron(
    [
        html.H1("Spotify Through the Ears", className="display-3"),
        html.P(
            "An exploration of bops, beats, bangers, and the listeners who play them"
        )
    ],
    className = 'my-div text-center',
)

stock_fig = go.Figure(data=top_data, layout=top_layout)

peep_fig = go.Figure(data = lil_peep_data, layout = lil_peep_layout)
peep_pos_fig = go.Figure(data = lil_peep_pos_data, layout = lil_peep_pos_layout)
x_streams_fig = go.Figure(data=x_streams_data, layout=x_streams_layout)
x_pos_fig = go.Figure(data=x_pos_data, layout=x_streams_layout)
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
                            html.Div([
                                dcc.Dropdown(
                                id='my-dropdown',
                                options=options_list,
                                placeholder="Select an artist"
                                ),
                                html.Div(id='output-container')
                            ])
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
            ),
            dcc.Graph(
                    figure=fig
                )
   ]
)
)

tab2_content = (
    html.H2("Our Favorite Artists"),
    dcc.Graph(
        figure= peep_fig
    ),
    dcc.Graph(
        figure= peep_pos_fig
    ),
    dcc.Graph(
        figure= x_streams_fig
    ),
    dcc.Graph(
        figure=x_streams_fig
    )
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
        body
    ]
)

#@app.callback(
#    dash.dependencies.Output('output-container', 'children'),
#    [dash.dependencies.Input('my-dropdown', 'value')])

#def update_output(value):
#    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
