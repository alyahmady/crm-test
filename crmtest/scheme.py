from django.conf import settings


def preprocessing_filter_spec(endpoints):
    filtered = []
    for path, path_regex, method, callback in endpoints:
        if path.lstrip("/").startswith(settings.API_PREFIX):
            filtered.append((path, path_regex, method, callback))

    return filtered
