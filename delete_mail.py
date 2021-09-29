"""Delete mail module."""
import requests
from constants import ACCESS_TOKEN, BASE_URI, DELETE_MSG, ERR_MSG, KEYWORDS


class Delete:
    """Delete mail main module."""

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
        msg_url = f"{BASE_URI}/{self.user_id}/messages?q={keyword}"
        response = requests.get(msg_url, headers=self.headers).json()
        messages = response["messages"]
        for i in range(len(messages)):
            ids.append(messages[i]["id"])
        return ids

    def delete_mails(self):
        """Delete spam messages."""
        for keyword in KEYWORDS:
            ids = self.get_ids(keyword)
            delete_uri = f"{BASE_URI}/{self.user_id}/messages/batchDelete"
            body = {"ids": ids}
            try:
                response = requests.post(
                    url=delete_uri, data=body, headers=self.headers
                )
                if response.text == "":
                    print(DELETE_MSG)
            except Exception:
                print(ERR_MSG)


ob = Delete()
ob.delete_mails()
