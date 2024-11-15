"""
match = {
    "/test/foo": dict(method="GET", controller="app.controllers.test.TestController.index"),
    "/test/bar": dict(method="POST", controller="app.controllers.test.TestController.other")
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
        middleware=["app.middlewares.authenticate.Authenticate"]
    )
}
