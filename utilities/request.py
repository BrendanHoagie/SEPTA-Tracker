class Request:

    _base_url = "https://www3.septa.org/api/"

    def __init__(
        self,
        url: str = None,
        required_params: list[str] = None,
        optional_params: list[str] = None,
    ):
        self._url = url
        self._required_params = required_params
        self._optional_params = optional_params

    def set_url(self, url: str) -> None:
        """Sets the internal url. This is the extension to the base url

        Args
            url: a str representing the specific extension held in this request
        """
        self._url = url

    def set_required_params(self, params: list[str]) -> None:
        """Sets the required parameters for the GET request

        Args
            params: a list of parameters required for the request, each parameter is a str
        """
        self._required_params = params

    def set_optional_params(self, params: list[str]) -> None:
        """Sets the optional parameters for the GET request

        Args
            params: a list of parameters that are optional for the request, each parameter is a str
        """
        self._optional_params = params

    def add_required_param(self, param: str) -> None:
        """Adds a single parameter to the list of required parameters

        Args
            param: a str containing the name of a required parameter
        """
        if not self._required_params:
            self._required_params = []
        self._required_params.append(param)

    def add_optional_param(self, param: str) -> None:
        """Adds a single parameter to the list of optional parameters

        Args
            param: a str containing the name of a optional parameter
        """
        if not self._optional_params:
            self._optional_params = []
        self._optional_params.append(param)

    def get_url(self, ext_only: bool) -> str:
        """Returns url of the request, either just the specific extension or the complete url

        Args:
            ext_only: a bool representing if the url should be just the request-specific extension
                      or the complete url (base + extension)

        Returns:
            a str representing the specified url type
        """
        return self._url if ext_only else self._base_url + self._url

    def get_required_params(self) -> list[str]:
        """Returns the list of required params for the request

        Returns:
            a list, each item is a str representing a required parameter for the GET request
        """
        return self._required_params

    def get_optional_params(self) -> list[str]:
        """Returns the list of optional params for the request

        Returns:
            a list, each item is a str representing a optional parameter for the GET request
        """
        return self._optional_params

    def __str__(self):

        formatted = f"url: {self._url}\nrequired params:\n"
        if self._required_params:
            for param in self._required_params:
                formatted += f"\t-{param}\n"
        formatted += "optional params:\n"
        if self._optional_params:
            for param in self._optional_params:
                formatted += f"\t-{param}\n"
        return formatted
