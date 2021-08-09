import responses

from resellme import Resellme

API_ENDPOINT = "https://api.resellme.co.zw/api/v1"


@responses.activate
def test_api_call_200():
    responses.add(responses.POST, f"{API_ENDPOINT}/searches",
                  json={'success': 'found'}, status=200)

    resellme = Resellme(api_key='MOCK_API')
    json_response = resellme.search_domain('xyz.co.zw')

    assert json_response == {"success": "found"}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == f"{API_ENDPOINT}/searches"
    assert responses.calls[0].response.text == '{"success": "found"}'
