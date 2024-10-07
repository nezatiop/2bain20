class Answer:
    
    def __init__(self, identifiantAns : str, reponses : str):
        self.identifiantAns = identifiantAns
        self.reponses = reponses
    
    def __str__(self):
        return f"[{self.identifiantAns}] {self.reponses}"


class Question:
    
    def __init__(self, identifiantQuest: str, Quest: str):
        self.identifiantQuest = identifiantQuest
        self.Quest = Quest
        self.Ans = []
        self.dico = {}
    
    def add(self,answer: Answer, VF = bool):
        if answer.identifiantAns not in self.dico:
            self.Ans.append({"id" : answer.identifiantAns, "ans" : answer.reponses})
            self.dico[answer.identifiantAns] = VF
            
    def __str__(self):
        resultQ = f"[{self.identifiantQuest}] {self.Quest}\n"
        for anstr in self.Ans:
            vraiorfaux = self.dico[anstr["id"]]
            answer = next((a for a in self.Ans if a["id"] == anstr["id"]), None)
            resultQ += f"    [{answer['id']}] {answer['ans']} ({vraiorfaux})\n"
        return resultQ

    def ask(self, nb: int = 2) -> bool:
        if nb > len(self.Ans):
            print("Pas assez de réponse")
            return False

        true_answers = [ans for ans in self.Ans if self.dico[ans["id"]]]
        false_answers = [ans for ans in self.Ans if not self.dico[ans["id"]]]
        
        is_there_true = False
        selected_answers = []
        
        for _ in range(nb):
            if true_answers and not is_there_true:
                selected_answers.append(true_answers.pop(0))
                is_there_true = True
            if false_answers:
                selected_answers.append(false_answers.pop(0))

        resultAsk = f"{self.Quest}\n"
        for i, answer in enumerate(selected_answers, start=1):
            resultAsk += f"   {i}/ {answer['ans']}\n"

        print(resultAsk)

        choice = input("Votre réponse? ")
        while not choice.isdigit():
            print("Veuillez entrer un nombre valide")
            choice = input("votre réponse? ")
        
        choice = int(choice)
        chosen_answer = selected_answers[choice - 1]

        return self.dico[chosen_answer["id"]]
    


def main():
        
    print("=== Bienvenue dans myQuizz 2.0 ===")

    questions = [
        Question('Q1', 'Quelle est la couleur du chat de Marchand?'),
        Question('Q2', 'Pourquoi Mélotte a un PC de gamer ?'),
        Question('Q3', 'Peut-on contrôler le cerveau de quelqu\'un avec une Arduino?')
    ]

    a1 = Answer('A1', "Il est blanc.")
    a2 = Answer('A2', "Il est rayé.")
    a3 = Answer('A3', "N'importe quoi, il a un Mac.")
    a4 = Answer('A4', "Parce qu'il joue pendant ses pauses.")
    a5 = Answer('A5', "Évidemment, c'est pour cela que les bisseurs 1BA sont tous restés à l'ECAM.")
    a6 = Answer('A6', "Non non, par contre il faut faire attention à la montre de Lurkin.")

    questions[0].add(a1, True)
    questions[0].add(a2, False)
    questions[1].add(a3, True)
    questions[1].add(a4, False)
    questions[2].add(a5, False)
    questions[2].add(a6, True)

    score = 0
    for question in questions:
        if question.ask():
            score += 1

    print("Quizz terminé.")
    print(f"Vous avez un score de {score}/{len(questions)}.")

main()
