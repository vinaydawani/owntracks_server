"""App config class"""

from typing import List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


# pylint: disable=E0213
class Conf(BaseSettings):
    """Conf class"""

    API_V1_STR: str = "/api/v1"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, _: Union[str, List[str]]) -> Union[List[str], str]:
        """Validate if a list of origins or csv

        Parameters
        ----------
        _ : Union[str, List[str]]
            passed cors paramets

        Returns
        -------
        Union[List[str], str]
            list of strs

        Raises
        ------
        ValueError
            If not valid origins or formatting
        """
        if isinstance(_, str) and not _.startswith("["):
            return [i.strip() for i in _.split(",")]
        elif isinstance(_, (list, str)):
            return _
        raise ValueError(_)

    # SQLALCHEMY_DATABASE_URI: Optional[str] = "sqlite:///example.db"
    POSTGRES_USERNAME: Optional[str] = "admin"
    POSTGRES_PASSWORD: Optional[str] = "password"
    POSTGRES_HOST: Optional[str] = "localhost"
    POSTGRES_PORT: Optional[int] = 5432
    POSTGRES_DB: Optional[str] = "postgres"

    class Config:
        """Class to modify models settings"""

        case_sensitive = True
        env_file = ".env"


config = Conf()
