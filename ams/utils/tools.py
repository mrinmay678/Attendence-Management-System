def checkFields(fields):
    def outer(endpoint):
        def inner(self, request, *args, **kwargs):
            for i in fields:
                if i not in request.data.keys():
                    raise ValueError(f"{i} missing")
            return endpoint(self, request, *args, **kwargs)
        return inner
    return outer