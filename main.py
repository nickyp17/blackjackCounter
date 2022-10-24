from src.card_counter import TrueCount

if __name__ == "__main__":
    print("-" * 50)
    print("Welcome to my Blackjack card counter application!")
    print("-" * 50)

    print(f"""
    In order to properly count you'll have to input if a high or low card was pulled.
    
    High cards are 10, Jack, Queen, King, and Ace.
    Low cards are 2, 3, 4, 5, and 6.
    
    If a low card is pulled type an 'l' and hit enter.
    If a high card is pulled type an 'h' and hit enter.
    
    To exit the program type 'q' and hit enter.
    ***    
    Have fun counting! And gamble responsibly!
    """)

    print("-" * 50)

    number_of_decks = int(input("How many decks are in play? "))
    true_count = TrueCount(number_of_decks)

    betting_unit = int(input("What is your betting unit? "))

    while True:
        print(f'Current true count: {true_count.total:.2f}')

        card = input("\tWas a high or low card pulled? (h/l): ")

        if card == 'h':
            true_count.high_card_pulled()
        elif card == 'l':
            true_count.low_card_pulled()
        elif card == 'q':
            print("Thanks for playing!")
            break

        betting_amount = (true_count.total - 1) * betting_unit
        print(f'\tBetting amount: {betting_amount:.2f}')

        print('-' * 50)
