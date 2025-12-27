def rock_paper_scissors(player1: str, player2: str) -> str:
    if player1 == player2:
        return "Tie"

    if (
        (player1 == "Rock" and player2 == "Scissors") or
        (player1 == "Paper" and player2 == "Rock") or
        (player1 == "Scissors" and player2 == "Paper")
    ):
        return "Player 1 wins"

    return "Player 2 wins"
