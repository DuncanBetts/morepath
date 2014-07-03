import morepath
from morepath.error import ConflictError
from webtest import TestApp as Client
import pytest


def setup_module(module):
    morepath.disable_implicit()


def test_cleanup():
    config = morepath.setup_testing()

    class app(morepath.App):
        testing_config = config

    config.commit()

    # second commit should clean up after the first one, so we
    # expect no conflict errors
    config.commit()
