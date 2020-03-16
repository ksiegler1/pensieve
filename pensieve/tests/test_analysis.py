import datetime as dt
from datetime import timedelta
import pytz
import pytest

from pensieve.analysis import Analysis
from pensieve.experimenter import Experiment


@pytest.fixture
def experiments():
    return [
        Experiment(
            slug="test_slug",
            type="pref",
            start_date=dt.datetime(2019, 12, 1, tzinfo=pytz.utc),
            end_date=dt.datetime(2020, 3, 1, tzinfo=pytz.utc),
            variants=[],
            normandy_slug="normandy-test-slug",
        ),
        Experiment(
            slug="test_slug",
            type="addon",
            start_date=dt.datetime(2019, 12, 1, tzinfo=pytz.utc),
            end_date=dt.datetime(2020, 3, 1, tzinfo=pytz.utc),
            variants=[],
            normandy_slug=None,
        ),
    ]


def test_should_analyse_experiment(experiments):
    analysis = Analysis("test", "test")
    date = dt.datetime(2019, 12, 1, tzinfo=pytz.utc) + timedelta(analysis.ANALYSIS_PERIOD)
    assert analysis._should_analyse_experiment(experiments[0], date) is True

    date = dt.datetime(2019, 12, 1, tzinfo=pytz.utc) + timedelta(0)
    assert analysis._should_analyse_experiment(experiments[0], date) is False

    date = dt.datetime(2019, 12, 1, tzinfo=pytz.utc) + timedelta(2)
    assert 2 != analysis.ANALYSIS_PERIOD
    assert analysis._should_analyse_experiment(experiments[0], date) is False