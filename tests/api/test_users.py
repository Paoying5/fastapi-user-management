def test_get_users(client):

    response = client.get(
        client.base_url + "/users"
    )

    print()

    print("STATUS =", response.status_code)

    print("BODY =", response.text)

    assert response.status_code == 200