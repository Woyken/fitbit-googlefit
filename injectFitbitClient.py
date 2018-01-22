import types


def get_sleep_v12(self, date):
    """
    https://wiki.fitbit.com/display/API/API-Get-Sleep
    date should be a datetime.date object.
    """
    url = "{0}/1.2/user/-/sleep/date/{year}-{month}-{day}.json".format(
        *self._get_common_args(),
        year=date.year,
        month=date.month,
        day=date.day
    )
    return self.make_request(url)


def inject_fitbit_client(client):
    client.get_sleep_v12 = types.MethodType(get_sleep_v12, client)
    return client
