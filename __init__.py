class BetterString:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
            },
        }

    FUNCTION = "event"
    RETURN_TYPES = ("STRING",)

    CATEGORY = "Better Things 💡"

    def event(self, string):
        return (string, )


NODE_CLASS_MAPPINGS = {
    "BetterString": BetterString
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BetterString": "Better String"
}