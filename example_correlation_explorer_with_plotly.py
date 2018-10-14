#######
# Super Simple Correlation Explorer
# 
# Choose Two Variables, Scatter Plot Results and 
# Use scipy.stats to run linear regression and plot a best fit line
# Built with Plot.ly, Dash and Flask
# 
# Part of QS Ledger github.com/markwk/qs_ledger
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from scipy import stats

# import data
df = pd.read_csv('data/combined_personal_data.csv')

# a bit of a cleanup, might be unnecessary in your case
df.drop([0], inplace=True)
df.drop('Unnamed: 0', axis=1, inplace=True)

app = dash.Dash()

# let's use all of of the columns as features for now
features = df.columns

app.layout = html.Div([
             html.Div([
                 dcc.Dropdown(id='xaxis',
                             options=[{'label': i, 'value': i} for i in features],
                             value='ProjectTime')
             ], style={'width': '48%','display':'inline-block'}),
             html.Div([
                 dcc.Dropdown(id='yaxis',
                              options=[{'label': i, 'value': i} for i in features],
                             value='Songs')
             ], style={'width': '48%','display':'inline-block'}),
            dcc.Graph(id='feature-graphic'),
            dcc.Markdown(
                id='correlation_stats'
            )
],style={'padding':10})

@app.callback(Output('feature-graphic','figure'),
             [Input('xaxis', 'value'),
              Input('yaxis', 'value')])
def update_graph(xaxis_name, yaxis_name):
     # we need to check for matching data in both columns
    temp_df = df[[xaxis_name,yaxis_name]].dropna()
    x = temp_df[xaxis_name]
    y = temp_df[yaxis_name]

    # Generated linear fit
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    line = slope*x+intercept
    
    fig = {'data':[go.Scatter(x=df[xaxis_name],
                               y=df[yaxis_name],
                               text=df['Date'],
                               mode='markers',
                               name="{} vs. {}".format(xaxis_name, yaxis_name),
                               marker={'size':5,
                                      'opacity':0.5,
                                      'line':{'width':0.5, 'color':'white'}})
                    ,
                    go.Scatter(
                      x=x,
                      y=line,
                      mode='lines',
                      marker=go.Marker(color='rgb(31, 119, 180)'),
                      name='Fit'
                     )]
            ,'layout':go.Layout(
                title='Simple Correlation Explorer for QS Ledger',
                xaxis={'title':xaxis_name},
                yaxis={'title':yaxis_name},
                hovermode='closest'
            )
           }
    
    return fig

@app.callback(
    Output('correlation_stats', 'children'),
    [Input('xaxis', 'value'),
    Input('yaxis', 'value')])
def callback_stats(xaxis_name, yaxis_name):    
    # we need to check for matching data in both columns
    temp_df = df[[xaxis_name,yaxis_name]].dropna()
    x = temp_df[xaxis_name]
    y = temp_df[yaxis_name]

    # Generated linear fit
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    line = slope*x+intercept
    
    correlation_stats = """
        X-Variable: {}
        Y-Variable: {}
        p_value: {}
        r_value: {}
        std_err: {}
        """.format(xaxis_name, yaxis_name, p_value, r_value, std_err)
    return correlation_stats

if __name__ == '__main__':
    app.run_server()