# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_analytics_dashboard.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: acaire-d <acaire-d@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/24 10:38:21 by anaiscaire        #+#    #+#              #
#    Updated: 2026/01/23 12:08:44 by acaire-d         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def session_metrics():
    print("\n=== Engagement Metrics ===")
    daily_active_users = [1250, 1340, 1180, 1420, 1380]
    sessions = [15, 45, 120, 10, 30, 180, 25, 5, 40, 35]
    session_max = max(sessions)
    session_average = sum(sessions)/len(sessions)
    print("Daily active users:", daily_active_users)
    print(f"Session lenght: avg {session_average} min, max {session_max} min")
    total_players = 100
    returning_players = 78

    retention_rate = (returning_players / total_players) * 100
    print(f"Retention rate: {retention_rate:.1f}%")


def dashboard():
    """
    Combining all data quests
    """
    data = [
        {"name": "alice", "score": 2300, "region": "north",
         "status": "premium", "cluster": "normal"},
        {"name": "bob", "score": 1500, "region": "north",
         "status": "normal", "cluster": "competitive"},
        {"name": "charlie", "score": 2150, "region": "east",
         "status": "premium", "cluster": "normal"},
        {"name": "diana", "score": 2050, "region": "central",
         "status": "premium", "cluster": "normal"},
        {"name": "eve", "score": 900, "region": "north",
         "status": "normal", "cluster": "competitive"},
        {"name": "frank", "score": 1800, "region": "east",
         "status": "normal", "cluster": "normal"},
        {"name": "grace", "score": 2500, "region": "central",
         "status": "premium", "cluster": "hardcore"},
        {"name": "hank", "score": 1200, "region": "central",
         "status": "normal", "cluster": "competitive"},
        {"name": "ivy", "score": 2100, "region": "north",
         "status": "premium", "cluster": "hardcore"},
        {"name": "jack", "score": 450, "region": "east",
         "status": "normal", "cluster": "competitive"}
    ]

    print("=== Player Performance Report ===")
    top_perf = [p["name"] for p in data if p['score'] > 2000]
    print(f"Top performers: {top_perf}")
    high_score = {p["name"]: p['score'] for p in data if p['score'] > 2000}
    print("High scorers (2000+):", high_score)
    active_reg = {p['region'] for p in data}
    print("Active regions:", active_reg)

    print("\n=== Revenue Analytics ===")
    region = ["north", "east", "central"]
    revenue_reg = {
        reg: sum([p['score'] for p in data if p['region'] == reg])
        for reg in region
    }
    print("Revenue by region:", revenue_reg)
    prem_players = [p['status'] for p in data if p['status'] == "premium"]
    print("Premium Players:", prem_players)
    player = len(data)
    prem_len = len(prem_players)
    rate = (prem_len / player) * 100
    print("Conversion rate:", rate)

    session_metrics()

    print("=== Advanced Insights ===")
    cluster = ["normal", "hardcore", "competitive"]
    cluster_dic = {
        clus: len([p for p in data if p["cluster"] == clus])
        for clus in cluster
    }
    print("Player clusters:", cluster_dic)
    at_risk = [p['score'] for p in data if p['score'] < 500]
    num_at_risk = len(at_risk)
    print("Churn prediction:", num_at_risk)

    recommendations = [
        (p1["name"], p2["name"])
        for p1 in data
        for p2 in data
        if p1["region"] == p2["region"] and p1["name"] != p2["name"]
    ]
    print(f"Recommendation engine: {len(recommendations)} matches generated")


if __name__ == "__main__":
    dashboard()
