import sys

print("=== Player Score Analytics ===")
num_of_args = len(sys.argv)

if num_of_args == 1:
    print(
        "No scores provided. Usage: "
        "python3 ft_score_analytics.py <score1> <score2> ..."
    )

else:
    try:
        list_of_args = []
        for i in range(1, num_of_args):
            list_of_args.append(int(sys.argv[i]))
        print(f"Scores processed: {list_of_args}")
        print(f"Total players: {len(list_of_args)}")
        print(f"Total score: {sum(list_of_args)}")
        print(f"Average score: {sum(list_of_args) / len(list_of_args)}")
        print(f"High score: {max(list_of_args)}")
        print(f"Low score: {min(list_of_args)}")
        print(f"Score range: {max(list_of_args) - min(list_of_args)}")
    except ValueError:
        print("Error : invalid input, Score needs to be a number!")
