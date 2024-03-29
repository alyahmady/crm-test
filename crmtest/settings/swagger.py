from .rest_framework import API_PREFIX

SPECTACULAR_SETTINGS = {
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_SETTINGS": {
        "persistAuthorization": True,
    },
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "TITLE": "CRM Test Project API",
    "DESCRIPTION": "This is a document to understand the API URLs and requirements",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
    "COMPONENT_SPLIT_REQUEST": True,
    "SCHEMA_PATH_PREFIX": rf"/{API_PREFIX}/",
    "PREPROCESSING_HOOKS": ["crmtest.scheme.preprocessing_filter_spec"],
}
