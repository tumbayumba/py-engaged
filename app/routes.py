"""
match = {
    "/test/foo": dict(method="POST", controller="TestController.index"),
    "/test/bar/{{id}}": dict(method="POST", controller="TestController.other")
}
"""

match = {
    "/test/foo": dict(method="POST", controller="app.controllers.TestController.TestController.index"),
    "/test/bar/{{id}}": dict(method="POST", controller="app.controllers.TestController.TestController.other")
}
