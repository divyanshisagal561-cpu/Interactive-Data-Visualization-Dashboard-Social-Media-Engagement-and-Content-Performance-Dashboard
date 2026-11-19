import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from IPython.display import display

data = {
    "Likes":
       [120, 250, 180, 400, 320,
        150, 500, 280, 350, 220,
        450, 190, 600, 310, 270,
        380, 520, 160, 430, 290,
        700, 340, 210, 480, 390,
        260, 550, 330, 410, 230,
        650, 370, 140, 460, 300,
        580, 420, 200, 510, 360,
        750, 310, 170, 490, 440,
        280, 620, 350, 530, 400],
    "Shares":
       [20, 45, 30, 80, 55,
        25, 100, 40, 65, 35,
        90, 28, 120, 50, 42,
        70, 95, 22, 85, 48,
        140, 60, 32, 105, 75,
        38, 110, 52, 88, 34,
        130, 68, 18, 98, 45,
        115, 78, 26, 108, 58,
        150, 50, 24, 100, 82,
        40, 125, 62, 112, 72],
    "Comments":
       [15, 30, 22, 65, 40,
        18, 85, 28, 50, 25,
        75, 20, 95, 35, 32,
        55, 80, 16, 70, 38,
        110, 45, 24, 90, 60,
        30, 100, 42, 72, 26,
        105, 52, 12, 82, 34,
        92, 62, 18, 88, 44,
        125, 36, 15, 85, 68,
        28, 98, 48, 95, 55],
    "Platform":
        ["Instagram", "YouTube", "Facebook", "Instagram", "LinkedIn",
        "X", "YouTube", "Instagram", "Facebook", "X",
        "Instagram", "LinkedIn", "YouTube", "Facebook", "X",
        "Instagram", "YouTube", "LinkedIn", "Facebook", "Instagram",
        "YouTube", "X", "Facebook", "Instagram", "LinkedIn",
        "X", "YouTube", "Instagram", "Facebook", "LinkedIn",
        "YouTube", "Instagram", "X", "Facebook", "LinkedIn",
        "YouTube", "Instagram", "X", "Facebook", "LinkedIn",
        "YouTube", "Facebook", "X", "Instagram", "LinkedIn",
        "X", "YouTube", "Facebook", "Instagram", "LinkedIn"],
    "Post_Date": pd.date_range
        (start="2026-01-01",
        periods=50,
        freq="D")}

df = pd.DataFrame(data)
display(df)

print("Dataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nDescriptive Statistics:")
display(df.describe())

print("\nPlatform-wise Post Count:")
print(df["Platform"].value_counts())

correlation = df[["Likes", "Shares", "Comments"]].corr()
print("Correlation Matrix:")
display(correlation)

plt.figure(figsize=(7, 5))

plt.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)

plt.colorbar(label="Correlation")

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=30)

plt.yticks(range(len(correlation.columns)), correlation.columns)

for i in range(len(correlation.columns)):
  for j in range(len(correlation.columns)):
    plt.text(j, i, round(correlation.iloc[i, j], 2), ha="center", va="center")

plt.title("Social Media Likes, Shares and Comments Correlation")

plt.tight_layout()

plt.show()

platform_summary = df.groupby("Platform").agg(
    Average_Likes=("Likes", "mean"),
    Average_Shares=("Shares", "mean"),
    Average_Comments=("Comments", "mean"),
    Post_Count=("Likes", "count")).round(2)

print("Platform-wise Engagement Summary:")
display(platform_summary)

platform_likes = df.groupby("Platform")["Likes"].mean().reset_index()

fig = make_subplots(rows=2, cols=2,subplot_titles=(
    "Relationship Between Likes and Comments",
    "Average Likes Differ Across Platforms",
    "Distribution of Likes Across Social Media Posts",
    "Likes Across Post Dates"),
    specs=[[{"type": "xy"},
            {"type": "xy"}],
           [{"type": "xy"},
            {"type": "xy"}]],
           vertical_spacing=0.16,
           horizontal_spacing=0.12)

fig.add_trace(
    go.Scatter(
        x=df["Likes"],
        y=df["Comments"],
        mode="markers",
        marker=dict(
            size=12,
            color=df["Shares"],
            colorscale="Viridis",
            showscale=True,
            colorbar=dict(title="Shares")),
        name="Social Media Posts",
        customdata=df[["Shares", "Platform"]],
        hovertemplate=
        "<b>Social Media Post</b><br>" +
        "Likes: %{x}<br>" +
        "Comments: %{y}<br>" +
        "Shares: %{customdata[0]}<br>" +
        "Platform: %{customdata[1]}<extra></extra>"),
    row=1, col=1
           )

fig.add_trace(
    go.Bar(
        x=platform_likes["Platform"],
        y=platform_likes["Likes"],
        text=platform_likes["Likes"].round(1),
        textposition="outside",
        name="Average Likes",
        hovertemplate=
        "Platform: %{x}<br>" +
        "Average Likes: %{y:.2f}<extra></extra>"),
    row=1, col=2)

fig.add_trace(
    go.Histogram(
        x=df["Likes"],
        nbinsx=8,
        name="Likes Distribution",
        hovertemplate=
        "Likes Range: %{x}<br>" +
        "Number of Posts: %{y}<extra></extra>"),
    row=2, col=1)

date_summary = df.sort_values("Post_Date")

fig.add_trace(
    go.Scatter(
        x=date_summary["Post_Date"],
        y=date_summary["Likes"],
        mode="lines+markers",
        name="Post Likes",
        marker=dict(size=9),
        hovertemplate=
        "Date: %{x|%d %b %Y}<br>" +
        "Likes: %{y}<extra></extra>"),
    row=2, col=2)

fig.update_xaxes(title_text="Likes",row=1, col=1)

fig.update_yaxes(title_text="Comments",row=1, col=1)

fig.update_xaxes(title_text="Social Media Platform",row=1, col=2)

fig.update_yaxes(title_text="Average Likes",row=1, col=2)

fig.update_xaxes(title_text="Likes",row=2, col=1)

fig.update_yaxes(title_text="Number of Posts",row=2, col=1)

fig.update_xaxes(title_text="Post Date",row=2, col=2)

fig.update_yaxes(title_text="Likes",row=2, col=2)

fig.update_layout(
    title=dict(
        text="SOCIAL MEDIA ENGAGEMENT AND CONTENT PERFORMANCE DASHBOARD",
        x=0.5,
        font=dict(size=22)),
    height=850,
    width=1200,
    template="plotly_white",
    showlegend=True,
    hovermode="closest")

fig.show()

fig.write_html("Social_Media_Engagement_Dashboard.html",include_plotlyjs=True)

print("Dashboard exported successfully!")
