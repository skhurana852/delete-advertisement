"""Delete mail module."""
import requests
from constants import ACCESS_TOKEN, BASE_URI, DELETE_MSG, ERR_MSG, KEYWORD


class Delete:
    """Delete mail class."""

    def __init__(self):
        """Initialize delete class."""
        access_token = ACCESS_TOKEN
        self.headers = {"Authorization": f"Bearer {access_token}"}
        self.user_id = "saranshkhurana5@gmail.com"

    def get_ids(self, keyword):
        """Get ids of spam messages.

        Parameters
        ----------
        keywords for filtering out spam message.

        Returns
        ---------
        ids of filtered messages.
        """
        ids = []
        page_token = ""
        while True:
            try:
                msg_url = f"{BASE_URI}/{self.user_id}/messages?q={keyword}&pageToken={page_token}"
                response = requests.get(msg_url, headers=self.headers).json()
                messages = response["messages"]
                for i in range(len(messages)):
                    ids.append(messages[i]["id"])
                page_token = response["nextPageToken"]
            except KeyError:
                break
            except Exception:
                print(ERR_MSG)
        return ids

    def delete_mails(self):
        """Delete spam messages."""
        ids = self.get_ids(KEYWORD)
        delete_uri = f"{BASE_URI}/{self.user_id}/messages/batchDelete"
        body = {"ids": ids}
        try:
            response = requests.post(
                url=delete_uri, data=body, headers=self.headers
            )
            if response.text == "":
                print(f"{len(ids)} {DELETE_MSG}")
        except Exception:
            print(ERR_MSG)

