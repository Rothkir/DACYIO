import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import requests
import discord
from io import BytesIO




def graph_history(id):
    url = f"https://steampricehistory.com/api/{id}"
    r = requests.get(url)
    data = r.json()
    
    prev_y = data[0]["y"]
    x = []
    y = []
    for d in data:
        x.append(dt.datetime.fromtimestamp(int(str(d["x"])[:-3])))
        y.append(prev_y)
        x.append(dt.datetime.fromtimestamp(int(str(d["x"])[:-3])))
        y.append(d["y"])

        prev_y = d["y"]

    fig = plt.figure()
    axes = fig.add_subplot()
    axes.plot(x, y, "orange")
    axes.set_title("Price evolution")
    axes.set_xlabel("Time")
    axes.set_ylabel("Price in USD")

    with BytesIO() as buf:
        plt.savefig(buf, dpi=150, fontweight = "bold")
        buf.seek(0)
        return discord.File(fp=buf, filename="Graph.png")