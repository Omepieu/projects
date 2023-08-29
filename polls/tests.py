from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question

def creer_question(question_text, jour):
    """
    créer une question avec `question_text`  qu'on lui donne et `jour` on lui donne nombre de jour qui puliera
    """
    heure = timezone.now()+datetime.timedelta(days=jour)
    return Question.objects.create(question_text=question_text, pub_date=heure)

# class QuestionModelTests(TestCase):
#     def test_fut_publication_plus_recent(self):
#         """
#         was_published_recently() retourne False de question whose pub_date
#         est dans le future.
#         """
#         time = timezone.now() + datetime.timedelta(days=1)
#         future_question = Question(pub_date=time)
#         self.assertIs(future_question.fut_publier_recent(), False)

#     def test_fut_publier_plus_recent_avec_ancienne_question(self):

#         time = timezone.now() - datetime.timedelta(days=1, seconds=1)
#         old_question = Question(pub_date=time)
#         self.assertIs(old_question.fut_publier_recent(), False)
    
#     def test_fut_publier_recent_question(self):

#         time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
#         recent_question = Question(pub_date=time)
#         self.assertIs(recent_question.fut_publier_recent(), True)

class QuestionIndexViewTests(TestCase):
    def test_non_questions(self):
        """
        Si les questions n'existent pas, on affiche un message approprie
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Polls n'est pas disponible")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_question_passe(self):
        """
        Questions avec une `pub_date` dans le passe est afficherai dans la page index 
        """
        question = creer_question(question_text="question est passe", jour=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question]
        )

    def test_question_futur(self):
        """
        Si les questions dans le futur ne doivent pas affihe dans la vue index, elles doivent afficher si date dispo
        """
        creer_question(question_text="question est au futur", jour=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "Polls n'est pas disponible")
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            []
        )
    
    def test_question_passe_et_futur(self):
        """
        Si les questions dans le passe et futur existent, afficher uniquement les questions dans le passe
        """
        question = creer_question(question_text="Deuxième question où la date est passe", jour=-30)
        creer_question(question_text="Deuxième question où la date est au futur", jour=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "Polls n'est pas disponible")
        self.assertQuerysetEqual(
            response.context["latest_question_list"], 
            [question]
        )
    def test_deux_questions_passe(self):
        """
        les questions où la date passe 
        """
        question1 = creer_question(question_text="Question 1, la date est passe", jour=-30)
        question2 = creer_question(question_text="Question 2, la date est passe", jour=-6)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [question1],
            [question2]

        )

class QuestionDetailViewTests(TestCase):

        def test_question_futur(self):
            question_futur = creer_question(question_text="Question dans le futur", jour=6)
            url = reverse("polls:detail", args=(question_futur.id,))
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)

        def test_questin_passe(self):
            question_passe = creer_question(question_text="Question dans le futur", jour=-6)
            url =reverse("polls:detail", args=(question_passe.id))
            response = self.client.get(url)
            self.assertContains(response, question_passe.question_text)
