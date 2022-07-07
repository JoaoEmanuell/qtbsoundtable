class MultiThreadError(Exception):
    """Muti Thread Error is a class responsible for issuing erros related of the MultiThreadError class

    """    
    def __init__(self, message: str = 'Multi Thread Error') -> None:
        """Init

        Args:
            message (str, optional): Error message. Defaults to 'Multi Thread Error'.

        """
        self.__message = message
        super().__init__(self.__message)

    def __str__(self) -> str:
        return self.__message
