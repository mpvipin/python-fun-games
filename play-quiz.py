try:
    class Question:
        def __init__(self, prompt, answer):
            self.prompt = prompt
            self.answer = answer


    question_prompts = [
        "What color are apples?\n(a) Red/Green\n(b) Orange\nYour answer__ ",
        "What color are bananas?\n(a) Red/Green\n(b) Yellow\nYour answer__ ",
    ]

    questions = [
        Question(question_prompts[0], "a"),
        Question(question_prompts[1], "b"),
    ]


    def run_quiz(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                score += 1
        print("you got", score, "out of", len(questions))


    run_quiz(questions)

except Exception:
    print("Caught any exception")
