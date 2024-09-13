
SEARCH_TITLE="| ID |    STATUS    |      CREATEDAT      |      UPDATEDAT      |  DESCRIPTION    |\n"


def vaild_id(_id):
    return f"Please enter a vaild Task ID.{_id} is not found"

def search_data(ID,entry:dict):
    _id_space =4
    status_space = 14
    time_space =21

    return f"|{str(ID).center(_id_space)}|{entry['status'].center(status_space)}|{entry['createdAt'].center(time_space)}|{entry['updatedAt'].center(time_space)}| {entry['description']} |\n"