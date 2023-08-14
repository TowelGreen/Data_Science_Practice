import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Row as R , Col as C
from dash import Input, Output, dcc, html
import plotly.express as px
import pandas as pd

trip_df = pd.read_csv("TravelerTrip.csv")

trip_df = trip_df.dropna()

trip_df['Start date']=pd.to_datetime(trip_df['Start date'])
trip_df['Year'] = trip_df['Start date'].dt.year

year_count=trip_df["Year"].value_counts().reset_index()
year_count=year_count.sort_values(by='Year')

accommodation_count =trip_df["Accommodation type"].value_counts().reset_index()


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


fig = px.line(year_count, x = 'Year' , y='count', title='Travel based on year')
fig2 =px.bar(accommodation_count, x= 'Accommodation type',y='count', title='Accommodation ')
fig3 = px.pie(trip_df, names='Transportation type', title='Transportation type')


fig.update_layout(
   xaxis = dict(
      tickmode = 'linear',
      tick0 = 1,
      dtick = 0
   )
)


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Theme Button", className="lead"
        ),
        dbc.Nav(
            [
                dcc.Dropdown(["plotly", "ggplot2", "seaborn", "simple_white", "none"],"plotly",id="dropdown")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


#get id for grpah 


app.layout = html.Div([sidebar,
    R(C(dcc.Graph(figure={},style=CONTENT_STYLE,id="fig1"),width=12)),
    R([C(dcc.Graph(figure={},style=CONTENT_STYLE,id="fig2"),width=7),
    C(dcc.Graph(figure={},style=CONTENT_STYLE,id="fig3"),width=5)])
])


@app.callback(
    Output(component_id='fig1', component_property='figure'),
    Output(component_id='fig2', component_property='figure'),
    Output(component_id='fig3', component_property='figure'),
    Input(component_id='dropdown', component_property='value')
)
def update_graph(theme):
    
    fig = px.line(year_count, x = 'Year' , y='count', title='Travel based on year',template=theme)
    fig2 =px.bar(accommodation_count, x= 'Accommodation type',y='count', title='Accommodation ',template=theme)
    fig3 = px.pie(trip_df, names='Transportation type', title='Transportation type',template=theme)
    return fig,fig2,fig3





if __name__ == '__main__':
    app.run_server(debug=True)