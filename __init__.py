class BetterString:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string_field": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            },
        }

    RETURN_TYPES = ("STRING",)

    CATEGORY = "Better Things 💡"


NODE_CLASS_MAPPINGS = {
    "BetterString": BetterString
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BetterString": "Better String"
}
