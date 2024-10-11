class BetterString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "chain": ("STRING", {"multiline": False, "forceInput": True, "defaultInput": True}),
            },
            "required": {
                "string": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    CATEGORY = "Better Things 💡"

    def action(self, string, chain="", ):
        if not chain.strip():
            return (string,)

        chain = chain.rstrip()
        if chain[-1] == ",":
            chain += ", "

        return (chain + string,)

    FUNCTION = action.__name__
