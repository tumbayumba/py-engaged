"""
match = {
    "/test/foo": dict(
        method="GET", 
        controller="app.controllers.test.TestController.index"
    ),
    "/test/bar": dict(
        method="POST", 
        controller="app.controllers.test.TestController.other", 
        middlewares=[
            "app.middlewares.authenticate.Authenticate",
            "app.middlewares.my_middleware.My"
        ]
    )
}
"""

match = {
    "/test/foo": dict(
        method="GET", 
        controller="app.controllers.test.TestController.index"
    ),
    "/test/bar": dict(
        method="POST", 
        controller="app.controllers.test.TestController.other", 
        middlewares=[
            "app.middlewares.authenticate.Authenticate",
            "app.middlewares.my_middleware.My"
        ]
    )
}
