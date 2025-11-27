from typing import Annotated

from pydantic import AfterValidator

from shared.lib.ulid_validators import validate_str_ulid

UlidStr = Annotated[str, AfterValidator(validate_str_ulid)]
