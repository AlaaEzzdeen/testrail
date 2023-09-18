import testrail_api
import os

def publish_results():
    client = testrail_api.TestRailAPI(
        os.environ['https://swe401pro.testrail.io'],
        os.environ['gr.eg.or.ymj.en.son6@gmail.com'],
        os.environ['aPAgZT6rynaBWwcJA48W-EK89Ugq/Qdsv6pBZeL2B']
    )

    project_id = os.environ['1']

    run_id = os.environ['TESTRAIL_RUN_ID']

    test_results = {
        'CT': {
            'status_id': 1, 
            'comment': 'Test passed successfully.'
        },
        'CF': {
            'status_id': -1,
            'comment': 'Test failed due to assertion error.'
        }
    }


    for case_id, result in test_results.items():
        client.send_post(
            f'add_result_for_case/{run_id}/{case_id}',
            result
        )

    publish_results()