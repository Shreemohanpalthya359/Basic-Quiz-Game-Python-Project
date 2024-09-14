def create_question():
    """Creates a question with options and answer."""
    question = input("Enter the question: ")
    options = []
    for i in range(4):
        option = input(f"Enter option {chr(65 + i)}: ")
        options.append(f"{chr(65 + i)}. {option}")
    answer = input("Enter the correct answer(s) (e.g., A, B, C, D): ").strip().upper()
    correct_answers = set(answer.split(","))

    return {
        "question": question,
        "options": options,
        "correct_answers": correct_answers
    }

def run_quiz(quiz):
    """Runs the quiz and calculates the score."""
    score = 0

    for i, item in enumerate(quiz):
        print(f"\nQuestion {i+1}: {item['question']}")
        for option in item['options']:
            print(option)

        answer = input("Enter your answer(s) (e.g., A, B, C ,D): ").strip().upper()
        user_answers = set(answer.split(","))

        if user_answers.issubset(item['correct_answers']):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answers are {', '.join(item['correct_answers'])}.\n")

    print(f"Your final score is {score} out of {len(quiz)}.\n")

def main():
    """Main function to control the quiz game."""
    print("Welcome to the Quiz Game!")

    quiz = []
    custom = input("Do you want to add custom questions? (yes/no): ").strip().lower()

    if custom == 'yes':
        num_custom_questions = int(input("How many custom questions do you want to add? "))
        for _ in range(num_custom_questions):
            quiz.append(create_question())

    run_quiz(quiz)

if __name__ == "__main__":
    main()