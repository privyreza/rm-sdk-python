import responses

from resellme import Resellme

API_ENDPOINT = "https://api.resellme.co.zw/api/"

MOCK_RESPONSE = {
    "name": "test.co.zw",
    "reseller_id": 1,
    "status": "pending",
    "updated_at": "2021-08-09T13:33:00.000000Z",
    "created_at": "2021-08-09T13:33:00.000000Z",
    "id": 1,
}


@responses.activate
def test_api_call_200():
    responses.add(
        responses.POST, f"{API_ENDPOINT}/searches", json=MOCK_RESPONSE, status=200
    )

    resellme = Resellme(api_key=MOCK_API)
    json_response = resellme.search_domain("xyz.co.zw")

    assert json_response["status"] == "pending"
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == f"{API_ENDPOINT}/searches"
