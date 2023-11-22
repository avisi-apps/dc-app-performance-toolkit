import re
from locustio.common_utils import init_logger, confluence_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='confluence')


@confluence_measure("locust_list_servers_action")
@run_as_specific_user(username='admin', password='admin')  # run as specific user
def app_specific_action(locust):
    r = locust.get('/rest/git-plugin/1.0/servers', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content

    if 'Github' not in content:
        logger.error(f"'Github' was not found in {content}")
    assert 'Github' in content  # assert specific string in response content

    if 'Bitbucket' not in content:
        logger.error(f"'Bitbucket' was not found in {content}")
    assert 'Bitbucket' in content  # assert specific string in response content
