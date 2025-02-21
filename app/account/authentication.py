from django.contrib.auth import get_user_model

User = get_user_model()

class EmailAuthBackend:
  """
    Authenticate using an e-mail address.
    """
  def authenticate(self, username=None, password=None):
    try:
      user = User.objects.get(email=username)
      if user.check_password(password):
        return user
      return None
    except (User.DoesNotExist, User.MultipleObjectsReturned):
      return None

  def get_user(self, user_id):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None
