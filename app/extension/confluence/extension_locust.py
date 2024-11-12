import re
from locustio.common_utils import init_logger, confluence_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='confluence')

@confluence_measure("locust_user_directory_api_query_user_directories_action")
@run_as_specific_user(username='admin', password='admin')  # run as specific user
def app_specific_action(locust):
    r = locust.get('/rest/nl-avisi-sync-add-on/1.0/directories', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content

    logger.locust_info(f'json: {content}, status_codeL {r.status_code}')  # log info for debug when verbose is true in confluence.yml file
    if '"synchronisable":false' not in content:
        logger.error(f"'synchronisable:false' was not found in {content}")

    assert r.status_code == 200  # assert specific string in response content
    assert '"synchronisable":false' in content  # assert specific string in response content
