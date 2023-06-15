from asgi_correlation_id.context import correlation_id


def get_base_headers() -> dict:
    return {
        'X-Request-ID': correlation_id.get(),
    }
