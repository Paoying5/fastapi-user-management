PAGINATION_HEADERS_OPENAPI = {
    "X-Total-Count": {
        "description": (
            "Total number of records matching "
            "the current filters."
        ),
        "schema": {
            "type": "integer",
        },
    },
    "X-Limit": {
        "description": (
            "Maximum number of records "
            "requested for this page."
        ),
        "schema": {
            "type": "integer",
        },
    },
    "X-Offset": {
        "description": (
            "Number of records skipped "
            "before this page."
        ),
        "schema": {
            "type": "integer",
        },
    },
    "X-Has-More": {
        "description": (
            "Whether more matching records "
            "exist after this page."
        ),
        "schema": {
            "type": "boolean",
        },
    },
}


def build_pagination_headers(
    *,
    total: int,
    limit: int,
    offset: int,
) -> dict[str, str]:
    has_more = (
        offset + limit
        < total
    )

    return {
        "X-Total-Count": str(total),
        "X-Limit": str(limit),
        "X-Offset": str(offset),
        "X-Has-More": (
            "true"
            if has_more
            else "false"
        ),
    }