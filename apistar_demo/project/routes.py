from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes
#from project.views import welcome
from apistar import Include, Route
from project.views import  create_poll, create_choices, students, students_id

routes = [
          # API to create Polls
          Route('/create_poll', 'POST', create_poll),
          # API to add choices to the polls
          Route('/create_choices', 'POST', create_choices),
          Route('/students', 'GET', students),
          Route('/students/{student_id}', 'GET', students_id)
          ]
