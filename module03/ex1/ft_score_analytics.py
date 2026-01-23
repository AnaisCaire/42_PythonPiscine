
import sys


def ft_score_analytics():
    """
    The Score Cruncher Module
    """
    print("=== Player Score Analytics ===")

    if (len(sys.argv) == 1):
        print(
            "No scores provided."
            " Usage: python3 ft_score_analytics.py"
              "<score1> <score2> ..."
            )
        return

    lst = sys.argv[1:]
    processed_scores = []
    for arg in lst:
        try:
            num = int(arg)
            processed_scores.append(num)
        except ValueError as e:
            print(f"Error: {e}")
            continue

    if not processed_scores:
        print("No valid numerical scores were given.")
        return

    print(f"Scores processed: {processed_scores}")
    print(f"Total players: {len(processed_scores)}")

    total_score = sum(processed_scores)
    print(f"Total score: {total_score}")

    avrg_score = total_score / (len(processed_scores))
    print(f"Average score: {avrg_score:.1f}")

    high_score = max(processed_scores)
    print(f"High score: {high_score}")

    low_score = min(processed_scores)
    print(f"Low score: {low_score}")

    range_score = high_score - low_score
    print(f"Score range: {range_score}")


if __name__ == "__main__":
    ft_score_analytics()
