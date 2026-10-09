from providers.data.data_usa_provider import DataUsaProvider


def test_data_tesseract_status_ok(data_api_client):
    tesseract = data_api_client.get_data_tesseract()
    assert tesseract["status"] == "ok"


def test_data_tesseract_exists(data_api_client):
    tesseract = DataUsaProvider.data_tesseract_exist()
    api_tesseract = data_api_client.get_data_tesseract()

    assert api_tesseract["module"] == tesseract["module"]


def test_data_tesseract_non_exists(data_api_client):
    tesseract = DataUsaProvider.data_tesseract_non_exist()
    api_tesseract = data_api_client.get_data_tesseract()

    assert api_tesseract["module"] != tesseract["module"]


def test_data_member_exists(data_api_client):
    member = DataUsaProvider.data_member_exist()
    api_members = data_api_client.get_data_members()
    for api_member in api_members["members"]:
        if api_member == member:
            print(api_member)
            return
    assert False


def test_data_member_non_exists(data_api_client):
    member = DataUsaProvider.data_member_not_exist()
    api_members = data_api_client.get_data_members()
    for api_member in api_members["members"]:
        if api_member != member:
            print(api_members["members"])
            print(member)
            return
    assert False
