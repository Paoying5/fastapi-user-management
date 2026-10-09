def get_openapi(client):
    response = client.get(
        "/openapi.json"
    )

    assert response.status_code == 200

    return response.json()


def resolve_schema(
    openapi: dict,
    schema: dict,
) -> dict:
    reference = schema.get("$ref")

    if reference is None:
        return schema

    prefix = "#/components/schemas/"

    assert reference.startswith(
        prefix
    )

    schema_name = reference.removeprefix(
        prefix
    )

    return openapi[
        "components"
    ][
        "schemas"
    ][
        schema_name
    ]


def extract_non_null_schema(
    schema: dict,
) -> dict:
    alternatives = schema.get(
        "anyOf"
    )

    if alternatives is None:
        return schema

    for alternative in alternatives:
        if (
            alternative.get("type")
            != "null"
        ):
            return alternative

    raise AssertionError(
        "No non-null schema found"
    )


def test_users_list_openapi_is_typed(
    client,
):
    openapi = get_openapi(
        client
    )

    response_schema = (
        openapi[
            "paths"
        ][
            "/users/"
        ][
            "get"
        ][
            "responses"
        ][
            "200"
        ][
            "content"
        ][
            "application/json"
        ][
            "schema"
        ]
    )

    api_response_schema = (
        resolve_schema(
            openapi,
            response_schema,
        )
    )

    data_schema = (
        api_response_schema[
            "properties"
        ][
            "data"
        ]
    )

    data_schema = (
        extract_non_null_schema(
            data_schema
        )
    )

    assert (
        data_schema["type"]
        == "array"
    )

    item_schema = (
        data_schema[
            "items"
        ]
    )

    assert (
        item_schema["$ref"]
        .endswith(
            "/UserResponse"
        )
    )


def test_user_detail_openapi_is_typed(
    client,
):
    openapi = get_openapi(
        client
    )

    response_schema = (
        openapi[
            "paths"
        ][
            "/users/{user_id}"
        ][
            "get"
        ][
            "responses"
        ][
            "200"
        ][
            "content"
        ][
            "application/json"
        ][
            "schema"
        ]
    )

    api_response_schema = (
        resolve_schema(
            openapi,
            response_schema,
        )
    )

    data_schema = (
        api_response_schema[
            "properties"
        ][
            "data"
        ]
    )

    data_schema = (
        extract_non_null_schema(
            data_schema
        )
    )

    assert (
        data_schema["$ref"]
        .endswith(
            "/UserResponse"
        )
    )


def test_users_pagination_headers_are_documented(
    client,
):
    openapi = get_openapi(
        client
    )

    headers = (
        openapi[
            "paths"
        ][
            "/users/"
        ][
            "get"
        ][
            "responses"
        ][
            "200"
        ][
            "headers"
        ]
    )

    assert (
        "X-Total-Count"
        in headers
    )

    assert (
        "X-Limit"
        in headers
    )

    assert (
        "X-Offset"
        in headers
    )

    assert (
        "X-Has-More"
        in headers
    )


def test_posts_pagination_headers_are_documented(
    client,
):
    openapi = get_openapi(
        client
    )

    headers = (
        openapi[
            "paths"
        ][
            "/posts/"
        ][
            "get"
        ][
            "responses"
        ][
            "200"
        ][
            "headers"
        ]
    )

    assert (
        "X-Total-Count"
        in headers
    )

    assert (
        "X-Limit"
        in headers
    )

    assert (
        "X-Offset"
        in headers
    )

    assert (
        "X-Has-More"
        in headers
    )