from motiondetect import df

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource


df['Start_string'] = df['Start'].dt.strftime("%Y-$m-%d %H:%M:%S")
df['End_string'] = df['End'].dt.strftime("%Y-$m-%d %H:%M:%S")

cds = ColumnDataSource(df)

f = figure(title='Motion Graph', x_axis_type="datetime",
           height=150, width=150, sizing_mode="stretch_both")
f.yaxis.ticker.desired_num_ticks = 1

hover = HoverTool(
    tooltips=[("Start ", "@Start_string"), ("End ", "@End_string")])
f.add_tools(hover)

plot = f.quad(left='Start', right='End',
              top=1, bottom=0, color='green', source=cds)
output_file("motiongraph1.html")
show(f)
