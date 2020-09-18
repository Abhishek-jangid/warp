from movie.models import User
from warp.constants import (
    data_key, error_key, msg_key, status_key, SUCCESS, ERROR
)



class UserService:

    def __init__(self, mobile):
        self.mobile = mobile

    def get_auth_token(self):
        print(self.mobile)
        a = User.get_user_with_mobile(self.mobile)
        print(a)
        return {
            status_key: SUCCESS,
            data_key: {
                'token': 'default'
            }
        }
