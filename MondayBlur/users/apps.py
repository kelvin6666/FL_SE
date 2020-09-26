from django.apps import AppConfig

#django auto generated file, to define app name
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
