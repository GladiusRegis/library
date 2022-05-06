from datetime import datetime, timedelta
from meetings.Meeting import Meeting
from meetings.Calendar import Calendar


def test_check_next_available_slot():
    # given
    birthday = Meeting(datetime(2020, 11, 9, 12, 0), 'My birthday!')
    birthday2 = Meeting(datetime(2020, 11, 9, 13, 0), 'My birthday!')
    birthday3 = Meeting(datetime(2020, 11, 9, 14, 0), 'My birthday!')
    calendar = Calendar()
    calendar.add_meeting(birthday)
    calendar.add_meeting(birthday2)
    calendar.add_meeting(birthday3)

    # when
    next_time_slot = calendar.next_available_slot(datetime(2020, 11, 9, 12, 0))

    # then
    assert next_time_slot == datetime(2020, 11, 9, 15, 0)


def test_is_given_datetime_available():
    # given
    calendar = Calendar()

    # when
    next_time_slot = calendar.next_available_slot(datetime(2020, 11, 9, 12, 0))

    # then
    assert next_time_slot == datetime(2020, 11, 9, 12, 0)


def test_add_meeting():
    # given
    birthday = Meeting(datetime(2020, 11, 9, 12, 0), 'My birthday!')
    birthday2 = Meeting(datetime(2020, 11, 9, 12, 0), 'My birthday!')
    calendar = Calendar()
    # when
    calendar.add_meeting(birthday)
    calendar.add_meeting(birthday2)
    # then
    assert len(calendar.meetings) == 1


def test_add_two_meeting():
    # given
    birthday = Meeting(datetime(2020, 11, 9, 12, 0), 'My birthday!')
    birthday2 = Meeting(datetime(2021, 11, 9, 12, 0), 'My birthday!')
    calendar = Calendar()
    # when
    calendar.add_meeting(birthday)
    calendar.add_meeting(birthday2)
    # then
    assert len(calendar.meetings) == 2