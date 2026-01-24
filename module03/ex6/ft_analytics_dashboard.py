
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

    achievements = {
        "alice": {'level_10', 'treasure_hunter', 'speed_demon', 'boss_slayer'},
        "bob": {'first_kill', 'level_10', 'boss_slayer', 'collector'},
        "charlie": {'level_10', 'treasure_hunter', 'perfectionist'},
        "diana": {'speed_demon', 'perfectionist', 'level_10', 'first_kill'},
        "eve": {'first_kill', 'level_10'},
        "frank": {'first_kill', 'treasure_hunter'},
        "grace": {'boss_slayer', 'perfectionist', 'speed_demon', 'level_10'},
        "hank": {'first_kill', 'speed_demon'},
        "ivy": {'boss_slayer', 'speed_demon', 'level_10'},
        "jack": {'first_kill'}
    }

    print("=== Game Analytics Dashboard ===")
    print("\n=== List Comprehensions ===")

    top_perf = [p["name"] for p in data if p['score'] > 2000]
    print(f"Top performers: {top_perf}")  # list

    prem_players = [p['name'] for p in data if p['status'] == "premium"]
    print("Premium Players:", prem_players)
    player = len(data)
    prem_len = len(prem_players)
    rate = (prem_len / player) * 100
    print("Conversion rate:", rate)

    at_risk = [p['score'] for p in data if p['score'] < 500]
    num_at_risk = len(at_risk)
    print("Players at risk:", num_at_risk)

    print("\n=== Sets Comprehensoions ===")

    active_reg = {p['region'] for p in data}
    print("Active regions:", active_reg)

    cluster = {p['cluster'] for p in data}
    print("Total clusters:", len(cluster))

    unique_players = {p['name'] for p in data}
    print("Unique players:", unique_players)

    print("\n=== dict comprehensions ===")

    high_score = {p["name"]: p['score'] for p in data if p['score'] > 2000}
    print("High scorers (2000+):", high_score)
    revenue_reg = {
        reg: sum([p['score'] for p in data if p['region'] == reg])
        for reg in active_reg
    }
    print("Revenue by region:", revenue_reg)

    cluster_dic = {
        clus: len([p for p in data if p["cluster"] == clus])
        for clus in cluster
    }
    print("Player clusters:", cluster_dic)

    print("\n=== Advanced Insights ===")
    # double loop
    recommendations = [
        (p1["name"], p2["name"])
        for p1 in data
        for p2 in data
        if p1["region"] == p2["region"] and p1["name"] < p2["name"]
    ]
    print(f"Recommendation engine: {len(recommendations)} matches generated")

    unique_ach = {
        badge for ach_set in achievements.values()
        for badge in ach_set
                  }
    print("Unique acheivements: ", unique_ach)


if __name__ == "__main__":
    dashboard()
