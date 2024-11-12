from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='jira')


@jira_measure("locust_app_specific_action")
@run_as_specific_user(username='admin', password='admin')  # run as specific user
def app_specific_action(locust):
    r = locust.get('/rest/editcustomfieldvalues/latest/customfields', catch_response=True)  # call app-specific GET endpoint
    json = r.json()

    assert r.status_code == 200

    assert json[0]['name'] == 'Abstruse'
