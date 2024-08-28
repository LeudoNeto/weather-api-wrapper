from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="OpenWeatherMap API Wrapper",
        default_version='v1',
        description="API Wrapper for OpenWeatherMap",
    ),
    public=True,
)

collect_weather_data_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user_defined_id': openapi.Schema(type=openapi.TYPE_STRING, description='ID do usuário')
    },
    required=['user_defined_id'],
    example={'user_defined_id': 'example_id_123'}
)

collect_weather_responses = {
    202: openapi.Response(
        description="Data collection initiated",
        examples={
            'application/json': {
                'message': 'Data collection initiated',
                'id': 'example_id_123'
            }
        }
    ),
    400: openapi.Response(
        description="Error response",
        examples={
            'application/json': {
                'error': 'ID is required'
            }
        }
    )
}

check_progress_responses = {
    200: openapi.Response(
        description="Progress response",
        examples={
            'application/json': {
                'progress': '75%'
            }
        }
    ),
    404: openapi.Response(
        description="Error response",
        examples={
            'application/json': {
                'error': 'ID not found'
            }
        }
    )
}