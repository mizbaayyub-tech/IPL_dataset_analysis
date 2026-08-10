import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------

st.set_page_config(
    page_title="IPL Match Analysis Dashboard",
    page_icon="🏏",
    layout="wide"
)

# ---------------------------------------
# LOAD DATA
# ---------------------------------------

df = pd.read_csv("matches.csv")
df.columns = df.columns.str.lower()

# ---------------------------------------
# TITLE
# ---------------------------------------

st.title("🏏 IPL Match Analysis Dashboard")
st.write("Interactive dashboard for analyzing IPL matches.")

# ---------------------------------------
# KPI CARDS
# ---------------------------------------

col1, col2, col3, col4 = st.columns(4)

teams = pd.concat([df["team1"], df["team2"]]).unique()

col1.metric("🏏 Matches", len(df))
col2.metric("👥 Teams", len(teams))
col3.metric("📅 Seasons", df["season"].nunique())
col4.metric("🏙 Cities", df["city"].nunique())

# ---------------------------------------
# SIDEBAR
# ---------------------------------------

st.sidebar.header("Filters")

season = st.sidebar.selectbox(
    "Season",
    ["All"] + sorted(df["season"].unique().tolist())
)

team = st.sidebar.selectbox(
    "Team",
    ["All"] + sorted(list(teams))
)

city = st.sidebar.selectbox(
    "City",
    ["All"] + sorted(df["city"].dropna().unique().tolist())
)

# ---------------------------------------
# FILTER DATA
# ---------------------------------------

filtered_df = df.copy()

if season != "All":
    filtered_df = filtered_df[
        filtered_df["season"] == season
    ]

if team != "All":
    filtered_df = filtered_df[
        (filtered_df["team1"] == team) |
        (filtered_df["team2"] == team)
    ]

if city != "All":
    filtered_df = filtered_df[
        filtered_df["city"] == city
    ]

# ---------------------------------------
# CHART 1
# ---------------------------------------

left, right = st.columns(2)

with left:

    team_wins = filtered_df["winner"].value_counts().reset_index()
    team_wins.columns = ["Team", "Wins"]

    fig = px.bar(
        team_wins.head(10),
        x="Team",
        y="Wins",
        color="Wins",
        text="Wins",
        color_continuous_scale="Turbo",
        template="plotly_white",
        title="Top Winning Teams"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    matches = (
        filtered_df.groupby("season")["id"]
        .count()
        .reset_index()
    )

    matches.columns = ["Season", "Matches"]

    fig = px.line(
        matches,
        x="Season",
        y="Matches",
        markers=True,
        template="plotly_white",
        title="Matches Per Season"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------
# CHART 2
# ---------------------------------------

left, right = st.columns(2)

with left:

    toss = filtered_df["toss_decision"].value_counts().reset_index()
    toss.columns = ["Decision", "Count"]

    fig = px.pie(
        toss,
        names="Decision",
        values="Count",
        hole=0.5,
        color_discrete_sequence=px.colors.qualitative.Bold,
        title="Toss Decision"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    venue = filtered_df["venue"].value_counts().head(10).reset_index()
    venue.columns = ["Venue", "Matches"]

    fig = px.bar(
        venue,
        x="Venue",
        y="Matches",
        color="Matches",
        text="Matches",
        color_continuous_scale="Viridis",
        template="plotly_white",
        title="Top Venues"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------
# CHART 3
# ---------------------------------------

left, right = st.columns(2)

with left:

    player = (
        filtered_df["player_of_match"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    player.columns = ["Player", "Awards"]

    fig = px.bar(
        player,
        x="Player",
        y="Awards",
        color="Awards",
        text="Awards",
        color_continuous_scale="Plasma",
        template="plotly_white",
        title="Top Player of the Match"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    fig = px.treemap(
        team_wins,
        path=["Team"],
        values="Wins",
        color="Wins",
        color_continuous_scale="RdBu",
        title="Team Wins Treemap"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------
# DATA TABLE
# ---------------------------------------

st.subheader("Filtered Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# ---------------------------------------
# DOWNLOAD BUTTON
# ---------------------------------------

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download CSV",
    csv,
    "filtered_ipl_data.csv",
    "text/csv"
)

# ---------------------------------------
# FOOTER
# ---------------------------------------

st.caption("Developed using Python • Pandas • Plotly • Streamlit")