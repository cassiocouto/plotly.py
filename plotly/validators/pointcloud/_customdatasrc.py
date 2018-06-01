import _plotly_utils.basevalidators


class CustomdatasrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='customdatasrc', parent_name='pointcloud', **kwargs
    ):
        super(CustomdatasrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )